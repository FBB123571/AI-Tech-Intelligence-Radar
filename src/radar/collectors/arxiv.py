from __future__ import annotations

import re
from xml.etree import ElementTree

import httpx

from radar.models import RawItem

ARXIV_API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_recent(query: str = "cat:cs.AI OR cat:cs.CL OR cat:cs.LG", max_results: int = 5) -> list[RawItem]:
    """Fetch recent arXiv entries (network optional; demo uses sample data)."""
    params = {"search_query": query, "start": 0, "max_results": max_results, "sortBy": "submittedDate", "sortOrder": "descending"}
    try:
        resp = httpx.get(ARXIV_API, params=params, timeout=15.0)
        resp.raise_for_status()
    except httpx.HTTPError:
        return []

    root = ElementTree.fromstring(resp.text)
    items: list[RawItem] = []
    for entry in root.findall("atom:entry", NS):
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip().replace("\n", " ")
        summary = (entry.findtext("atom:summary", default="", namespaces=NS) or "").strip()[:400]
        link = entry.find("atom:id", NS)
        url = link.text if link is not None else ""
        arxiv_id = ""
        m = re.search(r"arxiv\.org/abs/([\w./-]+)", url)
        if m:
            arxiv_id = m.group(1)
        items.append(
            RawItem(
                title=title,
                url=url,
                source="arXiv",
                summary=summary,
                metadata={"arxiv_id": arxiv_id, "has_code": "github.com" in summary.lower()},
            )
        )
    return items
