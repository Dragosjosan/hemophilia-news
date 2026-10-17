from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Select, and_, func, or_, select
from sqlalchemy.orm import Session, joinedload, selectinload

from app.db.models import Comment, Item, Topic, TopicTag


@dataclass(frozen=True, slots=True)
class FeedFilter:
    topic: str | None = None
    tag: str | None = None


@dataclass(frozen=True, slots=True)
class RankCandidate:
    id: int
    upvotes: int
    downvotes: int
    provenance_score: float | None
    created_at: datetime


ArchiveKey = tuple[datetime, int]


def _visible[*Ts](statement: Select[*Ts], feed_filter: FeedFilter) -> Select[*Ts]:
    statement = statement.where(Item.deleted_at.is_(None))
    if feed_filter.topic is not None:
        statement = statement.join(Topic, Item.topic_id == Topic.id).where(
            Topic.slug == feed_filter.topic
        )
    if feed_filter.tag is not None:
        statement = statement.where(Item.tags.any(TopicTag.name == feed_filter.tag))
    return statement


def list_rank_candidates(
    session: Session, feed_filter: FeedFilter, since: datetime
) -> list[RankCandidate]:
    statement = _visible(
        select(Item.id, Item.upvotes, Item.downvotes, Item.provenance_score, Item.created_at),
        feed_filter,
    ).where(Item.created_at >= since)
    return [RankCandidate(*row) for row in session.execute(statement)]


def list_archive_keys(
    session: Session,
    feed_filter: FeedFilter,
    before: datetime,
    after: ArchiveKey | None,
    limit: int,
) -> list[ArchiveKey]:
    statement = _visible(select(Item.created_at, Item.id), feed_filter).where(
        Item.created_at < before
    )
    if after is not None:
        created_at, item_id = after
        statement = statement.where(
            or_(
                Item.created_at < created_at,
                and_(Item.created_at == created_at, Item.id < item_id),
            )
        )
    statement = statement.order_by(Item.created_at.desc(), Item.id.desc()).limit(limit)
    return [(created_at, item_id) for created_at, item_id in session.execute(statement)]


def get_items_in_order(session: Session, ids: Sequence[int]) -> list[Item]:
    if not ids:
        return []
    statement = (
        select(Item)
        .where(Item.id.in_(ids))
        .options(joinedload(Item.topic), joinedload(Item.account), selectinload(Item.tags))
    )
    by_id = {item.id: item for item in session.scalars(statement)}
    return [by_id[item_id] for item_id in ids if item_id in by_id]


def count_visible_comments(session: Session, item_ids: Sequence[int]) -> dict[int, int]:
    if not item_ids:
        return {}
    statement = (
        select(Comment.item_id, func.count())
        .where(Comment.item_id.in_(item_ids), Comment.deleted_at.is_(None))
        .group_by(Comment.item_id)
    )
    return {item_id: count for item_id, count in session.execute(statement)}
