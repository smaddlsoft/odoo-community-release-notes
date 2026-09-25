"""Match release-note items against UI strings (.pot msgids) of CE and EE-only modules.

CE modules are read from the public GitHub clone, EE-only modules from the local
enterprise tarball.  Only module *names* end up in the output (no EE code).
"""
import json
import os
import re
import sys
from collections import defaultdict

SP = os.path.dirname(os.path.abspath(__file__))
CE = os.path.join(SP, "odoo-ce")
EE = os.path.join(SP, "ee", "odoo-20.0+e.20260924", "odoo", "addons")
mods = json.load(open(os.path.join(SP, "modules_runbot.json")))
lic = {n: m["license"] for n, m in mods["ee"].items()}


def module_dirs():
    out = {}
    for base in (os.path.join(CE, "addons"), os.path.join(CE, "odoo", "addons")):
        for n in os.listdir(base):
            if os.path.isfile(os.path.join(base, n, "__manifest__.py")):
                out[n] = ("CE", os.path.join(base, n))
    for n in os.listdir(EE):
        if n in out:
            continue
        if os.path.isfile(os.path.join(EE, n, "__manifest__.py")):
            ed = "CE" if lic.get(n) == "LGPL-3" else "EE"
            out[n] = (ed, os.path.join(EE, n))
    return out


MSGID = re.compile(r'^msgid "(.*)"\s*$|^"(.*)"\s*$|^msgstr', re.M)


def read_pot(path):
    ids, cur, inid = [], [], False
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith("msgid "):
                inid, cur = True, [line[7:].rstrip().rstrip('"')]
            elif line.startswith("msgstr"):
                if inid:
                    s = "".join(cur).replace('\\"', '"').replace("\\n", " ")
                    if s:
                        ids.append(" ".join(s.split()).lower())
                inid = False
            elif inid and line.startswith('"'):
                cur.append(line.strip()[1:-1])
    return ids


def build_index():
    idx = {}
    for n, (ed, path) in module_dirs().items():
        pot = os.path.join(path, "i18n", f"{n}.pot")
        if os.path.isfile(pot):
            idx[n] = (ed, read_pot(pot))
        else:
            idx[n] = (ed, [])
    return idx


STOP = {"odoo", "the", "a", "an", "new", "and", "or", "of", "to", "in", "on", "for", "with", "is", "are", "be",
        "can", "now", "has", "have", "been", "from", "by", "at", "as", "this", "that", "it", "its", "users", "user"}
QUOTE = re.compile(r'["“”«»]([^"“”«»]{3,60})["“”«»]')
CAPSEQ = re.compile(r"\b([A-Z][\w\-/]*(?:\s+(?:[A-Z][\w\-/]*|of|to|and|&|by|on|per|in)){1,5})")


def phrases(item):
    out = []
    t = item["title"]
    out.append(t)
    if ":" in t:
        out += [p.strip() for p in t.split(":") if p.strip()]
    out += QUOTE.findall(item["description"])
    for m in CAPSEQ.findall(item["description"]):
        out.append(m)
    res = []
    for p in out:
        p = " ".join(p.split()).strip(" .,;")
        words = [w for w in re.findall(r"\w+", p.lower()) if w not in STOP]
        if len(p) < 5 or not words:
            continue
        if p.lower() not in [r.lower() for r in res]:
            res.append(p)
    return res


def main():
    items = json.load(open(os.path.join(SP, "items.json"), encoding="utf-8"))
    idx = build_index()
    print("indexed modules:", len(idx), "CE:", sum(1 for v in idx.values() if v[0] == "CE"),
          "EE:", sum(1 for v in idx.values() if v[0] == "EE"), file=sys.stderr)
    # concatenate per module for fast substring search
    blobs = {n: (ed, "\n".join(ids)) for n, (ed, ids) in idx.items()}
    for it in items:
        hits = []
        for p in phrases(it):
            pl = p.lower()
            ce = [n for n, (ed, b) in blobs.items() if ed == "CE" and pl in b]
            ee = [n for n, (ed, b) in blobs.items() if ed == "EE" and pl in b]
            if ce or ee:
                hits.append({"phrase": p, "ce": ce[:12], "ce_n": len(ce), "ee": ee[:12], "ee_n": len(ee)})
        it["pot_hits"] = hits
    json.dump(items, open(os.path.join(SP, "items_hits.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump({n: ed for n, (ed, _) in idx.items()}, open(os.path.join(SP, "module_edition.json"), "w"), indent=0)


if __name__ == "__main__":
    main()
