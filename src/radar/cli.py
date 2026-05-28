from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from radar.agents.pipeline import run_pipeline, save_report
from radar.collectors.arxiv import fetch_recent
from radar.config import FOCUS_PATH


def cmd_demo(_: argparse.Namespace) -> int:
    print("[demo] Using sample data (no API key required)")
    report, scored = run_pipeline(week_label="2026-W22-DEMO")
    path = save_report(report)
    _print_table(scored)
    print(f"\nReport written: {path}")
    return 0


def cmd_fetch(args: argparse.Namespace) -> int:
    print("[fetch] Pulling arXiv (network required)")
    items = fetch_recent(max_results=args.limit)
    if not items:
        print("[warn] No items fetched; check network or use demo")
        return 1
    report, scored = run_pipeline(items, week_label="2026-LIVE")
    path = save_report(report, filename="live_weekly_report.md")
    _print_table(scored)
    print(f"\nReport written: {path}")
    return 0


def _print_table(scored: list) -> None:
    print("\n--- Scorer results ---")
    print(f"{'Rec':<8} {'Score':<6} {'Type':<8} Title")
    print("-" * 72)
    for it in sorted(scored, key=lambda x: -x.weighted_score):
        title = it.raw.title[:48].replace("\n", " ")
        print(f"{it.recommendation:<8} {it.weighted_score:<6} {it.item_type:<8} {title}")


def main() -> int:
    parser = argparse.ArgumentParser(description="AI Tech Intelligence Radar CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_demo = sub.add_parser("demo", help="Offline demo with sample data")
    p_demo.set_defaults(func=cmd_demo)

    p_fetch = sub.add_parser("fetch", help="Fetch arXiv and generate report")
    p_fetch.add_argument("--limit", type=int, default=5)
    p_fetch.set_defaults(func=cmd_fetch)

    args = parser.parse_args()
    if not FOCUS_PATH.exists():
        print(f"[error] Missing focus.yaml: {FOCUS_PATH}")
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
