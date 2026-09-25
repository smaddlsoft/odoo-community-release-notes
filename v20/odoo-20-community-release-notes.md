# Odoo 20 Community Edition Release Notes [Unofficial] (draft)

**👉 This is the Markdown copy. The main version, with screenshots, filters and search, is here: [https://smaddlsoft.github.io/odoo-community-release-notes/v20/index.html](https://smaddlsoft.github.io/odoo-community-release-notes/v20/index.html)**

> [!WARNING]
> **Early draft — please read with care.** The Community/Enterprise classification was produced with automated checks and hand review, but only part of it is verified in detail, so there are certainly errors and gaps. Each item shows its confidence level and evidence.  
> **Corrections and contributions are very welcome:** open an issue or send a pull request to https://github.com/smaddlsoft/odoo-community-release-notes.

> **Independent draft, not affiliated with or endorsed by Odoo S.A. or the Odoo Community Association (OCA).**  
> Informed by Odoo's official [Odoo 20 release notes](https://www.odoo.com/odoo-20-release-notes) (September 2026, 687 items). Each item was classified as available in Odoo Community (CE), partly available, or Enterprise-only (EE), and checked against the CE source ([odoo/odoo@20.0](https://github.com/odoo/odoo/tree/20.0)), the EE 20.0 source (licensed copy, used locally only — no EE code is reproduced here) and CE/EE 20.0 runbot databases.  
> Section headers link back to the official text; item notes are our own wording. Please report errors (see README).

## At a glance

| | Items | Share |
|---|---:|---:|
| ✅ Community | 341 | 50% |
| 🟡 Partly Community | 90 | 13% |
| 🔒 Enterprise only | 256 | 37% |
| **Total** | **687** | |

Confidence: **267** items verified (a direct check, or the item belongs to an Enterprise-only app), **362** module-level, **58** need review. Exact definitions: see [Method](#method) at the end.

Legend: ✅ in Community · 🟡 partly (details in the note) · 🔒 Enterprise only · ⚠️ change = removal/rename/behaviour change worth a look before migrating · IAP = needs Odoo paid in-app services · backported = also shipped in an earlier version · [H]/[M]/[L] = confidence (verified / module-level / needs review).

## Highlights for Community users

- **Offline mode** (General) — records can be created/edited/archived while offline, and past searches replayed — in the CE web client.

  ![Offline mode in Odoo 20 Community](img/general__offline-mode.png)
  <sub>Screenshot (CE test database): Offline mode on a German user interface — the orange “Offline arbeiten” (working offline) indicator in the top bar while the record stays open; its tooltip lists the changes still waiting to be sent.</sub>

- **Simplified access rights** (General) — ir.model.access and ir.rule merge into one ir.access model (group, operation, domain) and security/ir.access.csv; affects every module that ships security files.

  ![Simplified access rights in Odoo 20 Community](img/general__simplified-access-rights.png)
  <sub>Screenshot (CE test database): Access right form in developer mode — one record holds model, group, the Create/Read/Update/Delete operations and a domain.</sub>

- **Activities** (General) — activities can be assigned to a role (a team) instead of one person, in the redesigned dialogs.

  ![Activities in Odoo 20 Community](img/general__activities.png)
  <sub>Screenshot (CE test database): Schedule Activity dialog in the new dialog design — the new “Role” field assigns the activity to a team (here: Accounting Team).</sub>

- **Hierarchical view** (Contacts) — a hierarchy view shows companies with their contacts and sub-companies as a tree.

  ![Hierarchical view in Odoo 20 Community](img/contacts__hierarchical-view.png)
  <sub>Screenshot (CE test database): Contacts in the new hierarchy view — a company with its contacts and sub-companies as a tree (Acme Corporation; Azure Interior expands to its 3 contacts). The view is selected with the button top right.</sub>

- **Tax included/excluded on orders and invoices** (General) — switch tax-included/excluded prices per sales order, purchase order and invoice.

  ![Tax included/excluded on orders and invoices in Odoo 20 Community](img/general__tax-included-excluded-on-orders-and-invoices.png)
  <sub>Screenshot (CE test database): Sales order form — the new “Tax Excl.” switch above the order lines toggles between tax-excluded and tax-included prices.</sub>

- **Multiple partner identifiers** (General) — typed, validated partner identifiers (DUNS, national IDs) on the contact form.

  ![Multiple partner identifiers in Odoo 20 Community](img/general__multiple-partner-identifiers.png)
  <sub>Screenshot (CE test database): Contact form on a German user interface — the “+” next to the tax ID (TIN) offers further identifier types, here DUNS and company ID (Unternehmens-ID).</sub>

- **Translation** (General) — an in-context translation mode (module “Translation Mode”) shows every text on the screen with its translation and links to Weblate; translatable fields can also be imported/exported via CSV/Excel.

  ![Translation in Odoo 20 Community](img/general__translation.png)
  <sub>Screenshot (CE test database): Translation Mode on a German user interface — the side panel lists the texts of the screen (English source, German translation); the highlighted entry is the app title marked on the left, and “Translate” opens the term in Odoo’s Weblate project.</sub>

- **Multi-record drag and drop** (General) — reorder or move several records at once in list and Kanban views.

  ![Multi-record drag and drop in Odoo 20 Community](img/general__multi-record-drag-and-drop.png)
  <sub>Screenshot (CE test database): CRM pipeline on a German user interface — two selected opportunities (“2 ausgewählt”) dragged together to another stage; the placeholder reads “Move 2 records”. Select cards with Alt+click (Shift+click for a range).</sub>

- **Pin messages in the chatter** (General) — pin, filter and CC in the chatter; activities can be assigned to roles.

  ![Pin messages in the chatter in Odoo 20 Community](img/general__pin-messages-in-the-chatter.png)
  <sub>Screenshot (CE test database): Chatter — the new filter (All / Messages / Notes / Activities / Changes) and the pinned-messages button (pin icon).</sub>

- **Polls** (Discuss) — run quick polls inside any Discuss conversation, with emoji options, single or multiple answers and a time limit.

  ![Polls in Odoo 20 Community](img/discuss__polls.png)
  <sub>Screenshot (CE test database): Discuss on a German user interface — the new “Create Poll” dialog: question, options (with emoji), “allow multiple options” and a duration.</sub>

- **Multiple calendars in one place** (Calendar) — several calendars per user, shared team calendars, colleagues' calendars and pending activities in one view.

  ![Multiple calendars in one place in Odoo 20 Community](img/calendar__multiple-calendars-in-one-place.png)
  <sub>Screenshot (CE test database): Calendar — “+ Add a calendar” in the side panel for extra or shared calendars, and pending activities in the all-day row.</sub>

- **Lead distribution** (CRM) — per salesperson, choose how automatic lead assignment treats them: always in rotation, in rotation with a limit, or out of rotation.

  ![Lead distribution in Odoo 20 Community](img/crm__lead-distribution.png)
  <sub>Screenshot (CE test database): CRM → Configuration → Sales Teams → team member — the new “Auto-Assignment Rules”: Always in rotation, In rotation with a limit, Out of rotation.</sub>

- **Parent accounts** (Accounting) — parent accounts replace account groups and account codes become optional — structural change for charts of accounts and reporting modules.

  ![Parent accounts in Odoo 20 Community](img/accounting__parent-accounts.png)
  <sub>Screenshot (CE test database): Chart of accounts — the new “Parent Account” column (optional, shown via the column selector). The panel on the left is the existing grouping by code prefix, not the parent accounts.</sub>

- **Intuitive payment status** (Accounting) — payment states renamed (In Process → Paid → Reconciled); check custom reports and filters.

  ![Intuitive payment status in Odoo 20 Community](img/accounting__intuitive-payment-status.png)
  <sub>Screenshot (CE test database): Customer payments — the status column uses the renamed statuses: matched payments show “Reconciled” (formerly “Paid”); payments not yet matched show “Paid” (formerly “In Process”).</sub>

- **Employee Expenses menu item** (Accounting) — the separate Employee Expenses menu is gone: approved expenses become draft vendor bills and are handled with the other bills.

  ![Employee Expenses menu item in Odoo 20 Community](img/accounting__employee-expenses-menu-item.png)
  <sub>Screenshot (CE test database): Invoicing dashboard — approved expenses show up with the vendor bills in the Purchases card (“1 Expense”).</sub>

- **Withholding tax on payment improvements** (Accounting) — amount due / withhold due / net due split, and pay-only-withholding option in the payment wizard.
- **Dashboard** (Sales) — key figures and quick filters (to confirm, to deliver, to invoice, revenue) on top of the quotations list.

  ![Dashboard in Odoo 20 Community](img/sales__dashboard.png)
  <sub>Screenshot (CE test database): Quotations list — the new dashboard strip with To Confirm / To Deliver / To Invoice filters and revenue for the chosen period.</sub>

- **Product images** (Sales) — product images on sales order lines and in the quotation/order PDF.

  ![Product images in Odoo 20 Community](img/sales__product-images.png)
  <sub>Screenshot (CE test database): Sales order PDF — the product image is printed next to the order line (here: Screw Driver).</sub>

- **Description-only sales order lines** (Sales) — sales order lines no longer need a product (optional "Mandatory Product" setting).

  ![Description-only sales order lines in Odoo 20 Community](img/sales__description-only-sales-order-lines.png)
  <sub>Screenshot (CE test database): New quotation on a German user interface — an order line with only a description (“Auftragszeile ohne Produkt…”) and no product; above it the tax excluded/included switch (“exkl. Steuern / inkl. Steuern”).</sub>

- **Manufacturing order Kanban view** (Manufacturing) — MO Kanban grouped by week with component availability, deadlines and remaining time.

  ![Manufacturing order Kanban view in Odoo 20 Community](img/manufacturing__manufacturing-order-kanban-view.png)
  <sub>Screenshot (CE test database): Manufacturing orders Kanban — grouped by week with a workload bar, component availability and remaining time per order.</sub>

- **Continuous production** (Manufacturing) — record produced quantities per work order and start the next operations early; MOs can also be split and reset to draft.
- **Product replenishment** (Inventory) — one "Order" button, snooze and automate in the replenishment view; min/max suggestions from demand history.

  ![Product replenishment in Odoo 20 Community](img/inventory__product-replenishment.png)
  <sub>Screenshot (CE test database): Replenishment — a single “Order” button per line, next to “Automate” and “Snooze”.</sub>

- **Multiple currencies** (Point of Sale) — cash and bank payment methods accept several currencies (new “Currencies” field on the payment method); also service fees, snoozed products, simplified receipts and printer selection.

  ![Multiple currencies in Odoo 20 Community](img/point-of-sale__multiple-currencies.png)
  <sub>Screenshot (CE test database): Point of Sale → Configuration → Payment Methods → Cash — the new “Currencies” field (here EUR and USD).</sub>

- **Pay on Invoice provider** (Online Payments) — confirm orders without immediate payment; new Toss Payments provider, more Stripe/Mollie methods, wire transfers auto-confirmed from bank transactions.

  ![Pay on Invoice provider in Odoo 20 Community](img/online-payments__pay-on-invoice-provider.png)
  <sub>Screenshot (CE test database): Payment providers — the new “Pay on Invoice” provider (top left) and the new Toss Payments provider (bottom right).</sub>

- **llms.txt** (Website) — llms.txt, structured data by default, GTM field, banners, age verification and a reworked website builder.

  ![llms.txt in Odoo 20 Community](img/website__llms-txt.png)
  <sub>Screenshot (CE test database): Website settings, Tracking & SEO — the new llms.txt setting with “Edit llms.txt”.</sub>

- **Age verification popup** (Website) — a ready-made popup asks visitors to confirm their age and blocks access if they don't.

  ![Age verification popup in Odoo 20 Community](img/website__age-verification-popup.png)
  <sub>Screenshot (CE test database): Website editor — the age verification popup (“Are you 18 years or older?”), listed under Invisible Elements.</sub>

- **Mail: in-body tracking** (Technical) — tracking values are no longer stored — tracking messages are generated on the fly; affects modules that read mail.tracking.value.

## Déjà vu 😉

Good ideas travel. These Odoo 20 Community features have been around as OCA modules for a while. If you run one of these modules today, check whether you still need it in 20.0 (overlap is not the same as full parity).

| Odoo 20 feature | OCA module | Since | |
|---|---|---|---|
| CC email recipients | [`mail_composer_cc_bcc`](https://github.com/OCA/mail/tree/19.0/mail_composer_cc_bcc) (mail) | 15.0 | CC made it into core. OCA users have been cc'ing since 15.0. |
| Download attachments in bulk / Download invoice attachments | [`attachment_zipped_download`](https://github.com/OCA/knowledge/tree/19.0/attachment_zipped_download) (knowledge) | 14.0 | Zipping attachments in one go — the OCA has been zipping since 14.0. |
| Multiple partner identifiers | [`partner_identification`](https://github.com/OCA/partner-contact/tree/19.0/partner_identification) (partner-contact) | 8.0 | Several typed IDs per partner — the OCA has been counting them since 8.0. Yes, eight. |
| Peppol global location identifiers | [`partner_identification_gln`](https://github.com/OCA/partner-contact/tree/19.0/partner_identification_gln) (partner-contact) | 8.0 | GLN on partners, OCA-style since 8.0. |
| Sales order line numbering | [`sale_order_line_sequence`](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_sequence) (sale-workflow) | 9.0 | Line numbers! OCA users have been able to count their order lines since 9.0. |
| Mark orders as fully invoiced | [`sale_force_invoiced`](https://github.com/OCA/sale-workflow/tree/19.0/sale_force_invoiced) (sale-workflow) | 9.0 | "Consider it invoiced" — the OCA has been saying that since 9.0. |
| Product images | [`sale_order_report_product_image`](https://github.com/OCA/sale-reporting/tree/19.0/sale_order_report_product_image) (sale-reporting) | 11.0 | Pictures on quotations — framed by the OCA since 11.0. |
| Default Incoterm per vendor | [`purchase_partner_incoterm`](https://github.com/OCA/purchase-workflow/tree/19.0/purchase_partner_incoterm) (purchase-workflow) | 14.0 | A default Incoterm per vendor has been shipping from the OCA since 14.0. |
| Reset MO to draft | [`mrp_production_back_to_draft`](https://github.com/OCA/manufacture/tree/19.0/mrp_production_back_to_draft) (manufacture) | 14.0 | An undo button for manufacturing orders — OCA since 14.0. |
| Dynamic mailing lists | [`mass_mailing_list_dynamic`](https://github.com/OCA/mass-mailing/tree/19.0/mass_mailing_list_dynamic) (mass-mailing) | 10.0 | Mailing lists that fill themselves — the OCA has been sending them since 10.0. |
| Google Tag Manager (GTM) | [`website_google_tag_manager`](https://github.com/OCA/website/tree/19.0/website_google_tag_manager) (website) | 9.0 | Google Tag Manager in the settings — the OCA has been tagging along since 9.0. |
| Breadcrumbs on static pages | [`website_breadcrumb`](https://github.com/OCA/website/tree/18.0/website_breadcrumb) (website) | 8.0 | The OCA has been leaving breadcrumbs on website pages since 8.0. |
| llms.txt | [`website_llms`](https://github.com/OCA/website/tree/18.0/website_llms) (website) | 16.0 | Talking to LLMs — the OCA module is available from 16.0 on, well ahead of core. |
| Vendor purchase reference | [`stock_picking_supplier_ref`](https://github.com/OCA/stock-logistics-warehouse/tree/18.0/stock_picking_supplier_ref) (stock-logistics-warehouse) | 14.0 | The vendor's reference on the receipt — OCA since 14.0. |
| Return management | [`rma_sale`](https://github.com/OCA/rma/tree/19.0/rma_sale) (rma) | 12.0 | Returns straight from the customer portal — the OCA RMA modules have handled them since 12.0. |
| KPI banner on top of the new Invoicing dashboard (Invoices, Expenses, Receivable, Payable) | [`account_dashboard_banner`](https://github.com/OCA/account-financial-tools/tree/18.0/account_dashboard_banner) (account-financial-tools) | 16.0 | That KPI banner on the new Invoicing dashboard looks familiar — OCA account_dashboard_banner, since 16.0. |

## Heads-up for integrators and module maintainers

Items in Community apps that remove, rename or replace existing behaviour (check your customisations and community modules that extend these areas):

- ✅ **Material Symbols** — Icons switch from Font Awesome to Google Material Symbols.  
  <sub>Font Awesome replaced by Material Symbols in the web client — custom views/templates using `fa fa-*` icons need checking; CE `web`; ⚠️ change [H]</sub>
- ✅ **Partner autocomplete** — Partner autocomplete no longer turns industry data into partner tags; it stays in the chatter.  
  <sub>IAP service; industry no longer written as partner tags; CE `partner_autocomplete`; ⚠️ change IAP backported [M]</sub>
- ✅ **Simplified access rights** — Access rights and record rules are unified: an access right can carry a domain that limits which records it applies to.  
  <sub>`ir.model.access` and `ir.rule` are replaced by one `ir.access` model (model, group, operation, domain); modules ship `security/ir.access.csv`. Odoo provides `odoo/upgrade_code/19.4-00-ir-access.py` to convert module sources; CE `base`; ⚠️ change [H]</sub>
- ✅ **Mail: in-body tracking** — Tracking values are no longer stored; tracking messages are built on the fly. A separate module keeps stored tracking values for those who need them.  
  <sub>Tracking values are no longer stored by `mail`; the `mail.tracking.value` model moved to the new optional CE module `mail_tracking` (+ `mail_tracking_mass_mailing`, `mail_tracking_sms`). ⚠️ Same technical names as OCA `mail_tracking` / `mail_tracking_mass_mailing` (OCA/mail 18.0/19.0) — the OCA modules must be renamed for 20.0; CE `mail`, `mail_tracking`; ⚠️ change [H]</sub>
- 🟡 **Push notifications** — Push notifications no longer go through Firebase but through Odoo's own push service.  
  <sub>Browser web-push is CE; mobile-app push (formerly Firebase/OCN) is EE `mail_mobile`; CE `mail`, `web` · EE `mail_mobile`; ⚠️ change [M]</sub>
- ✅ **Employee Expenses menu item** — The separate 'Employee Expenses' menu is gone: approved expenses create draft bills in the expense journal.  
  <sub>Standalone 'Employee Expenses' menu removed; approved expenses create draft vendor bills in the expense journal; CE `hr_expense`; ⚠️ change [H]</sub>
- ✅ **Intuitive payment status** — Payment statuses renamed ('In Process' → 'Paid', 'Paid' → 'Reconciled'); 'Mark as Reconciled' moved to the action menu.  
  <sub>`account.payment.state` values are now draft / paid / reconciled / canceled / rejected; CE `account`; ⚠️ change [H]</sub>
- 🟡 **Manual reconciliation** — Manual reconciliation on any account; 'Allow Reconciliation' renamed 'Payment Reconciliation'.  
  <sub>Checkbox/logic in CE `account`; bank reconciliation view is EE; CE `account` · EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); ⚠️ change [M]</sub>
- ✅ **Parent accounts** — Parent accounts replace account groups to structure the chart of accounts; account codes become optional.  
  <sub>`account.group` is gone; `account.account.parent_id` structures the chart and `code` is no longer required; CE `account`; ⚠️ change [H]</sub>
- ✅ **Taxes in fiscal positions** — Taxes outside the fiscal position of an invoice are dropped, even without a replacement tax.  
  <sub>A product/account default tax outside the invoice's fiscal position is dropped even without a mapping; CE `account`; ⚠️ change [M]</sub>
- ✅ **Prevent app use** — Users without Attendances rights can no longer use the app.  
  <sub>Users without Attendances rights are blocked from the app; CE `hr_attendance`; ⚠️ change [M]</sub>
- ✅ **Remote Work** — Remote Work merged into Employees.  
  <sub>`hr_homeworking`, `hr_homeworking_calendar` and `hr_holidays_homeworking` were removed; work locations per weekday now live in `hr`; CE `hr`; ⚠️ change [H]</sub>
- ✅ **Simplified returns** — Return wizard removed; simpler returns.  
  <sub>The `stock.return.picking` wizard model no longer exists; CE `stock`; ⚠️ change [H]</sub>
- ✅ **Bill of materials** — Compare BoMs by quantities, merged status/availability columns, extra costs on the BoM, better component management.  
  <sub>BoM overview columns merged, extra-cost field on BoM, BoM comparison; CE `mrp`; ⚠️ change [M]</sub>
- ✅ **Flexible consumption** — Flexible consumption setting removed; all MOs consume flexibly.  
  <sub>Field `mrp.bom.consumption` removed; consumption is always flexible; CE `mrp`; ⚠️ change [H]</sub>
- 🟡 **Produce button** — One 'Produce' button replaces 'Produce' and 'Produce All'.  
  <sub>Single Produce button in CE Manufacturing; Shop Floor/Barcode parts EE; CE `mrp` · EE `mrp_workorder`, `stock_barcode_mrp`; ⚠️ change [M]</sub>
- ✅ **SOFORT** — SOFORT removed from all providers.  
  <sub>The `sofort` payment method record is gone; CE `payment`; ⚠️ change [H]</sub>
- ✅ **Employee access levels** — Employee access levels renamed, plus a restrictive 'Supervised' level.  
  <sub>POS employee access levels renamed; new restrictive 'Supervised' level; CE `pos_hr`; ⚠️ change [M]</sub>
- 🟡 **Profitability report** — Profitability panel removed from the project dashboard; new budget and margin reports.  
  <sub>The profitability panel is gone from the project dashboard. Margin reporting stays in CE (`project_account`, `sale_project_margin`); budget analysis needs EE `account_budget`; CE `project_account`, `sale_project_margin`, `project` · EE `account_budget`; OCA: `account_budget_oca` (account-budgeting); ⚠️ change [M]</sub>
- ✅ **Repair order status** — The 'Under Repair' status is removed.  
  <sub>`repair.order.state` no longer has 'under_repair'; CE `repair`; ⚠️ change [H]</sub>
- ✅ **Description-only sales order lines** — Order lines can be description-only; a 'Mandatory Product' setting enforces products.  
  <sub>`sale.order.line.product_id` is optional unless the 'Mandatory Product' setting is on; CE `sale`; ⚠️ change [H]</sub>
- ✅ **Events, Jobs, and Blog pages** — Standard 'Social Media' and 'Share' snippets in Events/Jobs/Blog sidebars.  
  <sub>Sidebar 'Follow Us'/'Share' blocks replaced by standard snippets; CE `website`, `website_event`, `website_blog`, `website_hr_recruitment`; ⚠️ change [M]</sub>

### Technical changes for module developers

Mostly not mentioned in Odoo's notes. Where Odoo ships an automatic source rewrite (`odoo/upgrade_code/`), run it on your repository first: `odoo-bin upgrade_code --addons-path=<repo> --from 19.0 --dry-run`.

- **Access rights: ir.access replaces ir.model.access and ir.rule** — The models ir.model.access and ir.rule no longer exist. A single ir.access model holds model, group, operation (e.g. "r", "cru") and an optional domain. Modules ship security/ir.access.csv with columns id,name,model_id,group_id/id,operation,domain instead of ir.model.access.csv + record-rule XML. Script: [`19.4-00-ir-access.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.4-00-ir-access.py). *Affects: every module with security files.*
- **Web client moves to OWL 3** — web ships OWL 3.0.0-alpha.49 plus an OWL 2 compatibility layer (web/static/src/owl2/). A large automatic rewrite of JS and templates is provided. Script: [`owl3-migration.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/owl3-migration.py). *Affects: every module with JS/OWL components or QWeb client templates.*
- **QWeb t-call: parameters passed as attributes** — t-set nodes inside t-call bodies are converted into attributes of the t-call (or moved before it when still needed). Xpaths that target t-set inside a t-call may need adapting. Script: [`19.1-00-t-call.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.1-00-t-call.py). *Affects: server-side QWeb templates and inheriting xpaths on t-call bodies.*
- **Account groups replaced by parent accounts** — account.group is gone; account.account has parent_id and code is optional. The script converts account group templates of charts of accounts. Script: [`19.3-00-account-groups.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.3-00-account-groups.py). *Affects: chart-of-accounts templates (l10n modules), reports on account.group.*
- **Account report XML: foldable lines and shorthand formula engines** — Report-line XML is rewritten (foldable handling, shorthand engine names such as domain/aggregation/tax_tags). Script: [`19.3-00-account-report-foldable.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.3-00-account-report-foldable.py). *Affects: modules defining account.report data (tax reports in l10n modules).*
- **XML data: type="base64" file fields become type="bytes"** — <field type="base64" file="..."/> is rewritten to type="bytes". Script: [`19.3-00-base64-in-xml.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.3-00-base64-in-xml.py). *Affects: data files loading binary files.*
- **Cache invalidation: registry.clear_cache → transaction.invalidate_ormcache** — Calls to registry.clear_cache(...) are replaced by transaction.invalidate_ormcache(...). Script: [`19.4-00-ormcache-on-transaction.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.4-00-ormcache-on-transaction.py). *Affects: Python code clearing ormcaches.*
- **_rec_names_search must be a tuple** — _rec_names_search = ['name'] becomes _rec_names_search = ('name',). Script: [`19.5-00-tuple-rec_names_search.py`](https://github.com/odoo/odoo/blob/20.0/odoo/upgrade_code/19.5-00-tuple-rec_names_search.py). *Affects: models defining _rec_names_search.*
- **Mail tracking values moved to the optional module mail_tracking** — Tracking messages are generated on the fly; mail.tracking.value now comes from the new CE module mail_tracking (not auto-installed). OCA's mail_tracking and mail_tracking_mass_mailing (OCA/mail) clash with the new CE names. *Affects: modules reading mail.tracking.value; OCA/mail modules with the same names.*
- **Font Awesome replaced by Material Symbols** — The web client no longer uses Font Awesome classes in its own templates. *Affects: views, templates and snippets using fa fa-* icon classes.*
- **PDF report engine becomes pluggable (Paper Muncher / wkhtmltopdf)** — New modules base_report_paper_muncher (new "Paper Muncher" engine, not auto-installed) and base_report_wkhtmltox (wkhtmltopdf/wkhtmltoimage engine, auto-installed). *Affects: deployment (Docker images, wkhtmltopdf installs), report customisations.*
- **Modules merged into core modules** — e.g. base_vat → base (+ l10n_eu_account_vies for VIES), stock_picking_batch → stock, website_sale_wishlist / website_sale_comparison → website_sale, hr_org_chart / hr_hourly_cost / hr_homeworking → hr, purchase_requisition_sale → purchase_alternative_sale. Full list in module-changes-20.0.yaml. *Affects: depends lists of community modules (e.g. OCA).*

### Module-level changes in Community (not in the official notes)

Diff of the CE module list (odoo/odoo 19.0 vs 20.0 (addons/), GitHub, 2026-09-25). Not part of Odoo's release notes, but it matters for every migration: `depends` in OCA modules must follow merged modules.

**⚠️ Name collisions with OCA modules** — new CE modules with the same technical name as existing OCA modules; the OCA modules cannot be migrated to 20.0 under their current name:

- `mail_tracking` (Discuss Tracking) ↔ OCA mail@18.0, mail@19.0
- `mail_tracking_mass_mailing` (Mass Mailing Tracking) ↔ OCA mail@18.0, mail@19.0

**Removed or merged CE modules (49)**

| Module (19.0) | Now in / status | OCA modules building on it |
|---|---|---|
| `account_add_gln` | account / account_edi_ubl_cii — GLN on partners | — |
| `account_peppol_advanced_fields` | to check | — |
| `account_peppol_response` | account_peppol | — |
| `base_iban` | base, account — IBAN handling in res.partner.bank (base/account) | — |
| `base_vat` | base, l10n_eu_account_vies — VAT check in base; VIES validation in new l10n_eu_account_vies | — |
| `delivery_mondialrelay` | (removed; EE delivery_sendcloud) | — |
| `delivery_stock_picking_batch` | stock_delivery | — |
| `hr_holidays_homeworking` | hr / hr_holidays | — |
| `hr_homeworking` | hr — hr.employee.location + weekday locations now in hr | — |
| `hr_homeworking_calendar` | hr | — |
| `hr_hourly_cost` | hr — hourly_cost field now in hr | — |
| `hr_org_chart` | hr — org chart controller now in hr | — |
| `hr_work_entry_holidays` | to check | — |
| `iot_base` | to check | — |
| `iot_box_image` | to check | — |
| `l10n_cn_city` | to check | — |
| `l10n_dk_nemhandel` | to check | — |
| `l10n_dk_nemhandel_response` | to check | — |
| `l10n_dk_oioubl` | to check | — |
| `l10n_ec_stock` | to check | — |
| `l10n_fr_hr_work_entry_holidays` | to check | — |
| `l10n_hu_edi_receive` | to check | — |
| `l10n_latam_base` | to check | — |
| `l10n_lk_invoice` | to check | — |
| `l10n_pl_bank_verification` | to check | — |
| `l10n_ro_cpv_code` | to check | — |
| `l10n_ro_edi_stock_batch` | to check | — |
| `l10n_sa_withholding_tax` | to check | — |
| `l10n_tr_nilvera` | moved to Enterprise — present in EE 20.0 tarball as OEEL | — |
| `l10n_tr_nilvera_base_vat` | to check | — |
| `l10n_tr_nilvera_edispatch` | moved to Enterprise | — |
| `l10n_tr_nilvera_einvoice` | moved to Enterprise | — |
| `l10n_tr_nilvera_einvoice_extended` | to check | — |
| `l10n_uy_pos` | to check | — |
| `pos_restaurant_adyen` | pos_adyen | — |
| `pos_restaurant_stripe` | to check | — |
| `pos_self_order_adyen` | to check | — |
| `pos_self_order_stripe` | to check | — |
| `pos_self_order_viva_com` | to check | — |
| `purchase_requisition_sale` | purchase_alternative_sale | — |
| `stock_picking_batch` | stock — stock.picking.batch model now defined in stock | `stock_picking_batch_account`, `stock_picking_batch_account_sale_type`, `stock_picking_batch_creation`, `stock_picking_batch_creation_split_kit` |
| `transifex` | (removed; translations via Weblate) | — |
| `website_sale_autocomplete` | website_address_autocomplete | — |
| `website_sale_collect_wishlist` | website_sale | — |
| `website_sale_comparison` | website_sale | `website_sale_comparison_hide_price`, `website_sale_comparison_specification_variant` |
| `website_sale_comparison_wishlist` | website_sale | — |
| `website_sale_mondialrelay` | (removed; EE delivery_sendcloud) | — |
| `website_sale_stock_wishlist` | website_sale | — |
| `website_sale_wishlist` | website_sale — product.wishlist model now in website_sale | `website_sale_wishlist_hide_price`, `website_sale_wishlist_keep` |

**New CE modules (51)**: `account_payment_custom`, `base_report_paper_muncher`*, `base_report_wkhtmltox`, `crm_sale_project`, `fleet_maintenance`, `hr_address_extended`*, `hr_calendar_google`, `iot_webserial`*, `l10n_be_pos`, `l10n_eg_edi_pos`, `l10n_es_website_sale`*, `l10n_eu_account_vies`*, `l10n_fr_payment`, `l10n_gr_edi_delivery_note`, `l10n_id_pos_self_order_qris`, `l10n_in_boe`*, `l10n_kr_sale`, `l10n_mk`*, `l10n_mm`*, `l10n_ph_invoice`*, `l10n_ph_sale`*, `l10n_pk_edi`*, `l10n_pk_edi_pos`*, `l10n_tw_edi_ecpay_sale`, `l10n_vn_edi_viettel_stock`, `mail_tracking`*, `mail_tracking_mass_mailing`, `mail_tracking_sms`, `marketing_card_event`, `mrp_delivery`, `mysubscription`, `populate`*, `portal_discuss`, `pos_bancontact_pay`*, `pos_partner_autocomplete`, `pos_sale_delivery`, `pos_sale_stock`, `pos_self_order_bancontact_pay`, `pos_self_order_event`, `pos_self_order_sms`, `pos_stock`, `printer`*, `purchase_alternative`*, `purchase_alternative_sale`, `purchase_alternative_stock`, `sale_project_margin`, `test_translation_mode`*, `website_address_autocomplete`, `website_mass_mailing_event`, `website_partnership`*, `website_sale_project`  
<sub>* = not auto-installed</sub>

## Overview per app

| App | ✅ | 🟡 | 🔒 | Total |
|---|---:|---:|---:|---:|
| [General](#general) | 36 | 2 | 3 | 41 |
| [Technical](#technical) | 4 | 1 | 0 | 5 |
| [Industries](#industries) | 0 | 0 | 25 | 25 |
| [Accounting](#accounting) | 22 | 6 | 17 | 45 |
| [Localizations](#localizations) | 10 | 41 | 4 | 55 |
| [AI](#ai) | 0 | 0 | 20 | 20 |
| [Appointments](#appointments) | 0 | 0 | 19 | 19 |
| [Appraisals](#appraisals) | 0 | 0 | 4 | 4 |
| [Attendances](#attendances) | 6 | 0 | 0 | 6 |
| [Barcode](#barcode) | 1 | 1 | 10 | 12 |
| [Blog](#blog) | 3 | 0 | 0 | 3 |
| [Calendar](#calendar) | 9 | 0 | 2 | 11 |
| [Contacts](#contacts) | 2 | 0 | 0 | 2 |
| [CRM](#crm) | 4 | 0 | 1 | 5 |
| [Dashboards](#dashboards) | 5 | 1 | 1 | 7 |
| [Discuss](#discuss) | 4 | 1 | 1 | 6 |
| [Documents](#documents) | 0 | 0 | 9 | 9 |
| [eCommerce](#ecommerce) | 34 | 1 | 3 | 38 |
| [eLearning](#elearning) | 1 | 0 | 0 | 1 |
| [Email Marketing](#email-marketing) | 14 | 0 | 0 | 14 |
| [Employees](#employees) | 3 | 0 | 1 | 4 |
| [ESG](#esg) | 0 | 0 | 1 | 1 |
| [Events](#events) | 1 | 0 | 0 | 1 |
| [Expenses](#expenses) | 2 | 0 | 1 | 3 |
| [Field Service](#field-service) | 0 | 0 | 1 | 1 |
| [Fleet](#fleet) | 0 | 0 | 1 | 1 |
| [Frontdesk](#frontdesk) | 0 | 0 | 1 | 1 |
| [Helpdesk](#helpdesk) | 0 | 0 | 3 | 3 |
| [Inventory](#inventory) | 19 | 0 | 3 | 22 |
| [Knowledge](#knowledge) | 0 | 0 | 1 | 1 |
| [Live Chat](#live-chat) | 0 | 0 | 1 | 1 |
| [Maintenance](#maintenance) | 2 | 0 | 1 | 3 |
| [Manufacturing](#manufacturing) | 20 | 2 | 2 | 24 |
| [Marketing Automation](#marketing-automation) | 0 | 0 | 6 | 6 |
| [Marketing Card](#marketing-card) | 3 | 0 | 0 | 3 |
| [Online Payments](#online-payments) | 16 | 0 | 0 | 16 |
| [Payroll](#payroll) | 0 | 0 | 15 | 15 |
| [Phone](#phone) | 0 | 0 | 10 | 10 |
| [Planning](#planning) | 0 | 0 | 20 | 20 |
| [PLM](#plm) | 0 | 0 | 4 | 4 |
| [Point of Sale](#point-of-sale) | 16 | 1 | 3 | 20 |
| [Project](#project) | 6 | 1 | 1 | 8 |
| [Purchase](#purchase) | 8 | 0 | 1 | 9 |
| [Quality](#quality) | 0 | 0 | 2 | 2 |
| [Recruitment](#recruitment) | 4 | 0 | 0 | 4 |
| [Referrals](#referrals) | 0 | 0 | 1 | 1 |
| [Rental](#rental) | 0 | 0 | 6 | 6 |
| [Repairs](#repairs) | 3 | 0 | 0 | 3 |
| [Sales](#sales) | 23 | 0 | 4 | 27 |
| [Shop Floor](#shop-floor) | 0 | 0 | 3 | 3 |
| [Sign](#sign) | 0 | 0 | 15 | 15 |
| [Social Marketing](#social-marketing) | 0 | 0 | 7 | 7 |
| [Spreadsheet](#spreadsheet) | 0 | 30 | 0 | 30 |
| [Studio](#studio) | 1 | 0 | 8 | 9 |
| [Subscriptions](#subscriptions) | 0 | 0 | 1 | 1 |
| [Time Off](#time-off) | 4 | 0 | 0 | 4 |
| [Timesheets](#timesheets) | 0 | 0 | 5 | 5 |
| [Website](#website) | 55 | 2 | 3 | 60 |
| [WhatsApp](#whatsapp) | 0 | 0 | 5 | 5 |

## Community and mixed apps

### General

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_18) · 36 ✅ · 2 🟡 · 3 🔒</sub>

- ✅ **Activities** — Activities can be assigned to a role instead of a person; the Schedule Activity dialog and chatter got UX improvements, and meeting activities show more context.  
  <sub>CE `mail`; [H]</sub>
- ✅ **Calendar view side panel** — In calendar views with scheduling enabled, drag records into the side panel to unschedule them.  
  <sub>Calendar view side panel (CE web); 'Scheduling' option of Gantt is EE; CE `web`; [M]</sub>
- ✅ **CC email recipients** — Add CC recipients when sending emails; the chatter shows who was in CC.  
  <sub>CE `mail`; 😉 déjà vu: OCA [`mail_composer_cc_bcc`](https://github.com/OCA/mail/tree/19.0/mail_composer_cc_bcc) since 15.0; [M]</sub>
- ✅ **Chatter filter** — Filter the chatter to show only messages or only tracked changes.  
  <sub>CE `mail`; [H]</sub>
- ✅ **Currency aggregates: date** — When totals are converted to another currency, the date of the exchange rate used is shown.  
  <sub>CE `web`; [M]</sub>
- ✅ **Decimal separator** — Both dot and comma are accepted as decimal separator when typing numbers, whatever the user's language.  
  <sub>CE `web`, `base`; [M]</sub>
- ✅ **Dialog design** — Redesigned dialogs.  
  <sub>CE `web`; [H]</sub>
- ✅ **Digest email KPIs** — More KPIs available in the periodic digest emails.  
  <sub>CE `digest`; [M]</sub>
- ✅ **Download attachments in bulk** — Download many attachments at once from the Technical menu, across models and records.  
  <sub>CE `base`, `web`; 😉 déjà vu: OCA [`attachment_zipped_download`](https://github.com/OCA/knowledge/tree/19.0/attachment_zipped_download) since 14.0; [M]</sub>
- ✅ **Email template preview** — Better email template preview, with navigation between sample records.  
  <sub>CE `mail`; [M]</sub>
- ✅ **Favorited searches** — Saved favourite searches in list views remember the visible columns.  
  <sub>CE `web`; [M]</sub>
- ✅ **File sharing on mobiles** — Share files from a phone to Odoo (e.g. a bill, expense receipt) to create records such as bills, expenses, tasks, leads, to-dos or time off.  
  <sub>PWA share-target is CE; OCR digitization of bills/expenses is EE (`*_extract`); CE `web`, `account`, `hr_expense`, `project`; [H]</sub>
- ✅ **Import product variants** — Import products with one line per variant, including attribute values, cost and on-hand quantity.  
  <sub>CE `base_import`, `product`; backported [M]</sub>
- ✅ **Incremental edits on duration fields** — Type +=, -=, *= or /= in duration fields to adjust the current value (e.g. +=2 adds two hours).  
  <sub>CE `web`; [M]</sub>
- ✅ **Label design** — Redesigned product, manufacturing and packaging labels.  
  <sub>CE `product`, `stock`, `mrp`; [M]</sub>
- ✅ **Link previews** — Links to an Odoo website shared on social platforms show a preview card.  
  <sub>CE `website`, `mail`; [M]</sub>
- ✅ **Link to current search** — Share a link to the current view that keeps filters, search and grouping.  
  <sub>CE `web`; [M]</sub>
- ✅ **List view: expand/collapse groups** — Alt+click expands or collapses all groups of the same level in list views.  
  <sub>CE `web`; [M]</sub>
- ✅ **Material Symbols** — Icons switch from Font Awesome to Google Material Symbols.  
  <sub>Font Awesome replaced by Material Symbols in the web client — custom views/templates using `fa fa-*` icons need checking; CE `web`; ⚠️ change [H]</sub>
- ✅ **Multi-record drag and drop** — Drag and drop several selected records at once in list and Kanban views.  
  <sub>CE `web`; [H]</sub>
- ✅ **Multiple partner identifiers** — Store several typed, validated identifiers per partner (e.g. DUNS or national IDs).  
  <sub>Multi-ID on the contact form is CE (`base`); identifier schemes for e-invoicing in `account_edi_ubl_cii`; CE `base`, `account`; 😉 déjà vu: OCA [`partner_identification`](https://github.com/OCA/partner-contact/tree/19.0/partner_identification) since 8.0; [H]</sub>
- ✅ **My Subscription page** — New 'My Subscription' page in the user menu with plan, IAP services and database management.  
  <sub>Module is LGPL in CE but only meaningful for databases with an odoo.com subscription; CE `mysubscription`; IAP [M]</sub>
- ✅ **Offline mode** — Create, edit, archive and delete records while offline, and re-run earlier searches.  
  <sub>CE `web`; [H]</sub>
- ✅ **Partner autocomplete** — Partner autocomplete no longer turns industry data into partner tags; it stays in the chatter.  
  <sub>IAP service; industry no longer written as partner tags; CE `partner_autocomplete`; ⚠️ change IAP backported [M]</sub>
- ✅ **Pin messages in the chatter** — Pin important messages in the chatter.  
  <sub>CE `mail`; [H]</sub>
- ✅ **Portal layout** — Portal users can reorder the cards on their portal home.  
  <sub>CE `portal`; [M]</sub>
- ✅ **Record deletion** — When a record cannot be deleted, Odoo offers to archive it instead.  
  <sub>CE `web`; [M]</sub>
- ✅ **Relative range tooltip** — Relative date filters (e.g. 'Last 30 days') show the actual dates in a tooltip.  
  <sub>CE `web`; [M]</sub>
- ✅ **Rich-text editor** — Simplified media toolbar in the rich-text editor.  
  <sub>CE `html_editor`; [M]</sub>
- ✅ **Product catalog: units of measure** — Choose the unit or packaging when adding products from the catalog.  
  <sub>CE `product`; [M]</sub>
- ✅ **Simplified access rights** — Access rights and record rules are unified: an access right can carry a domain that limits which records it applies to.  
  <sub>`ir.model.access` and `ir.rule` are replaced by one `ir.access` model (model, group, operation, domain); modules ship `security/ir.access.csv`. Odoo provides `odoo/upgrade_code/19.4-00-ir-access.py` to convert module sources; CE `base`; ⚠️ change [H]</sub>
- ✅ **Tablets: bottom sheets** — Bottom sheets (panels sliding up from the bottom) also on tablets in touch mode.  
  <sub>CE `web`; [M]</sub>
- ✅ **Tax included/excluded on orders and invoices** — Switch between tax-included and tax-excluded prices on sales orders, purchase orders and invoices; taxes can override the setting.  
  <sub>CE `account`, `sale`, `purchase`; [H]</sub>
- ✅ **Text messages** — Schedule text messages and use dynamic placeholders in SMS templates.  
  <sub>CE `sms`; [M]</sub>
- ✅ **Translation** — Optional in-context 'Translation Mode' (via command palette) to translate modules with Weblate; import/export of translatable fields in several languages via CSV/Excel.  
  <sub>Shipped as CE module `test_translation_mode` (sic) — install it to get the translation mode; CE `test_translation_mode`, `web`; [H]</sub>
- ✅ **Translation wizard** — New wizard to translate text and HTML fields.  
  <sub>CE `web`; [M]</sub>
- 🟡 **Mail plugins** — Gmail/Outlook plugins: search contacts, tasks or helpdesk tickets and log emails on them; pick recipients in multi-person threads.  
  <sub>Plugin backend for contacts/leads/tasks is CE; helpdesk tickets need EE Helpdesk; CE `mail_plugin`, `crm_mail_plugin`, `project_mail_plugin` · EE `helpdesk_mail_plugin`; OCA: `helpdesk_mgmt` (helpdesk); [M]</sub>
- 🟡 **Mobile** — Mobile: swipe down on the home screen for the command palette, date picker in a bottom sheet, better touch forms, new secure login screen.  
  <sub>Home-menu dashboard & mobile app login are EE (`web_enterprise`/mobile app); bottom-sheet date picker & touch forms are CE `web`; CE `web` · EE `web_enterprise`; OCA: `web_responsive` (web); [M]</sub>
- 🔒 **Gantt view** — Select a whole row/column in Gantt views, start/end buffers, and schedule/unschedule via a side panel (Studio option).  
  <sub>Gantt view is EE-only (`web_gantt`). OCA: web_timeline / project_timeline; EE `web_gantt`; [M]</sub>
- 🔒 **Map view: unlocated records** — Map view shows records without an address so they can be opened and fixed.  
  <sub>Map view is EE-only (`web_map`). OCA: web_view_leaflet_map; EE `web_map`; [M]</sub>
- 🔒 **Sendcloud shipping labels** — Choose PDF, ZPL or PNG for Sendcloud shipping labels.  
  <sub>Sendcloud connector is EE. OCA: delivery-carrier repo; EE `delivery_sendcloud`; [M]</sub>

### Technical

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_77) · 4 ✅ · 1 🟡 · 0 🔒</sub>

- ✅ **Mail: in-body tracking** — Tracking values are no longer stored; tracking messages are built on the fly. A separate module keeps stored tracking values for those who need them.  
  <sub>Tracking values are no longer stored by `mail`; the `mail.tracking.value` model moved to the new optional CE module `mail_tracking` (+ `mail_tracking_mass_mailing`, `mail_tracking_sms`). ⚠️ Same technical names as OCA `mail_tracking` / `mail_tracking_mass_mailing` (OCA/mail 18.0/19.0) — the OCA modules must be renamed for 20.0; CE `mail`, `mail_tracking`; ⚠️ change [H]</sub>
- ✅ **Many-to-one field improvements** — Many2one fields sync with the server and handle adding/removing values better, also with large lists.  
  <sub>CE `web`; [M]</sub>
- ✅ **Track source of postings** — Outgoing mail records record where their content came from, for auditing.  
  <sub>CE `mail`; [M]</sub>
- ✅ **Tracking user group changes** — Changes to a user's groups are logged in the user's chatter and in the server log.  
  <sub>CE `base`; [M]</sub>
- 🟡 **Push notifications** — Push notifications no longer go through Firebase but through Odoo's own push service.  
  <sub>Browser web-push is CE; mobile-app push (formerly Firebase/OCN) is EE `mail_mobile`; CE `mail`, `web` · EE `mail_mobile`; ⚠️ change [M]</sub>

### Accounting

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_79) · 22 ✅ · 6 🟡 · 17 🔒</sub>

- ✅ **Accounting Firms mode settings** — More flexible 'Accounting Firms mode' settings.  
  <sub>CE `account`; [M]</sub>
- ✅ **Bill/invoice matching rules** — 'Matching Rules' define payment tolerance and matching order for automatic bill/invoice reconciliation.  
  <sub>CE `account`; [M]</sub>
- ✅ **Cash journal entry hashing** — Cash journals can be secured with entry hashing on reconciliation.  
  <sub>CE `account`; [H]</sub>
- ✅ **Conversion rates** — Conversion rates are shown when registering foreign-currency payments.  
  <sub>CE `account`; [M]</sub>
- ✅ **Download invoice attachments** — Download a zip with all generated attachments (PDF, XML…) of selected invoices.  
  <sub>CE `account`; 😉 déjà vu: OCA [`attachment_zipped_download`](https://github.com/OCA/knowledge/tree/19.0/attachment_zipped_download) since 14.0; [L]</sub>
- ✅ **Employee Expenses menu item** — The separate 'Employee Expenses' menu is gone: approved expenses create draft bills in the expense journal.  
  <sub>Standalone 'Employee Expenses' menu removed; approved expenses create draft vendor bills in the expense journal; CE `hr_expense`; ⚠️ change [H]</sub>
- ✅ **Exchange entries** — Exchange differences are grouped into one line per invoice, with expandable details.  
  <sub>CE `account`; [M]</sub>
- ✅ **Improved duplicate detection** — Two-level duplicate warnings on invoices and bills (red: likely duplicate, yellow: check).  
  <sub>CE `account`; backported [M]</sub>
- ✅ **Intuitive payment status** — Payment statuses renamed ('In Process' → 'Paid', 'Paid' → 'Reconciled'); 'Mark as Reconciled' moved to the action menu.  
  <sub>`account.payment.state` values are now draft / paid / reconciled / canceled / rejected; CE `account`; ⚠️ change [H]</sub>
- ✅ **Inventory valuation** — Accrual entries (bills to receive, billed not received, etc.) can be created from the inventory valuation closing report.  
  <sub>Accrual actions (Bills To Receive, Billed Not Received…) are in CE purchase/account; CE `purchase`, `account`, `stock_account`; [M]</sub>
- ✅ **Multiple invoice details** — When sending several invoices at once, the dialog shows how each will be sent.  
  <sub>CE `account`; [M]</sub>
- ✅ **New currency: Caribbean Guilder** — Caribbean Guilder (XCG) added and set as default currency for Curaçao and Sint Maarten.  
  <sub>CE `base`; backported [H]</sub>
- ✅ **Parent accounts** — Parent accounts replace account groups to structure the chart of accounts; account codes become optional.  
  <sub>`account.group` is gone; `account.account.parent_id` structures the chart and `code` is no longer required; CE `account`; ⚠️ change [H]</sub>
- ✅ **Peppol global location identifiers** — Add GLN location identifiers to delivery contacts for Peppol.  
  <sub>CE `account_edi_ubl_cii`, `account_peppol`; 😉 déjà vu: OCA [`partner_identification_gln`](https://github.com/OCA/partner-contact/tree/19.0/partner_identification_gln) since 8.0; backported [H]</sub>
- ✅ **Prevent double payments in the payment wizard** — The payment wizard deducts pending payments to avoid paying twice, and sorts outstanding payments by date.  
  <sub>CE `account`; [M]</sub>
- ✅ **Professional percentage for receipts** — The 'Professional' percentage column also exists on purchase receipts.  
  <sub>CE `account`; backported [M]</sub>
- ✅ **Purchase order matching** — Better bill-to-PO matching: auto-complete checks existing lines first, shows a summary, warns on price/quantity differences, and allows unmatching.  
  <sub>CE `purchase`, `account`; [H]</sub>
- ✅ **Reset to Draft action in list views** — 'Reset to Draft' as a batch action in any journal entry list.  
  <sub>CE `account`; [M]</sub>
- ✅ **Split items on invoices** — Split selected journal items of an invoice, e.g. across quantities, assets or accounts.  
  <sub>CE `account`; [L]</sub>
- ✅ **Taxes in fiscal positions** — Taxes outside the fiscal position of an invoice are dropped, even without a replacement tax.  
  <sub>A product/account default tax outside the invoice's fiscal position is dropped even without a mapping; CE `account`; ⚠️ change [M]</sub>
- ✅ **Valuation without Inventory** — Track stock on hand and valuation without installing Inventory.  
  <sub>CE `stock_account`, `account`; [L]</sub>
- ✅ **Withholding tax on payment improvements** — Bills with withholding tax show amount due, withholding due and net due; the payment wizard can pay either part or both.  
  <sub>CE `l10n_account_withholding_tax`; [M]</sub>
- 🟡 **Bank consistency** — Journal entries on bank accounts must come from bank transactions; clearer feedback on statement balance inconsistencies.  
  <sub>CE `account` · EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [L]</sub>
- 🟡 **Bill options display** — Bill line options (depreciation model, vehicle, deferral) are stacked under the account.  
  <sub>CE `account` · EE `account_asset`, `account_accountant`; OCA: `account_asset_management` (account-financial-tools), `account_reconcile_oca` (account-reconcile); [L]</sub>
- 🟡 **Customer invoice reminders** — Send invoice reminders manually from the invoice list or form; automatic reminders configurable in settings.  
  <sub>Invoice reminder sending in CE `account`; follow-up levels/automation EE; CE `account` · EE `account_followup`; OCA: `account_credit_control` (credit-control); [M]</sub>
- 🟡 **Invoice email attachments** — Add files from Documents or earlier chatter attachments when emailing an invoice.  
  <sub>Chatter attachments CE; Documents-app files EE; CE `account` · EE `documents_account`; backported [M]</sub>
- 🟡 **Manual reconciliation** — Manual reconciliation on any account; 'Allow Reconciliation' renamed 'Payment Reconciliation'.  
  <sub>Checkbox/logic in CE `account`; bank reconciliation view is EE; CE `account` · EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); ⚠️ change [M]</sub>
- 🟡 **Onboarding improvements** — Easier accounting onboarding for e-invoicing and tax setup.  
  <sub>CE `account` · EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [L]</sub>
- 🔒 **Analytic distribution for write-offs** — Set an analytic distribution on write-offs during reconciliation.  
  <sub>`account.reconcile.wizard` (write-off) lives in EE `account_accountant`; EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [H]</sub>
- 🔒 **Annual report layout** — Annual reports use the company's document layout.  
  <sub>Annual/financial reports are EE (`account_reports`). OCA: account_financial_report, mis_builder; EE `account_reports`; [M]</sub>
- 🔒 **Asset depreciation** — Depreciation accepts rates and decimal numbers.  
  <sub>OCA: account_asset_management; EE `account_asset`; [M]</sub>
- 🔒 **Bank reconciliation summary report** — New bank reconciliation summary report (reconciled vs unreconciled at period end).  
  <sub>EE `account_reports`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder); [M]</sub>
- 🔒 **Bank synchronization: Syncfy** — Syncfy added as bank synchronization provider for Latin America.  
  <sub>Bank synchronization is an Odoo-hosted service (no bank-sync module in the 20.0 source tarball). OCA: bank-statement-import; [M]</sub>
- 🔒 **Bill line prediction** — When encoding a bill, product, account, taxes, analytics and vehicle are suggested from bill history and the label.  
  <sub>Line prediction (`_predict_*`) is in EE `account_accountant`; EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [M]</sub>
- 🔒 **Cumulative Translation Adjustment (CTA)** — Auditable Cumulative Translation Adjustment (CTA) line in balance sheet, trial balance and general ledger.  
  <sub>EE `account_reports`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder); [M]</sub>
- 🔒 **Currency exchange rate providers** — New automatic currency rate providers: Azerbaijan, Georgia, Kazakhstan, Saudi Arabia, Uzbekistan.  
  <sub>OCA: currency_rate_update; EE `currency_rate_live`; backported [M]</sub>
- 🔒 **Intercompany purchase order matching** — Synchronised inter-company vendor bills are matched with the synchronised purchase orders.  
  <sub>EE `account_inter_company_rules`; [L]</sub>
- 🔒 **Multi-ledger consolidation** — Multi-ledger consolidation now includes (rather than excludes) journals.  
  <sub>EE `account_reports`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder); [M]</sub>
- 🔒 **Optimized data entry** — Faster bank statement encoding with reconciliation-model shortcuts and transaction batching.  
  <sub>EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [M]</sub>
- 🔒 **PAIN version setting** — The PAIN (ISO 20022) version is set per payment method instead of per journal.  
  <sub>PAIN/ISO20022 payment files are EE (`account_iso20022`). OCA: account_banking_sepa_credit_transfer (bank-payment); EE `account_iso20022`; [H]</sub>
- 🔒 **Pay bills from Odoo** — Pay bills (single or batch) from Odoo with one signature via payment initiation (PISP).  
  <sub>EE `account_online_payment`; [L]</sub>
- 🔒 **Reconciliation with multiple accounts** — Split a bank transaction across several accounts more easily in reconciliation.  
  <sub>EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [M]</sub>
- 🔒 **Reminder workflow** — Simpler workflow for automatic and manual payment reminders.  
  <sub>OCA: account_credit_control; EE `account_followup`; [M]</sub>
- 🔒 **Run Auto Reconciliation** — Re-run automatic bank reconciliation on demand.  
  <sub>EE `account_accountant`; OCA: `account_reconcile_oca` (account-reconcile); [M]</sub>
- 🔒 **Simplification of asset models** — Asset models become depreciation models; asset settings live on the asset accounts.  
  <sub>OCA: account_asset_management; EE `account_asset`; ⚠️ change [M]</sub>

### Attendances

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_84) · 6 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Automatic check-out time** — Employees without fixed hours can set an automatic check-out time.  
  <sub>CE `hr_attendance`; [M]</sub>
- ✅ **Overtime analysis report** — New overtime analysis report showing which rule applied.  
  <sub>CE `hr_attendance`; [M]</sub>
- ✅ **Overtime rulesets** — Smart button to link new employees to an overtime ruleset.  
  <sub>CE `hr_attendance`; [M]</sub>
- ✅ **Photo at check-in** — Take a photo at check-in when the device has a camera.  
  <sub>CE `hr_attendance`; [M]</sub>
- ✅ **Prevent app use** — Users without Attendances rights can no longer use the app.  
  <sub>Users without Attendances rights are blocked from the app; CE `hr_attendance`; ⚠️ change [M]</sub>
- ✅ **Public holiday option ruleset** — Overtime rates for public holidays in rulesets.  
  <sub>CE `hr_attendance`; [M]</sub>

### Barcode

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_85) · 1 ✅ · 1 🟡 · 10 🔒</sub>

- ✅ **Bulk lot/serial number generation** — Generate lots/serial numbers in bulk.  
  <sub>Lot/serial generation is CE `stock`; Barcode adds scanning; CE `stock`; [H]</sub>
- 🟡 **Packages: pre-encoded contents** — Pre-encode package contents announced by the vendor; scanning the package receives it with its contents.  
  <sub>Pre-encoding packages in CE Inventory; scanning in EE Barcode; CE `stock` · EE `stock_barcode`; [M]</sub>
- 🔒 **Backorders** — Choose whether to create a backorder from Barcode.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Barcode product creation** — Scan an unknown barcode to create the product via Barcode Lookup.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Batch receipts** — Receipts from the same vendor are suggested as a batch.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Fixed button positions** — Buttons keep a fixed position to avoid mistakes.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Inventory count** — Enter the total counted quantity manually during inventory counts.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Light users** — Light users can be limited to the Barcode app.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Manual entry** — Enter lot numbers and quantities manually when scanning is impossible.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Manufacturing operations** — Manufacturing in Barcode: irrelevant settings removed, reserved lots only shown when enabled, mandatory scans no longer block by-product edits.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Mobile: user login button** — Login button in the mobile view.  
  <sub>EE `stock_barcode`; [H]</sub>
- 🔒 **Packages: untracked goods** — Untracked goods registered earlier stay in the package contents when scanned later.  
  <sub>EE `stock_barcode`; [H]</sub>

### Blog

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_86) · 3 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Blog module redesign** — More styles and options for blog posts, blog home and category pages.  
  <sub>CE `website_blog`; [H]</sub>
- ✅ **Recommended post** — Show a 'Recommended Post' at the end of a blog post.  
  <sub>CE `website_blog`; [H]</sub>
- ✅ **Scheduled blog posts** — Followers get an email when a scheduled post goes live.  
  <sub>CE `website_blog`; [M]</sub>

### Calendar

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_87) · 9 ✅ · 0 🟡 · 2 🔒</sub>

- ✅ **Browse other calendars** — Show colleagues' calendars from the sidebar.  
  <sub>CE `calendar`; [M]</sub>
- ✅ **Detection of times in "All day" event titles** — Events created in the 'All day' row pick up a time written in the title (e.g. '2 PM Meeting').  
  <sub>CE `calendar`; [M]</sub>
- ✅ **Google and Outlook synchronization** — Much faster and more reliable Google/Outlook calendar sync.  
  <sub>CE `google_calendar`, `microsoft_calendar`; [M]</sub>
- ✅ **Google Calendar sync** — Work locations set in Google Calendar are reflected in Odoo.  
  <sub>CE `google_calendar`; [M]</sub>
- ✅ **Linked records** — Link a calendar event to any Odoo record.  
  <sub>CE `calendar`; [M]</sub>
- ✅ **Manage pending activities** — See and handle pending activities in the calendar.  
  <sub>CE `calendar`, `mail`; [H]</sub>
- ✅ **Mobile calendar redesign** — Easier calendar navigation on mobile.  
  <sub>CE `calendar`, `web`; [M]</sub>
- ✅ **Multiple calendars in one place** — Several calendars per user, including shared team calendars.  
  <sub>New `calendar.calendar` model in CE `calendar`; CE `calendar`; [H]</sub>
- ✅ **Sync multiple Google calendars** — Sync several Google calendars, both ways.  
  <sub>CE `google_calendar`; [M]</sub>
- 🔒 **Manage and share availabilities** — Manage and share a link to your availabilities or appointments from Calendar.  
  <sub>Availability sharing links come from EE Appointments; EE `appointment`; OCA: `resource_booking` (calendar); [L]</sub>
- 🔒 **Non-recurring appointments** — Easier one-off (non-recurring) appointment openings from Appointments and Calendar.  
  <sub>EE `appointment`; OCA: `resource_booking` (calendar); [M]</sub>

### Contacts

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_88) · 2 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Contact enrichment** — Enrich one or many contacts with company data.  
  <sub>IAP enrichment service (credits); CE `partner_autocomplete`, `crm_iap_enrich`; IAP [H]</sub>
- ✅ **Hierarchical view** — New hierarchy view for contacts.  
  <sub>CE `web_hierarchy`, `contacts`; [H]</sub>

### CRM

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_89) · 4 ✅ · 0 🟡 · 1 🔒</sub>

- ✅ **Hidden address info** — Address fields are hidden to push creating a proper contact.  
  <sub>CE `base`; [M]</sub>
- ✅ **Lead distribution** — Per-salesperson lead assignment mode: always in rotation, in rotation with a limit, or out of rotation.  
  <sub>CE `crm`; [H]</sub>
- ✅ **Lead generation** — Lead generation offers more sources and now uses Dun & Bradstreet data instead of Clearbit.  
  <sub>IAP service (credits); CE `crm_iap_mine`; IAP [M]</sub>
- ✅ **Pipeline switcher** — Dropdown to switch between sales teams' pipelines.  
  <sub>CE `crm`; [M]</sub>
- 🔒 **Upsells from lead** — See a customer's subscriptions from the lead; create upsell/renewal quotes linked to the opportunity.  
  <sub>Needs Subscriptions (EE). OCA: contract / subscription_oca; EE `sale_subscription`; [M]</sub>

### Dashboards

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_90) · 5 ✅ · 1 🟡 · 1 🔒</sub>

- ✅ **Carousel data layer** — Carousels can hold a cell range, making dashboards responsive on mobile.  
  <sub>o-spreadsheet engine (CE); editing dashboards requires EE; CE `spreadsheet`; [M]</sub>
- ✅ **Favorite filters** — Save global filters as favourites and set a default one.  
  <sub>CE `spreadsheet_dashboard`; [M]</sub>
- ✅ **Fiscal year date filter** — New 'Fiscal Year' date filter.  
  <sub>CE `spreadsheet`; [M]</sub>
- ✅ **Private dashboards** — Private dashboards shared only with chosen users.  
  <sub>CE `spreadsheet_dashboard`; [L]</sub>
- ✅ **Region selector for geo charts** — Region selector on world geo charts.  
  <sub>CE `spreadsheet`; [M]</sub>
- 🟡 **Billing targets vs billable time** — Compare billing targets with billable time in the Timesheets dashboard.  
  <sub>Billing-target data in CE; the Timesheets dashboard analysis is EE; CE `hr_timesheet` · EE `sale_timesheet_enterprise`; [M]</sub>
- 🔒 **Frozen share links** — Menu to manage frozen (snapshot) share links.  
  <sub>EE `spreadsheet_dashboard_edition`; OCA: `spreadsheet_oca` (spreadsheet); [L]</sub>

### Discuss

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_91) · 4 ✅ · 1 🟡 · 1 🔒</sub>

- ✅ **Channel categories** — Group channels into categories.  
  <sub>CE `mail`; [H]</sub>
- ✅ **Favorite channels** — Mark channels as favourites.  
  <sub>CE `mail`; [M]</sub>
- ✅ **Mark notifications as unread** — Mark notifications as unread.  
  <sub>CE `mail`; [H]</sub>
- ✅ **Polls** — Create polls in conversations.  
  <sub>CE `mail`; [H]</sub>
- 🟡 **Call transcripts** — Record Discuss calls and get summaries.  
  <sub>Call recording plumbing in CE `mail`; AI summaries are EE; CE `mail` · EE `voip_ai`, `ai`; [L]</sub>
- 🔒 **"On a call" status** — Discuss shows when a user is on a phone call.  
  <sub>EE `voip`; OCA: `base_phone` (connector-telephony); [M]</sub>

### eCommerce

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_93) · 34 ✅ · 1 🟡 · 3 🔒</sub>

- ✅ **Attribute filters** — Attribute filters only show values relevant to the current page.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Automated cross-sell suggestions** — Automatically generate accessory, optional and alternative products.  
  <sub>Cross-sell generation code is in CE `website_sale` (not in an AI module); CE `website_sale`, `product`; [M]</sub>
- ✅ **Automated review requests** — Automated review-request emails with a configurable delay after the order.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Default journal for eCommerce orders** — Default accounting journal for eCommerce orders.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Dynamic product building block** — Better layout of the dynamic products block.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Email gift card directly to recipient** — Customers can email a purchased gift card straight to the recipient.  
  <sub>CE `loyalty`, `website_sale_loyalty`; [M]</sub>
- ✅ **External identifiers** — External identifiers on attributes for data feeds and microdata.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Extra step granularity** — Show the checkout's extra step only for products of selected categories.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Gelato: variant images** — Print images per variant for Gelato print-on-demand.  
  <sub>CE `sale_gelato`; [M]</sub>
- ✅ **Google Analytics events** — Google Analytics 4 eCommerce events are more complete and spec-compliant.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Guest orders: contact creation** — Contacts from guest orders are archived until the customer creates an account.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Location selector: country filter** — Filter pickup points by country.  
  <sub>CE `website_sale`, `delivery`; [M]</sub>
- ✅ **Loyalty progress bar** — Progress bars towards loyalty rewards in cart notifications and summary.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Minimum product quantity** — Minimum order quantity per product.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Open attribute value on search** — Searching by attribute value (e.g. 'black t-shirt') opens the product with that value selected.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Order dashboard** — Dashboard on top of the eCommerce order list.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Pay Now button** — Edit and translate the 'Pay now' buttons in checkout.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Preferred delivery date** — Customers can choose a preferred delivery date.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Prevent sales by category** — Block sales for a whole category while still showing prices.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Pricelist selector** — Pricelist selector on every shop page.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Product reference price** — Reference (unit) price shown on all shop pages by default.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Product features** — Ribbons, compare price, attributes and secondary images in dynamic product blocks.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Product variant thumbnails** — 'Show Thumbnails' on attributes uses variant images instead of value swatches.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Products grid building block** — New grid layout for the Products block.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Range filter for attribute values** — Range slider filter for numeric attributes.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Restrict packagings per website** — Restrict units and packagings per website.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Return management** — Customers can return products from the portal.  
  <sub>CE `website_sale`; 😉 déjà vu: OCA [`rma_sale`](https://github.com/OCA/rma/tree/19.0/rma_sale) since 12.0; [M]</sub>
- ✅ **Ribbon filters** — New ribbon filters 'On Sale' and 'In Stock'.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Simplified inventory management** — eCommerce works with simple stock tracking (one on-hand quantity, no transfers) without Inventory.  
  <sub>CE `website_sale`; [L]</sub>
- ✅ **Standalone categories** — Hide chosen categories from the shop page to build curated sections.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Stock-based product publishing** — Unpublish/republish products automatically based on stock.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Taxes included/excluded price display** — Tax-included or tax-excluded price display per pricelist (B2C and B2B on one site).  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Variant image management** — Manage variant images centrally in the product's eCommerce tab.  
  <sub>CE `website_sale`; [M]</sub>
- ✅ **Withdrawal requests** — New contact-form action to handle withdrawal requests.  
  <sub>CE `website_sale`; [M]</sub>
- 🟡 **Donations** — Donations in the cart flow, including recurring donations via subscriptions.  
  <sub>Donations in cart are CE; recurring donations need Subscriptions (EE); CE `website_sale` · EE `sale_subscription`; OCA: `contract` (contract), `subscription_oca` (contract); [M]</sub>
- 🔒 **AI-assisted product editing** — Ask the AI assistant to generate product images or change name, price or description from the shop.  
  <sub>EE `ai_website_sale`; [M]</sub>
- 🔒 **Mondial Relay handled via Sendcloud** — Mondial Relay module removed; Mondial Relay remains available via Sendcloud.  
  <sub>CE modules `website_sale_mondialrelay` and `delivery_mondialrelay` were removed; Mondial Relay now only via the EE Sendcloud connector. OCA: delivery-carrier; EE `delivery_sendcloud`; ⚠️ change [H]</sub>
- 🔒 **WhatsApp abandoned cart follow-up** — Follow up abandoned carts via WhatsApp.  
  <sub>EE `whatsapp`; OCA: `mail_gateway_whatsapp` (social); [M]</sub>

### eLearning

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_94) · 1 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Course access from portal** — Customers see and open their courses from the portal.  
  <sub>CE `website_slides`; [M]</sub>

### Email Marketing

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_95) · 14 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Click tracking** — See which recipient clicked which link.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Conditional content** — Show blocks conditionally per recipient.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Contact management** — Easier adding of contacts to mailing lists; recipients manage their own subscriptions.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Dynamic mailing lists** — Dynamic mailing lists computed when the mailing is sent.  
  <sub>CE `mass_mailing`; 😉 déjà vu: OCA [`mass_mailing_list_dynamic`](https://github.com/OCA/mass-mailing/tree/19.0/mass_mailing_list_dynamic) since 10.0; [M]</sub>
- ✅ **Employee/supplier mailings** — Send mailings to employees and suppliers.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Favorite blocks** — Save blocks as favourites for reuse.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Full-screen editing** — Mailing design is always edited full screen.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Link tracking** — Turn off link tracking directly in the editor.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Mailing template library** — Save mailings as templates, available in a dedicated menu.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **New fonts** — New fonts with fallbacks for email clients.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **New templates and blocks** — New templates and blocks.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Product and event snippets** — Product and event snippets filled from selected records.  
  <sub>CE `mass_mailing`; [M]</sub>
- ✅ **Social media accounts** — Connect social media accounts and style them in mailings.  
  <sub>Uses the CE `social_media` links; the EE Social app is not required; CE `mass_mailing`, `social_media`; [M]</sub>
- ✅ **UTM reference** — UTM uses a new 'Reference' field instead of creating sources on the fly.  
  <sub>CE `mass_mailing`; [M]</sub>

### Employees

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_96) · 3 ✅ · 0 🟡 · 1 🔒</sub>

- ✅ **Employee directory** — In multi-company databases all users can see employees of all companies.  
  <sub>CE `hr`; [M]</sub>
- ✅ **Remote Work** — Remote Work merged into Employees.  
  <sub>`hr_homeworking`, `hr_homeworking_calendar` and `hr_holidays_homeworking` were removed; work locations per weekday now live in `hr`; CE `hr`; ⚠️ change [H]</sub>
- ✅ **Variable working schedule** — Define variable working schedules from a calendar view.  
  <sub>CE `resource`, `hr`; [M]</sub>
- 🔒 **Salary simulation** — Simulate an employee's salary from their profile.  
  <sub>Salary simulation is Payroll (EE); EE `hr_payroll`; OCA: `payroll` (payroll); [M]</sub>

### Events

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_98) · 1 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Event combos** — Combo tickets combining registration with food/drinks at different VAT rates.  
  <sub>CE `sale`, `website_sale`; [M]</sub>

### Expenses

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_99) · 2 ✅ · 0 🟡 · 1 🔒</sub>

- ✅ **Consolidated expenses report** — Print several expenses in one consolidated report.  
  <sub>CE `hr_expense`; [L]</sub>
- ✅ **Expense limits per job position** — Maximum expense amounts per job position; managers can cap before approval.  
  <sub>CE `hr_expense`; [H]</sub>
- 🔒 **Salary rules for expense products** — Expense products can be linked to a salary rule.  
  <sub>Salary rules = Payroll (EE); EE `hr_payroll_expense`; [M]</sub>

### Inventory

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_104) · 19 ✅ · 0 🟡 · 3 🔒</sub>

- ✅ **Allocation report** — Allocate from the forecast report; redesigned allocation report.  
  <sub>CE `stock`; [M]</sub>
- ✅ **CMR document** — Download a pre-filled CMR consignment note from deliveries.  
  <sub>CE `stock_fleet`; [M]</sub>
- ✅ **Company-specific customer lead times** — Customer lead time per company.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Intercompany flows** — Inter-company resupply routes, delivery from another company's warehouse, correct valuation of transferred goods.  
  <sub>Inter-company resupply routes in CE `stock`; CE `stock`, `purchase_stock`; [M]</sub>
- ✅ **Inventory at a past date** — Stock at a past date with a date/time picker that keeps filters.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Inventory valuation: COGS update** — Cost changes after delivery (e.g. landed costs, price differences) update the delivery value and COGS.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Landed costs for specific products** — Landed costs on specific products of a transfer.  
  <sub>CE `stock_landed_costs`; [M]</sub>
- ✅ **Location-specific push routes** — Push routes depending on the exact destination location.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Picking notifications** — Subscribe to transfer status notifications.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Product packaging barcodes** — Manage packaging barcodes from the product form.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Product replenishment** — Single 'Order' button in replenishment; ordering ahead proposes sensible quantities.  
  <sub>CE `stock`; [H]</sub>
- ✅ **Simplified returns** — Return wizard removed; simpler returns.  
  <sub>The `stock.return.picking` wizard model no longer exists; CE `stock`; ⚠️ change [H]</sub>
- ✅ **Stock aging report** — Stock aging report from the Moves Analysis pivot.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Suggested stock levels for reordering rules** — Reordering-rule min/max suggested from demand history, coverage days and order frequency.  
  <sub>CE `stock`, `purchase_stock`; [M]</sub>
- ✅ **Traceability Report** — Traceability report shows upstream and downstream lots in one view.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Variant-specific HS codes** — HS codes per product variant.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Variant-specific packagings** — Packagings per variant.  
  <sub>CE `stock`; [M]</sub>
- ✅ **Vendor purchase reference** — Vendor reference shown on receipts.  
  <sub>CE `stock`; 😉 déjà vu: OCA [`stock_picking_supplier_ref`](https://github.com/OCA/stock-logistics-warehouse/tree/18.0/stock_picking_supplier_ref) since 14.0; [M]</sub>
- ✅ **ZPL location barcodes** — Location barcode labels in ZPL.  
  <sub>CE `stock`; [M]</sub>
- 🔒 **Preview Barcode instructions in operation type** — Preview Barcode operator instructions from the operation type.  
  <sub>EE `stock_barcode`; [M]</sub>
- 🔒 **Sendcloud: package reference** — Odoo's package reference is sent to Sendcloud for labels.  
  <sub>EE `delivery_sendcloud`; OCA: `delivery_sendcloud_oca` (delivery-carrier); [M]</sub>
- 🔒 **Sendcloud: pickup points** — Pick Sendcloud pickup points from sales orders or transfers, and correct them after eCommerce orders.  
  <sub>EE `delivery_sendcloud`; OCA: `delivery_sendcloud_oca` (delivery-carrier); [M]</sub>

### Maintenance

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_107) · 2 ✅ · 0 🟡 · 1 🔒</sub>

- ✅ **Maintenance teams on stages** — Maintenance stages per team.  
  <sub>CE `maintenance`; [M]</sub>
- ✅ **UX improvements** — UX improvements including a new status widget.  
  <sub>CE `maintenance`; [M]</sub>
- 🔒 **Maintenance requests: Gantt views** — Gantt views for equipment and work center maintenance requests.  
  <sub>Gantt views are EE; EE `mrp_maintenance`, `maintenance_enterprise`; [H]</sub>

### Manufacturing

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_108) · 20 ✅ · 2 🟡 · 2 🔒</sub>

- ✅ **Backorder planning** — Backorders of planned MOs are planned automatically.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Bill of materials** — Compare BoMs by quantities, merged status/availability columns, extra costs on the BoM, better component management.  
  <sub>BoM overview columns merged, extra-cost field on BoM, BoM comparison; CE `mrp`; ⚠️ change [M]</sub>
- ✅ **Component replacement** — 'Used In' shows BoM component lines to ease component replacement.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Continuous production** — Record produced quantities per work order; with 'Continuous Production' next operations start early.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Draft versus confirmed manufacturing orders** — Procurement creates draft or confirmed MOs, set per operation type.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Flexible consumption** — Flexible consumption setting removed; all MOs consume flexibly.  
  <sub>Field `mrp.bom.consumption` removed; consumption is always flexible; CE `mrp`; ⚠️ change [H]</sub>
- ✅ **Generate lots and serials when closing manufacturing orders** — Lots/serials are always generated when closing MOs.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Lot/serial number transfers** — The Transfers button on lots shows delivery move lines for precise recalls.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Manufacturing order Kanban view** — Redesigned MO Kanban grouped by week, with component status, work center, deadline and remaining time.  
  <sub>CE `mrp`; [H]</sub>
- ✅ **Manufacturing orders planned ASAP** — MOs are planned as soon as possible by default; list order sets priority.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **MO cost** — 'MO Cost' shows provisional cost during and real cost after production; subcontracting costs included.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Put in pack from MO** — The finished product goes into the MO's destination package automatically.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Reset MO to draft** — Reset done or cancelled MOs to draft.  
  <sub>CE `mrp`; 😉 déjà vu: OCA [`mrp_production_back_to_draft`](https://github.com/OCA/manufacture/tree/19.0/mrp_production_back_to_draft) since 14.0; [M]</sub>
- ✅ **Split manufacturing orders** — Split an ongoing MO to produce the rest later.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Subcontracting reception valuation** — Without a PO, subcontractor cost is set at reception from the vendor pricelist.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **To Replenish filter** — 'To Replenish' filter in the MO overview.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Traceability report expiration dates** — Expiration dates in the traceability report.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Work and manufacturing order reporting** — Better reporting on work orders and MOs.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Work center overview** — Work center overview with links to work orders and maintenance.  
  <sub>CE `mrp`; [M]</sub>
- ✅ **Work orders in blocked work centers** — Process work orders in blocked work centers.  
  <sub>CE `mrp`; [M]</sub>
- 🟡 **Produce button** — One 'Produce' button replaces 'Produce' and 'Produce All'.  
  <sub>Single Produce button in CE Manufacturing; Shop Floor/Barcode parts EE; CE `mrp` · EE `mrp_workorder`, `stock_barcode_mrp`; ⚠️ change [M]</sub>
- 🟡 **Work order views** — New work order Kanban and drag-and-drop Gantt planning (also by employee).  
  <sub>Kanban view CE; Gantt planning EE; CE `mrp` · EE `mrp_workorder`; [M]</sub>
- 🔒 **Shop Floor demo sheet** — Download a Shop Floor demo sheet to test barcode features.  
  <sub>EE `mrp_workorder`; [M]</sub>
- 🔒 **Visualize and confirm work orders** — Confirm work orders from the Work Order Planning Gantt, even with drafts.  
  <sub>Work Order Planning Gantt is EE; EE `mrp_workorder`; [M]</sub>

### Marketing Card

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_110) · 3 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Default target URLs** — Event URL suggested as default target for event campaigns.  
  <sub>CE `marketing_card`; [M]</sub>
- ✅ **Event app integration** — 'Send cards' from an event, with recipient conditions.  
  <sub>CE `marketing_card`; [M]</sub>
- ✅ **Language support** — Choose the language a card is sent in.  
  <sub>CE `marketing_card`; [M]</sub>

### Online Payments

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_111) · 16 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **ACH payments** — ACH payments can be tokenized.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Authorize.net** — Authorize.net webhooks for delayed confirmations.  
  <sub>CE `payment`; [M]</sub>
- ✅ **ECPay** — New ECPay payment provider (Taiwan).  
  <sub>CE `payment`; backported [M]</sub>
- ✅ **Mollie** — More Mollie methods (Apple Pay, Blik, in3, Google Pay, Klarna, MB WAY, Multibanco, Swish) and tokenization.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Pay on Invoice provider** — New 'Pay on Invoice' provider: confirm orders without paying immediately.  
  <sub>CE `payment`; [H]</sub>
- ✅ **Payment provider views** — Simpler payment provider views.  
  <sub>CE `payment`; [M]</sub>
- ✅ **PayPal** — PayPal: cards, alternative methods, tokenization, OAuth onboarding.  
  <sub>CE `payment`; [M]</sub>
- ✅ **PayU** — PayU provider for India.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Pricelist and amount restriction** — Restrict providers by pricelist and min/max amount.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Redsys** — Redsys tokenization for recurring payments.  
  <sub>CE `payment`; [M]</sub>
- ✅ **SOFORT** — SOFORT removed from all providers.  
  <sub>The `sofort` payment method record is gone; CE `payment`; ⚠️ change [H]</sub>
- ✅ **Stripe** — More Stripe methods (Alma, Apple Pay, ACSS debit, Google Pay, Satispay, Swish).  
  <sub>CE `payment`; [M]</sub>
- ✅ **Toss Payments** — New Toss Payments provider (South Korea).  
  <sub>CE `payment`; [H]</sub>
- ✅ **Wero** — Wero via Buckaroo and Worldline.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Wire transfers** — Wire transfers confirmed automatically from bank transactions.  
  <sub>CE `payment`; [M]</sub>
- ✅ **Xendit** — Xendit for Malaysia, Thailand and Vietnam.  
  <sub>CE `payment`; backported [M]</sub>

### Point of Sale

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_116) · 16 ✅ · 1 🟡 · 3 🔒</sub>

- ✅ **Base unit price on product label** — Reference (unit) price on product labels.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Convert order lines into a combo** — POS suggests turning order lines into combos.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Employee access levels** — Employee access levels renamed, plus a restrictive 'Supervised' level.  
  <sub>POS employee access levels renamed; new restrictive 'Supervised' level; CE `pos_hr`; ⚠️ change [M]</sub>
- ✅ **End of session** — Session closing posts one global sale instead of misc entries; payment entries at a set time.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Expired product notification** — Warning when selling expired products.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Mercado Pago terminal** — Mercado Pago terminal QR payments, refunds and cancellations, also for Chile.  
  <sub>CE `pos_mercado_pago`; [M]</sub>
- ✅ **Multiple currencies** — Several currencies at checkout in one POS.  
  <sub>CE `point_of_sale`; [H]</sub>
- ✅ **Print preparation tickets per product** — 'Split per product' prints one preparation ticket per product.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Printer management** — Several printers per POS; choose which one prints.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Receipt printing** — Configure receipt paper size (developer mode).  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Reorganizing products in POS interface** — Reorder products in the POS by drag and drop.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Self-ordering** — Self-ordering: customer notes at checkout (shown in the kitchen), optional products on mobile/kiosk, and more.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Service fees** — Service fees via presets, shown on invoices.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Simplified inventory management** — POS works with simple stock tracking (one on-hand quantity, no transfers) without Inventory.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Simplified receipts** — Simplified receipt with subtotals and taxes but no lines.  
  <sub>CE `point_of_sale`; [M]</sub>
- ✅ **Snooze products** — Snooze products to make them temporarily unavailable.  
  <sub>CE `point_of_sale`; [M]</sub>
- 🟡 **WhatsApp and SMS self-order receipt** — Self-order receipts via WhatsApp or SMS.  
  <sub>WhatsApp and SMS receipts via EE modules; CE `pos_self_order` · EE `whatsapp_pos_self_order`, `pos_enterprise_sms_whatsapp`; [M]</sub>
- 🔒 **Booking Kanban and pivot views** — Kanban and pivot views for bookings.  
  <sub>EE `pos_appointment`; [H]</sub>
- 🔒 **GoFood delivery integration** — GoFood orders and menu sync (Indonesia, Vietnam).  
  <sub>EE `pos_urban_piper`; backported [M]</sub>
- 🔒 **GrabFood delivery integration** — GrabFood orders and menu sync in several Southeast Asian countries.  
  <sub>EE `pos_urban_piper`; backported [M]</sub>

### Project

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_117) · 6 ✅ · 1 🟡 · 1 🔒</sub>

- ✅ **Assign project roles** — Assign team members to project roles.  
  <sub>CE `project`; [M]</sub>
- ✅ **Assign tasks to portal users** — Assign tasks to portal users who follow the project.  
  <sub>CE `project`; [M]</sub>
- ✅ **Collaborators separated from followers** — Give customers portal access to a project without making them followers.  
  <sub>CE `project`; [M]</sub>
- ✅ **Mobile: improved task header design** — Nicer task header on mobile.  
  <sub>CE `project`; [M]</sub>
- ✅ **Projects from opportunities** — Create projects from opportunities.  
  <sub>New CE module `crm_sale_project`; CE `crm_sale_project`; [H]</sub>
- ✅ **Task tracking in user portal** — Show task chatter changes in the portal.  
  <sub>CE `project`; [M]</sub>
- 🟡 **Profitability report** — Profitability panel removed from the project dashboard; new budget and margin reports.  
  <sub>The profitability panel is gone from the project dashboard. Margin reporting stays in CE (`project_account`, `sale_project_margin`); budget analysis needs EE `account_budget`; CE `project_account`, `sale_project_margin`, `project` · EE `account_budget`; OCA: `account_budget_oca` (account-budgeting); ⚠️ change [M]</sub>
- 🔒 **Printable task schedule** — Print a task schedule from the Gantt view.  
  <sub>Task schedule printing from Gantt (EE); EE `project_enterprise`; OCA: `web_timeline` (web), `project_timeline` (project); [M]</sub>

### Purchase

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_118) · 8 ✅ · 0 🟡 · 1 🔒</sub>

- ✅ **Alternatives comparison** — Clearer comparison of alternative purchase offers.  
  <sub>Alternatives now in the new CE module `purchase_alternative` (split from `purchase_requisition`); CE `purchase_alternative`; [H]</sub>
- ✅ **Default Incoterm per vendor** — Default Incoterm per vendor.  
  <sub>CE `purchase`; 😉 déjà vu: OCA [`purchase_partner_incoterm`](https://github.com/OCA/purchase-workflow/tree/19.0/purchase_partner_incoterm) since 14.0; [M]</sub>
- ✅ **End-customer address in portal** — End-customer address shown on POs in the vendor portal.  
  <sub>CE `purchase`; [M]</sub>
- ✅ **Expected arrival date** — Edit the expected arrival while keeping the vendor's original date for on-time statistics.  
  <sub>CE `purchase`; [M]</sub>
- ✅ **Product unit cost versus purchase unit cost** — Catalog shows cost per product unit next to cost per purchase unit.  
  <sub>CE `purchase`; [M]</sub>
- ✅ **Purchase agreement structure** — Sections and notes in purchase agreements / blanket orders.  
  <sub>CE `purchase`; [M]</sub>
- ✅ **Recompute Expected Arrival when deadline is in the past** — Recompute expected arrivals in one click when the order deadline has passed.  
  <sub>CE `purchase`; [M]</sub>
- ✅ **Total amounts on purchase order sections** — Totals on PO sections and subsections.  
  <sub>CE `purchase`; [M]</sub>
- 🔒 **Vendor quality rate** — Vendor quality rate based on quality checks.  
  <sub>EE `quality_control`; OCA: `quality_control_oca` (manufacture); [M]</sub>

### Recruitment

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_120) · 4 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Improved integration** — Better link between applicants, talent pool and jobs, with better matching.  
  <sub>CE `hr_recruitment`; [M]</sub>
- ✅ **Job form visibility conditions** — Online application fields shown depending on the selected job(s).  
  <sub>CE `hr_recruitment`; [M]</sub>
- ✅ **Matching score filter** — Filter applicants by 'Matching Score'.  
  <sub>CE `hr_recruitment_skills`; [M]</sub>
- ✅ **View talents from job position** — See matching talents from a job position.  
  <sub>CE `hr_recruitment`; [M]</sub>

### Repairs

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_123) · 3 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Invoice creation** — Invoice repairs directly without a quotation.  
  <sub>CE `repair`; [M]</sub>
- ✅ **Repair order status** — The 'Under Repair' status is removed.  
  <sub>`repair.order.state` no longer has 'under_repair'; CE `repair`; ⚠️ change [H]</sub>
- ✅ **Repair-related services** — Add services to repair orders.  
  <sub>CE `repair`; [M]</sub>

### Sales

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_124) · 23 ✅ · 0 🟡 · 4 🔒</sub>

- ✅ **Charge overages** — Charge overages on prepaid services from the invoicing wizard.  
  <sub>CE `sale`; [L]</sub>
- ✅ **Dashboard** — Sales dashboard above quotations and orders with key figures and quick filters.  
  <sub>CE `sale`; [H]</sub>
- ✅ **Description-only sales order lines** — Order lines can be description-only; a 'Mandatory Product' setting enforces products.  
  <sub>`sale.order.line.product_id` is optional unless the 'Mandatory Product' setting is on; CE `sale`; ⚠️ change [H]</sub>
- ✅ **Editable product variant price** — Edit variant sales prices directly.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Editable margins** — Edit the margin on a line to recompute the price.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Fixed prepayment amounts** — Fixed-amount prepayments.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Fixed Price pricelists** — Attribute extra prices apply on top of 'Fixed Price' pricelist rules.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Loyalty point expiration** — Loyalty points can expire.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Mark orders as fully invoiced** — Mark an order as fully invoiced.  
  <sub>CE `sale`; 😉 déjà vu: OCA [`sale_force_invoiced`](https://github.com/OCA/sale-workflow/tree/19.0/sale_force_invoiced) since 9.0; [M]</sub>
- ✅ **Periodic pricing** — Pricelist rules and surcharges for periods or weekdays.  
  <sub>Date-range rules and surcharges exist in CE `product`; the 'days of the week' part was not found in the 20.0 source (CE or EE) — needs review; CE `sale`; [L]</sub>
- ✅ **Price rules per packaging type** — Price rules per packaging type.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Pricelist report improvements** — Pricelist report grouped by category, with reference and barcode, and a date filter.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Product images** — Show product images on sales orders and their PDFs.  
  <sub>CE `sale`; 😉 déjà vu: OCA [`sale_order_report_product_image`](https://github.com/OCA/sale-reporting/tree/19.0/sale_order_report_product_image) since 11.0; [H]</sub>
- ✅ **Quotation sections** — Section quantities/units update all lines; multi-line section descriptions; reusable section templates.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Quotation templates** — Pick a quotation template when creating an order; sub-sections and options like 'Hide Price'; add products via the catalog.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Sales order creation from purchase orders** — Creating sales orders from customer POs reuses earlier corrections.  
  <sub>CE `sale`, `purchase_edi_ubl_bis3`, `account_edi_ubl_cii`; [M]</sub>
- ✅ **Sales order email template** — The default order email includes the customer reference.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Sales order line numbering** — Line numbers on the order, its PDF and the portal.  
  <sub>CE `sale`; 😉 déjà vu: OCA [`sale_order_line_sequence`](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_sequence) since 9.0; [M]</sub>
- ✅ **Sales order portal page** — Redesigned sales order portal page.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Services & Material** — Fixed-price and cost-based services and materials for re-invoicing.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Ship orders without Inventory** — Shipping confirmations and fulfilment without Inventory.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Single-use discount codes** — Discount codes usable once per customer.  
  <sub>CE `sale`; [M]</sub>
- ✅ **Stacked fields on sales order lines** — Margin, delivered % and tax columns stacked vertically on lines.  
  <sub>CE `sale`; [M]</sub>
- 🔒 **Payment-based commissions** — Commissions based on the amount paid.  
  <sub>Commissions app is EE (`sale_commission`). OCA: commission / sale_commission (commission repo); EE `sale_commission`; [H]</sub>
- 🔒 **Lazada** — Lazada marketplace connector (orders, delivery slips, stock).  
  <sub>EE `sale_lazada`; backported [M]</sub>
- 🔒 **Manager commissions** — Roll up team members' achievements into managers' commissions.  
  <sub>OCA: commission repo; EE `sale_commission`; [H]</sub>
- 🔒 **TikTok** — TikTok Shop connector (orders, delivery slips, stock).  
  <sub>EE `sale_tiktok`; backported [M]</sub>

### Spreadsheet

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_128) · 0 ✅ · 30 🟡 · 0 🔒</sub>

- 🟡 **Bubble charts** — Bubble charts.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Calculated columns** — Calculated columns in dynamic lists.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Calendar charts** — Calendar charts.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Cell value orientation** — Rotate cell text.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Charts** — Chart annotations and chart suggestions from a selection.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Column statistics** — Quick column statistics from the Data menu.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Conditional formatting by date** — Date-based conditional formatting.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Curly brackets** — Curly-brace array literals.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Custom format** — Custom date and number formats.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Data cleanup** — Remove unused data sources.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Disable automatic recalculation** — Turn off automatic recalculation (F9 to recalculate).  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Global filters** — Default operators for global filters; create filters from data-source properties.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **List insertion** — Insert a dynamic list from the spreadsheet.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Lock sheets** — Lock sheets.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Mobile: pinch to zoom** — Pinch to zoom on mobile.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Multiple selection on figures** — Select and move several figures at once.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Named range** — Named ranges usable in formulas.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **New functions** — New functions (e.g. CHOOSE, DROP, TAKE, FORMULATEXT).  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Pivot tables** — Domain filters on pivot tables built from sheet data.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Print settings** — Print settings with a print preview.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Property fields in inserted lists** — Property fields included when inserting a list.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Reduced JSON file size** — Smaller exported JSON files.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Regex formulas** — REGEXTEST and REGEXREPLACE.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Scientific notation** — Scientific number format.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Sheet background colors** — Background colour for a whole sheet.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Spill range operator** — Spill range operator (#).  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Template access** — Restrict template visibility to groups.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Top menu navigation** — Keyboard navigation of the top menus.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Top/bottom ranking conditional formatting** — 'Top/Bottom ranking' conditional formatting.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>
- 🟡 **Zoom in/out** — Zoom in and out.  
  <sub>Engine feature: o-spreadsheet ships LGPL in the CE `spreadsheet` module (used read-only by CE dashboards), but creating/editing spreadsheets needs EE `spreadsheet_edition`. CE users can get editing via OCA `spreadsheet_oca` (reporting-engine) once migrated; CE `spreadsheet` · EE `spreadsheet_edition`; OCA: `spreadsheet_oca` (spreadsheet); [M]</sub>

### Studio

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_129) · 1 ✅ · 0 🟡 · 8 🔒</sub>

- ✅ **Automation rules: activity plans** — Automation rules can launch activity plans.  
  <sub>Automation rules are CE (`base_automation`); Studio only exposes them; CE `base_automation`, `mail`; [M]</sub>
- 🔒 **Form view customization** — Reorder form buttons, smart buttons and tabs by drag and drop.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Kanban stage cutomization** — Customise Kanban stages from the form view.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **List view column width** — Min/max column widths in list views.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Many2Many fields in PDF reports** — Add many2many fields to PDF reports.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Report editor** — New report editor UI with warnings.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Report translations** — Translate report code in one block.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **User-friendly technical names** — Readable technical names for Studio fields.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Warning for past or future dates** — Warning icon for past/future dates on date fields.  
  <sub>EE `web_studio`; [H]</sub>

### Time Off

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_131) · 4 ✅ · 0 🟡 · 0 🔒</sub>

- ✅ **Calendar day vs working day deductions** — Count time off in working days or calendar days.  
  <sub>CE `hr_holidays`; [M]</sub>
- ✅ **Minimal amount for time-off requests** — Minimum duration for time-off requests.  
  <sub>CE `hr_holidays`; [M]</sub>
- ✅ **Overview: all employees** — Overview shows all employees, even without leave.  
  <sub>CE `hr_holidays`; [M]</sub>
- ✅ **Prevent app use** — New 'No' access level blocks the app.  
  <sub>New 'No' access level for Time Off; CE `hr_holidays`; [M]</sub>

### Website

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_133) · 55 ✅ · 2 🟡 · 3 🔒</sub>

- ✅ **Accented characters in URLs** — Accented characters in URLs.  
  <sub>CE `website`; [M]</sub>
- ✅ **Age verification popup** — Age-verification popup that blocks under-age visitors.  
  <sub>CE `website`; [H]</sub>
- ✅ **Animated number building block** — 'Animated Number' block for key figures.  
  <sub>CE `website`; [M]</sub>
- ✅ **Banners** — Banner above the header for promotions or announcements.  
  <sub>CE `website`; [M]</sub>
- ✅ **Blurred headers** — Blur effect on transparent headers.  
  <sub>CE `website`; [M]</sub>
- ✅ **Breadcrumbs on static pages** — Breadcrumbs on static pages.  
  <sub>CE `website`; 😉 déjà vu: OCA [`website_breadcrumb`](https://github.com/OCA/website/tree/18.0/website_breadcrumb) since 8.0; [M]</sub>
- ✅ **Card and column anchors** — Anchors on cards and columns.  
  <sub>CE `website`; [M]</sub>
- ✅ **Card enhancements** — Card animation on hover; whole card clickable.  
  <sub>CE `website`; [M]</sub>
- ✅ **Carousel transition** — Carousel transition speed.  
  <sub>CE `website`; [M]</sub>
- ✅ **Color palette preview** — Preview colour palettes on demo content.  
  <sub>CE `website`; [M]</sub>
- ✅ **Column content selection** — Ctrl+A selects a column's whole content.  
  <sub>CE `website`; [M]</sub>
- ✅ **Connection shape color** — Shape dividers take the right background colour from context.  
  <sub>CE `website`; [M]</sub>
- ✅ **Cookies** — Close button on the cookie bar; any page as cookie policy.  
  <sub>CE `website`; [M]</sub>
- ✅ **Countdown snippets** — Improved countdown snippets.  
  <sub>CE `website`; [M]</sub>
- ✅ **Customizable portal cards** — Customise portal home cards in the website editor.  
  <sub>CE `website`; [M]</sub>
- ✅ **DOM elements** — Page-specific body classes for styling.  
  <sub>CE `website`; [M]</sub>
- ✅ **Donation snippet customization** — Donation snippet can collect legally required data.  
  <sub>CE `website`; [M]</sub>
- ✅ **Dropzones and overlays** — Modernised drop zones and overlays in the editor.  
  <sub>CE `website`; [M]</sub>
- ✅ **Dynamic "Today" value** — Dynamic 'Today' default for date fields in forms.  
  <sub>CE `website`; [M]</sub>
- ✅ **Dynamic carousels** — Dynamic carousels for all modules (blogs, events, appointments…).  
  <sub>CE `website`; [M]</sub>
- ✅ **Events, Jobs, and Blog pages** — Standard 'Social Media' and 'Share' snippets in Events/Jobs/Blog sidebars.  
  <sub>Sidebar 'Follow Us'/'Share' blocks replaced by standard snippets; CE `website`, `website_event`, `website_blog`, `website_hr_recruitment`; ⚠️ change [M]</sub>
- ✅ **Font weight selector** — Set weights for light, normal and bold fonts.  
  <sub>CE `website`; [M]</sub>
- ✅ **Form enhancements** — Form options: 'no default' dropdown value, styled terms checkbox, and more.  
  <sub>CE `website`; [M]</sub>
- ✅ **Forum notifications** — Follow specific forum answers.  
  <sub>CE `website`; [M]</sub>
- ✅ **Fullscreen images** — Click images to see them full size.  
  <sub>CE `website`; [M]</sub>
- ✅ **General shadow options** — Global shadow styles for sections and cards.  
  <sub>CE `website`; [M]</sub>
- ✅ **Google Tag Manager (GTM)** — One identifier field for Google Analytics or Google Tag Manager.  
  <sub>CE `website`; 😉 déjà vu: OCA [`website_google_tag_manager`](https://github.com/OCA/website/tree/19.0/website_google_tag_manager) since 9.0; [M]</sub>
- ✅ **Inner content blocks: icons and Instagram** — Icon and Instagram inner blocks.  
  <sub>CE `website`; [M]</sub>
- ✅ **Job and eLearning course building blocks** — Dynamic blocks for jobs and courses (developer mode).  
  <sub>CE `website`; [M]</sub>
- ✅ **Link and button styling** — Edit theme-defined link/button styles from the Theme tab.  
  <sub>CE `website`; [M]</sub>
- ✅ **Link tracker: QR codes** — Turn tracked links into QR codes.  
  <sub>CE `website`; [M]</sub>
- ✅ **llms.txt** — Create an llms.txt file from website settings.  
  <sub>CE `website`; 😉 déjà vu: OCA [`website_llms`](https://github.com/OCA/website/tree/18.0/website_llms) since 16.0; [H]</sub>
- ✅ **Mega menu** — Mega menus accept blocks; new empty template.  
  <sub>CE `website`; [M]</sub>
- ✅ **Module-specific search** — Site search limited to all content or one module.  
  <sub>CE `website`; [M]</sub>
- ✅ **Multiple websites: change default site** — Change the default website by reordering websites.  
  <sub>CE `website`; [M]</sub>
- ✅ **New Icon List inner content block** — New 'Icon List' inner block.  
  <sub>CE `website`; [M]</sub>
- ✅ **Partners page** — New module to publish members and partners online.  
  <sub>New CE module `website_partnership`; CE `website_partnership`; [H]</sub>
- ✅ **Portal users: profile picture** — Portal users can change their profile picture.  
  <sub>CE `website`; [M]</sub>
- ✅ **Property fields supported in website forms** — Property fields usable in website forms for customer creation or newsletter signup.  
  <sub>CE `website`; [M]</sub>
- ✅ **Publish/unpublish partners** — Publish/unpublish partners in batch.  
  <sub>CE `website`; [M]</sub>
- ✅ **Redirections** — Easier creation of redirects.  
  <sub>CE `website`; [M]</sub>
- ✅ **Repositioning text over cover image** — Drag text over a cover image to reposition it.  
  <sub>CE `website`; [M]</sub>
- ✅ **Search results** — Translated page names in results, results by category, fuzzy search.  
  <sub>CE `website`; [M]</sub>
- ✅ **Sidebar revamp** — Sidebar folds secondary option groups.  
  <sub>CE `website`; [M]</sub>
- ✅ **Simplified inner content blocks** — Simpler 'Social Media' and 'Share' blocks.  
  <sub>CE `website`; [M]</sub>
- ✅ **Social media links** — Uniform handling of social media URLs.  
  <sub>CE `website`; [M]</sub>
- ✅ **Sitemap enhancements** — Sitemaps only list indexable 2XX URLs within Google limits.  
  <sub>CE `website`; [M]</sub>
- ✅ **Block preview for mobile devices** — Preview blocks on mobile.  
  <sub>CE `website`; [M]</sub>
- ✅ **Structured data** — Structured data added by default for rich results.  
  <sub>CE `website`; [M]</sub>
- ✅ **Theme layout and background options** — Clearer theme layout and background options.  
  <sub>CE `website`; [M]</sub>
- ✅ **Translation** — Translate form selection options, per-language static URLs, per-language media.  
  <sub>CE `website`; [M]</sub>
- ✅ **Vertical video format** — Vertical videos.  
  <sub>CE `website`; [M]</sub>
- ✅ **Visitor tracking** — More efficient visitor tracking.  
  <sub>CE `website`; [M]</sub>
- ✅ **Website editor UI/UX** — Improved editor UI/UX.  
  <sub>CE `website`; [M]</sub>
- ✅ **WhatsApp widget snippet** — WhatsApp chat button snippet.  
  <sub>CE `website`; [M]</sub>
- 🟡 **SEO** — Responsive images (srcset), no duplicate content on paginated pages, AI SEO help.  
  <sub>srcset & pagination SEO in CE; AI SEO helper EE; CE `website` · EE `ai_website`; [M]</sub>
- 🟡 **Website configuration wizard** — Better industry list in the setup wizard and AI-suggested positioning.  
  <sub>AI-powered positioning choices depend on IAP/AI; CE `website` · EE `ai_website`; IAP [L]</sub>
- 🔒 **AI Website Assistant** — AI website assistant can build pages from snippets, images and more.  
  <sub>EE `ai_website`; [M]</sub>
- 🔒 **AI-generated content indicator** — Editor marks blocks generated or changed by AI.  
  <sub>EE `ai_website`; [M]</sub>
- 🔒 **Appointment page layout** — Appointment page as list, cards or pictures.  
  <sub>EE `website_appointment`; OCA: `resource_booking` (calendar); [M]</sub>

### Localizations

Localization items bundle several countries' changes. Base data (charts of accounts, taxes, states) is CE; tax-report rendering (`account_reports`), payroll and many EDI connectors are EE. **Each item needs review by maintainers of that country's localization.**

- 🟡 **Argentina 🇦🇷** — Accounting: VAT book PDF without headers/footers for official ledger books, ARCA daily currency rates, 'Payment on Informed CBU' legend, SICORE export, better third-party check handling, withholdings in foreign currency, daily book export to Excel. Inventory: batch processing and manual vendor numbers for Remitos.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ar`, `l10n_ar_pos`, `l10n_ar_stock`, `l10n_ar_website_sale` · EE `l10n_ar_edi`, `l10n_ar_reports`; backported [L]</sub>
- ✅ **Armenia 🇦🇲** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); backported [H]</sub>
- 🟡 **Australia 🇦🇺** — Accounting: open-banking bank synchronization through Basiq.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_au` · EE `l10n_au_aba`, `l10n_au_hr_payroll`, `l10n_au_hr_payroll_account`, `l10n_au_hr_payroll_api`; [L]</sub>
- ✅ **Azerbaijan 🇦🇿** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); backported [H]</sub>
- ✅ **Bahrain 🇧🇭** — Accounting: state codes updated to ISO 3166-2.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); CE `l10n_bh` · EE `l10n_bh_reports`; [H]</sub>
- 🟡 **Bangladesh 🇧🇩** — Accounting: old tax report removed, 2026 Finance Act rates, tax groups by nature (VAT, TDS, VDS), chart of accounts with parent accounts.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_bd` · EE `l10n_bd_hr_payroll`, `l10n_bd_hr_payroll_account`, `l10n_bd_reports`; ⚠️ change [L]</sub>
- 🔒 **Belgium 🇧🇪** — Payroll: automated Dimona, joint committees, merged 'Regular Pay' structure, directors' pay, meal-voucher reporting, flexi-jobs, holiday pay, earning caps, CP302 year-end bonus, profit-sharing bonus.  
  <sub>Payroll localizations are EE (`l10n_be_hr_payroll*`); CE `l10n_be`, `l10n_be_pos`, `l10n_be_pos_restaurant`, `l10n_be_pos_sale` · EE `l10n_be_coda`, `l10n_be_codabox`, `l10n_be_codaclean`, `l10n_be_fiscal_categories`; ⚠️ change backported [H]</sub>
- 🟡 **Brazil 🇧🇷** — Accounting: NF-e/NFS-e for exports, OCR import of NFS-e, batch XML download, more fiscal fields on operation types, Avalara options, alphanumeric CNPJ, streamlined fiscal workflow. Inventory: more fiscal fields, NF-e data on shipping labels. POS: cancel NFC-e.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_br`, `l10n_br_sales`, `l10n_br_website_sale` · EE `l10n_br_avatax`, `l10n_br_avatax_sale`, `l10n_br_edi`, `l10n_br_edi_extract`; ⚠️ change backported [L]</sub>
- 🟡 **Canada 🇨🇦** — Accounting: detailed expense accounts, localized asset models, batch customer payments via CPA 005 pre-authorized debit files.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ca` · EE `l10n_ca_check_printing`, `l10n_ca_payment_cpa005`, `l10n_ca_reports`; [L]</sub>
- 🟡 **Chile 🇨🇱** — Accounting: expense accounts and asset models, XML import of customer invoices, commune data, non-billable amounts, CAF sharing across branches, F29 report on tax tags. Inventory: delivery-guide copies per SII layout.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_cl` · EE `l10n_cl_edi`, `l10n_cl_edi_exports`, `l10n_cl_edi_factoring`, `l10n_cl_edi_pos`; [L]</sub>
- 🟡 **China 🇨🇳** — Accounting: improved chart of accounts and statements, asset models, parent accounts, voucher batch printing, VAT & surcharges return, VAT differential taxation on invoice lines.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_cn` · EE `l10n_cn_reports`; backported [L]</sub>
- 🟡 **Colombia 🇨🇴** — Accounting: expense accounts and asset models, e-invoicing of free samples, better fiscal PDFs, DIAN-only connection (Carvajal dropped), contingency invoicing, CUFE-based duplicate detection, exogenous reports, mandate invoices for goods, discounts in XML, ZIP import of vendor bills.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_co`, `l10n_co_pos` · EE `l10n_co_edi`, `l10n_co_edi_pos`, `l10n_co_reports`; ⚠️ change [L]</sub>
- 🟡 **Dominican Republic 🇩🇴** — Accounting: e-invoicing (e-CF 31–34) via Infile to DGII, 606 purchase report as TXT, updated IT-1 report, cédula next to RNC for eCommerce e-invoicing.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_do` · EE `l10n_do_check_printing`, `l10n_do_edi`, `l10n_do_reports`; [L]</sub>
- 🟡 **Ecuador 🇪🇨** — Accounting: custom legend on e-document PDFs, cleaner chart of accounts, better invoice layout, new withholding taxes, provider RUC on documents. POS: blocks 'Consumidor Final' sales above the legal limit.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ec`, `l10n_ec_sale` · EE `l10n_ec_edi`, `l10n_ec_edi_pos`, `l10n_ec_edi_stock`, `l10n_ec_reports`; backported [L]</sub>
- 🟡 **Egypt 🇪🇬** — Accounting: ETA sync in the Send wizard with demo mode and batch PDF fetch, 6-digit chart with parent accounts, updated VAT/withholding reports, gross-up withholding, ETA unit codes, state changes. Payroll: calendar-day schedules, overtime, NOSI/ETA forms. POS: e-receipts to ETA.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_eg`, `l10n_eg_edi_eta`, `l10n_eg_edi_pos` · EE `l10n_eg_hr_contract_salary`, `l10n_eg_hr_payroll`, `l10n_eg_hr_payroll_account`, `l10n_eg_iot`; ⚠️ change [L]</sub>
- 🟡 **France 🇫🇷** — Accounting: PCG-compliant annual report templates (plaquettes); automatic detection of e-invoicing directory endpoints from the SIREN.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_fr`, `l10n_fr_account`, `l10n_fr_facturx_chorus_pro`, `l10n_fr_hr_holidays` · EE `l10n_fr_account_loans`, `l10n_fr_fec_import`, `l10n_fr_intrastat`, `l10n_fr_reports`; [L]</sub>
- ✅ **Georgia 🇬🇪** — Accounting: new base localization (chart of accounts, taxes, VAT report) and ISO state codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); CE `l10n_ge`; backported [H]</sub>
- 🟡 **Guatemala 🇬🇹** — Accounting: Factura Especial (FESP), FEL cancellation via Infile, E10 fuel tax, SAT VAT books. eCommerce and POS: FEL e-invoicing requirements.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_gt` · EE `l10n_gt_edi`, `l10n_gt_edi_pos`, `l10n_gt_reports`; backported [L]</sub>
- 🟡 **Hong Kong 🇭🇰** — Accounting: HKFRS-compliant chart and statements. Payroll: many additions (MPF, IR56 forms, Autopay, rentals, leave rules, pay schedules, casual/non-employee structures, termination rules).  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_hk` · EE `l10n_hk_autopay`, `l10n_hk_hr_payroll`, `l10n_hk_hr_payroll_account`, `l10n_hk_payment_autopay`; ⚠️ change [L]</sub>
- 🟡 **Hungary 🇭🇺** — Accounting: A60 EC sales list; received bills fetched from the NAV API.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_hu`, `l10n_hu_edi` · EE `l10n_hu_intrastat`, `l10n_hu_reports`, `l10n_hu_reports_a60`; backported [L]</sub>
- 🟡 **India 🇮🇳** — Accounting: price-adjustment credit notes, bill of entry for imports with landed costs, flexible TDS, GST composition scheme (CMP-08, GSTR-4), Schedule III financial statements.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_in`, `l10n_in_boe`, `l10n_in_edi`, `l10n_in_ewaybill` · EE `l10n_in_asset`, `l10n_in_edi_gstr`, `l10n_in_hr_contract_salary`, `l10n_in_hr_payroll`; [L]</sub>
- 🟡 **Indonesia 🇮🇩** — Accounting: updated chart and asset models, simpler contact tax fields, PPN Dipungut tax. Payroll: default accounts, overtime rule. POS: QRIS kiosk payments.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_id`, `l10n_id_efaktur_coretax`, `l10n_id_pos`, `l10n_id_pos_self_order_qris` · EE `l10n_id_hr_payroll`, `l10n_id_hr_payroll_account`, `l10n_id_reports`; [L]</sub>
- 🔒 **Iraq 🇮🇶** — Payroll: new base payroll localization (salary structure, social insurance, leaves, end of service, overtime).  
  <sub>Payroll localizations are EE (`l10n_iq_hr_payroll*`); CE `l10n_iq` · EE `l10n_iq_hr_payroll`, `l10n_iq_hr_payroll_account`; [H]</sub>
- 🟡 **Italy 🇮🇹** — Accounting: notes (causale) and attachments (allegati) on e-invoices.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_it`, `l10n_it_edi`, `l10n_it_edi_doi`, `l10n_it_edi_sale` · EE `l10n_it_intrastat`, `l10n_it_pos`, `l10n_it_reports`, `l10n_it_riba`; [L]</sub>
- 🟡 **Japan 🇯🇵** — Accounting: statements and chart per Chusho Kaikei Yoryou and e-Tax codes; consumption tax section in the tax return.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_jp`, `l10n_jp_ubl_pint` · EE `l10n_jp_reports`, `l10n_jp_zengin`; [L]</sub>
- 🟡 **Jordan 🇯🇴** — Accounting: better JoFotara error handling and credit-note sync, new invoice types, UX in the Send wizard. POS: JoFotara refunds and receipts.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_jo`, `l10n_jo_edi`, `l10n_jo_edi_pos` · EE `l10n_jo_hr_payroll`, `l10n_jo_hr_payroll_account`, `l10n_jo_reports`; backported [L]</sub>
- ✅ **Kazakhstan 🇰🇿** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); CE `l10n_kz` · EE `l10n_kz_reports`; backported [H]</sub>
- 🟡 **Korea 🇰🇷** — Accounting: improved VAT reports; 'Issuance Type' on invoices routes data to report lines.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_kr`, `l10n_kr_sale` · EE `l10n_kr_reports`; [L]</sub>
- 🟡 **Kuwait 🇰🇼** — Accounting: ISO state codes. Payroll: new base localization.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_kw` · EE `l10n_kw_hr_payroll`, `l10n_kw_hr_payroll_account`; [L]</sub>
- ✅ **Kyrgyzstan 🇰🇬** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); backported [H]</sub>
- ✅ **Lebanon 🇱🇧** — Accounting: ISO state codes, duplicates removed.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); CE `l10n_lb_account`; ⚠️ change [H]</sub>
- 🔒 **Lithuania 🇱🇹** — Payroll: inputs converted to the new salary input flow.  
  <sub>Payroll localizations are EE (`l10n_lt_hr_payroll*`); CE `l10n_lt` · EE `l10n_lt_hr_payroll`, `l10n_lt_hr_payroll_account`, `l10n_lt_intrastat`, `l10n_lt_reports`; [H]</sub>
- 🔒 **Luxembourg 🇱🇺** — Payroll: Decsal and Decmal reports.  
  <sub>Payroll localizations are EE (`l10n_lu_hr_payroll*`); CE `l10n_lu` · EE `l10n_lu_hr_payroll`, `l10n_lu_hr_payroll_account`, `l10n_lu_reports`; [H]</sub>
- 🟡 **Malaysia 🇲🇾** — Accounting: consolidated invoices, MyInvois across branches and for sole proprietors. POS: self-service MyInvois e-invoicing.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_my`, `l10n_my_edi`, `l10n_my_edi_pos`, `l10n_my_ubl_pint` · EE `l10n_my_hr_payroll`, `l10n_my_hr_payroll_account`, `l10n_my_reports`; [L]</sub>
- 🟡 **Mexico 🇲🇽** — Accounting: bimonthly global invoices, CFDI cancellation acknowledgment, services in foreign-trade invoices, updated rates, factoring payments, NIF B-6/B-3 statements, complementary trial balance XML, SAT download of missing bills, smarter XML reader. Inventory: driver on delivery order. Payroll: CFDI link in payslip email.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_mx` · EE `l10n_mx_edi`, `l10n_mx_edi_extended`, `l10n_mx_edi_landing`, `l10n_mx_edi_pos`; backported [L]</sub>
- 🟡 **Oman 🇴🇲** — Accounting: ISO state codes. Payroll: new base localization including WPS salary files.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_om` · EE `l10n_om_hr_payroll`, `l10n_om_hr_payroll_account`, `l10n_om_reports`; [L]</sub>
- 🟡 **Pakistan 🇵🇰** — Accounting: reworked chart with parent accounts, streamlined taxes, dynamic statements, MRP tax, new partner ID fields, FBR e-invoicing. Payroll: year-end tax adjustment. POS: FBR real-time reporting.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_pk`, `l10n_pk_edi`, `l10n_pk_edi_pos` · EE `l10n_pk_hr_payroll`, `l10n_pk_hr_payroll_account`; ⚠️ change backported [L]</sub>
- 🟡 **Peru 🇵🇪** — Accounting: 19 SUNAT inventory-and-balances sub-books, GRE for internal transfers, electronic vendor withholding documents, fixed-amount ISC. POS: SUNAT thermal receipts.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_pe`, `l10n_pe_pos` · EE `l10n_pe_edi`, `l10n_pe_edi_pos`, `l10n_pe_edi_stock`, `l10n_pe_edi_withholding`; backported [L]</sub>
- 🟡 **Philippines 🇵🇭** — Accounting: BIR-compliant partner ledger and books of accounts, BIR 2306/2307 certificates, entity type, disbursement voucher, BIR1600VT and 2551Q reports, senior/PWD discounts. Payroll: base package with BIR forms, loan deductions, annualization.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ph`, `l10n_ph_invoice`, `l10n_ph_sale` · EE `l10n_ph_check_printing`, `l10n_ph_hr_payroll`, `l10n_ph_hr_payroll_account`, `l10n_ph_reports`; [L]</sub>
- ✅ **Qatar 🇶🇦** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); CE `l10n_qa`; [H]</sub>
- 🟡 **Romania 🇷🇴** — Accounting: CPV codes in eFactura, updated VAT, ANAF PDF retrieval, period sync, SAF-T with stock, D300 XML, resend rejected invoices.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ro`, `l10n_ro_edi`, `l10n_ro_edi_stock` · EE `l10n_ro_hr_payroll`, `l10n_ro_hr_payroll_account`, `l10n_ro_intrastat`, `l10n_ro_reports`; backported [L]</sub>
- 🟡 **Saudi Arabia 🇸🇦** — Accounting: reworked chart and asset models, many ZATCA improvements (Send wizard sync, batch, invoice/transaction types, exemption reasons, address rules, multi-ID). Payroll: many additions (GOSI, end of service, leave rules). POS: better down payments, on-demand ZATCA PDF.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_sa`, `l10n_sa_edi`, `l10n_sa_edi_pos`, `l10n_sa_pos` · EE `l10n_sa_hr_contract_salary`, `l10n_sa_hr_payroll`, `l10n_sa_hr_payroll_account`, `l10n_sa_hr_payroll_attendance`; ⚠️ change backported [L]</sub>
- 🟡 **Singapore 🇸🇬** — Accounting: refined GST taxes, IRAS-compliant invoice PDFs, SFRS-compliant chart and statements.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_sg`, `l10n_sg_ubl_pint` · EE `l10n_sg_reports`; backported [L]</sub>
- 🟡 **Sri Lanka 🇱🇰** — Accounting: new localization (chart, taxes, statements, VAT 001, WHT 001) and compliant tax invoice layout.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_lk` · EE `l10n_lk_reports`; backported [L]</sub>
- 🟡 **Taiwan 🇹🇼** — Accounting: updated chart, statements and tax reports; ECPay details on quotations. eCommerce and POS: ECPay e-invoicing.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_tw`, `l10n_tw_edi_ecpay`, `l10n_tw_edi_ecpay_pos`, `l10n_tw_edi_ecpay_sale` · EE `l10n_tw_reports`; backported [L]</sub>
- ✅ **Tajikistan 🇹🇯** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); backported [H]</sub>
- 🟡 **Thailand 🇹🇭** — Accounting: TFRS-compliant chart, RD Prep CSV exports, 50 Tawi certificate, withholding summary report, separate tax invoices, updated debit/credit note PDFs.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_th` · EE `l10n_th_reports`; backported [L]</sub>
- 🟡 **Türkiye 🇹🇷** — Accounting: many e-invoicing improvements (scenarios, types, Nilvera — now Enterprise-only), parent accounts per GIB chart, multi-ID partner identifiers, stamp taxes, exchange rates. Inventory: e-Dispatch send/receive. Payroll: advanced structure, severance, 1003B, incentives.  
  <sub>Nilvera e-invoicing/e-dispatch moved from Community to Enterprise (`l10n_tr_nilvera*` now OEEL-1). Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_tr` · EE `l10n_tr_currency_live_rate`, `l10n_tr_hr_payroll`, `l10n_tr_hr_payroll_account`, `l10n_tr_nilvera`; ⚠️ change backported [L]</sub>
- ✅ **Turkmenistan 🇹🇲** — Accounting: ISO 3166-2 state names and codes.  
  <sub>Country states are base data (`base/data/res.country.state.csv`, CE); backported [H]</sub>
- 🟡 **United Arab Emirates 🇦🇪** — Accounting: redesigned IFRS chart with parent accounts, asset models, FTA audit file. Payroll: GPSSA/ADPF contributions, DEWS, Emiratization report, WPS, end of service, overtime, calendar-day schedules.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_ae`, `l10n_ae_pos` · EE `l10n_ae_faf`, `l10n_ae_hr_contract_salary`, `l10n_ae_hr_payroll`, `l10n_ae_hr_payroll_account`; backported [L]</sub>
- 🟡 **United Kingdom 🇬🇧** — Accounting: HMRC authorisation per company; VAT returns for several companies without re-authenticating.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_uk` · EE `l10n_uk_bacs`, `l10n_uk_hmrc`, `l10n_uk_intrastat`, `l10n_uk_reports`; [L]</sub>
- 🟡 **United States of America 🇺🇸** — Accounting: dedicated accounts per asset model, 'Avalara Included' AvaTax option, redesigned sales tax report. Payroll: NYC/Yonkers taxes, overtime deduction, new states, payment-date-based YTD. Time Off: better default leave types.  
  <sub>Mixed: chart of accounts/taxes/data are CE; Payroll parts are EE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_us`, `l10n_us_account` · EE `l10n_us_1099`, `l10n_us_check_printing`, `l10n_us_direct_deposit`, `l10n_us_hr_payroll`; backported [L]</sub>
- 🟡 **Uruguay 🇺🇾** — Accounting: DGI taxpayer lookup via Uruware; non-billable products on e-invoices.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_uy` · EE `l10n_uy_edi`, `l10n_uy_edi_pos`, `l10n_uy_edi_stock`, `l10n_uy_reports`; [L]</sub>
- 🟡 **Uzbekistan 🇺🇿** — Accounting: new base localization (chart, taxes, statements), so'm symbol, Russian reports, PINFL on B2C invoices.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_uz` · EE `l10n_uz_hr_payroll`, `l10n_uz_hr_payroll_account`, `l10n_uz_reports`; backported [L]</sub>
- 🟡 **Vietnam 🇻🇳** — Accounting: chart and balance sheet per Circular 99/2025, 01/GTGT declaration with Appendix 142 and XML export, internal transfer notes via SInvoice, parent accounts, new journals/ledgers. POS: SInvoice e-invoices.  
  <sub>Mixed: chart of accounts/taxes/data are CE; tax report rendering (`account_reports`) and several EDI/report modules are EE - see module lists. Needs review by maintainers of this country's localization; CE `l10n_vn`, `l10n_vn_edi_viettel`, `l10n_vn_edi_viettel_pos`, `l10n_vn_edi_viettel_stock` · EE `l10n_vn_reports`; backported [L]</sub>

### Industries

Industry packages live in the public [odoo/industry](https://github.com/odoo/industry/tree/20.0) repository, but their manifests declare license OEEL-1 and they depend on Enterprise apps (Knowledge, Studio, Planning, POS Enterprise…), so none is installable on CE. Table = direct Enterprise dependencies.

- 🔒 **Accounting Firm** — Accounting Firm package: identity documents, anti-money-laundering, and a Databases dashboard to manage client databases.  
  <sub>EE `accountant`, `crm_enterprise`, `databases`, `documents`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder), `dms` (dms), `sign_oca` (sign); backported [H]</sub>
- 🔒 **Agri-Equipment Rental** — New package for renting and maintaining agricultural machinery.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Beauty Parlor** — New package for beauty parlors: customers, appointments, treatment follow-up, invoicing.  
  <sub>EE `account_online_payment`, `knowledge`, `pos_enterprise`, `website_appointment_crm`; OCA: `document_page` (knowledge); backported [H]</sub>
- 🔒 **Catering** — New package for caterers, from first contact to on-site planning.  
  <sub>EE `crm_enterprise`, `planning`, `project_forecast`; OCA: `fieldservice` (field-service); [H]</sub>
- 🔒 **Community Care** — New package for community care organisations: staff planning and holidays, residents and their data, knowledge transfer.  
  <sub>EE `appointment`, `documents_project_sign`, `hr_sign`, `planning_holidays`; OCA: `resource_booking` (calendar); [H]</sub>
- 🔒 **Construction Builder** — Construction Builder renamed General Contractor; quotes built from reusable section templates.  
  <sub>EE `crm_enterprise`, `documents`, `helpdesk`, `sale_project_forecast`; OCA: `dms` (dms), `helpdesk_mgmt` (helpdesk); ⚠️ change [H]</sub>
- 🔒 **Construction Developer** — Construction Developer renamed Property Developer and rebuilt on standard Manufacturing and Inventory (BoMs, MOs, routings, locations).  
  <sub>EE `web_gantt`, `web_studio`; OCA: `web_timeline` (web), `project_timeline` (project); ⚠️ change [H]</sub>
- 🔒 **Custom Industrial Equipment** — New engineer-to-order package for EPC and turnkey projects, from design to manufacturing, procurement and installation.  
  <sub>EE `documents`, `mrp_plm`, `project_forecast`, `quality_control`; OCA: `dms` (dms), `quality_control_oca` (manufacture); [H]</sub>
- 🔒 **Deposit module** — The Deposit Management module (from Beverage Distributor / Micro-Brewery) can be installed on its own.  
  <sub>EE `mrp_workorder`, `web_studio`; [H]</sub>
- 🔒 **Electronic Refurbishment** — New package for refurbishing electronics, with refurbishment grades and VAT margin scheme.  
  <sub>EE `accountant`, `knowledge`, `web_studio`, `website_appointment`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder), `document_page` (knowledge), `resource_booking` (calendar); [H]</sub>
- 🔒 **Excise module** — Excise module separates production from inventory adjustments in the excise report.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Hospitality industries** — Hotel, Holiday House, Guest House and Campsite packages: housekeeping, bar/restaurant charges on the final bill, seasonal pricing.  
  <sub>EE `web_studio`; backported [H]</sub>
- 🔒 **Hotel** — Hotel package: guest count, multiple companies and branches.  
  <sub>EE `web_studio`; [H]</sub>
- 🔒 **Interior Design** — New package for interior designers: website inquiries, resource planning, purchasing, projects and profitability.  
  <sub>EE `appointment`, `documents_sign`; OCA: `resource_booking` (calendar); [H]</sub>
- 🔒 **Machine and Tool Rental** — New package for machine and tool rental: contracts, quarantine on return, consumption-based down payments, run-time monitoring, maintenance.  
  <sub>EE `web_studio`; backported [H]</sub>
- 🔒 **Mental Therapy** — New package for mental health professionals: patients, sessions, notes, invoicing.  
  <sub>EE `appointment_account_payment`, `appointment_crm`, `knowledge`; OCA: `document_page` (knowledge); backported [H]</sub>
- 🔒 **Nonprofit Organization** — Nonprofit package: better donation receipts; petitions removed.  
  <sub>EE `documents_project`, `hr_sign`, `sale_planning`, `sale_subscription`; OCA: `contract` (contract), `subscription_oca` (contract); ⚠️ change [H]</sub>
- 🔒 **Pet Groomer** — New package for pet groomers.  
  <sub>EE `crm_enterprise`, `pos_enterprise`, `web_studio`, `website_appointment_crm`; backported [H]</sub>
- 🔒 **Physical Therapy** — New package for physical therapists: patients, sessions, treatment tracking, billing.  
  <sub>EE `appointment_account_payment`, `appointment_crm`, `knowledge`; OCA: `document_page` (knowledge); backported [H]</sub>
- 🔒 **Property Management** — Property Owner Association and Real Estate packages can be combined with Property Management in one database.  
  <sub>EE `accountant`, `appointment`, `documents_project_sale`, `helpdesk`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder), `document_page` (knowledge), `helpdesk_mgmt` (helpdesk), `sign_oca` (sign), `contract` (contract), `subscription_oca` (contract), `resource_booking` (calendar); [H]</sub>
- 🔒 **Property Owner Association** — Property Owner Association package: owner history, general meetings, cost distribution based on meter readings.  
  <sub>EE `accountant`, `appointment`, `documents_project_sale`, `helpdesk`; OCA: `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder), `document_page` (knowledge), `helpdesk_mgmt` (helpdesk), `sign_oca` (sign), `resource_booking` (calendar); backported [H]</sub>
- 🔒 **Public Institution** — New package for public institutions: citizen support, appointments, portal, facility rental, events.  
  <sub>EE `account_followup`, `documents_project`, `hr_sign`, `website_appointment`; OCA: `account_credit_control` (credit-control), `resource_booking` (calendar); [H]</sub>
- 🔒 **Real Estate** — Real Estate package: editable matchmaking criteria; combinable with Property Management.  
  <sub>EE `appointment_crm`, `documents`, `knowledge`, `project_enterprise`; OCA: `dms` (dms), `document_page` (knowledge), `sign_oca` (sign), `web_timeline` (web), `project_timeline` (project), `sale_commission_oca` (commission); backported [H]</sub>
- 🔒 **Talent Acquisition** — Talent Acquisition package: better link between applicants, talent pool and job positions.  
  <sub>EE `appointment_crm`, `appointment_hr_recruitment`, `crm_enterprise`, `documents_hr`; OCA: `sign_oca` (sign), `resource_booking` (calendar); [H]</sub>
- 🔒 **Vineyard** — New package for vineyards, from grape to wine.  
  <sub>EE `mrp_plm`, `pos_enterprise`, `quality_mrp`, `web_studio`; [H]</sub>

## Enterprise-only apps

All items of these sections belong to Enterprise modules (license OEEL-1). Pointers to Community (OCA) modules covering the same area are given where they exist — they are not feature-equivalent and most are not migrated to 20.0 yet.

| App | Items | Possible OCA alternative |
|---|---:|---|
| [Industries](#industries) | 25 | `account_financial_report` (account-financial-reporting), `mis_builder` (mis-builder), `dms` (dms), `sign_oca` (sign), `document_page` (knowledge), `fieldservice` (field-service), `resource_booking` (calendar), `helpdesk_mgmt` (helpdesk), `web_timeline` (web), `project_timeline` (project), `quality_control_oca` (manufacture), `contract` (contract), `subscription_oca` (contract), `account_credit_control` (credit-control), `sale_commission_oca` (commission) |
| [AI](#ai) | 20 | — |
| [Appointments](#appointments) | 19 | `resource_booking` (calendar) |
| [Appraisals](#appraisals) | 4 | `hr_appraisal_oca` (hr) |
| [Documents](#documents) | 9 | `dms` (dms) |
| [ESG](#esg) | 1 | — |
| [Field Service](#field-service) | 1 | `fieldservice` (field-service) |
| [Fleet](#fleet) | 1 | — |
| [Frontdesk](#frontdesk) | 1 | — |
| [Helpdesk](#helpdesk) | 3 | `helpdesk_mgmt` (helpdesk) |
| [Knowledge](#knowledge) | 1 | `document_page` (knowledge) |
| [Live Chat](#live-chat) | 1 | — |
| [Marketing Automation](#marketing-automation) | 6 | — |
| [Payroll](#payroll) | 15 | `payroll` (payroll) |
| [Phone](#phone) | 10 | `base_phone` (connector-telephony) |
| [Planning](#planning) | 20 | `fieldservice` (field-service) |
| [PLM](#plm) | 4 | — |
| [Quality](#quality) | 2 | `quality_control_oca` (manufacture) |
| [Referrals](#referrals) | 1 | — |
| [Rental](#rental) | 6 | — |
| [Shop Floor](#shop-floor) | 3 | — |
| [Sign](#sign) | 15 | `sign_oca` (sign) |
| [Social Marketing](#social-marketing) | 7 | — |
| [Subscriptions](#subscriptions) | 1 | `contract` (contract), `subscription_oca` (contract) |
| [Timesheets](#timesheets) | 5 | `hr_timesheet_sheet` (timesheet), `project_timesheet_time_control` (project) |
| [WhatsApp](#whatsapp) | 5 | `mail_gateway_whatsapp` (social) |

### Industries

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_78) · module(s): `account_followup`, `account_online_payment`, `accountant`, `appointment`, `appointment_account_payment`, `appointment_crm`</sub>

- **Accounting Firm** — Accounting Firm package: identity documents, anti-money-laundering, and a Databases dashboard to manage client databases.
- **Agri-Equipment Rental** — New package for renting and maintaining agricultural machinery.
- **Beauty Parlor** — New package for beauty parlors: customers, appointments, treatment follow-up, invoicing.
- **Catering** — New package for caterers, from first contact to on-site planning.
- **Community Care** — New package for community care organisations: staff planning and holidays, residents and their data, knowledge transfer.
- **Construction Builder** — Construction Builder renamed General Contractor; quotes built from reusable section templates.
- **Construction Developer** — Construction Developer renamed Property Developer and rebuilt on standard Manufacturing and Inventory (BoMs, MOs, routings, locations).
- **Custom Industrial Equipment** — New engineer-to-order package for EPC and turnkey projects, from design to manufacturing, procurement and installation.
- **Deposit module** — The Deposit Management module (from Beverage Distributor / Micro-Brewery) can be installed on its own.
- **Electronic Refurbishment** — New package for refurbishing electronics, with refurbishment grades and VAT margin scheme.
- **Excise module** — Excise module separates production from inventory adjustments in the excise report.
- **Hospitality industries** — Hotel, Holiday House, Guest House and Campsite packages: housekeeping, bar/restaurant charges on the final bill, seasonal pricing.
- **Hotel** — Hotel package: guest count, multiple companies and branches.
- **Interior Design** — New package for interior designers: website inquiries, resource planning, purchasing, projects and profitability.
- **Machine and Tool Rental** — New package for machine and tool rental: contracts, quarantine on return, consumption-based down payments, run-time monitoring, maintenance.
- **Mental Therapy** — New package for mental health professionals: patients, sessions, notes, invoicing.
- **Nonprofit Organization** — Nonprofit package: better donation receipts; petitions removed.
- **Pet Groomer** — New package for pet groomers.
- **Physical Therapy** — New package for physical therapists: patients, sessions, treatment tracking, billing.
- **Property Management** — Property Owner Association and Real Estate packages can be combined with Property Management in one database.
- **Property Owner Association** — Property Owner Association package: owner history, general meetings, cost distribution based on meter readings.
- **Public Institution** — New package for public institutions: citizen support, appointments, portal, facility rental, events.
- **Real Estate** — Real Estate package: editable matchmaking criteria; combinable with Property Management.
- **Talent Acquisition** — Talent Acquisition package: better link between applicants, talent pool and job positions.
- **Vineyard** — New package for vineyards, from grape to wine.

### AI

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_81) · module(s): `ai`, `ai_agentic`</sub>

- **IAP credits required** — All AI features consume IAP credits.
- **Agentic automation** — Agents can update their own configuration, run from automated/scheduled actions, and show automation chat logs; agents get avatars.
- **AI agents: ask questions about a file** — Ask an agent questions about a file while previewing it.
- **AI agents: create records** — Ask an agent to create records, including from an uploaded instruction file.
- **AI agents: feedback** — Agents show live progress instead of a generic 'thinking' message.
- **AI agents: filter by time period** — Agents can filter by periods (weeks, quarters…) when building views.
- **AI agents: image generation** — Agents generate images and buttons for websites and mailings.
- **AI agents: reprocess sources** — Ask agents to reprocess their sources.
- **AI agents: send files** — Upload files and link documents in agent chats.
- **AI agents: update records** — Ask an agent to update records.
- **AI chat request options** — A '+' menu adds options to an AI request.
- **Automatic AI model selection** — Pick a provider; Odoo chooses the best model per task.
- **Connect Odoo to anything** — Connect external tools to the database via MCP (Model Context Protocol).
- **Default prompts** — Default prompts with context and dynamic values.
- **Interactive agent responses** — Answer agent questions and permission requests with buttons.
- **Preview cards in live chat** — Agents in live chat can show clickable record cards.
- **Stored conversations** — Agent conversations are kept for 30 days.
- **Tool call limit confirmation** — Agents ask for confirmation when they hit the tool-call limit.
- **Topics renamed to skills** — 'Topics' are renamed 'skills'.
- **Voice interaction** — Dictate requests to an agent.

### Appointments

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_82) · module(s): `appointment`</sub>

- **Accessory products for appointments** — Sell accessory products during appointment checkout.
- **Appointment booking flow** — Choosing a user/resource and a time slot happens on one page.
- **Appointment names** — Customer name, type and seats shown on bookings in Gantt and calendar.
- **Appointment page design** — Refreshed appointment pages on mobile and desktop.
- **Appointment rescheduling** — Reschedule booked appointments in a few clicks.
- **Appointments calendar view** — Create bookings and assign resources from any schedule calendar view.
- **Attendance at a glance** — Gantt view shows expected attendance per slot.
- **Automatic resource assignment** — Automatic resource assignment considers the number of participants.
- **Availability display** — Accurate availability across appointment types, including private busy events.
- **Booking capacity control** — Limit how many bookings can start in the same slot.
- **Booking shortcuts** — Kanban shortcuts to bookings to confirm, upcoming and today's.
- **Closed days management** — Easier management of closed days.
- **Consistent booking page design** — Booking pages follow website styling even without the Website app.
- **Customer feedback** — Ask customers for feedback after appointments.
- **Default party size** — Group bookings preselect two guests.
- **Maximum capacity override** — Override maximum capacity manually.
- **Performance improvements** — Faster availability computation and booking.
- **Web page redesign** — More consistent booking pages with clearer information.
- **Website editor blocks** — Website editor blocks can be placed anywhere on appointment pages.

### Appraisals

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_83) · module(s): `hr_appraisal`</sub>

- **External 360 feedbacks** — Send 360° feedback requests to any contact.
- **Next appraisal date** — Managers can edit the next appraisal date without extra rights.
- **Parent goal progression** — Parent goals show progress from their sub-goals.
- **Smart template selection** — New appraisals pick the department's template by default.

### Documents

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_92) · module(s): `documents`</sub>

- **Access right management** — User groups to manage file and folder access.
- **Auto-sort fleet documents** — Fleet documents are sorted and linked to vehicles by licence plate.
- **Bank statement attachments** — Bank statement attachments available in Accounting and Documents.
- **Branch management** — Branches supported in the Accounting–Documents integration.
- **Document request upload notification** — Requesters are notified when requested documents are uploaded.
- **Employee documents** — Better Employees folder structure; payslips in a dedicated folder with shortcuts in each employee's drive.
- **Markdown previews and thumbnails** — Previews and thumbnails for Markdown files.
- **Multi-file document request** — Request several files in one request.
- **Rename files with AI** — Rename uploaded files with AI.

### ESG

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_97) · module(s): `esg`</sub>

- **Assign emission factors with AI** — AI picks the most suitable emission factor for emissions.

### Field Service

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_100) · module(s): `planning`</sub>

- **Field Service merged into Planning** — Field Service app discontinued; its features move into Planning.

### Fleet

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_101) · module(s): `hr_payroll_fleet`</sub>

- **Driver assignment** — Changing an employee's car in Payroll updates the vehicle's driver.

### Frontdesk

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_102) · module(s): `frontdesk`</sub>

- **Member entry management** — Restrict check-in to members, optionally for specific stations.

### Helpdesk

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_103) · module(s): `helpdesk`</sub>

- **Filter unanswered tickets** — Filter tickets whose last message is from the customer.
- **Reminder email before auto-closing tickets** — Remind customers by email before a ticket is auto-closed.
- **Similar ticket detection** — AI finds similar tickets and suggests answers.

### Knowledge

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_105) · module(s): `knowledge`</sub>

- **Article settings quick access** — Right-click an article in the sidebar to change its settings.

### Live Chat

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_106) · module(s): `social_facebook`, `social_instagram`</sub>

- **Connect social media messaging** — Answer Messenger and Instagram DMs from live chat.

### Marketing Automation

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_109) · module(s): `marketing_automation`</sub>

- **AI-assisted campaign creation** — AI helps set up campaigns.
- **Event-based triggers** — Campaigns triggered by events such as page visits or list subscriptions.
- **Mailing template library** — Save mailings as templates in a dedicated menu.
- **New triggers and actions** — New triggers (event, date, anniversary, webhook, on demand) and actions.
- **Webhook integration** — Webhooks add participants from external systems in real time.
- **Workflow builder** — Visual drag-and-drop workflow builder.

### Payroll

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_112) · module(s): `hr_payroll`</sub>

- **Chatter on pay runs** — Chatter on pay runs.
- **Contract date modification** — Contract dates can't be changed if payslips exist; use a revision instead.
- **Dashboard** — Payroll dashboard focused on setup and control warnings.
- **Driver assignment** — Car changes update the vehicle's driver.
- **Employee type per company or branch** — Employee types restricted per company or branch.
- **Net to gross simulation** — Simulate gross salary from a net amount.
- **Pay run workflow** — Step-by-step pay run workflow.
- **Payslip sending options** — Choose when payslips are sent (confirmation, payment, manual).
- **Payslip UX** — Cleaner 'Salary Computation' tab.
- **Salary indexation** — Index salaries by percentage and/or fixed amount.
- **Salary rules** — Salary rules can belong to several categories and structures.
- **Test print pay runs** — Test a pay run with printed payslips.
- **Time entry exports** — Standard format for time entry exports.
- **Work entries removal** — Work entries and the Planning–Payroll integration removed; work entry and time off types merged.
- **Working schedules** — Working schedules can define hours per day without start/end times.

### Phone

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_113) · module(s): `voip`</sub>

- **Audio settings during a call** — Change microphone/speaker during a call.
- **Auto-fill and auto-log** — Softphone pre-fills the current record's number and logs the call.
- **Call flow designer** — Design incoming call flows (extensions, menus, time/location rules).
- **Call logging in chatter** — Log calls in the chatter during or after the call.
- **Call transfer to another device** — Move an ongoing call to another device.
- **Choose outgoing number** — Choose the outgoing caller ID among several numbers.
- **Floating widget** — Floating, draggable softphone.
- **Linphone** — Provision Linphone via QR code.
- **Push notifications** — Push notifications for incoming calls.
- **Simultaneous calling** — Start or take a second call during a call.

### Planning

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_114) · module(s): `planning`</sub>

- **Employee-specific materials** — Materials assigned to employees follow them onto their shifts.
- **Field Service: auto plan** — Auto-planning considers customer locations.
- **Field Service: customer equipment** — Track whether customer equipment is under a maintenance contract.
- **Field Service: customer ratings** — Customer satisfaction ratings for on-site interventions.
- **Field Service: intervention confirmation email** — Optional confirmation email to the customer when a shift is published.
- **Field Service: live map** — Live map of technicians.
- **Field Service: map view** — Map view of shift locations and technician availability.
- **Field Service: product barcodes** — Add products to a shift by scanning barcodes.
- **Field Service: report** — Studio fields appear on the field service report.
- **Field Service: routing preferences** — Ordered or optimised routing on the map.
- **Field Service: track customer history** — Customer equipment and intervention history.
- **Field Service: travel fees** — Invoice distance-based or fixed travel fees.
- **Field Service: website form** — Collect service requests via a website form.
- **Field Service: worksheets** — Worksheet templates use property fields; worksheets on shift templates.
- **Gantt view: travel times** — Travel times in the Gantt view via Mapbox.
- **Link shifts to tasks** — Link a shift to a specific task.
- **Multiple resource assignment** — Several resources on one shift.
- **Priority shifts** — Shift priorities respected by auto-planning.
- **Schedule shifts from side panel** — Drag shifts from the side panel into calendar or Gantt.
- **Send shifts via WhatsApp** — Send schedules via WhatsApp.

### PLM

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_115) · module(s): `mrp_plm`</sub>

- **BoM comparison** — Compare bills of materials visually.
- **Optional ECO version update** — Version bump optional when applying an ECO.
- **Product updates** — Introduce new products through ECOs and track product versions.
- **Universal ECO report** — One report with all BoM changes and cost comparison.

### Quality

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_119) · module(s): `quality_control`</sub>

- **Bypass quality checks** — Quality admins can validate transfers without doing the checks.
- **Failure location** — Set the failure location on a failed quality check.

### Referrals

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_121) · module(s): `hr_referral`</sub>

- **Contact outreach tracking** — Track how many people were contacted to promote a job.

### Rental

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_122) · module(s): `sale_renting`</sub>

- **Automatic price update** — Changing pricelist or period updates prices on rental orders.
- **Rental order creation** — Add rental products to a normal sales order; a rental period field appears.
- **Rental orders dashboard** — Dashboard on top of rental orders.
- **Simplified and unified pricelists** — Sales, subscription and rental prices unified in one 'Prices' tab using pricelists.
- **Strikethrough pricing** — Shop shows original and discounted rental prices.
- **Working schedules** — 'Unavailability days' replaced by working schedules.

### Shop Floor

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_125) · module(s): `mrp_workorder`</sub>

- **HTML note field** — HTML note on MOs in Manufacturing and Shop Floor.
- **Instruction updates** — Editing an instruction starts from the current text.
- **Work center barcode** — Scan a work center barcode to select it.

### Sign

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_126) · module(s): `sign`</sub>

- **Automated signature requests** — Send signature requests from automated actions with fixed or dynamic signers.
- **Custom fields in templates** — Create custom Sign fields while building templates.
- **Improved progress tracking** — Full signer list and status for requests with many signers.
- **Tag management** — View and edit tags on templates and requests.
- **Itsme** — itsme authentication available in 30+ countries.
- **Mobile and touchscreen support** — Sign is fully responsive with touch support.
- **Non-latin alphabets** — More alphabets (Cyrillic, Devanagari, Arabic…).
- **Qualified electronic signatures** — Qualified electronic signatures (eIDAS QES) via itsme.
- **Record updates** — Sign fields can update the linked Odoo record.
- **Reorder signers** — Reorder signers in the editor.
- **Send signature requests from activities** — Start signature requests from activities and activity plans.
- **Sign mode options menu** — Signers can print, delegate or refuse from an options menu.
- **Sign templates** — Predefined CC recipients and reassignable ownership on templates.
- **Signed PDFs: bookmarks and settings** — Signed PDFs keep bookmarks and metadata.
- **Touchscreen support** — Place and move Sign items with finger or stylus.

### Social Marketing

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_127) · module(s): `social`</sub>

- **Add mentions in social media posts** — Mentions in social posts.
- **AI assistant** — AI writes social posts.
- **Facebook and Instagram stories** — Post Facebook and Instagram stories.
- **Image display order** — Choose image order for multi-image posts.
- **Personal LinkedIn account** — Post on a personal LinkedIn account.
- **Platform-specific post scheduling** — Different schedule per platform.
- **Schedule first comment** — Schedule a first comment on your own post.

### Subscriptions

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_130) · module(s): `sale_subscription`</sub>

- **Loyalty programs** — Loyalty rules and rewards for subscriptions.

### Timesheets

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_132) · module(s): `timer`, `timesheet_grid`</sub>

- **ActivityWatch integration** — ActivityWatch integration turns tracked device activity into timesheet suggestions, privately.
- **Log timesheets from anywhere** — Timer in the top bar to log time from anywhere.
- **Timesheet assistant: sharing rules** — Share timesheet assistant rules with users or groups.
- **Timesheet assistant: side activities** — 'Side Activity' rules for short interruptions.
- **Timesheet assistant: time thresholds** — Minimum duration before an activity is suggested.

### WhatsApp

<sub>[Official section](https://www.odoo.com/odoo-20-release-notes#table_of_content_heading_1_134) · module(s): `whatsapp`</sub>

- **Default recipents on templates** — Default recipients on WhatsApp templates.
- **Interactive message templates** — Interactive WhatsApp templates.
- **Named parameters in templates** — Named parameters in templates.
- **Number blocking** — Block a number from Odoo.
- **Simplified authentication process** — Simpler business account authentication.

## Method

The feature list follows the items of Odoo's official release notes. Each item was read and assigned by hand to the module(s) it belongs to. Each module's edition (LGPL-3 = Community, OEEL-1 = Enterprise) comes from the module lists of a CE and an EE 20.0 test database. Evidence was then collected per item: its UI texts in the modules' translation templates, targeted code searches (Community: public source; Enterprise: licensed copy searched locally, module names only), checks on the test databases, CE screenshots, and the 19.0 → 20.0 module diff. Details: [README](README.md).

| Confidence | Meaning |
|---|---|
| **Verified** [H] | A direct check backs the status: a distinctive UI text of the item occurs only in the named module(s); a code search written for this item hits the named module; a test-database check or a CE screenshot confirms it; the item belongs to an app that exists only as Enterprise module(s), so nothing of it can be in Community; or an industry package depends on Enterprise modules. |
| **Module-level** [M] | The module the feature lives in is known and its edition verified, but no direct match was found for this particular item. Main risk: a Community app item whose UI actually comes from an Enterprise extension module. |
| **Needs review** [L] | Judgement call without direct evidence: the item probably spans Community and Enterprise, or it bundles many changes (most localizations). |

---

*Generated by `tools/render.py` from `data/odoo-20.0.yaml`. Per-item evidence: [odoo-20-evidence.md](odoo-20-evidence.md).*
