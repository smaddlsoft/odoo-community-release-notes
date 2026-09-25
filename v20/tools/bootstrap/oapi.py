"""Tiny Odoo JSON-2 client for the CE/EE runbots (keys live only in scratchpad/runbots.json)."""
import json, os, requests
_CFG = json.load(open(os.path.join(os.path.dirname(__file__), "runbots.json")))

def call(edition, model, method, **kw):
    c = _CFG[edition]
    r = requests.post(f"{c['url']}/json/2/{model}/{method}", json=kw, timeout=120,
                      headers={"Authorization": f"bearer {c['key']}", "X-Odoo-Database": c["db"],
                               "Content-Type": "application/json", "User-Agent": "oca-ce-release-notes"})
    if r.status_code != 200:
        raise RuntimeError(f"{edition} {model}.{method} -> {r.status_code}: {r.text[:500]}")
    return r.json()
