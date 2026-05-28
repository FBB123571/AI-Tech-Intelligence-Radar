from __future__ import annotations

import json
from pathlib import Path

from radar.agents.scorer import score_item
from radar.agents.writer import render_weekly_report
from radar.config import FOCUS_PATH, REPORTS_DIR, SAMPLE_ITEMS
from radar.models import RawItem, ScoredItem


def load_sample_items() -> list[RawItem]:
    with SAMPLE_ITEMS.open(encoding="utf-8") as f:
        rows = json.load(f)
    return [
        RawItem(
            title=r["title"],
            url=r["url"],
            source=r["source"],
            summary=r.get("summary", ""),
            published=r.get("published", ""),
            metadata=r.get("metadata", {}),
        )
        for r in rows
    ]


def run_pipeline(items: list[RawItem] | None = None, week_label: str = "2026-W22") -> tuple[str, list[ScoredItem]]:
    items = items or load_sample_items()
    scored = [score_item(it, FOCUS_PATH) for it in items]
    report = render_weekly_report(scored, week_label=week_label)
    return report, scored


def save_report(report: str, filename: str = "sample_weekly_report.md") -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / filename
    path.write_text(report, encoding="utf-8")
    return path
