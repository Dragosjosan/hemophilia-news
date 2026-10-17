from fastapi import APIRouter

from app.api.dependencies import TopicServiceDep
from app.dto.topics import TopicResponse

router = APIRouter(prefix="/topics", tags=["topics"])


@router.get("")
def list_topics(topics: TopicServiceDep) -> list[TopicResponse]:
    return topics.list_topics()
