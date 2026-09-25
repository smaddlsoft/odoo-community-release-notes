# Odoo Community release notes — 20.0 (draft)

Which items of Odoo's official [Odoo 20 release notes](https://www.odoo.com/odoo-20-release-notes) you get in
**Odoo Community (CE)**, which are **partly** in CE, and which are **Enterprise-only (EE)**, plus what integrators and
module maintainers need to know before migrating.

> Status: **draft v0.4 (2026-09-25)**. Independent work, not affiliated with or endorsed by Odoo S.A. or the Odoo
> Community Association (OCA). Item titles come from Odoo's release notes; summaries, classifications and evidence are
> our own.

| File | What it is |
|---|---|
| [**Filterable page**](https://smaddlsoft.github.io/odoo-community-release-notes/v20/index.html) | Filter by Community / partly / Enterprise, app and text (served by GitHub Pages from `index.html`) |
| [odoo-20-community-release-notes.md](odoo-20-community-release-notes.md) | The same notes as Markdown (generated) |
| [odoo-20-evidence.md](odoo-20-evidence.md) | Per-item evidence behind each classification (generated) |
| [data/odoo-20.0.yaml](data/odoo-20.0.yaml) | **Source of truth**: one record per official item |
| [data/summaries-20.0.yaml](data/summaries-20.0.yaml) | One-line summary per item, in our own words |
| [data/module-changes-20.0.yaml](data/module-changes-20.0.yaml) | New / removed / merged CE modules 19.0 → 20.0, name collisions with OCA modules |
| [data/technical-changes-20.0.yaml](data/technical-changes-20.0.yaml) | Developer-facing changes (`ir.access`, OWL 3, `upgrade_code` scripts…) |
| [data/oca-alternatives.yaml](data/oca-alternatives.yaml) | Pointers to OCA modules for Enterprise-only areas |
| [data/highlights.yaml](data/highlights.yaml) | Editorial pick of CE highlights, with screenshot captions |
| `img/` | Screenshots of Odoo Community (20.0 test database), cropped and marked; named after the highlight's id |
| [tools/](tools/) | `render.py` (Markdown), `site.py` + `site_template.html` (page), `bootstrap/` (first-draft pipeline) |

## Method

1. **Parse** the official page into its 687 items (section + title).
2. **Module map:** list every 20.0 module with its license from a CE and an EE 20.0 test database (runbot, JSON-2 API).
   657 modules are LGPL-3 (Community), 877 are OEEL-1 (Enterprise).
3. **Read and assign every item by hand** to the module(s) it belongs to and a status: ✅ Community, 🟡 partly
   (some parts need Enterprise; the note says which), 🔒 Enterprise only. App sections start from the app's module;
   exceptions (e.g. a Gantt view inside a Community app) are set per item.
4. **Collect evidence automatically** for each item, then review conflicts:
   - *UI text:* distinctive phrases of the item (its title, quoted labels) are looked up in each module's translation
     template (`i18n/*.pot`), which contains all of the module's user-visible texts;
   - *code:* a search pattern written for the item is run over the Community source (public GitHub `20.0`) and over
     the Enterprise source (a licensed copy, searched locally; only module names are reported, no code is copied);
   - *test database:* checks on the CE/EE runbots (does a model, field or selection value exist; which module
     provides it; which modules were removed), plus screenshots of the Community UI;
   - *dependencies:* for industry packages, whether their dependency tree contains Enterprise modules.
5. **Module diff** of the CE `addons/` folder 19.0 → 20.0, cross-checked against 3,266 OCA module names.

### Confidence levels

Every item carries one of three levels. The per-item reasons are listed in [odoo-20-evidence.md](odoo-20-evidence.md).

| Level | Exact meaning | Items |
|---|---|---:|
| **Verified** (`H`) | At least one direct check backs the status: (a) a distinctive UI text of the item occurs only in the named module(s) (at most four modules match); (b) a code search written for this item hits the named module; (c) a test-database check or a CE screenshot confirms it; (d) the item belongs to an app that exists **only** as Enterprise module(s), so nothing of it can be in Community (125 items: AI, Appointments, Sign, Payroll, …); (e) an industry package's dependencies include Enterprise modules. | 263 |
| **Module-level** (`M`) | We know which module the feature lives in and verified that module's edition, but found no direct match for this particular item. Main risk: a Community app item whose UI actually comes from an Enterprise extension module. | 367 |
| **Needs review** (`L`) | A judgement call without direct evidence: the item likely spans Community and Enterprise and we could not pin down which parts, or it bundles many changes (most localizations: one item covers accounting, payroll and point of sale of a country). | 57 |

By status: ✅ Community 341 (56 verified, 278 module-level, 7 needs review) · 🟡 partly 90 (0 verified, 44 module-level, 46 needs review) ·
🔒 Enterprise 256 (207 verified, 45 module-level, 4 needs review).

## How to correct or extend

1. Edit the record in `data/odoo-20.0.yaml`: set `status` (`ce` | `partial` | `ee`), adjust `ce_modules` /
   `ee_modules`, write a short `notes` in your own words, add an `evidence` line (file path in `odoo/odoo`, test
   database check, screenshot…) and set `confidence: H` once verified. Summaries live in `data/summaries-20.0.yaml`.
2. Run `python tools/render.py` and `python tools/site.py` (needs PyYAML) from this folder.
3. Commit data and generated files together.

Rules: do not paste Odoo's release-note text beyond item titles, never paste Enterprise source code (reference EE
only by module name), and only publish screenshots of Community.

## Known limitations of this draft

- 57 items still need review (mostly localizations) and 367 are module-level only.
- "Partly" is coarse. The note says which part is Enterprise, but may be incomplete.
- UI behaviour was verified through the API, source code and 14 screenshots, not by testing each feature.
- OCA alternatives are pointers, not parity claims; none of the listed repositories had a 20.0 branch yet.
- Open checks that need a look at the Community and Enterprise user interface (all marked *needs review*):
  `calendar/manage-and-share-availabilities` (no "Share availabilities" button seen in CE Calendar),
  `dashboards/private-dashboards` and `dashboards/frozen-share-links` (CE Dashboards has "My Dashboard" and a Share
  button), `ecommerce/simplified-inventory-management`, `accounting/valuation-without-inventory`,
  `accounting/split-items-on-invoices`, `accounting/bank-consistency`.
