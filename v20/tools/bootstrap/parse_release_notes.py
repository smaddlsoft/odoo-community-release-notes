"""Parse the official Odoo release notes page into a flat JSON list of items.

Usage: python parse_rn.py rn20.html items.json
"""
import json
import re
import sys

from bs4 import BeautifulSoup

src, dst = sys.argv[1], sys.argv[2]
soup = BeautifulSoup(open(src, encoding="utf-8").read(), "lxml")
main = soup.find("main")


def clean(t):
    return " ".join(t.split())


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


items = []
section = None
section_anchor = None
subsection = None
for el in main.find_all(["h2", "h3", "h4", "p", "li"]):
    if el.name == "h2":
        section = clean(el.get_text())
        section_anchor = el.get("id")
        subsection = None
        continue
    if el.name in ("h3", "h4"):
        subsection = clean(el.get_text())
        continue
    if section is None:
        continue
    style = (el.get("style") or "").replace(" ", "")
    if el.name == "p" and "font-weight:bold" in style and "font-size:1.5em" in style:
        title = clean(el.get_text())
        container = el.parent
        parts = []
        for sib in el.find_next_siblings():
            txt = clean(sib.get_text(" "))
            if txt:
                parts.append(txt)
        items.append({
            "section": section,
            "section_anchor": section_anchor,
            "subsection": subsection,
            "title": title,
            "description": " ".join(parts),
        })

# de-duplicate ids per section
seen = {}
for it in items:
    base = f"{slug(it['section'])}/{slug(it['title'])}"[:90]
    n = seen.get(base, 0)
    seen[base] = n + 1
    it["id"] = base if n == 0 else f"{base}-{n + 1}"

json.dump(items, open(dst, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
from collections import Counter
c = Counter(it["section"] for it in items)
print(len(items), "items")
for k, v in c.items():
    print(f"  {v:4d}  {k}")
