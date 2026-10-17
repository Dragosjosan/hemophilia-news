import base64
import binascii
import json
from dataclasses import dataclass
from datetime import UTC, datetime


class InvalidCursorError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class RankedCursor:
    snapshot_id: str
    offset: int


@dataclass(frozen=True, slots=True)
class ArchiveCursor:
    cutoff: datetime
    after: tuple[datetime, int] | None = None


Cursor = RankedCursor | ArchiveCursor


def encode_cursor(cursor: Cursor) -> str:
    payload: dict[str, object]
    match cursor:
        case RankedCursor(snapshot_id, offset):
            payload = {"z": "r", "s": snapshot_id, "o": offset}
        case ArchiveCursor(cutoff, after):
            payload = {"z": "a", "c": _iso(cutoff)}
            if after is not None:
                payload |= {"t": _iso(after[0]), "i": after[1]}
    raw = json.dumps(payload, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def decode_cursor(token: str) -> Cursor:
    try:
        raw = base64.urlsafe_b64decode(token + "=" * (-len(token) % 4))
        payload = json.loads(raw)
        match payload:
            case {"z": "r", "s": str(snapshot_id), "o": int(offset)} if offset >= 0:
                return RankedCursor(snapshot_id, offset)
            case {"z": "a", "c": str(cutoff), "t": str(created_at), "i": int(item_id)}:
                return ArchiveCursor(_parse(cutoff), (_parse(created_at), item_id))
            case {"z": "a", "c": str(cutoff)}:
                return ArchiveCursor(_parse(cutoff))
    except (binascii.Error, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise InvalidCursorError(token) from error
    raise InvalidCursorError(token)


def _iso(value: datetime) -> str:
    return value.astimezone(UTC).isoformat()


def _parse(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError("cursor timestamps must be timezone-aware")
    return parsed.astimezone(UTC)
