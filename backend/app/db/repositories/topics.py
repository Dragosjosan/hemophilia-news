from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.db.models import Item, Topic


def list_topics(session: Session) -> list[Topic]:
    statement = select(Topic).options(selectinload(Topic.tags)).order_by(Topic.sort_order, Topic.id)
    return list(session.scalars(statement))


def count_items_since(session: Session, since: datetime) -> dict[int, int]:
    statement = (
        select(Item.topic_id, func.count())
        .where(Item.created_at >= since, Item.deleted_at.is_(None))
        .group_by(Item.topic_id)
    )
    return {topic_id: count for topic_id, count in session.execute(statement)}
