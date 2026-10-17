from collections.abc import Callable, Hashable
from dataclasses import dataclass
from datetime import datetime, timedelta
from threading import Lock
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class Snapshot:
    id: str
    key: Hashable
    item_ids: tuple[int, ...]
    cutoff: datetime
    expires_at: datetime


class SnapshotCache:
    def __init__(self, ttl: timedelta, new_id: Callable[[], str] = lambda: uuid4().hex) -> None:
        self._ttl = ttl
        self._new_id = new_id
        self._by_id: dict[str, Snapshot] = {}
        self._latest: dict[Hashable, Snapshot] = {}
        self._lock = Lock()

    def get(self, snapshot_id: str, now: datetime) -> Snapshot | None:
        with self._lock:
            snapshot = self._by_id.get(snapshot_id)
            return snapshot if snapshot is not None and now < snapshot.expires_at else None

    def latest(
        self,
        key: Hashable,
        now: datetime,
        build: Callable[[], tuple[tuple[int, ...], datetime]],
    ) -> Snapshot:
        with self._lock:
            current = self._latest.get(key)
            if current is not None and now < current.expires_at:
                return current
            item_ids, cutoff = build()
            snapshot = Snapshot(self._new_id(), key, item_ids, cutoff, now + self._ttl)
            self._prune(now)
            self._by_id[snapshot.id] = snapshot
            self._latest[key] = snapshot
            return snapshot

    def _prune(self, now: datetime) -> None:
        expired = [sid for sid, snapshot in self._by_id.items() if now >= snapshot.expires_at]
        for snapshot_id in expired:
            del self._by_id[snapshot_id]
