from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RawItem:
    title: str
    url: str
    source: str
    summary: str = ""
    published: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ScoredItem:
    raw: RawItem
    item_type: str = "unknown"
    tags: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    weighted_score: float = 0.0
    recommendation: str = "观望"
    rationale: str = ""
