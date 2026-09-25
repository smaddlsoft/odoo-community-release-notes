# Bootstrap pipeline (run locally)

Used once per release to produce the first draft of `data/odoo-<version>.yaml`. After that, the YAML is
edited by hand through PRs.

Expected working directory layout (outside any synced/public folder):

```
work/
├── parse_release_notes.py, match.py, build.py, decisions.py, oapi.py   (these files)
├── rn20.html            official release-notes page (curl)
├── odoo-ce/             git clone --depth 1 -b 20.0 https://github.com/odoo/odoo
├── ee/odoo-20.0+e.*/    Enterprise source, extracted from your own subscription download — NEVER commit
├── industry/            sparse clone of odoo/industry (manifests only)
├── runbots.json         {"ce": {"url","db","key"}, "ee": {...}} — API keys, NEVER commit
└── modules_runbot.json  dump of ir.module.module from both runbots
```

Steps: `parse_release_notes.py rn20.html items.json` → `match.py` (UI-string hits) → edit `decisions.py`
(section defaults + per-item overrides + probe regexes) → `build.py ../data/odoo-20.0.yaml`.
Only module names and CE file paths reach the output; EE files are searched but never copied.
