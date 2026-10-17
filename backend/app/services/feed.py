from collections.abc import Callable
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.config import Settings
from app.db.models import AccountKind, Item, utc_now
from app.db.repositories import items as item_repo
from app.db.repositories.items import ArchiveKey, FeedFilter
from app.dto.items import FeedPageResponse, FeedQuery, ItemResponse
from app.services.cursors import ArchiveCursor, RankedCursor, decode_cursor, encode_cursor
from app.services.ranking import ItemStats, RankingSettings, score
from app.services.snapshots import Snapshot, SnapshotCache


class FeedService:
    def __init__(
        self,
        session: Session,
        snapshots: SnapshotCache,
        settings: Settings,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        self._session = session
        self._snapshots = snapshots
        self._clock = clock
        self._page_size = settings.feed_page_size
        self._window = timedelta(days=settings.rank_window_days)
        self._ranking = RankingSettings(
            gravity=settings.rank_gravity,
            provenance_weight=settings.rank_provenance_w,
            click_weight=settings.rank_click_w,
            downvote_penalty=settings.rank_downvote_p,
        )

    def get_page(self, query: FeedQuery) -> FeedPageResponse:
        feed_filter = FeedFilter(query.topic, query.tag)
        cursor = decode_cursor(query.cursor) if query.cursor else None
        size = self._page_size

        if isinstance(cursor, ArchiveCursor):
            keys = item_repo.list_archive_keys(
                self._session, feed_filter, cursor.cutoff, cursor.after, size + 1
            )
            return self._page([], keys, size, cursor.cutoff)

        snapshot = self._snapshot_for(feed_filter, cursor)
        offset = cursor.offset if cursor else 0
        ranked_ids = list(snapshot.item_ids[offset : offset + size])
        end = offset + len(ranked_ids)
        if end < len(snapshot.item_ids):
            return self._response(ranked_ids, encode_cursor(RankedCursor(snapshot.id, end)))

        room = size - len(ranked_ids)
        keys = item_repo.list_archive_keys(
            self._session, feed_filter, snapshot.cutoff, None, room + 1
        )
        return self._page(ranked_ids, keys, room, snapshot.cutoff)

    def _snapshot_for(self, feed_filter: FeedFilter, cursor: RankedCursor | None) -> Snapshot:
        now = self._clock()
        if cursor is not None:
            snapshot = self._snapshots.get(cursor.snapshot_id, now)
            if snapshot is not None and snapshot.key == feed_filter:
                return snapshot
        return self._snapshots.latest(feed_filter, now, lambda: self._rank(feed_filter, now))

    def _rank(self, feed_filter: FeedFilter, now: datetime) -> tuple[tuple[int, ...], datetime]:
        cutoff = now - self._window
        candidates = item_repo.list_rank_candidates(self._session, feed_filter, cutoff)
        ordered = sorted(
            candidates,
            key=lambda c: (
                score(
                    ItemStats(c.upvotes, c.downvotes, c.created_at, c.provenance_score),
                    now,
                    self._ranking,
                ),
                c.created_at,
                c.id,
            ),
            reverse=True,
        )
        return tuple(c.id for c in ordered), cutoff

    def _page(
        self,
        ranked_ids: list[int],
        archive_keys: list[ArchiveKey],
        archive_room: int,
        cutoff: datetime,
    ) -> FeedPageResponse:
        taken = archive_keys[:archive_room]
        next_cursor = None
        if len(archive_keys) > archive_room:
            after = taken[-1] if taken else None
            next_cursor = encode_cursor(ArchiveCursor(cutoff, after))
        return self._response(ranked_ids + [item_id for _, item_id in taken], next_cursor)

    def _response(self, item_ids: list[int], next_cursor: str | None) -> FeedPageResponse:
        items = [
            item
            for item in item_repo.get_items_in_order(self._session, item_ids)
            if item.deleted_at is None
        ]
        comment_counts = item_repo.count_visible_comments(self._session, [i.id for i in items])
        return FeedPageResponse(
            items=[_to_response(item, comment_counts.get(item.id, 0)) for item in items],
            next_cursor=next_cursor,
        )


def _to_response(item: Item, comment_count: int) -> ItemResponse:
    return ItemResponse(
        id=item.id,
        title=item.title,
        url=item.url,
        domain=item.domain,
        topic=item.topic.slug,
        tags=[tag.name for tag in item.tags],
        score=item.upvotes - item.downvotes,
        comment_count=comment_count,
        submitted_by=None if item.account.kind is AccountKind.AGENT else item.account.username,
        created_at=item.created_at,
    )
