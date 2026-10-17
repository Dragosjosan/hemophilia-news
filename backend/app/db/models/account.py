from datetime import datetime
from enum import StrEnum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import Base, UtcDateTime, utc_now


class AccountKind(StrEnum):
    HUMAN = "human"
    AGENT = "agent"
    ADMIN = "admin"


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    kind: Mapped[AccountKind] = mapped_column(
        Enum(
            AccountKind,
            native_enum=False,
            length=16,
            values_callable=lambda kinds: [kind.value for kind in kinds],
        )
    )
    can_publish: Mapped[bool] = mapped_column(default=False)
    password_hash: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(UtcDateTime(), default=utc_now)
