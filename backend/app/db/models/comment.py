from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import Base, UtcDateTime, utc_now


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), index=True)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("comments.id"), index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(UtcDateTime(), default=utc_now)
    deleted_at: Mapped[datetime | None] = mapped_column(UtcDateTime())
    deleted_by_id: Mapped[int | None] = mapped_column(ForeignKey("accounts.id"))
