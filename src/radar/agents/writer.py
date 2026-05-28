from __future__ import annotations

from datetime import datetime

from radar.models import ScoredItem


def render_weekly_report(items: list[ScoredItem], week_label: str | None = None) -> str:
    week = week_label or datetime.now().strftime("%Y-W%W")
    focus = [i for i in items if i.recommendation == "关注"]
    watch = [i for i in items if i.recommendation == "观望"]
    skip = [i for i in items if i.recommendation == "暂不投入"]

    lines = [
        f"# AI Lab 技术情报周报 · {week}",
        "",
        f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')} · Demo 流水线（规则 Scorer，可替换为 LLM Agent）",
        "",
        "## 本周必读（关注）",
        "",
    ]
    if not focus:
        lines.append("_（本周暂无「关注」档位条目）_")
    for idx, it in enumerate(sorted(focus, key=lambda x: -x.weighted_score), 1):
        lines.extend(_item_block(idx, it))

    lines.extend(["", "## 观望", ""])
    for idx, it in enumerate(sorted(watch, key=lambda x: -x.weighted_score), 1):
        lines.extend(_item_block(idx, it))

    lines.extend(["", "## 附录：暂不投入但值得知晓", ""])
    for idx, it in enumerate(sorted(skip, key=lambda x: -x.weighted_score)[:5], 1):
        lines.extend(_item_block(idx, it, brief=True))

    lines.extend(
        [
            "",
            "## 数据说明",
            f"- 去重后条目：{len(items)}",
            f"- 关注 / 观望 / 暂不：{len(focus)} / {len(watch)} / {len(skip)}",
            "- 人工复核：轮值编辑（目标 <30 min）",
            "",
        ]
    )
    return "\n".join(lines)


def _item_block(idx: int, it: ScoredItem, brief: bool = False) -> list[str]:
    r = it.raw
    block = [
        f"{idx}. **[{r.title}]({r.url})** — **{it.recommendation}** — 综合 {it.weighted_score}/5",
        f"   - 来源：{r.source} · 类型：{it.item_type} · 标签：{', '.join(it.tags)}",
    ]
    if not brief:
        block.append(f"   - {it.rationale}")
    return block
