from app.dto.topics import TopicResponse

# Placeholder until topics move into the database (see DESIGN.md, news-api).
_TOPICS = [
    TopicResponse(slug="hemophilia", name="Hemophilia", tags=[], remaining_today=0),
    TopicResponse(slug="ai", name="AI", tags=[], remaining_today=0),
]


def list_topics() -> list[TopicResponse]:
    return _TOPICS
