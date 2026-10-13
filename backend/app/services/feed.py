from app.dto.items import FeedPageResponse


def get_feed_page(topic: str | None, tag: str | None, cursor: str | None) -> FeedPageResponse:
    # Placeholder until items are persisted.
    return FeedPageResponse(items=[], next_cursor=None)
