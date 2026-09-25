"""Render the Community release notes (Markdown) from the per-item dataset.

Usage:  python tools/render.py            (run from the version folder, e.g. v20/)

Inputs : data/odoo-20.0.yaml            one record per official release-note item
         data/oca-alternatives.yaml     pointers to OCA modules for EE-only areas
         data/highlights.yaml           editorial pick of CE highlights (ids)
Outputs: odoo-20-community-release-notes.md
         odoo-20-evidence.md            per-item evidence appendix
"""
import collections
import os

import yaml

VERSION = "20.0"
OFFICIAL = "https://www.odoo.com/odoo-20-release-notes"
PAGES_URL = "https://smaddlsoft.github.io/odoo-community-release-notes/v20/index.html"  # update if the repository moves
ICON = {"ce": "✅", "partial": "🟡", "ee": "🔒"}
LABEL = {"ce": "Community", "partial": "Partly Community", "ee": "Enterprise only"}
CONF = {"H": "verified", "M": "module-level", "L": "needs review"}

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
recs = yaml.safe_load(open(os.path.join(root, "data", f"odoo-{VERSION}.yaml"), encoding="utf-8"))
alts = yaml.safe_load(open(os.path.join(root, "data", "oca-alternatives.yaml"), encoding="utf-8"))
hl_path = os.path.join(root, "data", "highlights.yaml")
highlights = yaml.safe_load(open(hl_path, encoding="utf-8")) if os.path.exists(hl_path) else []
by_id = {r["id"]: r for r in recs}
sum_path = os.path.join(root, "data", f"summaries-{VERSION}.yaml")
SUMMARY = yaml.safe_load(open(sum_path, encoding="utf-8")) if os.path.exists(sum_path) else {}


def mods(ms):
    return ", ".join(f"`{m}`" for m in ms)


def oca_for(r):
    out = []
    for a in alts:
        if set(a["match"]) & set(r.get("ee_modules") or []):
            out += [f"`{o['module']}` ({o['repo']})" for o in a["oca"]]
    return out


def line(r, show_icon=True):
    """Two-line list item: title + summary, then a small line with the CE/EE details."""
    head = (ICON[r["status"]] + " " if show_icon else "") + f"**{r['title']}**"
    if SUMMARY.get(r["id"]):
        head += " — " + SUMMARY[r["id"]]
    detail = []
    if r.get("notes"):
        detail.append(r["notes"].rstrip("."))
    m = []
    if r.get("ce_modules"):
        m.append("CE " + mods(r["ce_modules"][:4]))
    if r.get("ee_modules"):
        m.append("EE " + mods(r["ee_modules"][:4]))
    if m:
        detail.append(" · ".join(m))
    if r["status"] != "ce":
        o = oca_for(r)
        if o and "OCA:" not in (r.get("notes") or ""):
            detail.append("OCA: " + ", ".join(o))
    tags = []
    if "change" in r.get("tags", []):
        tags.append("⚠️ change")
    if "iap" in r.get("tags", []):
        tags.append("IAP")
    if "backport" in r.get("tags", []):
        tags.append("backported")
    tags.append(f"[{r['confidence']}]")
    sub = "; ".join(detail + [" ".join(tags)])
    return f"- {head}  \n  <sub>{sub}</sub>"


sections = list(dict.fromkeys(r["section"] for r in recs))
count = collections.Counter(r["status"] for r in recs)
per = {s: collections.Counter(r["status"] for r in recs if r["section"] == s) for s in sections}
conf = collections.Counter(r["confidence"] for r in recs)
ee_apps = [s for s in sections if per[s]["ee"] == sum(per[s].values())]
mixed = [s for s in sections if s not in ee_apps]

L = []
w = L.append
w(f"# Odoo 20 — Community Edition release notes (DRAFT)\n")
w("> **Independent draft, not affiliated with or endorsed by Odoo S.A. or the Odoo Community Association (OCA).**  ")
w(f"> Built from the official [Odoo 20 release notes]({OFFICIAL}) (September 2026, {len(recs)} items). Each item was "
  "classified as available in Odoo Community (CE), partly available, or Enterprise-only (EE), and checked against the CE source "
  "([odoo/odoo@20.0](https://github.com/odoo/odoo/tree/20.0)), the EE 20.0 source (licensed copy, used locally only — "
  "no EE code is reproduced here) and CE/EE 20.0 runbot databases.  ")
w("> Section headers link back to the official text; item notes are our own wording. Please report errors (see README).  ")
w(f"> **Filterable version:** {PAGES_URL}\n")

w("## At a glance\n")
w(f"| | Items | Share |\n|---|---:|---:|")
for k in ("ce", "partial", "ee"):
    w(f"| {ICON[k]} {LABEL[k]} | {count[k]} | {100 * count[k] / len(recs):.0f}% |")
