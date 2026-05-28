from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from radar.agents.classifier import classify
from radar.models import RawItem, ScoredItem


def _load_focus(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _keyword_boost(text: str, focus: dict[str, Any]) -> float:
    boost = 0.0
    for area in focus.get("focus_areas", []):
        for kw in area.get("keywords", []):
            if kw.lower() in text.lower():
                boost += float(area.get("weight_boost", 0.05))
    for kw in focus.get("ignore_keywords", []):
        if kw.lower() in text.lower():
            return -1.0
    return min(boost, 0.35)


def score_item(item: RawItem, focus_path: Path) -> ScoredItem:
    focus = _load_focus(focus_path)
    weights = focus.get("scorer_weights", {})
    w_fit = float(weights.get("lab_fit", 0.30))
    w_rep = float(weights.get("reproducibility", 0.25))
    w_imp = float(weights.get("impact", 0.20))
    w_cost = float(weights.get("cost", 0.15))
    w_risk = float(weights.get("risk", 0.10))

    item_type, tags = classify(item)
    text = f"{item.title} {item.summary}"
    meta = item.metadata

    lab_fit = 3.0 + _keyword_boost(text, focus) * 10
    lab_fit = max(1.0, min(5.0, lab_fit))

    reproducibility = 3.5
    if item_type in ("repo", "model"):
        reproducibility = 4.5
    elif item_type == "paper" and meta.get("has_code"):
        reproducibility = 4.0

    impact = 3.0 + min(float(meta.get("stars", 0)) / 5000.0, 1.5)
    impact = max(1.0, min(5.0, impact))

    cost = 4.0 if meta.get("runs_on_single_gpu", True) else 2.5
    risk = 4.0 if meta.get("license_ok", True) else 2.0

    if _keyword_boost(text, focus) < 0:
        lab_fit = 1.5

    weighted = (
        lab_fit * w_fit
        + reproducibility * w_rep
        + impact * w_imp
        + cost * w_cost
        + risk * w_risk
    )

    thresholds = focus.get("thresholds", {})
    focus_min = float(thresholds.get("focus_min_score", 4.0))
    watch_min = float(thresholds.get("watch_min_score", 3.0))

    if weighted >= focus_min:
        rec = "关注"
    elif weighted >= watch_min:
        rec = "观望"
    else:
        rec = "暂不投入"

    rationale = (
        f"类型={item_type}；Lab契合={lab_fit:.1f}，可复现={reproducibility:.1f}，"
        f"影响力={impact:.1f}；综合 {weighted:.2f}。"
    )

    return ScoredItem(
        raw=item,
        item_type=item_type,
        tags=tags,
        scores={
            "lab_fit": round(lab_fit, 2),
            "reproducibility": round(reproducibility, 2),
            "impact": round(impact, 2),
            "cost": round(cost, 2),
            "risk": round(risk, 2),
        },
        weighted_score=round(weighted, 2),
        recommendation=rec,
        rationale=rationale,
    )
