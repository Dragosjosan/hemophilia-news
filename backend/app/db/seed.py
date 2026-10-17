from dataclasses import dataclass
from datetime import datetime, timedelta
from urllib.parse import urlsplit

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.config import settings
from app.db.connection import build_engine, build_session_factory, session_scope
from app.db.models import Account, AccountKind, Comment, Item, Topic, TopicTag, utc_now

BOT = "josan"


@dataclass(frozen=True, slots=True)
class _SeedItem:
    hours_ago: float
    topic: str
    author: str
    score: int
    title: str
    url: str
    tags: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class _SeedComment:
    item: int
    parent: int | None
    author: str
    hours_ago: float
    text: str


ACCOUNTS = (
    (BOT, AccountKind.AGENT),
    ("dragos", AccountKind.ADMIN),
    ("mkessler", AccountKind.HUMAN),
    ("lena_r", AccountKind.HUMAN),
    ("tbauer", AccountKind.HUMAN),
)

SEED_ITEMS = (
    _SeedItem(
        0.6,
        "ai",
        BOT,
        64,
        "Microsoft Agent Framework 1.2 adds durable multi-agent workflows",
        "https://learn.microsoft.com/agent-framework",
        ("microsoft", "latestnews", "agents"),
    ),
    _SeedItem(
        1.8,
        "hemophilia",
        BOT,
        41,
        "Phase 3 data on once-weekly efanesoctocog alfa in children under 6",
        "https://ashpublications.org/blood",
        ("factor-viii", "pediatrics"),
    ),
    _SeedItem(
        3.2,
        "ai",
        BOT,
        38,
        "Open-weight 32B model reaches frontier scores on SWE-bench Verified",
        "https://arxiv.org/abs/2610.01234",
        ("research", "models"),
    ),
    _SeedItem(
        5.1,
        "ai",
        "dragos",
        22,
        "Show: property-based tests for LLM tool-calling with Hypothesis",
        "https://github.com/dragosjosan",
        ("tooling", "testing"),
    ),
    _SeedItem(
        7.4,
        "hemophilia",
        BOT,
        33,
        "Hemophilia B gene therapy: 5-year follow-up shows sustained factor IX expression",
        "https://nejm.org",
        ("gene-therapy", "hemophilia-b"),
    ),
    _SeedItem(
        9.1,
        "ai",
        BOT,
        19,
        "EU AI Act: general-purpose model obligations taking effect in Q4",
        "https://digital-strategy.ec.europa.eu",
        ("policy", "latestnews"),
    ),
    _SeedItem(
        12,
        "ai",
        BOT,
        88,
        "Azure AI Foundry adds per-agent cost tracing",
        "https://azure.microsoft.com/blog",
        ("microsoft", "latestnews"),
    ),
    _SeedItem(
        14,
        "hemophilia",
        BOT,
        52,
        "FDA advisory committee reviews subcutaneous anti-TFPI therapy for inhibitor patients",
        "https://fda.gov",
        ("regulatory", "inhibitors"),
    ),
    _SeedItem(
        16,
        "ai",
        BOT,
        47,
        "A taxonomy of failure modes in production LLM agents",
        "https://arxiv.org/abs/2609.08812",
        ("research", "agents"),
    ),
    _SeedItem(
        18,
        "ai",
        BOT,
        30,
        "Speculative decoding in vLLM: benchmarks on consumer GPUs",
        "https://blog.vllm.ai",
        ("inference",),
    ),
    _SeedItem(
        21,
        "hemophilia",
        BOT,
        27,
        "Real-world bleed rates after switching from standard to extended half-life FVIII",
        "https://onlinelibrary.wiley.com/journal/hae",
        ("factor-viii", "real-world-evidence"),
    ),
    _SeedItem(
        24,
        "ai",
        BOT,
        25,
        "Mutation testing as a quality gate for agent-written code",
        "https://martinfowler.com",
        ("testing", "tooling"),
    ),
    _SeedItem(
        28,
        "hemophilia",
        BOT,
        21,
        "WFH updates guidance on prophylaxis trough targets",
        "https://wfh.org",
        ("guidelines", "prophylaxis"),
    ),
    _SeedItem(
        31,
        "ai",
        BOT,
        61,
        "Structured outputs now supported in streaming responses",
        "https://platform.openai.com/docs",
        ("latestnews", "api"),
    ),
    _SeedItem(
        36,
        "ai",
        BOT,
        72,
        "Microsoft Research: small language models as orchestrator sub-agents",
        "https://microsoft.com/research",
        ("microsoft", "research"),
    ),
    _SeedItem(
        39,
        "hemophilia",
        BOT,
        18,
        "Perioperative management on emicizumab: single-center retrospective",
        "https://ashpublications.org/bloodadvances",
        ("emicizumab", "surgery"),
    ),
    _SeedItem(
        42,
        "ai",
        BOT,
        34,
        "FastAPI adds native server-sent events responses",
        "https://fastapi.tiangolo.com/release-notes",
        ("tooling", "python"),
    ),
    _SeedItem(
        45,
        "ai",
        BOT,
        29,
        "Open model tops leaderboard for German legal text retrieval",
        "https://huggingface.co",
        ("models", "german"),
    ),
    _SeedItem(
        49,
        "hemophilia",
        BOT,
        15,
        "Home-treatment PK dashboards: patient-reported usability study",
        "https://jmir.org",
        ("pharmacokinetics", "digital-health"),
    ),
    _SeedItem(
        52,
        "ai",
        BOT,
        40,
        "Benchmarks are saturating: the case for task-specific evals",
        "https://huyenchip.com",
        ("research", "evals"),
    ),
    _SeedItem(
        55,
        "ai",
        BOT,
        36,
        "Reasoning model distills released under MIT license",
        "https://huggingface.co/models",
        ("models", "latestnews"),
    ),
)

