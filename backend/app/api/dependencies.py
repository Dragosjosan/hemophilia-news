from collections.abc import Iterator
from typing import Annotated, cast

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.config import Settings
from app.db.connection import SessionFactory
from app.services.feed import FeedService
from app.services.snapshots import SnapshotCache
from app.services.topics import TopicService


def get_session(request: Request) -> Iterator[Session]:
    session_factory = cast(SessionFactory, request.app.state.session_factory)
    with session_factory() as session:
        yield session


def get_settings(request: Request) -> Settings:
    return cast(Settings, request.app.state.settings)


def get_snapshots(request: Request) -> SnapshotCache:
    return cast(SnapshotCache, request.app.state.snapshots)


DatabaseSession = Annotated[Session, Depends(get_session)]
AppSettings = Annotated[Settings, Depends(get_settings)]
Snapshots = Annotated[SnapshotCache, Depends(get_snapshots)]


def get_feed_service(
    session: DatabaseSession, snapshots: Snapshots, settings: AppSettings
) -> FeedService:
    return FeedService(session, snapshots, settings)


def get_topic_service(session: DatabaseSession, settings: AppSettings) -> TopicService:
    return TopicService(session, settings)


FeedServiceDep = Annotated[FeedService, Depends(get_feed_service)]
TopicServiceDep = Annotated[TopicService, Depends(get_topic_service)]
