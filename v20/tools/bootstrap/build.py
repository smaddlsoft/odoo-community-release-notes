"""Merge parsed items + string hits + decisions + code probes into data/odoo-20.0.yaml.

Writes only public facts (module names, CE file paths, our own notes) into the project folder.
"""
import ast
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import yaml

from decisions import O, SECTION_DEFAULTS, SPREADSHEET_NOTE

SP = os.path.dirname(os.path.abspath(__file__))
CE = os.path.join(SP, "odoo-ce")
EE = os.path.join(SP, "ee", "odoo-20.0+e.20260924", "odoo", "addons")
OUT = sys.argv[1]
items = json.load(open(os.path.join(SP, "items_hits.json"), encoding="utf-8"))
edition = json.load(open(os.path.join(SP, "module_edition.json")))
runbot = json.load(open(os.path.join(SP, "modules_runbot.json")))

# ---------------------------------------------------------------- code probes
EE_ONLY = sorted(n for n, e in edition.items() if e == "EE")
_ee_cache = None


def ee_corpus():
    global _ee_cache
    pkl = os.path.join(SP, "ee_corpus.pkl")
    if _ee_cache is None and os.path.exists(pkl):
        import pickle
        _ee_cache = pickle.load(open(pkl, "rb"))
    if _ee_cache is None:
        _ee_cache = []
        for n in EE_ONLY:
            base = os.path.join(EE, n)
            for root, dirs, files in os.walk(base):
                dirs[:] = [d for d in dirs if d not in ("i18n", "lib", "tests", "img", "fonts", "description")]
                for f in files:
                    if f.endswith((".py", ".xml", ".js", ".csv")):
                        try:
                            _ee_cache.append((n, open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()))
                        except OSError:
                            pass
        import pickle
        pickle.dump(_ee_cache, open(pkl, "wb"))
    return _ee_cache