w(f"| **Total** | **{len(recs)}** | |\n")
w(f"Confidence: **{conf['H']}** items verified (a direct check, or the item belongs to an Enterprise-only app), "
  f"**{conf['M']}** module-level, **{conf['L']}** need review. Exact definitions: see [Method](#method) at the end.\n")
w("Legend: ✅ in Community · 🟡 partly (details in the note) · 🔒 Enterprise only · ⚠️ change = removal/rename/behaviour change "
  "worth a look before migrating · IAP = needs Odoo paid in-app services · backported = also shipped in an earlier version · "
  "[H]/[M]/[L] = confidence (verified / module-level / needs review).\n")

if highlights:
    w("## Highlights for Community users\n")
    for h in highlights:
        r = by_id.get(h["id"])
        if r:
            w(f"- **{r['title']}** ({r['section']}) — {h['why']}")
            img = f"img/{h['id'].replace('/', '__')}.png"
            if os.path.exists(os.path.join(root, img)):
                w(f"\n  ![{r['title']} in Odoo 20 Community]({img})")
                if h.get("caption"):
                    w(f"  <sub>Screenshot (CE test database): {h['caption']}</sub>")
                w("")
    w("")

w("## Heads-up for integrators and module maintainers\n")
w("Items in Community apps that remove, rename or replace existing behaviour (check your customisations and community "
  "modules that extend these areas):\n")
for r in recs:
    if "change" in r.get("tags", []) and r["status"] != "ee" and r["section"] not in ("Localizations", "Industries"):
        w(line(r))
w("")

tc_path = os.path.join(root, "data", f"technical-changes-{VERSION}.yaml")
if os.path.exists(tc_path):
    tc = yaml.safe_load(open(tc_path, encoding="utf-8"))
    w("### Technical changes for module developers\n")
    w("Mostly not mentioned in Odoo's notes. Where Odoo ships an automatic source rewrite (`odoo/upgrade_code/`), run it on "
      "your repository first: `odoo-bin upgrade_code --addons-path=<repo> --from 19.0 --dry-run`.\n")
    for t in tc["items"]:
        s = f"- **{t['title']}** — {t['what'].strip()}"
        if t.get("script"):
            s += f" Script: [`{t['script'].split('/')[-1]}`]({tc['base']}{t['script']})."
        s += f" *Affects: {t['impact']}.*"
        w(s)
    w("")

mc_path = os.path.join(root, "data", f"module-changes-{VERSION}.yaml")
if os.path.exists(mc_path):
    mc = yaml.safe_load(open(mc_path, encoding="utf-8"))
    w("### Module-level changes in Community (not in the official notes)\n")
    w(f"Diff of the CE module list ({mc['compared']}). Not part of Odoo's release notes, but it matters for every "
      "migration: `depends` in OCA modules must follow merged modules.\n")
    col = [n for n in mc["new"] if n.get("oca_name_collision")]
    if col:
        w("**⚠️ Name collisions with OCA modules** — new CE modules with the same technical name as existing OCA modules; "
          "the OCA modules cannot be migrated to 20.0 under their current name:\n")
        for n in col:
            w(f"- `{n['module']}` ({n['name']}) ↔ OCA {', '.join(n['oca_name_collision'])}")
        w("")
    w(f"**Removed or merged CE modules ({len(mc['removed'])})**\n")
    w("| Module (19.0) | Now in / status | OCA modules building on it |\n|---|---|---|")
    for r in mc["removed"]:
        o = ", ".join(f"`{x}`" for x in r["oca_modules_with_prefix"][:4]) or "—"
        now = r["now_in"] if r["now_in"] != "?" else "to check"
        w(f"| `{r['module']}` | {now}{' — ' + r['note'] if r.get('note') else ''} | {o} |")
    w("")
    w(f"**New CE modules ({len(mc['new'])})**: " + ", ".join(
        f"`{n['module']}`" + ("" if n["auto_install"] else "*") for n in mc["new"]) + "  \n<sub>* = not auto-installed</sub>\n")

w("## Overview per app\n")
w("| App | ✅ | 🟡 | 🔒 | Total |\n|---|---:|---:|---:|---:|")
for s in sections:
    c = per[s]
    w(f"| [{s}](#{s.lower().replace(' ', '-')}) | {c['ce']} | {c['partial']} | {c['ee']} | {sum(c.values())} |")
w("")

w("## Community and mixed apps\n")
for s in mixed:
    if s in ("Localizations", "Industries"):
        continue
    rs = [r for r in recs if r["section"] == s]
    anchor = rs[0].get("source", OFFICIAL)
    w(f"### {s}\n")
    w(f"<sub>[Official section]({anchor}) · {per[s]['ce']} ✅ · {per[s]['partial']} 🟡 · {per[s]['ee']} 🔒</sub>\n")
    for st in ("ce", "partial", "ee"):
        for r in rs:
            if r["status"] == st:
                w(line(r))
    w("")

