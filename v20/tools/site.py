"""Build the filterable release-notes page from data/.

Usage (from the version folder, e.g. v20/):
  python tools/site.py                   -> index.html (GitHub Pages; images referenced from img/)
  python tools/site.py --inline OUT.html -> page content with images embedded (for a single-file preview)
"""
import base64
import collections
import datetime
import hashlib
import json
import os
import sys

import yaml

VERSION = "20.0"
REPO_URL = "https://github.com/smaddlsoft/odoo-community-release-notes"  # update if the repository moves
VERSION_DIR = "v20"
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def load(name):
    return yaml.safe_load(open(os.path.join(root, "data", name), encoding="utf-8"))


recs = load(f"odoo-{VERSION}.yaml")
summ = load(f"summaries-{VERSION}.yaml")
alts = load("oca-alternatives.yaml")
highlights = load("highlights.yaml")
technical = load(f"technical-changes-{VERSION}.yaml")
modules = load(f"module-changes-{VERSION}.yaml")
inline = "--inline" in sys.argv


def img_ref(item_id):
    rel = f"img/{item_id.replace('/', '__')}.png"
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return None
    data = open(path, "rb").read()
    if inline:
        return "data:image/png;base64," + base64.b64encode(data).decode()
    return rel + "?v=" + hashlib.sha1(data).hexdigest()[:8]  # new URL whenever the image changes (no stale cache)


def oca(r):
    out = []
    for a in alts:
        if set(a["match"]) & set(r.get("ee_modules") or []):
            out += [f"{o['module']} ({o['repo']})" for o in a["oca"]]
    return out


items = [{
    "id": r["id"], "section": r["section"], "title": r["title"], "summary": summ.get(r["id"], ""),
    "status": r["status"], "confidence": r["confidence"], "ce": r.get("ce_modules") or [], "ee": r.get("ee_modules") or [],
    "notes": r.get("notes") or "", "tags": r.get("tags") or [], "evidence": r.get("evidence") or [],
    "source": r.get("source") or "", "oca": oca(r),
} for r in recs]
payload = {
    "meta": {"version": VERSION, "generated": datetime.date.today().isoformat(),
             "official": "https://www.odoo.com/odoo-20-release-notes",
             "repo": REPO_URL, "data": f"{REPO_URL}/blob/main/{VERSION_DIR}/data/odoo-{VERSION}.yaml",
             "readme": f"{REPO_URL}/blob/main/{VERSION_DIR}/README.md", "issues": f"{REPO_URL}/issues/new",
             "conf": dict(collections.Counter(r["confidence"] for r in recs))},
    "sections": list(dict.fromkeys(r["section"] for r in recs)),
    "items": items,
    "highlights": [dict(h, img=img_ref(h["id"])) for h in highlights],
    "technical": technical,
    "modules": modules,
}
data = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
body = open(os.path.join(here, "site_template.html"), encoding="utf-8").read().replace("/*__DATA__*/", data)

if inline:
    out = sys.argv[sys.argv.index("--inline") + 1]
    open(out, "w", encoding="utf-8").write(body)
else:
    out = os.path.join(root, "index.html")
    head, rest = body.split("<style>", 1)
    doc = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
           + head + "<style>\n[hidden]{display:none!important}\n" + rest.split("</style>", 1)[0] + "</style>\n</head>\n<body>\n"
           + rest.split("</style>", 1)[1] + "\n</body>\n</html>\n")
    open(out, "w", encoding="utf-8").write(doc)
print("wrote", out, f"{os.path.getsize(out) / 1024:.0f} KB", len(items), "items")
