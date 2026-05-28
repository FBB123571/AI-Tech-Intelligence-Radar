from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
REPORTS_DIR = ROOT / "reports"
FOCUS_PATH = ROOT / "src" / "focus.yaml"
SAMPLE_ITEMS = DATA_DIR / "sample" / "items.json"
