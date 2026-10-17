from collections.abc import Callable
from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.config import Settings
from app.db.models import utc_now
from app.db.repositories import topics as topic_repo
from app.dto.topics import TopicResponse


def start_of_utc_day(now: datetime) -> datetime:
    return now.astimezone(UTC).replace(hour=0, minute=0, second=0, microsecond=0)


class TopicService:
    def __init__(
        self, session: Session, settings: Settings, clock: Callable[[], datetime] = utc_now
    ) -> None:
        self._session = session
        self._daily_cap = settings.daily_cap_per_topic
        self._clock = clock

    def list_topics(self) -> list[TopicResponse]:
        used_today = topic_repo.count_items_since(self._session, start_of_utc_day(self._clock()))
        return [
            TopicResponse(
                slug=topic.slug,
                name=topic.name,
                tags=[tag.name for tag in topic.tags],
                remaining_today=max(self._daily_cap - used_today.get(topic.id, 0), 0),
            )
            for topic in topic_repo.list_topics(self._session)
        ]
