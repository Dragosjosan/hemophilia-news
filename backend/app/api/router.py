from fastapi import APIRouter

from app.api.routes import items, topics
from app.config import settings

api_router = APIRouter(prefix=settings.api_prefix)
api_router.include_router(items.router)
api_router.include_router(topics.router)
