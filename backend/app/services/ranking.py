from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class ItemStats:
    upvotes: int
    downvotes: int
    created_at: datetime
    provenance: float | None = None
    unique_clicks: int = 0


@dataclass(frozen=True, slots=True)
class RankingSettings:
    gravity: float = 1.3
    provenance_weight: float = 0.5
    click_weight: float = 0.0
    downvote_penalty: float = 0.8


def score(stats: ItemStats, now: datetime, settings: RankingSettings) -> float:
    net = stats.upvotes - stats.downvotes
    provenance = min(max(stats.provenance or 0.0, 0.0), 1.0)
    numerator = (
        1
        + max(net, 0)
        + settings.provenance_weight * provenance
        + settings.click_weight * max(stats.unique_clicks, 0)
    )
    age_hours = max((now - stats.created_at).total_seconds() / 3600, 0.0)
    penalty: float = settings.downvote_penalty ** max(-net, 0)
    return float(numerator / (age_hours + 2) ** settings.gravity * penalty)
