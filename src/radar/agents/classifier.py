from __future__ import annotations

import re

from radar.models import RawItem

_TYPE_RULES: list[tuple[str, list[str]]] = [
    ("paper", [r"arxiv", r"paper", r"preprint", r"\d{4}\.\d{4,5}"]),
    ("model", [r"model", r"hugging\s*face", r"checkpoint", r"weights"]),
    ("repo", [r"github", r"repository", r"open.?source", r"release"]),
    ("tool", [r"sdk", r"api", r"framework", r"library", r"package"]),
    ("blog", [r"blog", r"announce", r"introducing"]),
]


def classify(item: RawItem) -> tuple[str, list[str]]:
    blob = f"{item.title} {item.summary} {item.url}".lower()
    item_type = "blog"
    for name, patterns in _TYPE_RULES:
        if any(re.search(p, blob) for p in patterns):
            item_type = name
            break

    tags: list[str] = []
    for kw in ("rag", "agent", "multimodal", "quantization", "llm", "vision", "reasoning"):
        if kw in blob:
            tags.append(kw)
    if not tags:
        tags.append("general")
    return item_type, tags