def probe_ce(rx):
    r = subprocess.run(["git", "grep", "-l", "-I", "-i", "-E", rx, "--", "addons/*.py", "addons/*.xml", "addons/*.js",
                        "odoo/addons/*.py", "odoo/addons/*.xml", "odoo/addons/*.csv", ":!*/tests/*", ":!*/static/lib/*"],
                       cwd=CE, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    mods = {}
    for line in r.stdout.splitlines():
        parts = line.split("/")
        m = parts[2] if parts[0] == "odoo" else parts[1]
        mods.setdefault(m, []).append(line)
    return mods


def probe_ee(rx):
    c = re.compile(rx, re.I)
    mods = {}
    for n, txt in ee_corpus():
        if c.search(txt):
            mods[n] = mods.get(n, 0) + 1
    return mods


def fmt_mods(d, k=6):
    ks = sorted(d, key=lambda m: -(len(d[m]) if isinstance(d[m], list) else d[m]))
    return ", ".join(ks[:k]) + (f" (+{len(ks) - k})" if len(ks) > k else "")


# ---------------------------------------------------------------- industries
IND = os.path.join(SP, "industry")
ind_manifest = {}
for n in os.listdir(IND):
    mf = os.path.join(IND, n, "__manifest__.py")
    if os.path.isfile(mf):
        ind_manifest[n] = ast.literal_eval(open(mf, encoding="utf-8").read())
ce_manifest_cache = {}


def deps_of(m):
    if m in ind_manifest:
        return ind_manifest[m].get("depends", [])
    if m not in ce_manifest_cache:
        for base in (os.path.join(CE, "addons"), os.path.join(CE, "odoo", "addons"), EE):
            mf = os.path.join(base, m, "__manifest__.py")
            if os.path.isfile(mf):
                ce_manifest_cache[m] = ast.literal_eval(open(mf, encoding="utf-8").read()).get("depends", [])
                break
        else:
            ce_manifest_cache[m] = []
    return ce_manifest_cache[m]


def ee_deps(m):
    seen, stack, ee = set(), [m], set()
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        if edition.get(x) == "EE":
            ee.add(x)
        stack += deps_of(x)
    direct = [d for d in ind_manifest.get(m, {}).get("depends", []) if edition.get(d) == "EE"]
    return sorted(ee), direct


IND_MAP = {
    "Accounting Firm": ["accounting_firm"], "Agri-Equipment Rental": ["agri_equipment_rental"],
    "Beauty Parlor": ["beauty_parlor"], "Catering": ["catering"], "Community Care": ["community_care"],
    "Construction Builder": ["construction"], "Construction Developer": ["construction_developer"],
    "Custom Industrial Equipment": ["custom_industrial_equipment"], "Deposit module": ["deposit_management"],
    "Electronic Refurbishment": ["electronic_refurbishment"], "Excise module": ["excise_management"],
    "Hospitality industries": ["hotel", "holiday_house", "guest_house", "campsite"], "Hotel": ["hotel"],
    "Interior Design": ["interior_design"], "Machine and Tool Rental": ["machine_tool_rental"],
    "Mental Therapy": ["mental_therapy"], "Nonprofit Organization": ["non_profit_organization"],
    "Pet Groomer": ["pet_groomer"], "Physical Therapy": ["physical_therapy"],
    "Property Management": ["property_assets_distribution", "condominium", "industry_real_estate"],
    "Property Owner Association": ["condominium"], "Public Institution": ["public_institution"],
    "Real Estate": ["industry_real_estate", "real_estate"], "Talent Acquisition": ["headhunter"],
    "Vineyard": ["vineyard"],
}

# ---------------------------------------------------------------- localizations
PART = re.compile(r"\b(Accounting|Payroll|Point of Sale|Inventory|Employees|Time Off|Sales|Website|eCommerce|"
                  r"Attendances|Expenses|Fleet|Purchase|Manufacturing|Recruitment|Human Resources|HR|Documents|Sign|"
                  r"Timesheets|Project):\s")
CC_FIX = {"gb": "uk"}


def flag_cc(title):
    cps = [ord(ch) for ch in title if 0x1F1E6 <= ord(ch) <= 0x1F1FF]
    if len(cps) >= 2:
        cc = "".join(chr(c - 0x1F1E6 + 97) for c in cps[:2])
        return CC_FIX.get(cc, cc)
    return None


def l10n_mods(cc):
    pat = re.compile(rf"^l10n_{cc}(_|$)")
    ce = sorted(n for n, e in edition.items() if e == "CE" and pat.match(n))
    ee = sorted(n for n, e in edition.items() if e == "EE" and pat.match(n))
    return ce, ee


CHANGE_RX = re.compile(r"\b(removed|replaced|renamed|merged|no longer|discontinued|deprecated)\b", re.I)
IAP_RX = re.compile(r"\b(IAP|credits)\b")


# ---------------------------------------------------------------- main merge
def main():
    probes = {}
    jobs = []
    for i, it in enumerate(items):
        for rx in O.get(i, {}).get("p", []):
            jobs.append((i, rx))
    with ThreadPoolExecutor(8) as ex:
        ce_res = list(ex.map(lambda j: probe_ce(j[1]), jobs))
    ee_corpus()
    ee_res = [probe_ee(j[1]) for j in jobs]
    for (i, rx), cer, eer in zip(jobs, ce_res, ee_res):
        probes.setdefault(i, []).append((rx, cer, eer))

    records = []
    for i, it in enumerate(items):
        sec = it["section"]
        st, conf, cem, eem = SECTION_DEFAULTS[sec]
        o = O.get(i, {})
        rec = {
            "id": it["id"], "section": sec, "title": it["title"],
            "source": "https://www.odoo.com/odoo-20-release-notes#" + (it["section_anchor"] or ""),
            "status": o.get("s", st), "confidence": o.get("conf", conf if "s" not in o else ("M" if o.get("ce") or o.get("ee") else "L")),
            "ce_modules": list(o.get("ce", cem if o.get("s", st) != "ee" else [])),
            "ee_modules": list(o.get("ee", eem if o.get("s", st) != "ce" else [])),
            "evidence": [], "notes": o.get("n", ""), "flags": [],
            "tags": (["change"] if CHANGE_RX.search(it["description"]) else [])
                    + (["iap"] if IAP_RX.search(it["description"]) or "IAP" in o.get("n", "") else [])
                    + (["backport"] if "(available from" in it["description"] else [])
                    + list(o.get("t", [])),
        }
        if "conf" in o:
            rec["confidence"] = o["conf"]
        if sec == "Spreadsheet" and not rec["notes"]:
            rec["notes"] = SPREADSHEET_NOTE
        rec["evidence"] += list(o.get("ev", []))
        # industries
        if sec == "Industries":
            mods = [m for m in IND_MAP.get(it["title"], []) if m in ind_manifest]
            if mods:
                eeall = {}
                for m in mods:
                    eeall[m] = ee_deps(m)
                blocked = {m: v for m, v in eeall.items() if v[0]}
                if blocked:
                    rec["status"], rec["confidence"] = "ee", "H"
                    rec["ee_modules"] = sorted({d for v in blocked.values() for d in v[1]} or {d for v in blocked.values() for d in v[0]})
                    rec["evidence"].append("industry module(s) " + ", ".join(mods) + " (github.com/odoo/industry 20.0, manifest license "
                                           + "/".join(sorted({ind_manifest[m].get("license", "?") for m in mods})) + ") depend on EE module(s): "
                                           + "; ".join(f"{m} -> {', '.join(v[1] or v[0][:6])}" for m, v in blocked.items()))
                else:
                    rec["status"], rec["confidence"] = "ce", "H"
                    rec["evidence"].append("industry module(s) " + ", ".join(mods) + ": all dependencies are CE")
                rec["ce_modules"] = []
            else:
                rec["flags"].append("industry module not mapped")
        # localizations
        if sec == "Localizations":
            cc = flag_cc(it["title"])
            parts = [p for p in PART.findall(it["description"])]
            cem, eem = l10n_mods(cc) if cc else ([], [])
            rec["ce_modules"], rec["ee_modules"] = cem[:12], eem[:12]
            desc = it["description"]
            if parts and set(parts) <= {"Payroll"}:
                rec["status"], rec["confidence"] = "ee", "H"
                rec["notes"] = "Payroll localizations are EE (`l10n_%s_hr_payroll*`)" % cc
            elif parts == ["Accounting"] and "ISO 3166-2" in desc and len(desc) < 260:
                rec["status"], rec["confidence"] = "ce", "M"
                rec["notes"] = "Country states are base data (`base/data/res.country.state.csv`, CE)"
                n_states = sum(1 for l in open(os.path.join(CE, "odoo", "addons", "base", "data", "res.country.state.csv"), encoding="utf-8")
                               if l.startswith(f"state_{cc}_"))
                if n_states:
                    rec["confidence"] = "H"
                    rec["evidence"].append(f"CE source: odoo/addons/base/data/res.country.state.csv has {n_states} state_{cc}_* records")
            else:
                rec["status"] = "partial"
                rec["notes"] = ("Mixed: chart of accounts/taxes/data are CE; " + ("Payroll parts are EE; " if "Payroll" in parts else "")
                                + "tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization.")
            rec["localization_parts"] = parts
        # validate modules against the real module list
        for key, want in (("ce_modules", "CE"), ("ee_modules", "EE")):
            fixed = []
            for m in rec[key]:
                e = edition.get(m)
                if e is None:
                    rec["flags"].append(f"module `{m}` does not exist in 20.0")
                elif e != want:
                    rec["flags"].append(f"module `{m}` is {e}, not {want} (auto-moved)")
                    rec["ee_modules" if e == "EE" else "ce_modules"].append(m)
                else:
                    fixed.append(m)
            rec[key] = fixed
        # string evidence (.pot msgids)
        for h in it["pot_hits"]:
            n = h["ce_n"] + h["ee_n"]
            if 0 < n <= 4 and len(h["phrase"]) >= 8:
                side = []
                if h["ce"]:
                    side.append("CE: " + ", ".join(h["ce"]))
                if h["ee"]:
                    side.append("EE: " + ", ".join(h["ee"]))
                rec["evidence"].append(f"UI string \"{h['phrase']}\" -> " + " | ".join(side))
        # code probes
        for rx, cer, eer in probes.get(i, []):
            s = f"code /{rx}/ -> CE: {fmt_mods(cer) or '-'} | EE-only: {fmt_mods(eer) or '-'}"
            rec["evidence"].append(s)
        lic = {n: m["license"] for n, m in runbot["ee"].items()}
        if rec["ee_modules"]:
            rec["evidence"].append("module license (EE runbot ir.module.module): " + ", ".join(f"{m}={lic.get(m, '?')}" for m in rec["ee_modules"][:6]))
        if rec["ce_modules"]:
            ce_inst = {n for n, m in runbot["ce"].items() if m["license"] == "LGPL-3"}
            rec["evidence"].append("module license (CE runbot): " + ", ".join(f"{m}={'LGPL-3' if m in ce_inst else lic.get(m, '?')}" for m in rec["ce_modules"][:6]))
        records.append(rec)
    yaml.safe_dump(records, open(OUT, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False, width=140)
    from collections import Counter
    print(Counter(r["status"] for r in records))
    print(Counter(r["confidence"] for r in records))
    print("flags:", sum(1 for r in records if r["flags"]))
    for r in records:
        if r["flags"]:
            print("  ", r["id"], r["flags"])


if __name__ == "__main__":
    main()
