from fastapi import APIRouter

from app.dto.items import FeedPageResponse
from app.services import feed

router = APIRouter(prefix="/items", tags=["items"])


@router.get("")
def list_items(
    topic: str | None = None, tag: str | None = None, cursor: str | None = None
) -> FeedPageResponse:
    return feed.get_feed_page(topic, tag, cursor)
