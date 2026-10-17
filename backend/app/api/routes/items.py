from typing import Annotated

from fastapi import APIRouter, Query

from app.api.dependencies import FeedServiceDep
from app.dto.items import FeedPageResponse, FeedQuery

router = APIRouter(prefix="/items", tags=["items"])


@router.get("")
def list_items(query: Annotated[FeedQuery, Query()], feed: FeedServiceDep) -> FeedPageResponse:
    return feed.get_page(query)
