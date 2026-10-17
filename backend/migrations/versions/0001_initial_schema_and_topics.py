from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "accounts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column(
            "kind",
            sa.Enum("human", "agent", "admin", name="accountkind", native_enum=False, length=16),
            nullable=False,
        ),
        sa.Column("can_publish", sa.Boolean(), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.String(length=24), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_accounts")),
        sa.UniqueConstraint("username", name=op.f("uq_accounts_username")),
    )
    op.create_table(
        "topics",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slug", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_topics")),
        sa.UniqueConstraint("slug", name=op.f("uq_topics_slug")),
    )
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=300), nullable=False),
        sa.Column("url", sa.String(length=2048), nullable=False),
        sa.Column("canonical_url", sa.String(length=2048), nullable=False),
        sa.Column("domain", sa.String(length=255), nullable=False),
        sa.Column("topic_id", sa.Integer(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("source_name", sa.String(length=200), nullable=True),
        sa.Column("published_at", sa.String(length=24), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("primary_ref", sa.String(length=200), nullable=True),
        sa.Column("provenance_score", sa.Float(), nullable=True),
        sa.Column("upvotes", sa.Integer(), nullable=False),
        sa.Column("downvotes", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.String(length=24), nullable=False),
        sa.Column("deleted_at", sa.String(length=24), nullable=True),
        sa.Column("deleted_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"], ["accounts.id"], name=op.f("fk_items_account_id_accounts")
        ),
        sa.ForeignKeyConstraint(
            ["deleted_by_id"], ["accounts.id"], name=op.f("fk_items_deleted_by_id_accounts")
        ),
        sa.ForeignKeyConstraint(["topic_id"], ["topics.id"], name=op.f("fk_items_topic_id_topics")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_items")),
        sa.UniqueConstraint("canonical_url", name=op.f("uq_items_canonical_url")),
    )
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_items_account_id"), ["account_id"], unique=False)
        batch_op.create_index("ix_items_created_at_id", ["created_at", "id"], unique=False)
        batch_op.create_index(batch_op.f("ix_items_topic_id"), ["topic_id"], unique=False)

    op.create_table(
        "topic_tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("topic_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=48), nullable=False),
        sa.ForeignKeyConstraint(
            ["topic_id"], ["topics.id"], name=op.f("fk_topic_tags_topic_id_topics")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_topic_tags")),
        sa.UniqueConstraint("topic_id", "name", name="uq_topic_tags_topic_id_name"),
    )
    with op.batch_alter_table("topic_tags", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_topic_tags_topic_id"), ["topic_id"], unique=False)

    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(length=24), nullable=False),
        sa.Column("deleted_at", sa.String(length=24), nullable=True),
        sa.Column("deleted_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"], ["accounts.id"], name=op.f("fk_comments_account_id_accounts")
        ),
        sa.ForeignKeyConstraint(
            ["deleted_by_id"], ["accounts.id"], name=op.f("fk_comments_deleted_by_id_accounts")
        ),
        sa.ForeignKeyConstraint(["item_id"], ["items.id"], name=op.f("fk_comments_item_id_items")),
        sa.ForeignKeyConstraint(
            ["parent_id"], ["comments.id"], name=op.f("fk_comments_parent_id_comments")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_comments")),
    )
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_comments_account_id"), ["account_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_comments_item_id"), ["item_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_comments_parent_id"), ["parent_id"], unique=False)

    op.create_table(
        "item_tags",
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["item_id"], ["items.id"], name=op.f("fk_item_tags_item_id_items")),
        sa.ForeignKeyConstraint(
            ["tag_id"], ["topic_tags.id"], name=op.f("fk_item_tags_tag_id_topic_tags")
        ),
        sa.PrimaryKeyConstraint("item_id", "tag_id", name=op.f("pk_item_tags")),
    )
    _insert_launch_topics()


LAUNCH_TOPICS = (
    (
        "ai",
        "AI",
        (
            "agents",
            "api",
            "evals",
            "german",
            "inference",
            "latestnews",
            "microsoft",
            "models",
            "policy",
            "python",
            "research",
            "testing",
            "tooling",
        ),
    ),
    (
        "hemophilia",
        "Hemophilia",
        (
            "digital-health",
            "emicizumab",
            "factor-viii",
            "gene-therapy",
            "guidelines",
            "hemophilia-b",
            "inhibitors",
            "pediatrics",
            "pharmacokinetics",
            "prophylaxis",
            "real-world-evidence",
            "regulatory",
            "surgery",
        ),
    ),
)


def _insert_launch_topics() -> None:
    topics = sa.table(
        "topics",
        sa.column("id", sa.Integer),
        sa.column("slug", sa.String),
        sa.column("name", sa.String),
        sa.column("sort_order", sa.Integer),
    )
    topic_tags = sa.table(
        "topic_tags",
        sa.column("topic_id", sa.Integer),
        sa.column("name", sa.String),
    )
    op.bulk_insert(
        topics,
        [
            {"id": topic_id, "slug": slug, "name": name, "sort_order": topic_id}
            for topic_id, (slug, name, _) in enumerate(LAUNCH_TOPICS, start=1)
        ],
    )
    op.bulk_insert(
        topic_tags,
        [
            {"topic_id": topic_id, "name": tag}
            for topic_id, (_, _, tags) in enumerate(LAUNCH_TOPICS, start=1)
            for tag in tags
        ],
    )


def downgrade() -> None:
    op.drop_table("item_tags")
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_comments_parent_id"))
        batch_op.drop_index(batch_op.f("ix_comments_item_id"))
        batch_op.drop_index(batch_op.f("ix_comments_account_id"))

    op.drop_table("comments")
    with op.batch_alter_table("topic_tags", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_topic_tags_topic_id"))

    op.drop_table("topic_tags")
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_items_topic_id"))
        batch_op.drop_index("ix_items_created_at_id")
        batch_op.drop_index(batch_op.f("ix_items_account_id"))

    op.drop_table("items")
    op.drop_table("topics")
    op.drop_table("accounts")
