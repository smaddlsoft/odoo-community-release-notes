# Screenshots

Screenshots come from a **Community** 20.0 test database only (never publish Enterprise screens). A file in `img/`
named after a highlight's id (`/` replaced by `__`) is embedded automatically, with the `caption` from
`data/highlights.yaml`. Crop to the relevant area and mark the feature (an orange box, as in the existing images),
so readers can match the image with the text. Then run `python tools/render.py` and `python tools/site.py`.

## Done (10)

| Highlight | File |
|---|---|
| Simplified access rights (`ir.access` form) | `img/general__simplified-access-rights.png` |
| Tax included/excluded switch | `img/general__tax-included-excluded-on-orders-and-invoices.png` |
| Multiple calendars / pending activities | `img/calendar__multiple-calendars-in-one-place.png` |
| Parent accounts | `img/accounting__parent-accounts.png` |
| Payment status "Reconciled" | `img/accounting__intuitive-payment-status.png` |
| Sales dashboard | `img/sales__dashboard.png` |
| Manufacturing order Kanban | `img/manufacturing__manufacturing-order-kanban-view.png` |
| Replenishment | `img/inventory__product-replenishment.png` |
| Pay on Invoice / Toss Payments | `img/online-payments__pay-on-invoice-provider.png` |
| llms.txt setting | `img/website__llms-txt.png` |

## Missing (3) — to take by hand

| Highlight | Where (CE test database, logged in) | What to show | File |
|---|---|---|---|
| New app icons | Open the main menu / home screen (`/odoo`) | The app icons in the new style | `img/general__material-symbols.png` |
| New dialog design | Any sales order → click **Activity** in the chatter | The Schedule Activity dialog (also shows assigning to a role) | `img/general__dialog-design.png` |
| Product images | Sales → a furniture order (e.g. S00007) → enable product images if needed | Product images on the order lines | `img/sales__product-images.png` |

## Open visual checks

Items the code could not settle. Look at them in the CE and EE test databases and record the result in
`data/odoo-20.0.yaml` (evidence line + `confidence: H`):

| Item id | Question | Current status |
|---|---|---|
| calendar/manage-and-share-availabilities | No "Share availabilities" button is visible in the CE Calendar (checked on the screenshot). Is it in EE with Appointments? | 🔒 EE (L) |
| dashboards/private-dashboards | CE Dashboards has a "My Dashboard" menu and a Share button. Can a dashboard be restricted to users/groups in CE? | ✅ CE (L) |
| dashboards/frozen-share-links | Is the menu to manage frozen share links present in CE Dashboards → Configuration? | 🔒 EE (L) |
| ecommerce/simplified-inventory-management | eCommerce without Inventory: is an on-hand quantity used in CE? | ✅ CE (L) |
| accounting/valuation-without-inventory | Product form without Inventory: stock on hand + valuation in CE Invoicing? | ✅ CE (L) |
| accounting/split-items-on-invoices | Invoice → Journal Items → "split" action present in CE? | ✅ CE (L) |
| accounting/bank-consistency | Can a CE user post a manual entry on a bank account? | 🟡 (L) |