SEED_COMMENTS = (
    _SeedComment(
        1,
        None,
        "mkessler",
        0.4,
        "Checkpointing between hops was the missing piece for long scrape jobs. Does resume replay tool calls or only messages?",
    ),
    _SeedComment(
        1,
        1,
        "dragos",
        0.3,
        "Messages only, per the release notes. Tool calls need to be idempotent on your side.",
    ),
    _SeedComment(
        1,
        None,
        "lena_r",
        0.2,
        "Typed message contracts between orchestrator and workers make the swarm far easier to test.",
    ),
    _SeedComment(
        2,
        None,
        "tbauer",
        1.2,
        "Trough levels in the under-6 cohort are the number to watch. The full table is in the supplementary appendix.",
    ),
    _SeedComment(
        5,
        None,
        "lena_r",
        6,
        "Five years of stable expression is meaningful. Durability past ten years remains open.",
    ),
    _SeedComment(
        7,
        None,
        "mkessler",
        11,
        "Per-agent cost tracing is what makes the cheap-scraper / expensive-poster split measurable.",
    ),
    _SeedComment(
        8,
        None,
        "tbauer",
        13,
        "Committee vote expected next week. Briefing documents are already public.",
    ),
)


def seed_demo(session: Session, now: datetime) -> bool:
    if session.scalar(select(func.count()).select_from(Item)):
        return False

    accounts = {name: _get_or_create_account(session, name, kind) for name, kind in ACCOUNTS}
    topics = {topic.slug: topic for topic in session.scalars(select(Topic))}
    tags = {(tag.topic_id, tag.name): tag for tag in session.scalars(select(TopicTag))}

    items = [
        Item(
            title=seed.title,
            url=seed.url,
            canonical_url=seed.url,
            domain=_domain(seed.url),
            topic=topics[seed.topic],
            account=accounts[seed.author],
            tags=[tags[(topics[seed.topic].id, name)] for name in seed.tags],
            upvotes=seed.score,
            created_at=now - timedelta(hours=seed.hours_ago),
        )
        for seed in SEED_ITEMS
    ]
    session.add_all(items)
    session.flush()

    comments: list[Comment] = []
    for seed in SEED_COMMENTS:
        comment = Comment(
            item_id=items[seed.item - 1].id,
            parent_id=comments[seed.parent - 1].id if seed.parent else None,
            account_id=accounts[seed.author].id,
            text=seed.text,
            created_at=now - timedelta(hours=seed.hours_ago),
        )
        session.add(comment)
        session.flush()
        comments.append(comment)
    return True


def _get_or_create_account(session: Session, username: str, kind: AccountKind) -> Account:
    account = session.scalar(select(Account).where(Account.username == username))
    if account is None:
        account = Account(username=username, kind=kind, can_publish=kind is not AccountKind.HUMAN)
        session.add(account)
        session.flush()
    return account


def _domain(url: str) -> str:
    host = urlsplit(url).hostname or ""
    return host.removeprefix("www.")


def main() -> None:
    engine = build_engine(settings.database_url)
    with session_scope(build_session_factory(engine)) as session:
        created = seed_demo(session, utc_now())
    engine.dispose()
    print("Seeded demo data." if created else "Items already exist; nothing seeded.")


if __name__ == "__main__":
    main()