w("### Localizations\n")
w("Localization items bundle several countries' changes. Base data (charts of accounts, taxes, states) is CE; tax-report "
  "rendering (`account_reports`), payroll and many EDI connectors are EE. **Each item needs review by maintainers of that "
  "country's localization.**\n")
for r in recs:
    if r["section"] == "Localizations":
        w(line(r))
w("")

w("### Industries\n")
w("Industry packages live in the public [odoo/industry](https://github.com/odoo/industry/tree/20.0) repository, but their "
  "manifests declare license OEEL-1 and they depend on Enterprise apps (Knowledge, Studio, Planning, POS Enterprise…), so none is "
  "installable on CE. Table = direct Enterprise dependencies.\n")
for r in recs:
    if r["section"] == "Industries":
        w(line(r))
w("")

w("## Enterprise-only apps\n")
w("All items of these sections belong to Enterprise modules (license OEEL-1). Pointers to Community (OCA) modules covering the "
  "same area are given where they exist — they are not feature-equivalent and most are not migrated to 20.0 yet.\n")
w("| App | Items | Possible OCA alternative |\n|---|---:|---|")
for s in ee_apps:
    rs = [r for r in recs if r["section"] == s]
    o = []
    for r in rs:
        for x in oca_for(r):
            if x not in o:
                o.append(x)
    w(f"| [{s}](#{s.lower().replace(' ', '-')}) | {len(rs)} | {', '.join(o) or '—'} |")
w("")
for s in ee_apps:
    rs = [r for r in recs if r["section"] == s]
    w(f"### {s}\n")
    w(f"<sub>[Official section]({rs[0].get('source', OFFICIAL)}) · module(s): {mods(sorted({m for r in rs for m in r['ee_modules']})[:6])}</sub>\n")
    for r in rs:
        w(f"- **{r['title']}** — {SUMMARY.get(r['id'], '')}")
    w("")

w("## Method\n")
w("Every item of the official page was read and assigned by hand to the module(s) it belongs to. Each module's edition "
  "(LGPL-3 = Community, OEEL-1 = Enterprise) comes from the module lists of a CE and an EE 20.0 test database. Evidence was "
  "then collected per item: its UI texts in the modules' translation templates, targeted code searches (Community: public "
  "source; Enterprise: licensed copy searched locally, module names only), checks on the test databases, CE screenshots, "
  "and the 19.0 → 20.0 module diff. Details: [README](README.md).\n")
w("| Confidence | Meaning |\n|---|---|")
w("| **Verified** [H] | A direct check backs the status: a distinctive UI text of the item occurs only in the named module(s); "
  "a code search written for this item hits the named module; a test-database check or a CE screenshot confirms it; the item "
  "belongs to an app that exists only as Enterprise module(s), so nothing of it can be in Community; or an industry package "
  "depends on Enterprise modules. |")
w("| **Module-level** [M] | The module the feature lives in is known and its edition verified, but no direct match was found "
  "for this particular item. Main risk: a Community app item whose UI actually comes from an Enterprise extension module. |")
w("| **Needs review** [L] | Judgement call without direct evidence: the item probably spans Community and Enterprise, or it "
  "bundles many changes (most localizations). |")
w("")
w("---\n")
w(f"*Generated by `tools/render.py` from `data/odoo-{VERSION}.yaml`. Per-item evidence: [odoo-20-evidence.md](odoo-20-evidence.md).*")
open(os.path.join(root, "odoo-20-community-release-notes.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# evidence appendix
E = ["# Odoo 20 — per-item evidence (DRAFT)\n",
     "Machine-generated from `data/odoo-20.0.yaml`. *UI string* = the phrase occurs in the module's translation template (.pot); "
     "*code* = regex match in module source (CE: public GitHub 20.0; EE: only module names are reported).\n"]
for s in sections:
    E.append(f"## {s}\n")
    for r in recs:
        if r["section"] != s:
            continue
        E.append(f"**{ICON[r['status']]} {r['title']}** `{r['id']}` — confidence {r['confidence']} ({CONF[r['confidence']]})  ")
        for e in r.get("evidence") or []:
            E.append(f"  - {e}")
        if not r.get("evidence"):
            E.append("  - no direct evidence yet (classified from the module/app it belongs to)")
        E.append("")
open(os.path.join(root, "odoo-20-evidence.md"), "w", encoding="utf-8").write("\n".join(E) + "\n")
print("rendered", len(recs), "items;", dict(count), dict(conf))
