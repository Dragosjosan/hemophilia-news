from fastapi import APIRouter

from app.dto.topics import TopicResponse
from app.services import topics

router = APIRouter(prefix="/topics", tags=["topics"])


@router.get("")
def list_topics() -> list[TopicResponse]:
    return topics.list_topics()
