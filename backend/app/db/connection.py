from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from sqlalchemy import Engine, create_engine, event, make_url
from sqlalchemy.orm import Session, sessionmaker

SessionFactory = sessionmaker[Session]

_SQLITE_PRAGMAS = (
    "PRAGMA journal_mode=WAL",
    "PRAGMA busy_timeout=5000",
    "PRAGMA foreign_keys=ON",
)


def prepare_database_directory(database_url: str) -> None:
    url = make_url(database_url)
    if url.get_backend_name() == "sqlite" and url.database not in (None, "", ":memory:"):
        Path(url.database).parent.mkdir(parents=True, exist_ok=True)


def build_engine(database_url: str) -> Engine:
    engine = create_engine(database_url)
    if engine.dialect.name == "sqlite":
        event.listen(engine, "connect", _apply_sqlite_pragmas)
    return engine


def _apply_sqlite_pragmas(dbapi_connection: Any, _record: Any) -> None:
    cursor = dbapi_connection.cursor()
    for pragma in _SQLITE_PRAGMAS:
        cursor.execute(pragma)
    cursor.close()


def build_session_factory(engine: Engine) -> SessionFactory:
    return sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def session_scope(session_factory: SessionFactory) -> Iterator[Session]:
    with session_factory() as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
