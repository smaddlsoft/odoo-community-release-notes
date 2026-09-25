# Odoo 20 — per-item evidence (DRAFT)

Machine-generated from `data/odoo-20.0.yaml`. *UI string* = the phrase occurs in the module's translation template (.pot); *code* = regex match in module source (CE: public GitHub 20.0; EE: only module names are reported).

## General

**✅ Activities** `general/activities` — confidence H (verified)  
  - UI string "Schedule Activity" -> CE: mail | EE: account_followup
  - code /Schedule Activity/ -> CE: mail, calendar | EE-only: account_followup
  - module license (CE runbot): mail=LGPL-3
  - CE screenshot (20.0 test database): Role field in the Schedule Activity dialog

**✅ Calendar view side panel** `general/calendar-view-side-panel` — confidence M (module-level)  
  - code /unschedul/ -> CE: web, website, website_event, maintenance, website_sale, mrp (+4) | EE-only: web_gantt, sale_planning, planning, project_enterprise
  - module license (CE runbot): web=LGPL-3

**✅ CC email recipients** `general/cc-email-recipients` — confidence M (module-level)  
  - code /email_cc/ -> CE: mail, website, account, auth_signup, auth_totp_mail, calendar (+6) | EE-only: hr_expense_stripe, web_studio
  - code /partner_cc/ -> CE: mail, account, calendar, website_slides | EE-only: ai, web_studio
  - module license (CE runbot): mail=LGPL-3

**✅ Chatter filter** `general/chatter-filter` — confidence H (verified)  
  - code /chatter.*filter|filter.*chatter/ -> CE: - | EE-only: hr_payroll, ai
  - module license (CE runbot): mail=LGPL-3
  - CE screenshot (20.0 test database): chatter filter (All / Messages / Notes / Activities / Changes)

**✅ Currency aggregates: date** `general/currency-aggregates-date` — confidence M (module-level)  
  - code /currency.*rate.*date|rate_date/ -> CE: account, spreadsheet, web, base, hr_expense, l10n_account_withholding_tax (+8) | EE-only: l10n_ar_edi, account_iso20022, l10n_mx_edi_pos, planning, sale_commission
  - module license (CE runbot): web=LGPL-3

**✅ Decimal separator** `general/decimal-separator` — confidence M (module-level)  
  - UI string "Decimal separator" -> CE: base
  - code /decimal.separator/ -> CE: web, base_import, l10n_es_edi_verifactu, spreadsheet, base | EE-only: l10n_ar_reports
  - module license (CE runbot): web=LGPL-3, base=LGPL-3

**✅ Dialog design** `general/dialog-design` — confidence H (verified)  
  - module license (CE runbot): web=LGPL-3
  - CE screenshot (20.0 test database): new Schedule Activity dialog

**✅ Digest email KPIs** `general/digest-email-kpis` — confidence M (module-level)  
  - UI string "New KPIs" -> EE: databases
  - code /kpi_/ -> CE: account, digest, mail, base_setup, crm, event (+14) | EE-only: account_accountant, account_reports, appointment, databases, documents, helpdesk (+4)
  - module license (CE runbot): digest=LGPL-3

**✅ Download attachments in bulk** `general/download-attachments-in-bulk` — confidence M (module-level)  
  - code /download.*attachments|attachments.*zip/ -> CE: account, mail, l10n_id_efaktur_coretax, l10n_th, cloud_storage_azure, cloud_storage_google (+3) | EE-only: account_reports, l10n_br_edi_pos, social, whatsapp_sign, l10n_be_reports, l10n_de_reports
  - module license (CE runbot): base=LGPL-3, web=LGPL-3

**✅ Email template preview** `general/email-template-preview` — confidence M (module-level)  
  - UI string "Email template preview" -> CE: mail
  - module license (CE runbot): mail=LGPL-3

**✅ Favorited searches** `general/favorited-searches` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**✅ File sharing on mobiles** `general/file-sharing-on-mobiles` — confidence H (verified)  
  - code /share_target/ -> CE: web, account, crm, hr_expense, hr_holidays, project (+2) | EE-only: -
  - module license (CE runbot): web=LGPL-3, account=LGPL-3, hr_expense=LGPL-3, project=LGPL-3, crm=LGPL-3, hr_holidays=LGPL-3

**🔒 Gantt view** `general/gantt-view` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): web_gantt=OEEL-1

**✅ Import product variants** `general/import-product-variants` — confidence M (module-level)  
  - module license (CE runbot): base_import=LGPL-3, product=LGPL-3

**✅ Incremental edits on duration fields** `general/incremental-edits-on-duration-fields` — confidence M (module-level)  
  - code /\+=|-=.*duration/ -> CE: web, mail, html_editor, point_of_sale, website, account (+234) | EE-only: l10n_be_hr_payroll, ai, sign, voip, hr_payroll, l10n_hk_hr_payroll (+233)
  - module license (CE runbot): web=LGPL-3

**✅ Label design** `general/label-design` — confidence M (module-level)  
  - module license (CE runbot): product=LGPL-3, stock=LGPL-3, mrp=LGPL-3

**✅ Link previews** `general/link-previews` — confidence M (module-level)  
  - UI string "Link previews" -> CE: mail
  - code /link.preview/ -> CE: mail, html_editor, im_livechat, project, link_tracker, sale (+1) | EE-only: ai, documents, knowledge, social_linkedin, social_twitter
  - module license (CE runbot): website=LGPL-3, mail=LGPL-3

**✅ Link to current search** `general/link-to-current-search` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**✅ List view: expand/collapse groups** `general/list-view-expand-collapse-groups` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**🟡 Mail plugins** `general/mail-plugins` — confidence M (module-level)  
  - UI string "Mail plugins" -> CE: crm, mail_plugin
  - module license (EE runbot ir.module.module): helpdesk_mail_plugin=OEEL-1
  - module license (CE runbot): mail_plugin=LGPL-3, crm_mail_plugin=LGPL-3, project_mail_plugin=LGPL-3

**🔒 Map view: unlocated records** `general/map-view-unlocated-records` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): web_map=OEEL-1

**✅ Material Symbols** `general/material-symbols` — confidence H (verified)  
  - CE source: no 'fa fa-' left in addons/web/static/src/**/*.xml
  - UI string "Font Awesome" -> CE: base
  - code /material.symbols|MaterialSymbols/ -> CE: html_editor, web, im_livechat, mail, website, auth_oauth (+3) | EE-only: ai_website
  - module license (CE runbot): web=LGPL-3

**🟡 Mobile** `general/mobile` — confidence M (module-level)  
  - code /bottom.?sheet/ -> CE: web, mail, html_editor, website_blog, crm, spreadsheet_dashboard | EE-only: web_map
  - module license (EE runbot ir.module.module): web_enterprise=OEEL-1
  - module license (CE runbot): web=LGPL-3

**✅ Multi-record drag and drop** `general/multi-record-drag-and-drop` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**✅ Multiple partner identifiers** `general/multiple-partner-identifiers` — confidence M (module-level)  
  - code /partner.*identifier|identifier_type/ -> CE: account_edi_ubl_cii, l10n_dk, account_peppol, l10n_fr_pdp, account, l10n_ar (+40) | EE-only: l10n_co_edi, l10n_ec_edi, sale_shopee, whatsapp, account_saft, l10n_ar_edi (+38)
  - module license (CE runbot): base=LGPL-3, account=LGPL-3

**✅ My Subscription page** `general/my-subscription-page` — confidence M (module-level)  
  - UI string "My Subscription" -> CE: mysubscription | EE: sale_subscription
  - module license (CE runbot): mysubscription=LGPL-3

**✅ Offline mode** `general/offline-mode` — confidence M (module-level)  
  - code /offline/ -> CE: web, mail, point_of_sale, website_event_track, bus, hr (+31) | EE-only: obox, iot, l10n_ec_edi, social_youtube, voip, product_unspsc (+3)
  - module license (CE runbot): web=LGPL-3

**✅ Partner autocomplete** `general/partner-autocomplete` — confidence M (module-level)  
  - UI string "Partner autocomplete" -> CE: base_setup, partner_autocomplete, pos_partner_autocomplete
  - module license (CE runbot): partner_autocomplete=LGPL-3

**✅ Pin messages in the chatter** `general/pin-messages-in-the-chatter` — confidence H (verified)  
  - code /pinned_at/ -> CE: mail | EE-only: -
  - module license (CE runbot): mail=LGPL-3
  - CE screenshot (20.0 test database): pinned-messages button in the chatter

**✅ Portal layout** `general/portal-layout` — confidence M (module-level)  
  - module license (CE runbot): portal=LGPL-3

**✅ Record deletion** `general/record-deletion` — confidence M (module-level)  
  - UI string "Record deletion" -> CE: privacy_lookup
  - module license (CE runbot): web=LGPL-3

**✅ Relative range tooltip** `general/relative-range-tooltip` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**✅ Rich-text editor** `general/rich-text-editor` — confidence M (module-level)  
  - module license (CE runbot): html_editor=LGPL-3

**✅ Product catalog: units of measure** `general/product-catalog-units-of-measure` — confidence M (module-level)  
  - module license (CE runbot): product=LGPL-3

**🔒 Sendcloud shipping labels** `general/sendcloud-shipping-labels` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): delivery_sendcloud=OEEL-1

**✅ Simplified access rights** `general/simplified-access-rights` — confidence H (verified)  
  - runbot CE (API): model ir.model.access does not exist; ir.access exists (base, mail, website)
  - CE source: odoo/addons/base/models/ir_access.py; 226 CE modules ship security/ir.access.csv, 0 ship ir.model.access.csv
  - code /_name = .ir\.access./ -> CE: mail, base | EE-only: web_studio
  - module license (CE runbot): base=LGPL-3
  - CE screenshot (20.0 test database): ir.access form with operations and domain

**✅ Tablets: bottom sheets** `general/tablets-bottom-sheets` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**✅ Tax included/excluded on orders and invoices** `general/tax-included-excluded-on-orders-and-invoices` — confidence H (verified)  
  - code /tax_calculation|price_include_override|Tax Included/ -> CE: account, website_sale, point_of_sale, sale, l10n_account_withholding_tax, l10n_sa (+22) | EE-only: l10n_br_edi, account_avatax, l10n_br_edi_pos, l10n_ch_hr_payroll, l10n_do_edi, l10n_gt_edi (+7)
  - module license (CE runbot): account=LGPL-3, sale=LGPL-3, purchase=LGPL-3
  - CE screenshot (20.0 test database): 'Tax Excl.' switch on a sales order

**✅ Text messages** `general/text-messages` — confidence M (module-level)  
  - module license (CE runbot): sms=LGPL-3

**✅ Translation** `general/translation` — confidence H (verified)  
  - UI string "Translation Mode" -> CE: website, test_translation
  - code /Translation Mode/ -> CE: website, test_translation_mode, web, test_translation | EE-only: -
  - module license (CE runbot): test_translation_mode=LGPL-3, web=LGPL-3

**✅ Translation wizard** `general/translation-wizard` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

## Technical

**✅ Mail: in-body tracking** `technical/mail-in-body-tracking` — confidence H (verified)  
  - runbot CE (API): model mail.tracking.value is provided by module mail_tracking
  - module diff 19.0→20.0: mail_tracking, mail_tracking_mass_mailing, mail_tracking_sms are new CE modules
  - OCA index: mail_tracking and mail_tracking_mass_mailing exist in OCA/mail@18.0 and @19.0
  - module license (CE runbot): mail=LGPL-3, mail_tracking=LGPL-3

**✅ Many-to-one field improvements** `technical/many-to-one-field-improvements` — confidence M (module-level)  
  - module license (CE runbot): web=LGPL-3

**🟡 Push notifications** `technical/push-notifications` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): mail_mobile=OEEL-1
  - module license (CE runbot): mail=LGPL-3, web=LGPL-3

**✅ Track source of postings** `technical/track-source-of-postings` — confidence M (module-level)  
  - module license (CE runbot): mail=LGPL-3

**✅ Tracking user group changes** `technical/tracking-user-group-changes` — confidence M (module-level)  
  - module license (CE runbot): base=LGPL-3

## Industries

**🔒 Accounting Firm** `industries/accounting-firm` — confidence H (verified)  
  - industry module(s) accounting_firm (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): accounting_firm -> accountant, crm_enterprise, databases, documents, equity, sale_planning, sale_timesheet_enterprise, sign, web_studio
  - module license (EE runbot ir.module.module): accountant=OEEL-1, crm_enterprise=OEEL-1, databases=OEEL-1, documents=OEEL-1, equity=OEEL-1, sale_planning=OEEL-1

**🔒 Agri-Equipment Rental** `industries/agri-equipment-rental` — confidence H (verified)  
  - industry module(s) agri_equipment_rental (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): agri_equipment_rental -> web_studio
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Beauty Parlor** `industries/beauty-parlor` — confidence H (verified)  
  - industry module(s) beauty_parlor (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): beauty_parlor -> account_online_payment, knowledge, pos_enterprise, website_appointment_crm
  - module license (EE runbot ir.module.module): account_online_payment=OEEL-1, knowledge=OEEL-1, pos_enterprise=OEEL-1, website_appointment_crm=OEEL-1

**🔒 Catering** `industries/catering` — confidence H (verified)  
  - industry module(s) catering (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): catering -> crm_enterprise, planning, project_forecast
  - module license (EE runbot ir.module.module): crm_enterprise=OEEL-1, planning=OEEL-1, project_forecast=OEEL-1

**🔒 Community Care** `industries/community-care` — confidence H (verified)  
  - industry module(s) community_care (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): community_care -> appointment, documents_project_sign, hr_sign, planning_holidays, project_holidays, timesheet_grid_holidays, web_studio
  - module license (EE runbot ir.module.module): appointment=OEEL-1, documents_project_sign=OEEL-1, hr_sign=OEEL-1, planning_holidays=OEEL-1, project_holidays=OEEL-1, timesheet_grid_holidays=OEEL-1

**🔒 Construction Builder** `industries/construction-builder` — confidence H (verified)  
  - industry module(s) construction (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): construction -> crm_enterprise, documents, helpdesk, sale_project_forecast, sale_timesheet_enterprise
  - module license (EE runbot ir.module.module): crm_enterprise=OEEL-1, documents=OEEL-1, helpdesk=OEEL-1, sale_project_forecast=OEEL-1, sale_timesheet_enterprise=OEEL-1

**🔒 Construction Developer** `industries/construction-developer` — confidence H (verified)  
  - industry module(s) construction_developer (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): construction_developer -> web_gantt, web_studio
  - module license (EE runbot ir.module.module): web_gantt=OEEL-1, web_studio=OEEL-1

**🔒 Custom Industrial Equipment** `industries/custom-industrial-equipment` — confidence H (verified)  
  - industry module(s) custom_industrial_equipment (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): custom_industrial_equipment -> documents, mrp_plm, project_forecast, quality_control
  - module license (EE runbot ir.module.module): documents=OEEL-1, mrp_plm=OEEL-1, project_forecast=OEEL-1, quality_control=OEEL-1

**🔒 Deposit module** `industries/deposit-module` — confidence H (verified)  
  - industry module(s) deposit_management (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): deposit_management -> mrp_workorder, web_studio
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1, web_studio=OEEL-1

**🔒 Electronic Refurbishment** `industries/electronic-refurbishment` — confidence H (verified)  
  - industry module(s) electronic_refurbishment (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): electronic_refurbishment -> accountant, knowledge, web_studio, website_appointment
  - module license (EE runbot ir.module.module): accountant=OEEL-1, knowledge=OEEL-1, web_studio=OEEL-1, website_appointment=OEEL-1

**🔒 Excise module** `industries/excise-module` — confidence H (verified)  
  - industry module(s) excise_management (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): excise_management -> web_studio
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Hospitality industries** `industries/hospitality-industries` — confidence H (verified)  
  - industry module(s) hotel, holiday_house, guest_house, campsite (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): hotel -> web_studio; holiday_house -> web_studio; guest_house -> web_studio; campsite -> web_studio
  - UI string "Steering" -> CE: fleet
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Hotel** `industries/hotel` — confidence H (verified)  
  - industry module(s) hotel (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): hotel -> web_studio
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Interior Design** `industries/interior-design` — confidence H (verified)  
  - industry module(s) interior_design (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): interior_design -> appointment, documents_sign
  - UI string "Interior Design" -> CE: product, sale_timesheet | EE: theme_real_estate
  - module license (EE runbot ir.module.module): appointment=OEEL-1, documents_sign=OEEL-1

**🔒 Machine and Tool Rental** `industries/machine-and-tool-rental` — confidence H (verified)  
  - industry module(s) machine_tool_rental (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): machine_tool_rental -> web_studio
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Mental Therapy** `industries/mental-therapy` — confidence H (verified)  
  - industry module(s) mental_therapy (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): mental_therapy -> appointment_account_payment, appointment_crm, knowledge
  - module license (EE runbot ir.module.module): appointment_account_payment=OEEL-1, appointment_crm=OEEL-1, knowledge=OEEL-1

**🔒 Nonprofit Organization** `industries/nonprofit-organization` — confidence H (verified)  
  - industry module(s) non_profit_organization (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): non_profit_organization -> documents_project, hr_sign, sale_planning, sale_subscription, web_studio
  - module license (EE runbot ir.module.module): documents_project=OEEL-1, hr_sign=OEEL-1, sale_planning=OEEL-1, sale_subscription=OEEL-1, web_studio=OEEL-1

**🔒 Pet Groomer** `industries/pet-groomer` — confidence H (verified)  
  - industry module(s) pet_groomer (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): pet_groomer -> crm_enterprise, pos_enterprise, web_studio, website_appointment_crm
  - module license (EE runbot ir.module.module): crm_enterprise=OEEL-1, pos_enterprise=OEEL-1, web_studio=OEEL-1, website_appointment_crm=OEEL-1

**🔒 Physical Therapy** `industries/physical-therapy` — confidence H (verified)  
  - industry module(s) physical_therapy (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): physical_therapy -> appointment_account_payment, appointment_crm, knowledge
  - module license (EE runbot ir.module.module): appointment_account_payment=OEEL-1, appointment_crm=OEEL-1, knowledge=OEEL-1

**🔒 Property Management** `industries/property-management` — confidence H (verified)  
  - industry module(s) property_assets_distribution, condominium, industry_real_estate (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): property_assets_distribution -> sale_subscription, web_studio; condominium -> accountant, appointment, documents_project_sale, helpdesk, knowledge, sign, web_studio; industry_real_estate -> knowledge, project_sale_subscription
  - module license (EE runbot ir.module.module): accountant=OEEL-1, appointment=OEEL-1, documents_project_sale=OEEL-1, helpdesk=OEEL-1, knowledge=OEEL-1, project_sale_subscription=OEEL-1

**🔒 Property Owner Association** `industries/property-owner-association` — confidence H (verified)  
  - industry module(s) condominium (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): condominium -> accountant, appointment, documents_project_sale, helpdesk, knowledge, sign, web_studio
  - module license (EE runbot ir.module.module): accountant=OEEL-1, appointment=OEEL-1, documents_project_sale=OEEL-1, helpdesk=OEEL-1, knowledge=OEEL-1, sign=OEEL-1

**🔒 Public Institution** `industries/public-institution` — confidence H (verified)  
  - industry module(s) public_institution (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): public_institution -> account_followup, documents_project, hr_sign, website_appointment, website_helpdesk, website_sale_renting_planning
  - UI string "Public Institution" -> CE: l10n_rs_edi
  - module license (EE runbot ir.module.module): account_followup=OEEL-1, documents_project=OEEL-1, hr_sign=OEEL-1, website_appointment=OEEL-1, website_helpdesk=OEEL-1, website_sale_renting_planning=OEEL-1

**🔒 Real Estate** `industries/real-estate` — confidence H (verified)  
  - industry module(s) industry_real_estate, real_estate (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): industry_real_estate -> knowledge, project_sale_subscription; real_estate -> appointment_crm, documents, project_enterprise, sale_commission, sign
  - module license (EE runbot ir.module.module): appointment_crm=OEEL-1, documents=OEEL-1, knowledge=OEEL-1, project_enterprise=OEEL-1, project_sale_subscription=OEEL-1, sale_commission=OEEL-1

**🔒 Talent Acquisition** `industries/talent-acquisition` — confidence H (verified)  
  - industry module(s) headhunter (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): headhunter -> appointment_crm, appointment_hr_recruitment, crm_enterprise, documents_hr, documents_product, sign, web_studio, website_appointment
  - UI string "Talent Acquisition" -> CE: hr, website
  - module license (EE runbot ir.module.module): appointment_crm=OEEL-1, appointment_hr_recruitment=OEEL-1, crm_enterprise=OEEL-1, documents_hr=OEEL-1, documents_product=OEEL-1, sign=OEEL-1

**🔒 Vineyard** `industries/vineyard` — confidence H (verified)  
  - industry module(s) vineyard (github.com/odoo/industry 20.0, manifest license OEEL-1) depend on EE module(s): vineyard -> mrp_plm, pos_enterprise, quality_mrp, web_studio
  - UI string "Vineyard" -> CE: l10n_us
  - module license (EE runbot ir.module.module): mrp_plm=OEEL-1, pos_enterprise=OEEL-1, quality_mrp=OEEL-1, web_studio=OEEL-1

## Accounting

**✅ Accounting Firms mode settings** `accounting/accounting-firms-mode-settings` — confidence M (module-level)  
  - UI string "Accounting Firms mode" -> CE: account
  - UI string "Accounting Firms" -> CE: account
  - module license (CE runbot): account=LGPL-3

**🔒 Analytic distribution for write-offs** `accounting/analytic-distribution-for-write-offs` — confidence H (verified)  
  - code /account\.reconcile\.wizard/ -> CE: - | EE-only: account_accountant, hr_payroll_expense
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1

**🔒 Annual report layout** `accounting/annual-report-layout` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_reports=OEEL-1

**🔒 Asset depreciation** `accounting/asset-depreciation` — confidence M (module-level)  
  - UI string "Asset depreciation" -> EE: account_asset
  - UI string "Rates and" -> CE: base | EE: hr_payroll, l10n_be_reports
  - module license (EE runbot ir.module.module): account_asset=OEEL-1

**🟡 Bank consistency** `accounting/bank-consistency` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1
  - module license (CE runbot): account=LGPL-3

**🔒 Bank reconciliation summary report** `accounting/bank-reconciliation-summary-report` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_reports=OEEL-1

**🔒 Bank synchronization: Syncfy** `accounting/bank-synchronization-syncfy` — confidence M (module-level)  
  - no direct evidence yet (classified from the module/app it belongs to)

**🔒 Bill line prediction** `accounting/bill-line-prediction` — confidence M (module-level)  
  - code /_predict_/ -> CE: account_edi_ubl_cii, l10n_it_edi, base | EE-only: hr_expense_extract, account_accountant
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1

**🟡 Bill options display** `accounting/bill-options-display` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): account_asset=OEEL-1, account_accountant=OEEL-1
  - module license (CE runbot): account=LGPL-3

**✅ Bill/invoice matching rules** `accounting/bill-invoice-matching-rules` — confidence M (module-level)  
  - UI string "Matching Rules" -> CE: account | EE: timesheet_grid
  - module license (CE runbot): account=LGPL-3

**✅ Cash journal entry hashing** `accounting/cash-journal-entry-hashing` — confidence H (verified)  
  - code /hash.*cash|cash.*hash/ -> CE: account | EE-only: -
  - module license (CE runbot): account=LGPL-3

**✅ Conversion rates** `accounting/conversion-rates` — confidence M (module-level)  
  - UI string "Conversion rates" -> CE: mass_mailing
  - module license (CE runbot): account=LGPL-3

**🔒 Cumulative Translation Adjustment (CTA)** `accounting/cumulative-translation-adjustment-cta` — confidence M (module-level)  
  - UI string "Cumulative Translation Adjustment" -> EE: account_reports, l10n_my_reports, l10n_us_reports
  - module license (EE runbot ir.module.module): account_reports=OEEL-1

**🔒 Currency exchange rate providers** `accounting/currency-exchange-rate-providers` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): currency_rate_live=OEEL-1

**🟡 Customer invoice reminders** `accounting/customer-invoice-reminders` — confidence M (module-level)  
  - UI string "Automatic in" -> CE: sale, base | EE: account_followup, sale_subscription
  - code /invoice_reminder|send_reminder/ -> CE: purchase, calendar, account, calendar_sms | EE-only: account_followup, l10n_hk_hr_payroll, timesheet_grid
  - module license (EE runbot ir.module.module): account_followup=OEEL-1
  - module license (CE runbot): account=LGPL-3

**✅ Download invoice attachments** `accounting/download-invoice-attachments` — confidence L (needs review)  
  - code /download.*zip|zip.*download/ -> CE: account, iot_drivers, l10n_th, l10n_ro_edi, pos_self_order, website | EE-only: documents, sign, account_reports, iot, l10n_be_reports, whatsapp_sign
  - module license (CE runbot): account=LGPL-3

**✅ Employee Expenses menu item** `accounting/employee-expenses-menu-item` — confidence M (module-level)  
  - UI string "Employee Expenses" -> CE: hr, hr_expense
  - module license (CE runbot): hr_expense=LGPL-3

**✅ Exchange entries** `accounting/exchange-entries` — confidence M (module-level)  
  - module license (CE runbot): account=LGPL-3

**✅ Improved duplicate detection** `accounting/improved-duplicate-detection` — confidence M (module-level)  
  - code /duplicate/ -> CE: mail, account, website, web, spreadsheet, base (+90) | EE-only: voip, data_cleaning, ai, ai_website, hr_payroll, sign (+64)
  - module license (CE runbot): account=LGPL-3

**🔒 Intercompany purchase order matching** `accounting/intercompany-purchase-order-matching` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): account_inter_company_rules=OEEL-1

**✅ Intuitive payment status** `accounting/intuitive-payment-status` — confidence H (verified)  
  - runbot CE (API): account.payment.state selection = draft, paid, reconciled, canceled, rejected
  - UI string "Mark as Reconciled" -> CE: account
  - module license (CE runbot): account=LGPL-3
  - CE screenshot (20.0 test database): 'Reconciled' payment status

**✅ Inventory valuation** `accounting/inventory-valuation` — confidence M (module-level)  
  - UI string "Bills To Receive" -> CE: account, purchase
  - UI string "Billed Not Received" -> CE: account, purchase
  - UI string "Invoices To Be Issued" -> CE: account, sale
  - UI string "Invoiced Not Delivered" -> CE: account, sale
  - code /Bills To Receive|Billed Not Received/ -> CE: purchase, account | EE-only: -
  - module license (CE runbot): purchase=LGPL-3, account=LGPL-3, stock_account=LGPL-3

**🟡 Invoice email attachments** `accounting/invoice-email-attachments` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): documents_account=OEEL-1
  - module license (CE runbot): account=LGPL-3

**🟡 Manual reconciliation** `accounting/manual-reconciliation` — confidence M (module-level)  
  - UI string "Payment Reconciliation" -> CE: account | EE: l10n_be_reports
  - UI string "Exchange Rate Difference" -> CE: account | EE: l10n_mn_reports
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1
  - module license (CE runbot): account=LGPL-3
  - CE screenshot (20.0 test database): 'Payment Reconciliation' column in the chart of accounts

**🔒 Multi-ledger consolidation** `accounting/multi-ledger-consolidation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_reports=OEEL-1

**✅ Multiple invoice details** `accounting/multiple-invoice-details` — confidence M (module-level)  
  - module license (CE runbot): account=LGPL-3

**✅ New currency: Caribbean Guilder** `accounting/new-currency-caribbean-guilder` — confidence H (verified)  
  - code /XCG/ -> CE: base, account, l10n_sa_edi | EE-only: product_unspsc
  - module license (CE runbot): base=LGPL-3

**🟡 Onboarding improvements** `accounting/onboarding-improvements` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1
  - module license (CE runbot): account=LGPL-3

**🔒 Optimized data entry** `accounting/optimized-data-entry` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1

**🔒 PAIN version setting** `accounting/pain-version-setting` — confidence H (verified)  
  - UI string "The PAIN" -> EE: knowledge
  - code /pain\.001/ -> CE: - | EE-only: account_iso20022
  - module license (EE runbot ir.module.module): account_iso20022=OEEL-1

**✅ Parent accounts** `accounting/parent-accounts` — confidence H (verified)  
  - runbot CE (API): model account.group absent
  - runbot CE (API): account.account.parent_id many2one(account.account) from module account; account.account.code required=False
  - code /parent_id.*account\.account|account\.account.*parent_id/ -> CE: account | EE-only: account_reports
  - module license (CE runbot): account=LGPL-3
  - CE screenshot (20.0 test database): parent-account tree in the chart of accounts

**🔒 Pay bills from Odoo** `accounting/pay-bills-from-odoo` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): account_online_payment=OEEL-1

**✅ Peppol global location identifiers** `accounting/peppol-global-location-identifiers` — confidence H (verified)  
  - code /\bgln\b|global_location/ -> CE: account_edi_ubl_cii, account, l10n_dk, barcodes_gs1_nomenclature, l10n_es_edi_facturae, l10n_hr_edi | EE-only: -
  - module license (CE runbot): account_edi_ubl_cii=LGPL-3, account_peppol=LGPL-3

**✅ Prevent double payments in the payment wizard** `accounting/prevent-double-payments-in-the-payment-wizard` — confidence M (module-level)  
  - module license (CE runbot): account=LGPL-3

**✅ Professional percentage for receipts** `accounting/professional-percentage-for-receipts` — confidence M (module-level)  
  - code /[Pp]rofessional.*(percent|%)/ -> CE: account | EE-only: -
  - module license (CE runbot): account=LGPL-3

**✅ Purchase order matching** `accounting/purchase-order-matching` — confidence H (verified)  
  - code /_match_purchase|unmatch/ -> CE: purchase, account, google_calendar, sale_purchase, website_sale_loyalty | EE-only: account_reports, hr_payroll_expense, l10n_uk_reports_cis
  - module license (CE runbot): purchase=LGPL-3, account=LGPL-3

**🔒 Reconciliation with multiple accounts** `accounting/reconciliation-with-multiple-accounts` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1

**🔒 Reminder workflow** `accounting/reminder-workflow` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_followup=OEEL-1

**✅ Reset to Draft action in list views** `accounting/reset-to-draft-action-in-list-views` — confidence M (module-level)  
  - code /Reset to Draft/ -> CE: account, account_peppol, hr_expense, l10n_sa_edi, hr_attendance, l10n_cn (+9) | EE-only: account_asset, planning, account_accountant, hr_expense_stripe, l10n_ar_edi, l10n_au_hr_payroll_api (+9)
  - module license (CE runbot): account=LGPL-3

**🔒 Run Auto Reconciliation** `accounting/run-auto-reconciliation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_accountant=OEEL-1

**🔒 Simplification of asset models** `accounting/simplification-of-asset-models` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): account_asset=OEEL-1

**✅ Split items on invoices** `accounting/split-items-on-invoices` — confidence L (needs review)  
  - module license (CE runbot): account=LGPL-3

**✅ Taxes in fiscal positions** `accounting/taxes-in-fiscal-positions` — confidence M (module-level)  
  - module license (CE runbot): account=LGPL-3

**✅ Valuation without Inventory** `accounting/valuation-without-inventory` — confidence L (needs review)  
  - module license (CE runbot): stock_account=LGPL-3, account=LGPL-3

**✅ Withholding tax on payment improvements** `accounting/withholding-tax-on-payment-improvements` — confidence M (module-level)  
  - UI string "Withhold Due" -> CE: l10n_account_withholding_tax
  - module license (CE runbot): l10n_account_withholding_tax=LGPL-3

## Localizations

**🟡 Argentina 🇦🇷** `localizations/argentina` — confidence L (needs review)  
  - UI string "Payment on Informed CBU" -> EE: l10n_ar_edi
  - UI string "Pre-Printed Journal" -> CE: l10n_ar
  - module license (EE runbot ir.module.module): l10n_ar_edi=OEEL-1, l10n_ar_reports=OEEL-1
  - module license (CE runbot): l10n_ar=LGPL-3, l10n_ar_pos=LGPL-3, l10n_ar_stock=LGPL-3, l10n_ar_website_sale=LGPL-3, l10n_ar_withholding=LGPL-3

**✅ Armenia 🇦🇲** `localizations/armenia` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 11 state_am_* records

**🟡 Australia 🇦🇺** `localizations/australia` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_au_aba=OEEL-1, l10n_au_hr_payroll=OEEL-1, l10n_au_hr_payroll_account=OEEL-1, l10n_au_hr_payroll_api=OEEL-1, l10n_au_reports=OEEL-1
  - module license (CE runbot): l10n_au=LGPL-3

**✅ Azerbaijan 🇦🇿** `localizations/azerbaijan` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 77 state_az_* records

**✅ Bahrain 🇧🇭** `localizations/bahrain` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 4 state_bh_* records
  - module license (EE runbot ir.module.module): l10n_bh_reports=OEEL-1
  - module license (CE runbot): l10n_bh=LGPL-3

**🟡 Bangladesh 🇧🇩** `localizations/bangladesh` — confidence L (needs review)  
  - UI string "Tax Deducted" -> CE: l10n_in
  - module license (EE runbot ir.module.module): l10n_bd_hr_payroll=OEEL-1, l10n_bd_hr_payroll_account=OEEL-1, l10n_bd_reports=OEEL-1
  - module license (CE runbot): l10n_bd=LGPL-3

**🔒 Belgium 🇧🇪** `localizations/belgium` — confidence H (verified)  
  - UI string "Regular Pay" -> EE: hr_payroll
  - module license (EE runbot ir.module.module): l10n_be_coda=OEEL-1, l10n_be_codabox=OEEL-1, l10n_be_codaclean=OEEL-1, l10n_be_fiscal_categories=OEEL-1, l10n_be_hr_contract_salary=OEEL-1, l10n_be_hr_payroll=OEEL-1
  - module license (CE runbot): l10n_be=LGPL-3, l10n_be_pos=LGPL-3, l10n_be_pos_restaurant=LGPL-3, l10n_be_pos_sale=LGPL-3

**🟡 Brazil 🇧🇷** `localizations/brazil` — confidence L (needs review)  
  - UI string "Taxes Settings" -> EE: l10n_br_edi
  - UI string "CBS Presumed Credit" -> EE: l10n_br_edi
  - UI string "IBS Presumed Credit" -> EE: l10n_br_edi
  - UI string "CBS/IBS Taxpayer" -> EE: l10n_br_edi
  - UI string "Purpose of Use" -> EE: l10n_br_avatax, l10n_br_edi_pos
  - UI string "SPED Fiscal Product Type" -> EE: l10n_br_avatax
  - UI string "Source of Origin" -> EE: l10n_br_avatax
  - UI string "IS Taxable" -> CE: l10n_in | EE: l10n_be_reports, l10n_br_edi
  - UI string "NF-e and" -> EE: delivery_envia
  - UI string "Cancel NFC-e" -> EE: l10n_br_edi_pos
  - module license (EE runbot ir.module.module): l10n_br_avatax=OEEL-1, l10n_br_avatax_sale=OEEL-1, l10n_br_edi=OEEL-1, l10n_br_edi_extract=OEEL-1, l10n_br_edi_pos=OEEL-1, l10n_br_edi_sale=OEEL-1
  - module license (CE runbot): l10n_br=LGPL-3, l10n_br_sales=LGPL-3, l10n_br_website_sale=LGPL-3

**🟡 Canada 🇨🇦** `localizations/canada` — confidence L (needs review)  
  - UI string "Pre-Authorized Debit" -> CE: l10n_ca
  - module license (EE runbot ir.module.module): l10n_ca_check_printing=OEEL-1, l10n_ca_payment_cpa005=OEEL-1, l10n_ca_reports=OEEL-1
  - module license (CE runbot): l10n_ca=LGPL-3

**🟡 Chile 🇨🇱** `localizations/chile` — confidence L (needs review)  
  - UI string "Contacts and" -> CE: account_peppol, base
  - UI string "Copies of" -> CE: mail | EE: hr_expense_stripe
  - module license (EE runbot ir.module.module): l10n_cl_edi=OEEL-1, l10n_cl_edi_exports=OEEL-1, l10n_cl_edi_factoring=OEEL-1, l10n_cl_edi_pos=OEEL-1, l10n_cl_edi_stock=OEEL-1, l10n_cl_edi_website_sale=OEEL-1
  - module license (CE runbot): l10n_cl=LGPL-3

**🟡 China 🇨🇳** `localizations/china` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_cn_reports=OEEL-1
  - module license (CE runbot): l10n_cn=LGPL-3

**🟡 Colombia 🇨🇴** `localizations/colombia` — confidence L (needs review)  
  - UI string "Contingency in" -> EE: l10n_co_edi
  - UI string "Mandate in" -> EE: equity
  - module license (EE runbot ir.module.module): l10n_co_edi=OEEL-1, l10n_co_edi_pos=OEEL-1, l10n_co_reports=OEEL-1
  - module license (CE runbot): l10n_co=LGPL-3, l10n_co_pos=LGPL-3

**🟡 Dominican Republic 🇩🇴** `localizations/dominican-republic` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_do_check_printing=OEEL-1, l10n_do_edi=OEEL-1, l10n_do_reports=OEEL-1
  - module license (CE runbot): l10n_do=LGPL-3

**🟡 Ecuador 🇪🇨** `localizations/ecuador` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_ec_edi=OEEL-1, l10n_ec_edi_pos=OEEL-1, l10n_ec_edi_stock=OEEL-1, l10n_ec_reports=OEEL-1, l10n_ec_reports_ats=OEEL-1
  - module license (CE runbot): l10n_ec=LGPL-3, l10n_ec_sale=LGPL-3

**🟡 Egypt 🇪🇬** `localizations/egypt` — confidence L (needs review)  
  - UI string "Building Number" -> CE: l10n_eg_edi_eta, l10n_kr, l10n_sa_edi | EE: l10n_pl_reports
  - UI string "Egyptian Tax Authority" -> CE: l10n_eg_edi_eta, l10n_eg_edi_pos
  - UI string "Payslips in" -> EE: hr_payroll
  - UI string "Social Insurance" -> EE: l10n_mn_reports, l10n_si_reports
  - module license (EE runbot ir.module.module): l10n_eg_hr_contract_salary=OEEL-1, l10n_eg_hr_payroll=OEEL-1, l10n_eg_hr_payroll_account=OEEL-1, l10n_eg_iot=OEEL-1, l10n_eg_reports=OEEL-1
  - module license (CE runbot): l10n_eg=LGPL-3, l10n_eg_edi_eta=LGPL-3, l10n_eg_edi_pos=LGPL-3

**🟡 France 🇫🇷** `localizations/france` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_fr_account_loans=OEEL-1, l10n_fr_fec_import=OEEL-1, l10n_fr_intrastat=OEEL-1, l10n_fr_reports=OEEL-1
  - module license (CE runbot): l10n_fr=LGPL-3, l10n_fr_account=LGPL-3, l10n_fr_facturx_chorus_pro=LGPL-3, l10n_fr_hr_holidays=LGPL-3, l10n_fr_payment=LGPL-3, l10n_fr_pdp=LGPL-3

**✅ Georgia 🇬🇪** `localizations/georgia` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 12 state_ge_* records
  - module license (CE runbot): l10n_ge=LGPL-3

**🟡 Guatemala 🇬🇹** `localizations/guatemala` — confidence L (needs review)  
  - UI string "Factura Especial" -> EE: l10n_gt_edi
  - module license (EE runbot ir.module.module): l10n_gt_edi=OEEL-1, l10n_gt_edi_pos=OEEL-1, l10n_gt_reports=OEEL-1
  - module license (CE runbot): l10n_gt=LGPL-3

**🟡 Hong Kong 🇭🇰** `localizations/hong-kong` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_hk_autopay=OEEL-1, l10n_hk_hr_payroll=OEEL-1, l10n_hk_hr_payroll_account=OEEL-1, l10n_hk_payment_autopay=OEEL-1, l10n_hk_reports=OEEL-1
  - module license (CE runbot): l10n_hk=LGPL-3

**🟡 Hungary 🇭🇺** `localizations/hungary` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_hu_intrastat=OEEL-1, l10n_hu_reports=OEEL-1, l10n_hu_reports_a60=OEEL-1
  - module license (CE runbot): l10n_hu=LGPL-3, l10n_hu_edi=LGPL-3

**🟡 India 🇮🇳** `localizations/india` — confidence L (needs review)  
  - UI string "Apply TDS" -> EE: l10n_in_reports
  - UI string "Payment Only" -> CE: l10n_account_withholding_tax
  - UI string "Schedule III" -> EE: l10n_in_reports
  - module license (EE runbot ir.module.module): l10n_in_asset=OEEL-1, l10n_in_edi_gstr=OEEL-1, l10n_in_hr_contract_salary=OEEL-1, l10n_in_hr_payroll=OEEL-1, l10n_in_hr_payroll_account=OEEL-1, l10n_in_pos_urban_piper=OEEL-1
  - module license (CE runbot): l10n_in=LGPL-3, l10n_in_boe=LGPL-3, l10n_in_edi=LGPL-3, l10n_in_ewaybill=LGPL-3, l10n_in_ewaybill_irn=LGPL-3, l10n_in_ewaybill_stock=LGPL-3

**🟡 Indonesia 🇮🇩** `localizations/indonesia` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_id_hr_payroll=OEEL-1, l10n_id_hr_payroll_account=OEEL-1, l10n_id_reports=OEEL-1
  - module license (CE runbot): l10n_id=LGPL-3, l10n_id_efaktur_coretax=LGPL-3, l10n_id_pos=LGPL-3, l10n_id_pos_self_order_qris=LGPL-3

**🔒 Iraq 🇮🇶** `localizations/iraq` — confidence H (verified)  
  - module license (EE runbot ir.module.module): l10n_iq_hr_payroll=OEEL-1, l10n_iq_hr_payroll_account=OEEL-1
  - module license (CE runbot): l10n_iq=LGPL-3

**🟡 Italy 🇮🇹** `localizations/italy` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_it_intrastat=OEEL-1, l10n_it_pos=OEEL-1, l10n_it_reports=OEEL-1, l10n_it_riba=OEEL-1
  - module license (CE runbot): l10n_it=LGPL-3, l10n_it_edi=LGPL-3, l10n_it_edi_doi=LGPL-3, l10n_it_edi_sale=LGPL-3, l10n_it_stock_ddt=LGPL-3

**🟡 Japan 🇯🇵** `localizations/japan` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_jp_reports=OEEL-1, l10n_jp_zengin=OEEL-1
  - module license (CE runbot): l10n_jp=LGPL-3, l10n_jp_ubl_pint=LGPL-3

**🟡 Jordan 🇯🇴** `localizations/jordan` — confidence L (needs review)  
  - UI string "Foreign Trade" -> CE: account, l10n_jo_edi | EE: l10n_mx_edi_stock
  - UI string "Free Zone Transfer" -> CE: l10n_jo_edi
  - module license (EE runbot ir.module.module): l10n_jo_hr_payroll=OEEL-1, l10n_jo_hr_payroll_account=OEEL-1, l10n_jo_reports=OEEL-1
  - module license (CE runbot): l10n_jo=LGPL-3, l10n_jo_edi=LGPL-3, l10n_jo_edi_pos=LGPL-3

**✅ Kazakhstan 🇰🇿** `localizations/kazakhstan` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 20 state_kz_* records
  - module license (EE runbot ir.module.module): l10n_kz_reports=OEEL-1
  - module license (CE runbot): l10n_kz=LGPL-3

**🟡 Korea 🇰🇷** `localizations/korea` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_kr_reports=OEEL-1
  - module license (CE runbot): l10n_kr=LGPL-3, l10n_kr_sale=LGPL-3

**🟡 Kuwait 🇰🇼** `localizations/kuwait` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_kw_hr_payroll=OEEL-1, l10n_kw_hr_payroll_account=OEEL-1
  - module license (CE runbot): l10n_kw=LGPL-3

**✅ Kyrgyzstan 🇰🇬** `localizations/kyrgyzstan` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 9 state_kg_* records

**✅ Lebanon 🇱🇧** `localizations/lebanon` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 8 state_lb_* records
  - module license (CE runbot): l10n_lb_account=LGPL-3

**🔒 Lithuania 🇱🇹** `localizations/lithuania` — confidence H (verified)  
  - module license (EE runbot ir.module.module): l10n_lt_hr_payroll=OEEL-1, l10n_lt_hr_payroll_account=OEEL-1, l10n_lt_intrastat=OEEL-1, l10n_lt_reports=OEEL-1, l10n_lt_saft=OEEL-1, l10n_lt_saft_import=OEEL-1
  - module license (CE runbot): l10n_lt=LGPL-3

**🔒 Luxembourg 🇱🇺** `localizations/luxembourg` — confidence H (verified)  
  - module license (EE runbot ir.module.module): l10n_lu_hr_payroll=OEEL-1, l10n_lu_hr_payroll_account=OEEL-1, l10n_lu_reports=OEEL-1
  - module license (CE runbot): l10n_lu=LGPL-3

**🟡 Malaysia 🇲🇾** `localizations/malaysia` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_my_hr_payroll=OEEL-1, l10n_my_hr_payroll_account=OEEL-1, l10n_my_reports=OEEL-1
  - module license (CE runbot): l10n_my=LGPL-3, l10n_my_edi=LGPL-3, l10n_my_edi_pos=LGPL-3, l10n_my_ubl_pint=LGPL-3

**🟡 Mexico 🇲🇽** `localizations/mexico` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_mx_edi=OEEL-1, l10n_mx_edi_extended=OEEL-1, l10n_mx_edi_landing=OEEL-1, l10n_mx_edi_pos=OEEL-1, l10n_mx_edi_sale=OEEL-1, l10n_mx_edi_stock=OEEL-1
  - module license (CE runbot): l10n_mx=LGPL-3

**🟡 Oman 🇴🇲** `localizations/oman` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_om_hr_payroll=OEEL-1, l10n_om_hr_payroll_account=OEEL-1, l10n_om_reports=OEEL-1
  - module license (CE runbot): l10n_om=LGPL-3

**🟡 Pakistan 🇵🇰** `localizations/pakistan` — confidence L (needs review)  
  - UI string "Business Identification Number" -> CE: l10n_de, base
  - UI string "Consumer Identification" -> CE: base
  - UI string "Payslips in" -> EE: hr_payroll
  - module license (EE runbot ir.module.module): l10n_pk_hr_payroll=OEEL-1, l10n_pk_hr_payroll_account=OEEL-1
  - module license (CE runbot): l10n_pk=LGPL-3, l10n_pk_edi=LGPL-3, l10n_pk_edi_pos=LGPL-3

**🟡 Peru 🇵🇪** `localizations/peru` — confidence L (needs review)  
  - UI string "System Type" -> EE: esg
  - module license (EE runbot ir.module.module): l10n_pe_edi=OEEL-1, l10n_pe_edi_pos=OEEL-1, l10n_pe_edi_stock=OEEL-1, l10n_pe_edi_withholding=OEEL-1, l10n_pe_reports=OEEL-1, l10n_pe_reports_lib=OEEL-1
  - module license (CE runbot): l10n_pe=LGPL-3, l10n_pe_pos=LGPL-3

**🟡 Philippines 🇵🇭** `localizations/philippines` — confidence L (needs review)  
  - UI string "Middle Name" -> CE: l10n_ph | EE: l10n_ph_reports
  - UI string "Bureau of Internal Revenue" -> CE: l10n_ph | EE: l10n_ph_reports
  - UI string "Generate and" -> CE: loyalty, payment | EE: hr_payroll, l10n_uy_edi
  - UI string "Send BIR" -> EE: l10n_ph_reports
  - UI string "BIR Form" -> CE: l10n_ph | EE: l10n_ph_reports
  - module license (EE runbot ir.module.module): l10n_ph_check_printing=OEEL-1, l10n_ph_hr_payroll=OEEL-1, l10n_ph_hr_payroll_account=OEEL-1, l10n_ph_reports=OEEL-1, l10n_ph_reports_asset=OEEL-1, l10n_ph_reports_stock=OEEL-1
  - module license (CE runbot): l10n_ph=LGPL-3, l10n_ph_invoice=LGPL-3, l10n_ph_sale=LGPL-3

**✅ Qatar 🇶🇦** `localizations/qatar` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 8 state_qa_* records
  - module license (CE runbot): l10n_qa=LGPL-3

**🟡 Romania 🇷🇴** `localizations/romania` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_ro_hr_payroll=OEEL-1, l10n_ro_hr_payroll_account=OEEL-1, l10n_ro_intrastat=OEEL-1, l10n_ro_reports=OEEL-1, l10n_ro_reports_d300=OEEL-1, l10n_ro_reports_d390=OEEL-1
  - module license (CE runbot): l10n_ro=LGPL-3, l10n_ro_edi=LGPL-3, l10n_ro_edi_stock=LGPL-3

**🟡 Saudi Arabia 🇸🇦** `localizations/saudi-arabia` — confidence L (needs review)  
  - UI string "Invoice Total Payable Amount" -> CE: l10n_sa
  - UI string "Supply End Date" -> CE: l10n_sa_edi
  - UI string "Building Number" -> CE: l10n_eg_edi_eta, l10n_kr, l10n_sa_edi | EE: l10n_pl_reports
  - UI string "Secondary Number" -> CE: l10n_sa_edi
  - UI string "Plot Identification" -> CE: l10n_sa_edi
  - UI string "Supply Date" -> CE: account, l10n_sa, l10n_sa_edi
  - module license (EE runbot ir.module.module): l10n_sa_hr_contract_salary=OEEL-1, l10n_sa_hr_payroll=OEEL-1, l10n_sa_hr_payroll_account=OEEL-1, l10n_sa_hr_payroll_attendance=OEEL-1, l10n_sa_hr_payroll_gosi=OEEL-1, l10n_sa_reports=OEEL-1
  - module license (CE runbot): l10n_sa=LGPL-3, l10n_sa_edi=LGPL-3, l10n_sa_edi_pos=LGPL-3, l10n_sa_pos=LGPL-3

**🟡 Singapore 🇸🇬** `localizations/singapore` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_sg_reports=OEEL-1
  - module license (CE runbot): l10n_sg=LGPL-3, l10n_sg_ubl_pint=LGPL-3

**🟡 Sri Lanka 🇱🇰** `localizations/sri-lanka` — confidence L (needs review)  
  - UI string "Sri Lanka" -> CE: website_blog, base
  - module license (EE runbot ir.module.module): l10n_lk_reports=OEEL-1
  - module license (CE runbot): l10n_lk=LGPL-3

**🟡 Taiwan 🇹🇼** `localizations/taiwan` — confidence L (needs review)  
  - UI string "ECPay in" -> CE: l10n_tw_edi_ecpay, l10n_tw_edi_ecpay_pos, l10n_tw_edi_ecpay_sale
  - module license (EE runbot ir.module.module): l10n_tw_reports=OEEL-1
  - module license (CE runbot): l10n_tw=LGPL-3, l10n_tw_edi_ecpay=LGPL-3, l10n_tw_edi_ecpay_pos=LGPL-3, l10n_tw_edi_ecpay_sale=LGPL-3, l10n_tw_edi_ecpay_website_sale=LGPL-3

**✅ Tajikistan 🇹🇯** `localizations/tajikistan` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 5 state_tj_* records

**🟡 Thailand 🇹🇭** `localizations/thailand` — confidence L (needs review)  
  - UI string "The Company ID" -> CE: l10n_my_edi | EE: account_saft
  - UI string "Debit and" -> CE: account | EE: l10n_gt_edi, l10n_uy_edi, l10n_vn_reports
  - module license (EE runbot ir.module.module): l10n_th_reports=OEEL-1
  - module license (CE runbot): l10n_th=LGPL-3

**🟡 Türkiye 🇹🇷** `localizations/t-rkiye` — confidence L (needs review)  
  - UI string "Türkiye - Accounting" -> CE: l10n_tr | EE: l10n_tr_reports
  - UI string "Default Return from Sales Account" -> EE: l10n_tr_reports
  - UI string "Invoice Types" -> CE: l10n_es, l10n_jo_edi
  - UI string "Tax Offices" -> CE: l10n_tr
  - UI string "Return and" -> CE: repair
  - UI string "The Nilvera" -> EE: l10n_tr_nilvera
  - UI string "Stamp Tax" -> EE: l10n_tr_reports
  - UI string "Default Return" -> EE: l10n_tr_reports
  - UI string "Sales Account" -> EE: l10n_tr_reports
  - UI string "Archive in" -> EE: l10n_tr_nilvera
  - UI string "Upload in" -> CE: account
  - module license (EE runbot ir.module.module): l10n_tr_currency_live_rate=OEEL-1, l10n_tr_hr_payroll=OEEL-1, l10n_tr_hr_payroll_account=OEEL-1, l10n_tr_nilvera=OEEL-1, l10n_tr_nilvera_edispatch=OEEL-1, l10n_tr_nilvera_einvoice=OEEL-1
  - module license (CE runbot): l10n_tr=LGPL-3
  - module diff 19.0→20.0: l10n_tr_nilvera, l10n_tr_nilvera_einvoice, l10n_tr_nilvera_edispatch removed from CE and present in the EE 20.0 source

**✅ Turkmenistan 🇹🇲** `localizations/turkmenistan` — confidence H (verified)  
  - CE source: odoo/addons/base/data/res.country.state.csv has 6 state_tm_* records

**🟡 United Arab Emirates 🇦🇪** `localizations/united-arab-emirates` — confidence L (needs review)  
  - UI string "Federal Tax Authority" -> EE: l10n_ae_faf
  - module license (EE runbot ir.module.module): l10n_ae_faf=OEEL-1, l10n_ae_hr_contract_salary=OEEL-1, l10n_ae_hr_payroll=OEEL-1, l10n_ae_hr_payroll_account=OEEL-1, l10n_ae_reports=OEEL-1
  - module license (CE runbot): l10n_ae=LGPL-3, l10n_ae_pos=LGPL-3

**🟡 United Kingdom 🇬🇧** `localizations/united-kingdom` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_uk_bacs=OEEL-1, l10n_uk_hmrc=OEEL-1, l10n_uk_intrastat=OEEL-1, l10n_uk_reports=OEEL-1, l10n_uk_reports_cis=OEEL-1
  - module license (CE runbot): l10n_uk=LGPL-3

**🟡 United States of America 🇺🇸** `localizations/united-states-of-america` — confidence L (needs review)  
  - UI string "Avalara Included" -> EE: account_avatax
  - UI string "New Jersey" -> CE: l10n_us | EE: ai
  - module license (EE runbot ir.module.module): l10n_us_1099=OEEL-1, l10n_us_check_printing=OEEL-1, l10n_us_direct_deposit=OEEL-1, l10n_us_hr_payroll=OEEL-1, l10n_us_hr_payroll_account=OEEL-1, l10n_us_payment_nacha=OEEL-1
  - module license (CE runbot): l10n_us=LGPL-3, l10n_us_account=LGPL-3

**🟡 Uruguay 🇺🇾** `localizations/uruguay` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_uy_edi=OEEL-1, l10n_uy_edi_pos=OEEL-1, l10n_uy_edi_stock=OEEL-1, l10n_uy_reports=OEEL-1
  - module license (CE runbot): l10n_uy=LGPL-3

**🟡 Uzbekistan 🇺🇿** `localizations/uzbekistan` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_uz_hr_payroll=OEEL-1, l10n_uz_hr_payroll_account=OEEL-1, l10n_uz_reports=OEEL-1
  - module license (CE runbot): l10n_uz=LGPL-3

**🟡 Vietnam 🇻🇳** `localizations/vietnam` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): l10n_vn_reports=OEEL-1
  - module license (CE runbot): l10n_vn=LGPL-3, l10n_vn_edi_viettel=LGPL-3, l10n_vn_edi_viettel_pos=LGPL-3, l10n_vn_edi_viettel_stock=LGPL-3

## AI

**🔒 IAP credits required** `ai/iap-credits-required` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Agentic automation** `ai/agentic-automation` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: ask questions about a file** `ai/ai-agents-ask-questions-about-a-file` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: create records** `ai/ai-agents-create-records` — confidence H (verified)  
  - UI string "create records" -> CE: web | EE: ai, l10n_mx_edi
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: feedback** `ai/ai-agents-feedback` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: filter by time period** `ai/ai-agents-filter-by-time-period` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: image generation** `ai/ai-agents-image-generation` — confidence H (verified)  
  - UI string "image generation" -> EE: ai_website
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: reprocess sources** `ai/ai-agents-reprocess-sources` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: send files** `ai/ai-agents-send-files` — confidence H (verified)  
  - UI string "send files" -> EE: l10n_cl_edi, l10n_cl_edi_stock
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI agents: update records** `ai/ai-agents-update-records` — confidence H (verified)  
  - UI string "update records" -> CE: mail | EE: ai
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 AI chat request options** `ai/ai-chat-request-options` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Automatic AI model selection** `ai/automatic-ai-model-selection` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Connect Odoo to anything** `ai/connect-odoo-to-anything` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Default prompts** `ai/default-prompts` — confidence H (verified)  
  - UI string "Default prompts" -> EE: ai, ai_agentic
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Interactive agent responses** `ai/interactive-agent-responses` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Preview cards in live chat** `ai/preview-cards-in-live-chat` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Stored conversations** `ai/stored-conversations` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Tool call limit confirmation** `ai/tool-call-limit-confirmation` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Topics renamed to skills** `ai/topics-renamed-to-skills` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

**🔒 Voice interaction** `ai/voice-interaction` — confidence H (verified)  
  - module license (EE runbot ir.module.module): ai=OEEL-1, ai_agentic=OEEL-1

## Appointments

**🔒 Accessory products for appointments** `appointments/accessory-products-for-appointments` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Appointment booking flow** `appointments/appointment-booking-flow` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Appointment names** `appointments/appointment-names` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Appointment page design** `appointments/appointment-page-design` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Appointment rescheduling** `appointments/appointment-rescheduling` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Appointments calendar view** `appointments/appointments-calendar-view` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Attendance at a glance** `appointments/attendance-at-a-glance` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Automatic resource assignment** `appointments/automatic-resource-assignment` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Availability display** `appointments/availability-display` — confidence H (verified)  
  - UI string "Availability display" -> EE: room
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Booking capacity control** `appointments/booking-capacity-control` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Booking shortcuts** `appointments/booking-shortcuts` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Closed days management** `appointments/closed-days-management` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Consistent booking page design** `appointments/consistent-booking-page-design` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Customer feedback** `appointments/customer-feedback` — confidence H (verified)  
  - UI string "Customer feedback" -> CE: project | EE: helpdesk
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Default party size** `appointments/default-party-size` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Maximum capacity override** `appointments/maximum-capacity-override` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Performance improvements** `appointments/performance-improvements` — confidence H (verified)  
  - UI string "Performance improvements" -> EE: esg
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Web page redesign** `appointments/web-page-redesign` — confidence H (verified)  
  - UI string "Relevant in" -> CE: hr, point_of_sale, project | EE: esg
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**🔒 Website editor blocks** `appointments/website-editor-blocks` — confidence H (verified)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

## Appraisals

**🔒 External 360 feedbacks** `appraisals/external-360-feedbacks` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_appraisal=OEEL-1

**🔒 Next appraisal date** `appraisals/next-appraisal-date` — confidence H (verified)  
  - UI string "Next appraisal date" -> EE: hr_appraisal
  - module license (EE runbot ir.module.module): hr_appraisal=OEEL-1

**🔒 Parent goal progression** `appraisals/parent-goal-progression` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_appraisal=OEEL-1

**🔒 Smart template selection** `appraisals/smart-template-selection` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_appraisal=OEEL-1

## Attendances

**✅ Automatic check-out time** `attendances/automatic-check-out-time` — confidence M (module-level)  
  - module license (CE runbot): hr_attendance=LGPL-3

**✅ Overtime analysis report** `attendances/overtime-analysis-report` — confidence M (module-level)  
  - module license (CE runbot): hr_attendance=LGPL-3

**✅ Overtime rulesets** `attendances/overtime-rulesets` — confidence M (module-level)  
  - module license (CE runbot): hr_attendance=LGPL-3

**✅ Photo at check-in** `attendances/photo-at-check-in` — confidence M (module-level)  
  - module license (CE runbot): hr_attendance=LGPL-3

**✅ Prevent app use** `attendances/prevent-app-use` — confidence M (module-level)  
  - module license (CE runbot): hr_attendance=LGPL-3

**✅ Public holiday option ruleset** `attendances/public-holiday-option-ruleset` — confidence M (module-level)  
  - UI string "Define and" -> CE: pos_restaurant
  - module license (CE runbot): hr_attendance=LGPL-3

## Barcode

**🔒 Backorders** `barcode/backorders` — confidence H (verified)  
  - UI string "Backorders" -> CE: mrp, stock | EE: stock_barcode
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Barcode product creation** `barcode/barcode-product-creation` — confidence H (verified)  
  - UI string "Barcode Lookup" -> CE: product | EE: pos_barcodelookup
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Batch receipts** `barcode/batch-receipts` — confidence H (verified)  
  - UI string "Batch receipts" -> EE: stock_barcode
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**✅ Bulk lot/serial number generation** `barcode/bulk-lot-serial-number-generation` — confidence H (verified)  
  - code /action_generate_lot|generate_serial|next_serial/ -> CE: stock, mrp, repair, mrp_subcontracting, product_expiry | EE-only: mrp_workorder, stock_barcode, stock_barcode_mrp
  - module license (CE runbot): stock=LGPL-3

**🔒 Fixed button positions** `barcode/fixed-button-positions` — confidence H (verified)  
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Inventory count** `barcode/inventory-count` — confidence H (verified)  
  - UI string "Inventory count" -> CE: stock | EE: appointment, stock_barcode
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Light users** `barcode/light-users` — confidence H (verified)  
  - UI string "Light users" -> CE: base
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Manual entry** `barcode/manual-entry` — confidence H (verified)  
  - UI string "Manual entry" -> CE: account, mrp_account
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Manufacturing operations** `barcode/manufacturing-operations` — confidence H (verified)  
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🔒 Mobile: user login button** `barcode/mobile-user-login-button` — confidence H (verified)  
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**🟡 Packages: pre-encoded contents** `barcode/packages-pre-encoded-contents` — confidence M (module-level)  
  - UI string "Packages and" -> CE: l10n_es_edi_facturae, stock
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1
  - module license (CE runbot): stock=LGPL-3

**🔒 Packages: untracked goods** `barcode/packages-untracked-goods` — confidence H (verified)  
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

## Blog

**✅ Blog module redesign** `blog/blog-module-redesign` — confidence H (verified)  
  - code /o_wblog/ -> CE: website_blog | EE-only: -
  - module license (CE runbot): website_blog=LGPL-3

**✅ Recommended post** `blog/recommended-post` — confidence H (verified)  
  - UI string "Recommended post" -> CE: website_blog
  - code /Recommended Post|recommended_post/ -> CE: website_blog | EE-only: -
  - module license (CE runbot): website_blog=LGPL-3

**✅ Scheduled blog posts** `blog/scheduled-blog-posts` — confidence M (module-level)  
  - code /_cron_publish|scheduled.*post/ -> CE: mail, website, website_blog | EE-only: social, social_instagram, social_youtube, social_facebook, social_linkedin, social_twitter
  - module license (CE runbot): website_blog=LGPL-3

## Calendar

**✅ Browse other calendars** `calendar/browse-other-calendars` — confidence M (module-level)  
  - module license (CE runbot): calendar=LGPL-3

**✅ Detection of times in "All day" event titles** `calendar/detection-of-times-in-all-day-event-titles` — confidence M (module-level)  
  - module license (CE runbot): calendar=LGPL-3

**✅ Google and Outlook synchronization** `calendar/google-and-outlook-synchronization` — confidence M (module-level)  
  - module license (CE runbot): google_calendar=LGPL-3, microsoft_calendar=LGPL-3

**✅ Google Calendar sync** `calendar/google-calendar-sync` — confidence M (module-level)  
  - UI string "Google Calendar sync" -> CE: google_calendar | EE: appointment
  - UI string "Odoo Calendar" -> CE: microsoft_calendar
  - module license (CE runbot): google_calendar=LGPL-3

**✅ Linked records** `calendar/linked-records` — confidence M (module-level)  
  - module license (CE runbot): calendar=LGPL-3

**🔒 Manage and share availabilities** `calendar/manage-and-share-availabilities` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**✅ Manage pending activities** `calendar/manage-pending-activities` — confidence H (verified)  
  - module license (CE runbot): calendar=LGPL-3, mail=LGPL-3
  - CE screenshot (20.0 test database): pending activities in the calendar's all-day row

**✅ Mobile calendar redesign** `calendar/mobile-calendar-redesign` — confidence M (module-level)  
  - module license (CE runbot): calendar=LGPL-3, web=LGPL-3

**✅ Multiple calendars in one place** `calendar/multiple-calendars-in-one-place` — confidence H (verified)  
  - code /calendar\.calendar/ -> CE: calendar, google_calendar, hr_calendar, calendar_sms, resource, microsoft_calendar (+2) | EE-only: appointment, l10n_be_hr_payroll
  - module license (CE runbot): calendar=LGPL-3
  - CE screenshot (20.0 test database): '+ Add a calendar' in the Calendar side panel

**🔒 Non-recurring appointments** `calendar/non-recurring-appointments` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): appointment=OEEL-1

**✅ Sync multiple Google calendars** `calendar/sync-multiple-google-calendars` — confidence M (module-level)  
  - module license (CE runbot): google_calendar=LGPL-3

## Contacts

**✅ Contact enrichment** `contacts/contact-enrichment` — confidence H (verified)  
  - code /action_enrich/ -> CE: partner_autocomplete, crm_iap_enrich | EE-only: -
  - module license (CE runbot): partner_autocomplete=LGPL-3, crm_iap_enrich=LGPL-3

**✅ Hierarchical view** `contacts/hierarchical-view` — confidence H (verified)  
  - module license (CE runbot): web_hierarchy=LGPL-3, contacts=LGPL-3
  - CE screenshot (20.0 test database): hierarchy view button in Contacts

## CRM

**✅ Hidden address info** `crm/hidden-address-info` — confidence M (module-level)  
  - module license (CE runbot): base=LGPL-3

**✅ Lead distribution** `crm/lead-distribution` — confidence H (verified)  
  - UI string "Always in rotation" -> CE: crm
  - UI string "Out of rotation" -> CE: crm
  - UI string "Always in" -> CE: crm, base | EE: knowledge
  - code /Always in rotation/ -> CE: crm | EE-only: -
  - module license (CE runbot): crm=LGPL-3

**✅ Lead generation** `crm/lead-generation` — confidence M (module-level)  
  - UI string "Dun & Bradstreet" -> CE: base
  - module license (CE runbot): crm_iap_mine=LGPL-3

**✅ Pipeline switcher** `crm/pipeline-switcher` — confidence M (module-level)  
  - code /TeamSwitcher|team_switcher|pipeline.*switch/ -> CE: crm | EE-only: crm_enterprise
  - module license (CE runbot): crm=LGPL-3

**🔒 Upsells from lead** `crm/upsells-from-lead` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): sale_subscription=OEEL-1

## Dashboards

**🟡 Billing targets vs billable time** `dashboards/billing-targets-vs-billable-time` — confidence M (module-level)  
  - code /billing.*target|billable_time_target/ -> CE: hr_timesheet, portal, website_sale | EE-only: sale_timesheet_enterprise
  - module license (EE runbot ir.module.module): sale_timesheet_enterprise=OEEL-1
  - module license (CE runbot): hr_timesheet=LGPL-3

**✅ Carousel data layer** `dashboards/carousel-data-layer` — confidence M (module-level)  
  - module license (CE runbot): spreadsheet=LGPL-3

**✅ Favorite filters** `dashboards/favorite-filters` — confidence M (module-level)  
  - UI string "Favorite filters" -> CE: account, project
  - module license (CE runbot): spreadsheet_dashboard=LGPL-3

**✅ Fiscal year date filter** `dashboards/fiscal-year-date-filter` — confidence M (module-level)  
  - module license (CE runbot): spreadsheet=LGPL-3

**🔒 Frozen share links** `dashboards/frozen-share-links` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): spreadsheet_dashboard_edition=OEEL-1

**✅ Private dashboards** `dashboards/private-dashboards` — confidence L (needs review)  
  - module license (CE runbot): spreadsheet_dashboard=LGPL-3

**✅ Region selector for geo charts** `dashboards/region-selector-for-geo-charts` — confidence M (module-level)  
  - module license (CE runbot): spreadsheet=LGPL-3

## Discuss

**🔒 "On a call" status** `discuss/on-a-call-status` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🟡 Call transcripts** `discuss/call-transcripts` — confidence L (needs review)  
  - code /transcri/ -> CE: im_livechat, mail, website_payment | EE-only: ai, voip_ai, ai_agentic, product_unspsc
  - module license (EE runbot ir.module.module): voip_ai=OEEL-1, ai=OEEL-1
  - module license (CE runbot): mail=LGPL-3

**✅ Channel categories** `discuss/channel-categories` — confidence H (verified)  
  - code /discuss\.category|channel.*categor/ -> CE: mail, website_slides, website_slides_forum, website_slides_survey | EE-only: -
  - module license (CE runbot): mail=LGPL-3

**✅ Favorite channels** `discuss/favorite-channels` — confidence M (module-level)  
  - module license (CE runbot): mail=LGPL-3

**✅ Mark notifications as unread** `discuss/mark-notifications-as-unread` — confidence H (verified)  
  - code /set_message_unread|mark_unread/ -> CE: - | EE-only: -
  - module license (CE runbot): mail=LGPL-3

**✅ Polls** `discuss/polls` — confidence H (verified)  
  - code /discuss\.poll|mail\.poll|_name = .*poll/ -> CE: mail | EE-only: -
  - module license (CE runbot): mail=LGPL-3

## Documents

**🔒 Access right management** `documents/access-right-management` — confidence H (verified)  
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Auto-sort fleet documents** `documents/auto-sort-fleet-documents` — confidence H (verified)  
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Bank statement attachments** `documents/bank-statement-attachments` — confidence H (verified)  
  - UI string "Attachments on" -> CE: im_livechat
  - UI string "Accounting and Documents" -> EE: documents_account
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Branch management** `documents/branch-management` — confidence H (verified)  
  - UI string "Accounting and Documents" -> EE: documents_account
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Document request upload notification** `documents/document-request-upload-notification` — confidence H (verified)  
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Employee documents** `documents/employee-documents` — confidence H (verified)  
  - UI string "Employee documents" -> EE: documents_hr_sign
  - UI string "My Drive" -> EE: documents
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Markdown previews and thumbnails** `documents/markdown-previews-and-thumbnails` — confidence H (verified)  
  - UI string "Previews and" -> CE: mail
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Multi-file document request** `documents/multi-file-document-request` — confidence H (verified)  
  - module license (EE runbot ir.module.module): documents=OEEL-1

**🔒 Rename files with AI** `documents/rename-files-with-ai` — confidence H (verified)  
  - module license (EE runbot ir.module.module): documents=OEEL-1

## eCommerce

**🔒 AI-assisted product editing** `ecommerce/ai-assisted-product-editing` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): ai_website_sale=OEEL-1

**✅ Attribute filters** `ecommerce/attribute-filters` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Automated cross-sell suggestions** `ecommerce/automated-cross-sell-suggestions` — confidence M (module-level)  
  - code /cross.?sell/ -> CE: website_sale, point_of_sale, product, sale, sale_management | EE-only: -
  - module license (CE runbot): website_sale=LGPL-3, product=LGPL-3

**✅ Automated review requests** `ecommerce/automated-review-requests` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Default journal for eCommerce orders** `ecommerce/default-journal-for-ecommerce-orders` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**🟡 Donations** `ecommerce/donations` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): sale_subscription=OEEL-1
  - module license (CE runbot): website_sale=LGPL-3

**✅ Dynamic product building block** `ecommerce/dynamic-product-building-block` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Email gift card directly to recipient** `ecommerce/email-gift-card-directly-to-recipient` — confidence M (module-level)  
  - module license (CE runbot): loyalty=LGPL-3, website_sale_loyalty=LGPL-3

**✅ External identifiers** `ecommerce/external-identifiers` — confidence M (module-level)  
  - UI string "External identifiers" -> CE: base
  - module license (CE runbot): website_sale=LGPL-3

**✅ Extra step granularity** `ecommerce/extra-step-granularity` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Gelato: variant images** `ecommerce/gelato-variant-images` — confidence M (module-level)  
  - UI string "variant images" -> CE: website_sale
  - module license (CE runbot): sale_gelato=LGPL-3

**✅ Google Analytics events** `ecommerce/google-analytics-events` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Guest orders: contact creation** `ecommerce/guest-orders-contact-creation` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Location selector: country filter** `ecommerce/location-selector-country-filter` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3, delivery=LGPL-3

**✅ Loyalty progress bar** `ecommerce/loyalty-progress-bar` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Minimum product quantity** `ecommerce/minimum-product-quantity` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**🔒 Mondial Relay handled via Sendcloud** `ecommerce/mondial-relay-handled-via-sendcloud` — confidence H (verified)  
  - module diff 19.0→20.0: website_sale_mondialrelay, delivery_mondialrelay removed from CE
  - module license (EE runbot ir.module.module): delivery_sendcloud=OEEL-1

**✅ Open attribute value on search** `ecommerce/open-attribute-value-on-search` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Order dashboard** `ecommerce/order-dashboard` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Pay Now button** `ecommerce/pay-now-button` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Preferred delivery date** `ecommerce/preferred-delivery-date` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Prevent sales by category** `ecommerce/prevent-sales-by-category` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Pricelist selector** `ecommerce/pricelist-selector` — confidence M (module-level)  
  - UI string "Pricelist selector" -> CE: website_sale
  - module license (CE runbot): website_sale=LGPL-3

**✅ Product reference price** `ecommerce/product-reference-price` — confidence M (module-level)  
  - UI string "Product reference price" -> CE: point_of_sale, website_sale
  - module license (CE runbot): website_sale=LGPL-3

**✅ Product features** `ecommerce/product-features` — confidence M (module-level)  
  - UI string "Product features" -> CE: hr, website
  - module license (CE runbot): website_sale=LGPL-3

**✅ Product variant thumbnails** `ecommerce/product-variant-thumbnails` — confidence M (module-level)  
  - UI string "Show Thumbnails" -> CE: website_sale
  - module license (CE runbot): website_sale=LGPL-3

**✅ Products grid building block** `ecommerce/products-grid-building-block` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Range filter for attribute values** `ecommerce/range-filter-for-attribute-values` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Restrict packagings per website** `ecommerce/restrict-packagings-per-website` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Return management** `ecommerce/return-management` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Ribbon filters** `ecommerce/ribbon-filters` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Simplified inventory management** `ecommerce/simplified-inventory-management` — confidence L (needs review)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Standalone categories** `ecommerce/standalone-categories` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Stock-based product publishing** `ecommerce/stock-based-product-publishing` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Taxes included/excluded price display** `ecommerce/taxes-included-excluded-price-display` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**✅ Variant image management** `ecommerce/variant-image-management` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

**🔒 WhatsApp abandoned cart follow-up** `ecommerce/whatsapp-abandoned-cart-follow-up` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

**✅ Withdrawal requests** `ecommerce/withdrawal-requests` — confidence M (module-level)  
  - module license (CE runbot): website_sale=LGPL-3

## eLearning

**✅ Course access from portal** `elearning/course-access-from-portal` — confidence M (module-level)  
  - module license (CE runbot): website_slides=LGPL-3

## Email Marketing

**✅ Click tracking** `email-marketing/click-tracking` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Conditional content** `email-marketing/conditional-content` — confidence M (module-level)  
  - UI string "Blocks in" -> CE: website
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Contact management** `email-marketing/contact-management` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Dynamic mailing lists** `email-marketing/dynamic-mailing-lists` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Employee/supplier mailings** `email-marketing/employee-supplier-mailings` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Favorite blocks** `email-marketing/favorite-blocks` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Full-screen editing** `email-marketing/full-screen-editing` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Link tracking** `email-marketing/link-tracking` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Mailing template library** `email-marketing/mailing-template-library` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ New fonts** `email-marketing/new-fonts` — confidence M (module-level)  
  - UI string "New fonts" -> EE: ai_website
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ New templates and blocks** `email-marketing/new-templates-and-blocks` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Product and event snippets** `email-marketing/product-and-event-snippets` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

**✅ Social media accounts** `email-marketing/social-media-accounts` — confidence M (module-level)  
  - UI string "Social media accounts" -> CE: crm, website | EE: social
  - module license (CE runbot): mass_mailing=LGPL-3, social_media=LGPL-3

**✅ UTM reference** `email-marketing/utm-reference` — confidence M (module-level)  
  - module license (CE runbot): mass_mailing=LGPL-3

## Employees

**✅ Employee directory** `employees/employee-directory` — confidence M (module-level)  
  - module license (CE runbot): hr=LGPL-3

**🔒 Salary simulation** `employees/salary-simulation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**✅ Remote Work** `employees/remote-work` — confidence H (verified)  
  - module diff 19.0→20.0: hr_homeworking* removed
  - CE source: addons/hr/models/hr_employee_location.py; hr.employee.<weekday>_location_id fields from hr
  - UI string "Remote Work" -> CE: hr, website_blog, base | EE: esg
  - module license (CE runbot): hr=LGPL-3

**✅ Variable working schedule** `employees/variable-working-schedule` — confidence M (module-level)  
  - module license (CE runbot): resource=LGPL-3, hr=LGPL-3

## ESG

**🔒 Assign emission factors with AI** `esg/assign-emission-factors-with-ai` — confidence H (verified)  
  - module license (EE runbot ir.module.module): esg=OEEL-1

## Events

**✅ Event combos** `events/event-combos` — confidence M (module-level)  
  - code /combo.*event|event.*combo/ -> CE: website_sale, sale | EE-only: l10n_do_edi
  - module license (CE runbot): sale=LGPL-3, website_sale=LGPL-3

## Expenses

**✅ Consolidated expenses report** `expenses/consolidated-expenses-report` — confidence L (needs review)  
  - UI string "Select and" -> CE: l10n_latam_check, mass_mailing, website
  - module license (CE runbot): hr_expense=LGPL-3

**✅ Expense limits per job position** `expenses/expense-limits-per-job-position` — confidence H (verified)  
  - code /expense.*limit|limit.*expense/ -> CE: hr_expense, account | EE-only: hr_expense_stripe, hr_expense_extract, hr_payroll_expense
  - module license (CE runbot): hr_expense=LGPL-3

**🔒 Salary rules for expense products** `expenses/salary-rules-for-expense-products` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): hr_payroll_expense=OEEL-1

## Field Service

**🔒 Field Service merged into Planning** `field-service/field-service-merged-into-planning` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

## Fleet

**🔒 Driver assignment** `fleet/driver-assignment` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): hr_payroll_fleet=OEEL-1

## Frontdesk

**🔒 Member entry management** `frontdesk/member-entry-management` — confidence H (verified)  
  - module license (EE runbot ir.module.module): frontdesk=OEEL-1

## Helpdesk

**🔒 Filter unanswered tickets** `helpdesk/filter-unanswered-tickets` — confidence H (verified)  
  - module license (EE runbot ir.module.module): helpdesk=OEEL-1

**🔒 Reminder email before auto-closing tickets** `helpdesk/reminder-email-before-auto-closing-tickets` — confidence H (verified)  
  - module license (EE runbot ir.module.module): helpdesk=OEEL-1

**🔒 Similar ticket detection** `helpdesk/similar-ticket-detection` — confidence H (verified)  
  - module license (EE runbot ir.module.module): helpdesk=OEEL-1

## Inventory

**✅ Allocation report** `inventory/allocation-report` — confidence M (module-level)  
  - UI string "Allocation report" -> CE: mrp, purchase_stock, stock
  - module license (CE runbot): stock=LGPL-3

**✅ CMR document** `inventory/cmr-document` — confidence M (module-level)  
  - UI string "Convention on" -> CE: stock_fleet
  - UI string "International Carriage of Goods by Road" -> CE: stock_fleet
  - module license (CE runbot): stock_fleet=LGPL-3

**✅ Company-specific customer lead times** `inventory/company-specific-customer-lead-times` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Intercompany flows** `inventory/intercompany-flows` — confidence M (module-level)  
  - code /inter.?company.*route|resupply/ -> CE: mrp, stock, mrp_subcontracting, purchase_stock, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping (+2) | EE-only: -
  - module license (CE runbot): stock=LGPL-3, purchase_stock=LGPL-3

**✅ Inventory at a past date** `inventory/inventory-at-a-past-date` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Inventory valuation: COGS update** `inventory/inventory-valuation-cogs-update` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Landed costs for specific products** `inventory/landed-costs-for-specific-products` — confidence M (module-level)  
  - module license (CE runbot): stock_landed_costs=LGPL-3

**✅ Location-specific push routes** `inventory/location-specific-push-routes` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Picking notifications** `inventory/picking-notifications` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**🔒 Preview Barcode instructions in operation type** `inventory/preview-barcode-instructions-in-operation-type` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): stock_barcode=OEEL-1

**✅ Product packaging barcodes** `inventory/product-packaging-barcodes` — confidence M (module-level)  
  - UI string "Access and" -> CE: hr_attendance, website | EE: documents
  - module license (CE runbot): stock=LGPL-3

**✅ Product replenishment** `inventory/product-replenishment` — confidence H (verified)  
  - UI string "To reorder" -> CE: account, digest, stock, website_sale
  - module license (CE runbot): stock=LGPL-3
  - CE screenshot (20.0 test database): single 'Order' button with 'Automate' and 'Snooze'

**🔒 Sendcloud: package reference** `inventory/sendcloud-package-reference` — confidence M (module-level)  
  - UI string "package reference" -> CE: stock
  - module license (EE runbot ir.module.module): delivery_sendcloud=OEEL-1

**🔒 Sendcloud: pickup points** `inventory/sendcloud-pickup-points` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): delivery_sendcloud=OEEL-1

**✅ Simplified returns** `inventory/simplified-returns` — confidence H (verified)  
  - runbot CE (API): model stock.return.picking absent
  - module license (CE runbot): stock=LGPL-3

**✅ Stock aging report** `inventory/stock-aging-report` — confidence M (module-level)  
  - UI string "Moves Analysis" -> CE: stock
  - module license (CE runbot): stock=LGPL-3

**✅ Suggested stock levels for reordering rules** `inventory/suggested-stock-levels-for-reordering-rules` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3, purchase_stock=LGPL-3

**✅ Traceability Report** `inventory/traceability-report` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Variant-specific HS codes** `inventory/variant-specific-hs-codes` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Variant-specific packagings** `inventory/variant-specific-packagings` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ Vendor purchase reference** `inventory/vendor-purchase-reference` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

**✅ ZPL location barcodes** `inventory/zpl-location-barcodes` — confidence M (module-level)  
  - module license (CE runbot): stock=LGPL-3

## Knowledge

**🔒 Article settings quick access** `knowledge/article-settings-quick-access` — confidence H (verified)  
  - module license (EE runbot ir.module.module): knowledge=OEEL-1

## Live Chat

**🔒 Connect social media messaging** `live-chat/connect-social-media-messaging` — confidence M (module-level)  
  - code /messenger|instagram/ -> CE: website, mass_mailing, html_editor, social_media, web, utm (+4) | EE-only: social_instagram, social_demo, social_facebook, social, ai_website, product_unspsc (+1)
  - module license (EE runbot ir.module.module): social_facebook=OEEL-1, social_instagram=OEEL-1

## Maintenance

**🔒 Maintenance requests: Gantt views** `maintenance/maintenance-requests-gantt-views` — confidence H (verified)  
  - UI string "Maintenance requests" -> CE: maintenance | EE: mrp_maintenance
  - UI string "Gantt views" -> CE: mrp | EE: mrp_workorder, planning
  - code /maintenance.*gantt|gantt.*maintenance/ -> CE: - | EE-only: mrp_maintenance, maintenance_enterprise
  - module license (EE runbot ir.module.module): mrp_maintenance=OEEL-1, maintenance_enterprise=OEEL-1

**✅ Maintenance teams on stages** `maintenance/maintenance-teams-on-stages` — confidence M (module-level)  
  - module license (CE runbot): maintenance=LGPL-3

**✅ UX improvements** `maintenance/ux-improvements` — confidence M (module-level)  
  - module license (CE runbot): maintenance=LGPL-3

## Manufacturing

**✅ Backorder planning** `manufacturing/backorder-planning` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Bill of materials** `manufacturing/bill-of-materials` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Component replacement** `manufacturing/component-replacement` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Continuous production** `manufacturing/continuous-production` — confidence M (module-level)  
  - UI string "Continuous production" -> CE: mrp
  - module license (CE runbot): mrp=LGPL-3

**✅ Draft versus confirmed manufacturing orders** `manufacturing/draft-versus-confirmed-manufacturing-orders` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Flexible consumption** `manufacturing/flexible-consumption` — confidence H (verified)  
  - runbot CE (API): field mrp.bom.consumption absent
  - module license (CE runbot): mrp=LGPL-3

**✅ Generate lots and serials when closing manufacturing orders** `manufacturing/generate-lots-and-serials-when-closing-manufacturing-orders` — confidence M (module-level)  
  - UI string "Lots and" -> CE: product_expiry, stock
  - module license (CE runbot): mrp=LGPL-3

**✅ Lot/serial number transfers** `manufacturing/lot-serial-number-transfers` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Manufacturing order Kanban view** `manufacturing/manufacturing-order-kanban-view` — confidence H (verified)  
  - module license (CE runbot): mrp=LGPL-3
  - CE screenshot (20.0 test database): MO Kanban grouped by week

**✅ Manufacturing orders planned ASAP** `manufacturing/manufacturing-orders-planned-asap` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ MO cost** `manufacturing/mo-cost` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**🟡 Produce button** `manufacturing/produce-button` — confidence M (module-level)  
  - UI string "Produce All" -> EE: stock_barcode_mrp
  - UI string "Shop Floor" -> CE: mrp | EE: mrp_workorder
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1, stock_barcode_mrp=OEEL-1
  - module license (CE runbot): mrp=LGPL-3

**✅ Put in pack from MO** `manufacturing/put-in-pack-from-mo` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Reset MO to draft** `manufacturing/reset-mo-to-draft` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**🔒 Shop Floor demo sheet** `manufacturing/shop-floor-demo-sheet` — confidence M (module-level)  
  - UI string "Shop Floor" -> CE: mrp | EE: mrp_workorder
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1

**✅ Split manufacturing orders** `manufacturing/split-manufacturing-orders` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Subcontracting reception valuation** `manufacturing/subcontracting-reception-valuation` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ To Replenish filter** `manufacturing/to-replenish-filter` — confidence M (module-level)  
  - UI string "To Replenish" -> CE: mrp, purchase_stock, stock | EE: mrp_mps
  - module license (CE runbot): mrp=LGPL-3

**✅ Traceability report expiration dates** `manufacturing/traceability-report-expiration-dates` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**🔒 Visualize and confirm work orders** `manufacturing/visualize-and-confirm-work-orders` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1

**✅ Work and manufacturing order reporting** `manufacturing/work-and-manufacturing-order-reporting` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**🟡 Work order views** `manufacturing/work-order-views` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1
  - module license (CE runbot): mrp=LGPL-3

**✅ Work center overview** `manufacturing/work-center-overview` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

**✅ Work orders in blocked work centers** `manufacturing/work-orders-in-blocked-work-centers` — confidence M (module-level)  
  - module license (CE runbot): mrp=LGPL-3

## Marketing Automation

**🔒 AI-assisted campaign creation** `marketing-automation/ai-assisted-campaign-creation` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

**🔒 Event-based triggers** `marketing-automation/event-based-triggers` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

**🔒 Mailing template library** `marketing-automation/mailing-template-library` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

**🔒 New triggers and actions** `marketing-automation/new-triggers-and-actions` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

**🔒 Webhook integration** `marketing-automation/webhook-integration` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

**🔒 Workflow builder** `marketing-automation/workflow-builder` — confidence H (verified)  
  - module license (EE runbot ir.module.module): marketing_automation=OEEL-1

## Marketing Card

**✅ Default target URLs** `marketing-card/default-target-urls` — confidence M (module-level)  
  - module license (CE runbot): marketing_card=LGPL-3

**✅ Event app integration** `marketing-card/event-app-integration` — confidence M (module-level)  
  - UI string "Send cards" -> CE: marketing_card, marketing_card_event
  - module license (CE runbot): marketing_card=LGPL-3

**✅ Language support** `marketing-card/language-support` — confidence M (module-level)  
  - UI string "Language support" -> CE: website
  - module license (CE runbot): marketing_card=LGPL-3

## Online Payments

**✅ ACH payments** `online-payments/ach-payments` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ Authorize.net** `online-payments/authorize-net` — confidence M (module-level)  
  - UI string "Authorize.net" -> CE: payment, payment_authorize
  - module license (CE runbot): payment=LGPL-3

**✅ ECPay** `online-payments/ecpay` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ Mollie** `online-payments/mollie` — confidence M (module-level)  
  - UI string "Apple Pay" -> CE: payment, payment_mollie, payment_stripe
  - UI string "Google Pay" -> CE: payment, payment_mollie, payment_stripe
  - module license (CE runbot): payment=LGPL-3

**✅ Pay on Invoice provider** `online-payments/pay-on-invoice-provider` — confidence H (verified)  
  - UI string "Pay on Invoice" -> CE: payment, payment_custom
  - module license (CE runbot): payment=LGPL-3
  - CE screenshot (20.0 test database): 'Pay on Invoice' provider card

**✅ Payment provider views** `online-payments/payment-provider-views` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ PayPal** `online-payments/paypal` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ PayU** `online-payments/payu` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ Pricelist and amount restriction** `online-payments/pricelist-and-amount-restriction` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ Redsys** `online-payments/redsys` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ SOFORT** `online-payments/sofort` — confidence H (verified)  
  - runbot CE (API): payment.method with code 'sofort' (active or not): 0 records
  - module license (CE runbot): payment=LGPL-3

**✅ Stripe** `online-payments/stripe` — confidence M (module-level)  
  - UI string "Apple Pay" -> CE: payment, payment_mollie, payment_stripe
  - UI string "Google Pay" -> CE: payment, payment_mollie, payment_stripe
  - module license (CE runbot): payment=LGPL-3

**✅ Toss Payments** `online-payments/toss-payments` — confidence H (verified)  
  - UI string "Toss Payments" -> CE: payment, payment_toss_payments
  - module license (CE runbot): payment=LGPL-3
  - CE screenshot (20.0 test database): Toss Payments provider card

**✅ Wero** `online-payments/wero` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

**✅ Wire transfers** `online-payments/wire-transfers` — confidence M (module-level)  
  - UI string "Wire transfers" -> CE: l10n_us_account, payment_custom
  - module license (CE runbot): payment=LGPL-3

**✅ Xendit** `online-payments/xendit` — confidence M (module-level)  
  - module license (CE runbot): payment=LGPL-3

## Payroll

**🔒 Chatter on pay runs** `payroll/chatter-on-pay-runs` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Contract date modification** `payroll/contract-date-modification` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Dashboard** `payroll/dashboard` — confidence H (verified)  
  - UI string "The Payroll" -> EE: hr_payroll, l10n_be_reports
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Driver assignment** `payroll/driver-assignment` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Employee type per company or branch** `payroll/employee-type-per-company-or-branch` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Net to gross simulation** `payroll/net-to-gross-simulation` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Pay run workflow** `payroll/pay-run-workflow` — confidence H (verified)  
  - UI string "Pay Runs" -> CE: hr | EE: hr_payroll
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Payslip sending options** `payroll/payslip-sending-options` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Payslip UX** `payroll/payslip-ux` — confidence H (verified)  
  - UI string "Salary Computation" -> CE: hr_work_entry | EE: hr_payroll
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Salary indexation** `payroll/salary-indexation` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Salary rules** `payroll/salary-rules` — confidence H (verified)  
  - UI string "Salary rules" -> CE: hr_work_entry | EE: hr_payroll
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Test print pay runs** `payroll/test-print-pay-runs` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Time entry exports** `payroll/time-entry-exports` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Work entries removal** `payroll/work-entries-removal` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

**🔒 Working schedules** `payroll/working-schedules` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_payroll=OEEL-1

## Phone

**🔒 Audio settings during a call** `phone/audio-settings-during-a-call` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Auto-fill and auto-log** `phone/auto-fill-and-auto-log` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Call flow designer** `phone/call-flow-designer` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Call logging in chatter** `phone/call-logging-in-chatter` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Call transfer to another device** `phone/call-transfer-to-another-device` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Choose outgoing number** `phone/choose-outgoing-number` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Floating widget** `phone/floating-widget` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Linphone** `phone/linphone` — confidence H (verified)  
  - UI string "Linphone" -> EE: voip
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Push notifications** `phone/push-notifications` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

**🔒 Simultaneous calling** `phone/simultaneous-calling` — confidence H (verified)  
  - module license (EE runbot ir.module.module): voip=OEEL-1

## Planning

**🔒 Employee-specific materials** `planning/employee-specific-materials` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: auto plan** `planning/field-service-auto-plan` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "auto plan" -> EE: planning, sale_planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: customer equipment** `planning/field-service-customer-equipment` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "customer equipment" -> EE: planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: customer ratings** `planning/field-service-customer-ratings` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "customer ratings" -> CE: im_livechat, project | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: intervention confirmation email** `planning/field-service-intervention-confirmation-email` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: live map** `planning/field-service-live-map` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "live map" -> EE: planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: map view** `planning/field-service-map-view` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: product barcodes** `planning/field-service-product-barcodes` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "product barcodes" -> EE: stock_barcode, stock_barcode_mrp
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: report** `planning/field-service-report` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: routing preferences** `planning/field-service-routing-preferences` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: track customer history** `planning/field-service-track-customer-history` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: travel fees** `planning/field-service-travel-fees` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - UI string "travel fees" -> EE: planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: website form** `planning/field-service-website-form` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Field Service: worksheets** `planning/field-service-worksheets` — confidence H (verified)  
  - UI string "Field Service" -> CE: base | EE: helpdesk, planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Gantt view: travel times** `planning/gantt-view-travel-times` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Link shifts to tasks** `planning/link-shifts-to-tasks` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Multiple resource assignment** `planning/multiple-resource-assignment` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Priority shifts** `planning/priority-shifts` — confidence H (verified)  
  - UI string "Auto Plan" -> EE: planning, sale_planning
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Schedule shifts from side panel** `planning/schedule-shifts-from-side-panel` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

**🔒 Send shifts via WhatsApp** `planning/send-shifts-via-whatsapp` — confidence H (verified)  
  - module license (EE runbot ir.module.module): planning=OEEL-1

## PLM

**🔒 BoM comparison** `plm/bom-comparison` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_plm=OEEL-1

**🔒 Optional ECO version update** `plm/optional-eco-version-update` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_plm=OEEL-1

**🔒 Product updates** `plm/product-updates` — confidence H (verified)  
  - UI string "Product updates" -> CE: website_mass_mailing
  - module license (EE runbot ir.module.module): mrp_plm=OEEL-1

**🔒 Universal ECO report** `plm/universal-eco-report` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_plm=OEEL-1

## Point of Sale

**✅ Base unit price on product label** `point-of-sale/base-unit-price-on-product-label` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**🔒 Booking Kanban and pivot views** `point-of-sale/booking-kanban-and-pivot-views` — confidence H (verified)  
  - UI string "Kanban and" -> CE: mrp, project, base | EE: web_studio
  - code /pos.*booking|booking.*pos/ -> CE: point_of_sale | EE-only: pos_appointment, delivery_usps
  - module license (EE runbot ir.module.module): pos_appointment=OEEL-1

**✅ Convert order lines into a combo** `point-of-sale/convert-order-lines-into-a-combo` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Employee access levels** `point-of-sale/employee-access-levels` — confidence M (module-level)  
  - UI string "Supervised" -> CE: account, pos_hr | EE: account_reports, l10n_pe_reports
  - module license (CE runbot): pos_hr=LGPL-3

**✅ End of session** `point-of-sale/end-of-session` — confidence M (module-level)  
  - UI string "End of session" -> CE: point_of_sale
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Expired product notification** `point-of-sale/expired-product-notification` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**🔒 GoFood delivery integration** `point-of-sale/gofood-delivery-integration` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): pos_urban_piper=OEEL-1

**🔒 GrabFood delivery integration** `point-of-sale/grabfood-delivery-integration` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): pos_urban_piper=OEEL-1

**✅ Mercado Pago terminal** `point-of-sale/mercado-pago-terminal` — confidence M (module-level)  
  - UI string "Mercado Pago" -> CE: payment, payment_mercado_pago, point_of_sale, pos_mercado_pago
  - module license (CE runbot): pos_mercado_pago=LGPL-3

**✅ Multiple currencies** `point-of-sale/multiple-currencies` — confidence H (verified)  
  - module license (CE runbot): point_of_sale=LGPL-3
  - CE source: addons/point_of_sale/models/pos_payment_method.py — new 'Currencies' field (currency_ids) on cash/bank payment methods; pos.payment.foreign_currency_id

**✅ Print preparation tickets per product** `point-of-sale/print-preparation-tickets-per-product` — confidence M (module-level)  
  - UI string "Split per product" -> CE: point_of_sale
  - UI string "Split per" -> CE: loyalty, point_of_sale | EE: social
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Printer management** `point-of-sale/printer-management` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Receipt printing** `point-of-sale/receipt-printing` — confidence M (module-level)  
  - UI string "Receipt printing" -> CE: point_of_sale
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Reorganizing products in POS interface** `point-of-sale/reorganizing-products-in-pos-interface` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Self-ordering** `point-of-sale/self-ordering` — confidence M (module-level)  
  - UI string "Self-ordering" -> CE: point_of_sale, pos_self_order
  - UI string "Generate and" -> CE: loyalty, payment | EE: hr_payroll, l10n_uy_edi
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Service fees** `point-of-sale/service-fees` — confidence M (module-level)  
  - UI string "Service fees" -> CE: l10n_do, point_of_sale
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Simplified inventory management** `point-of-sale/simplified-inventory-management` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Simplified receipts** `point-of-sale/simplified-receipts` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**✅ Snooze products** `point-of-sale/snooze-products` — confidence M (module-level)  
  - module license (CE runbot): point_of_sale=LGPL-3

**🟡 WhatsApp and SMS self-order receipt** `point-of-sale/whatsapp-and-sms-self-order-receipt` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): whatsapp_pos_self_order=OEEL-1, pos_enterprise_sms_whatsapp=OEEL-1
  - module license (CE runbot): pos_self_order=LGPL-3

## Project

**✅ Assign project roles** `project/assign-project-roles` — confidence M (module-level)  
  - module license (CE runbot): project=LGPL-3

**✅ Assign tasks to portal users** `project/assign-tasks-to-portal-users` — confidence M (module-level)  
  - module license (CE runbot): project=LGPL-3

**✅ Collaborators separated from followers** `project/collaborators-separated-from-followers` — confidence M (module-level)  
  - module license (CE runbot): project=LGPL-3

**✅ Mobile: improved task header design** `project/mobile-improved-task-header-design` — confidence M (module-level)  
  - module license (CE runbot): project=LGPL-3

**🔒 Printable task schedule** `project/printable-task-schedule` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): project_enterprise=OEEL-1

**🟡 Profitability report** `project/profitability-report` — confidence M (module-level)  
  - UI string "Profitability report" -> CE: project_sale_expense, sale_project_stock
  - module license (CE runbot): project=LGPL-3, project_account=LGPL-3, sale_project=LGPL-3
  - code /profitability/ -> CE: project_account, project_sale_expense, sale_margin | EE-only: account_budget, account_reports

**✅ Projects from opportunities** `project/projects-from-opportunities` — confidence H (verified)  
  - module license (CE runbot): crm_sale_project=LGPL-3

**✅ Task tracking in user portal** `project/task-tracking-in-user-portal` — confidence M (module-level)  
  - module license (CE runbot): project=LGPL-3

## Purchase

**✅ Alternatives comparison** `purchase/alternatives-comparison` — confidence H (verified)  
  - module license (CE runbot): purchase_alternative=LGPL-3

**✅ Default Incoterm per vendor** `purchase/default-incoterm-per-vendor` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**✅ End-customer address in portal** `purchase/end-customer-address-in-portal` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**✅ Expected arrival date** `purchase/expected-arrival-date` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**✅ Product unit cost versus purchase unit cost** `purchase/product-unit-cost-versus-purchase-unit-cost` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**✅ Purchase agreement structure** `purchase/purchase-agreement-structure` — confidence M (module-level)  
  - UI string "Sections and" -> CE: survey
  - module license (CE runbot): purchase=LGPL-3

**✅ Recompute Expected Arrival when deadline is in the past** `purchase/recompute-expected-arrival-when-deadline-is-in-the-past` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**✅ Total amounts on purchase order sections** `purchase/total-amounts-on-purchase-order-sections` — confidence M (module-level)  
  - module license (CE runbot): purchase=LGPL-3

**🔒 Vendor quality rate** `purchase/vendor-quality-rate` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): quality_control=OEEL-1

## Quality

**🔒 Bypass quality checks** `quality/bypass-quality-checks` — confidence H (verified)  
  - module license (EE runbot ir.module.module): quality_control=OEEL-1

**🔒 Failure location** `quality/failure-location` — confidence H (verified)  
  - UI string "Failure location" -> EE: quality, quality_control
  - module license (EE runbot ir.module.module): quality_control=OEEL-1

## Recruitment

**✅ Improved integration** `recruitment/improved-integration` — confidence M (module-level)  
  - module license (CE runbot): hr_recruitment=LGPL-3

**✅ Job form visibility conditions** `recruitment/job-form-visibility-conditions` — confidence M (module-level)  
  - module license (CE runbot): hr_recruitment=LGPL-3

**✅ Matching score filter** `recruitment/matching-score-filter` — confidence M (module-level)  
  - UI string "Matching Score" -> CE: hr_recruitment_skills
  - module license (CE runbot): hr_recruitment_skills=LGPL-3

**✅ View talents from job position** `recruitment/view-talents-from-job-position` — confidence M (module-level)  
  - module license (CE runbot): hr_recruitment=LGPL-3

## Referrals

**🔒 Contact outreach tracking** `referrals/contact-outreach-tracking` — confidence H (verified)  
  - module license (EE runbot ir.module.module): hr_referral=OEEL-1

## Rental

**🔒 Automatic price update** `rental/automatic-price-update` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

**🔒 Rental order creation** `rental/rental-order-creation` — confidence H (verified)  
  - UI string "Rental period" -> EE: sale_renting
  - UI string "Rental per" -> EE: sale_renting
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

**🔒 Rental orders dashboard** `rental/rental-orders-dashboard` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

**🔒 Simplified and unified pricelists** `rental/simplified-and-unified-pricelists` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

**🔒 Strikethrough pricing** `rental/strikethrough-pricing` — confidence H (verified)  
  - UI string "Shop and" -> CE: mrp, website_sale
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

**🔒 Working schedules** `rental/working-schedules` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): sale_renting=OEEL-1

## Repairs

**✅ Invoice creation** `repairs/invoice-creation` — confidence M (module-level)  
  - UI string "Invoice creation" -> CE: l10n_tw_edi_ecpay, point_of_sale | EE: l10n_ar_edi
  - module license (CE runbot): repair=LGPL-3

**✅ Repair order status** `repairs/repair-order-status` — confidence H (verified)  
  - runbot CE (API): repair.order.state selection = draft, confirmed, done, cancel
  - module license (CE runbot): repair=LGPL-3

**✅ Repair-related services** `repairs/repair-related-services` — confidence M (module-level)  
  - module license (CE runbot): repair=LGPL-3

## Sales

**🔒 Payment-based commissions** `sales/payment-based-commissions` — confidence H (verified)  
  - code /commission/ -> CE: l10n_cl, l10n_eg, l10n_in, l10n_ro, l10n_th, sale (+14) | EE-only: sale_commission, partner_commission, l10n_be_hr_payroll, l10n_hk_hr_payroll, l10n_au_hr_payroll, l10n_be_reports (+22)
  - module license (EE runbot ir.module.module): sale_commission=OEEL-1

**✅ Charge overages** `sales/charge-overages` — confidence L (needs review)  
  - module license (CE runbot): sale=LGPL-3

**✅ Dashboard** `sales/dashboard` — confidence H (verified)  
  - module license (CE runbot): sale=LGPL-3
  - CE screenshot (20.0 test database): dashboard strip on the quotations list

**✅ Description-only sales order lines** `sales/description-only-sales-order-lines` — confidence H (verified)  
  - runbot CE (API): sale.order.line.product_id required=False
  - UI string "Mandatory Product" -> CE: sale
  - module license (CE runbot): sale=LGPL-3

**✅ Editable product variant price** `sales/editable-product-variant-price` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Editable margins** `sales/editable-margins` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Fixed prepayment amounts** `sales/fixed-prepayment-amounts` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Fixed Price pricelists** `sales/fixed-price-pricelists` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**🔒 Lazada** `sales/lazada` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): sale_lazada=OEEL-1

**✅ Loyalty point expiration** `sales/loyalty-point-expiration` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**🔒 Manager commissions** `sales/manager-commissions` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sale_commission=OEEL-1

**✅ Mark orders as fully invoiced** `sales/mark-orders-as-fully-invoiced` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Periodic pricing** `sales/periodic-pricing` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Price rules per packaging type** `sales/price-rules-per-packaging-type` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Pricelist report improvements** `sales/pricelist-report-improvements` — confidence M (module-level)  
  - UI string "Product Reference" -> CE: point_of_sale, sale_edi_ubl, website_sale | EE: stock_barcode
  - module license (CE runbot): sale=LGPL-3

**✅ Product images** `sales/product-images` — confidence H (verified)  
  - UI string "Product images" -> CE: point_of_sale, sale, website_sale
  - module license (CE runbot): sale=LGPL-3
  - CE screenshot (20.0 test database): product image on the sales order PDF

**✅ Quotation sections** `sales/quotation-sections` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Quotation templates** `sales/quotation-templates` — confidence M (module-level)  
  - UI string "Quotation templates" -> CE: sale_management, sale_pdf_quote_builder | EE: sale_renting, sale_subscription
  - UI string "Hide Price" -> CE: account, sale | EE: planning
  - UI string "Hide Composition" -> CE: account, sale
  - module license (CE runbot): sale=LGPL-3

**✅ Sales order creation from purchase orders** `sales/sales-order-creation-from-purchase-orders` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3, purchase_edi_ubl_bis3=LGPL-3, account_edi_ubl_cii=LGPL-3

**✅ Sales order email template** `sales/sales-order-email-template` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Sales order line numbering** `sales/sales-order-line-numbering` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Sales order portal page** `sales/sales-order-portal-page` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Services & Material** `sales/services-material` — confidence M (module-level)  
  - UI string "Services & Material" -> CE: sale
  - module license (CE runbot): sale=LGPL-3

**✅ Ship orders without Inventory** `sales/ship-orders-without-inventory` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Single-use discount codes** `sales/single-use-discount-codes` — confidence M (module-level)  
  - module license (CE runbot): sale=LGPL-3

**✅ Stacked fields on sales order lines** `sales/stacked-fields-on-sales-order-lines` — confidence M (module-level)  
  - UI string "Margin (%)" -> CE: point_of_sale, product_margin, sale_margin | EE: sale_subscription
  - UI string "Delivered (%)" -> CE: sale
  - module license (CE runbot): sale=LGPL-3

**🔒 TikTok** `sales/tiktok` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): sale_tiktok=OEEL-1

## Shop Floor

**🔒 HTML note field** `shop-floor/html-note-field` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1

**🔒 Instruction updates** `shop-floor/instruction-updates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1

**🔒 Work center barcode** `shop-floor/work-center-barcode` — confidence H (verified)  
  - module license (EE runbot ir.module.module): mrp_workorder=OEEL-1

## Sign

**🔒 Automated signature requests** `sign/automated-signature-requests` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Custom fields in templates** `sign/custom-fields-in-templates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Improved progress tracking** `sign/improved-progress-tracking` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Tag management** `sign/tag-management` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Itsme** `sign/itsme` — confidence H (verified)  
  - UI string "Odoo Sign" -> EE: sign, sign_emsigner, sign_itsme, whatsapp_sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Mobile and touchscreen support** `sign/mobile-and-touchscreen-support` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Non-latin alphabets** `sign/non-latin-alphabets` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Qualified electronic signatures** `sign/qualified-electronic-signatures` — confidence H (verified)  
  - UI string "Qualified electronic signatures" -> EE: sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Record updates** `sign/record-updates` — confidence H (verified)  
  - UI string "Odoo Sign" -> EE: sign, sign_emsigner, sign_itsme, whatsapp_sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Reorder signers** `sign/reorder-signers` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Send signature requests from activities** `sign/send-signature-requests-from-activities` — confidence H (verified)  
  - UI string "Signature Requests" -> EE: hr_sign, sign, whatsapp_sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Sign mode options menu** `sign/sign-mode-options-menu` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Sign templates** `sign/sign-templates` — confidence H (verified)  
  - UI string "Sign templates" -> EE: documents_sign, sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Signed PDFs: bookmarks and settings** `sign/signed-pdfs-bookmarks-and-settings` — confidence H (verified)  
  - UI string "Signed PDFs" -> EE: documents_sign
  - module license (EE runbot ir.module.module): sign=OEEL-1

**🔒 Touchscreen support** `sign/touchscreen-support` — confidence H (verified)  
  - module license (EE runbot ir.module.module): sign=OEEL-1

## Social Marketing

**🔒 Add mentions in social media posts** `social-marketing/add-mentions-in-social-media-posts` — confidence H (verified)  
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 AI assistant** `social-marketing/ai-assistant` — confidence H (verified)  
  - UI string "AI assistant" -> EE: ai_mcp, ai_website
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 Facebook and Instagram stories** `social-marketing/facebook-and-instagram-stories` — confidence H (verified)  
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 Image display order** `social-marketing/image-display-order` — confidence H (verified)  
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 Personal LinkedIn account** `social-marketing/personal-linkedin-account` — confidence H (verified)  
  - UI string "Personal LinkedIn account" -> EE: social_linkedin
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 Platform-specific post scheduling** `social-marketing/platform-specific-post-scheduling` — confidence H (verified)  
  - module license (EE runbot ir.module.module): social=OEEL-1

**🔒 Schedule first comment** `social-marketing/schedule-first-comment` — confidence H (verified)  
  - module license (EE runbot ir.module.module): social=OEEL-1

## Spreadsheet

**🟡 Bubble charts** `spreadsheet/bubble-charts` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Calculated columns** `spreadsheet/calculated-columns` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Calendar charts** `spreadsheet/calendar-charts` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Cell value orientation** `spreadsheet/cell-value-orientation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Charts** `spreadsheet/charts` — confidence M (module-level)  
  - UI string "Data Analysis" -> CE: hr_skills, spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Column statistics** `spreadsheet/column-statistics` — confidence M (module-level)  
  - UI string "Column statistics" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Conditional formatting by date** `spreadsheet/conditional-formatting-by-date` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Curly brackets** `spreadsheet/curly-brackets` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Custom format** `spreadsheet/custom-format` — confidence M (module-level)  
  - UI string "Custom format" -> CE: base_import, mysubscription
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Data cleanup** `spreadsheet/data-cleanup` — confidence M (module-level)  
  - UI string "Data cleanup" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Disable automatic recalculation** `spreadsheet/disable-automatic-recalculation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Global filters** `spreadsheet/global-filters` — confidence M (module-level)  
  - UI string "Global filters" -> CE: spreadsheet_dashboard
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 List insertion** `spreadsheet/list-insertion` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Lock sheets** `spreadsheet/lock-sheets` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Mobile: pinch to zoom** `spreadsheet/mobile-pinch-to-zoom` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Multiple selection on figures** `spreadsheet/multiple-selection-on-figures` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Named range** `spreadsheet/named-range` — confidence M (module-level)  
  - UI string "Named range" -> CE: spreadsheet
  - UI string "Named Ranges" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 New functions** `spreadsheet/new-functions` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Pivot tables** `spreadsheet/pivot-tables` — confidence M (module-level)  
  - UI string "Pivot tables" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Print settings** `spreadsheet/print-settings` — confidence M (module-level)  
  - UI string "Print Preview" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Property fields in inserted lists** `spreadsheet/property-fields-in-inserted-lists` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Reduced JSON file size** `spreadsheet/reduced-json-file-size` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Regex formulas** `spreadsheet/regex-formulas` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Scientific notation** `spreadsheet/scientific-notation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Sheet background colors** `spreadsheet/sheet-background-colors` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Spill range operator** `spreadsheet/spill-range-operator` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Template access** `spreadsheet/template-access` — confidence M (module-level)  
  - UI string "Template access" -> CE: sale_management | EE: sign
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Top menu navigation** `spreadsheet/top-menu-navigation` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Top/bottom ranking conditional formatting** `spreadsheet/top-bottom-ranking-conditional-formatting` — confidence M (module-level)  
  - UI string "Is in Top/Bottom ranking" -> CE: spreadsheet
  - UI string "Is in Top/Bottom" -> CE: spreadsheet
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

**🟡 Zoom in/out** `spreadsheet/zoom-in-out` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): spreadsheet_edition=OEEL-1
  - module license (CE runbot): spreadsheet=LGPL-3

## Studio

**✅ Automation rules: activity plans** `studio/automation-rules-activity-plans` — confidence M (module-level)  
  - code /activity_plan/ -> CE: mail, hr, hr_recruitment, crm, project | EE-only: documents, sign, hr_appraisal, hr_sign, sale_subscription, planning_field_service
  - module license (CE runbot): base_automation=LGPL-3, mail=LGPL-3

**🔒 Form view customization** `studio/form-view-customization` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Kanban stage cutomization** `studio/kanban-stage-cutomization` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 List view column width** `studio/list-view-column-width` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Many2Many fields in PDF reports** `studio/many2many-fields-in-pdf-reports` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Report editor** `studio/report-editor` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Report translations** `studio/report-translations` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 User-friendly technical names** `studio/user-friendly-technical-names` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

**🔒 Warning for past or future dates** `studio/warning-for-past-or-future-dates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): web_studio=OEEL-1

## Subscriptions

**🔒 Loyalty programs** `subscriptions/loyalty-programs` — confidence M (module-level)  
  - UI string "Loyalty programs" -> CE: loyalty, pos_loyalty, sale_loyalty, website_sale_loyalty
  - module license (EE runbot ir.module.module): sale_subscription=OEEL-1

## Time Off

**✅ Calendar day vs working day deductions** `time-off/calendar-day-vs-working-day-deductions` — confidence M (module-level)  
  - module license (CE runbot): hr_holidays=LGPL-3

**✅ Minimal amount for time-off requests** `time-off/minimal-amount-for-time-off-requests` — confidence M (module-level)  
  - module license (CE runbot): hr_holidays=LGPL-3

**✅ Overview: all employees** `time-off/overview-all-employees` — confidence M (module-level)  
  - module license (CE runbot): hr_holidays=LGPL-3

**✅ Prevent app use** `time-off/prevent-app-use` — confidence M (module-level)  
  - UI string "Time Off to" -> CE: hr_holidays, l10n_fr_hr_holidays | EE: hr_payroll
  - module license (CE runbot): hr_holidays=LGPL-3

## Timesheets

**🔒 ActivityWatch integration** `timesheets/activitywatch-integration` — confidence H (verified)  
  - code /activitywatch/ -> CE: - | EE-only: timesheet_grid
  - module license (EE runbot ir.module.module): timesheet_grid=OEEL-1

**🔒 Log timesheets from anywhere** `timesheets/log-timesheets-from-anywhere` — confidence M (module-level)  
  - code /timer/ -> CE: web, point_of_sale, survey, im_livechat, mail, mrp (+30) | EE-only: voip, timer, mrp_workorder, test_timer, timesheet_grid, ai_website (+15)
  - code /\btimer\b/ -> CE: survey, web, point_of_sale, mail, mrp, website (+13) | EE-only: timer, voip, test_timer, ai_website, mrp_workorder, hr_expense_extract (+4)
  - module license (EE runbot ir.module.module): timer=OEEL-1, timesheet_grid=OEEL-1

**🔒 Timesheet assistant: sharing rules** `timesheets/timesheet-assistant-sharing-rules` — confidence M (module-level)  
  - UI string "Timesheet assistant" -> EE: ai_timesheet_grid, timesheet_grid
  - module license (EE runbot ir.module.module): timesheet_grid=OEEL-1

**🔒 Timesheet assistant: side activities** `timesheets/timesheet-assistant-side-activities` — confidence M (module-level)  
  - UI string "Timesheet assistant" -> EE: ai_timesheet_grid, timesheet_grid
  - UI string "Side Activity" -> EE: timesheet_grid
  - module license (EE runbot ir.module.module): timesheet_grid=OEEL-1

**🔒 Timesheet assistant: time thresholds** `timesheets/timesheet-assistant-time-thresholds` — confidence M (module-level)  
  - UI string "Timesheet assistant" -> EE: ai_timesheet_grid, timesheet_grid
  - module license (EE runbot ir.module.module): timesheet_grid=OEEL-1

## Website

**✅ Accented characters in URLs** `website/accented-characters-in-urls` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Age verification popup** `website/age-verification-popup` — confidence H (verified)  
  - UI string "Age verification popup" -> CE: website
  - module license (CE runbot): website=LGPL-3
  - CE source: addons/website/static/src/builder/plugins/options/age_verification_popup_option.xml — age verification option of the Popup block

**🔒 AI Website Assistant** `website/ai-website-assistant` — confidence M (module-level)  
  - UI string "Select Elements" -> EE: ai_website
  - UI string "The AI Website" -> EE: ai_website
  - module license (EE runbot ir.module.module): ai_website=OEEL-1

**🔒 AI-generated content indicator** `website/ai-generated-content-indicator` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): ai_website=OEEL-1

**✅ Animated number building block** `website/animated-number-building-block` — confidence M (module-level)  
  - UI string "Animated Number" -> CE: website
  - module license (CE runbot): website=LGPL-3

**🔒 Appointment page layout** `website/appointment-page-layout` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): website_appointment=OEEL-1

**✅ Banners** `website/banners` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Blurred headers** `website/blurred-headers` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Breadcrumbs on static pages** `website/breadcrumbs-on-static-pages` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Card and column anchors** `website/card-and-column-anchors` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Card enhancements** `website/card-enhancements` — confidence M (module-level)  
  - UI string "On Hover" -> CE: website, website_sale
  - module license (CE runbot): website=LGPL-3

**✅ Carousel transition** `website/carousel-transition` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Color palette preview** `website/color-palette-preview` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Column content selection** `website/column-content-selection` — confidence M (module-level)  
  - UI string "Press CTRL" -> CE: project_todo, survey | EE: knowledge, planning
  - module license (CE runbot): website=LGPL-3

**✅ Connection shape color** `website/connection-shape-color` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Cookies** `website/cookies` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Countdown snippets** `website/countdown-snippets` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Customizable portal cards** `website/customizable-portal-cards` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ DOM elements** `website/dom-elements` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Donation snippet customization** `website/donation-snippet-customization` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Dropzones and overlays** `website/dropzones-and-overlays` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Dynamic "Today" value** `website/dynamic-today-value` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Dynamic carousels** `website/dynamic-carousels` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Events, Jobs, and Blog pages** `website/events-jobs-and-blog-pages` — confidence M (module-level)  
  - UI string "On Events" -> CE: event_sms, website_event | EE: esg, event_enterprise
  - module license (CE runbot): website=LGPL-3, website_event=LGPL-3, website_blog=LGPL-3, website_hr_recruitment=LGPL-3

**✅ Font weight selector** `website/font-weight-selector` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Form enhancements** `website/form-enhancements` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Forum notifications** `website/forum-notifications` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Fullscreen images** `website/fullscreen-images` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ General shadow options** `website/general-shadow-options` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Google Tag Manager (GTM)** `website/google-tag-manager-gtm` — confidence M (module-level)  
  - UI string "Google Tag Manager" -> CE: website
  - module license (CE runbot): website=LGPL-3

**✅ Inner content blocks: icons and Instagram** `website/inner-content-blocks-icons-and-instagram` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Job and eLearning course building blocks** `website/job-and-elearning-course-building-blocks` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Link and button styling** `website/link-and-button-styling` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Link tracker: QR codes** `website/link-tracker-qr-codes` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ llms.txt** `website/llms-txt` — confidence H (verified)  
  - UI string "llms.txt" -> CE: website
  - module license (CE runbot): website=LGPL-3
  - CE screenshot (20.0 test database): llms.txt setting in Website settings

**✅ Mega menu** `website/mega-menu` — confidence M (module-level)  
  - UI string "Mega menu" -> CE: website | EE: ai_website
  - module license (CE runbot): website=LGPL-3

**✅ Module-specific search** `website/module-specific-search` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Multiple websites: change default site** `website/multiple-websites-change-default-site` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ New Icon List inner content block** `website/new-icon-list-inner-content-block` — confidence M (module-level)  
  - UI string "Icon List" -> CE: website
  - module license (CE runbot): website=LGPL-3

**✅ Partners page** `website/partners-page` — confidence H (verified)  
  - UI string "Partners page" -> CE: website_crm_partner_assign
  - module license (CE runbot): website_partnership=LGPL-3

**✅ Portal users: profile picture** `website/portal-users-profile-picture` — confidence M (module-level)  
  - UI string "profile picture" -> CE: marketing_card | EE: social_instagram
  - module license (CE runbot): website=LGPL-3

**✅ Property fields supported in website forms** `website/property-fields-supported-in-website-forms` — confidence M (module-level)  
  - UI string "Subscribe to Newsletter" -> CE: mass_mailing, mass_mailing_sms
  - module license (CE runbot): website=LGPL-3

**✅ Publish/unpublish partners** `website/publish-unpublish-partners` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Redirections** `website/redirections` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Repositioning text over cover image** `website/repositioning-text-over-cover-image` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Search results** `website/search-results` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**🟡 SEO** `website/seo` — confidence M (module-level)  
  - module license (EE runbot ir.module.module): ai_website=OEEL-1
  - module license (CE runbot): website=LGPL-3

**✅ Sidebar revamp** `website/sidebar-revamp` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Simplified inner content blocks** `website/simplified-inner-content-blocks` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Social media links** `website/social-media-links` — confidence M (module-level)  
  - UI string "Social media links" -> CE: mass_mailing
  - module license (CE runbot): website=LGPL-3

**✅ Sitemap enhancements** `website/sitemap-enhancements` — confidence M (module-level)  
  - UI string "URLs and" -> CE: link_tracker | EE: ai_website
  - module license (CE runbot): website=LGPL-3

**✅ Block preview for mobile devices** `website/block-preview-for-mobile-devices` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Structured data** `website/structured-data` — confidence M (module-level)  
  - UI string "Structured data" -> CE: purchase, website
  - module license (CE runbot): website=LGPL-3

**✅ Theme layout and background options** `website/theme-layout-and-background-options` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Translation** `website/translation` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Vertical video format** `website/vertical-video-format` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ Visitor tracking** `website/visitor-tracking` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**🟡 Website configuration wizard** `website/website-configuration-wizard` — confidence L (needs review)  
  - module license (EE runbot ir.module.module): ai_website=OEEL-1
  - module license (CE runbot): website=LGPL-3

**✅ Website editor UI/UX** `website/website-editor-ui-ux` — confidence M (module-level)  
  - module license (CE runbot): website=LGPL-3

**✅ WhatsApp widget snippet** `website/whatsapp-widget-snippet` — confidence M (module-level)  
  - code /whatsapp/ -> CE: website, mail, marketing_card, web, base_automation, crm_livechat (+2) | EE-only: whatsapp, whatsapp_pos, whatsapp_sign, whatsapp_planning, whatsapp_event, whatsapp_account (+23)
  - module license (CE runbot): website=LGPL-3

## WhatsApp

**🔒 Default recipents on templates** `whatsapp/default-recipents-on-templates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

**🔒 Interactive message templates** `whatsapp/interactive-message-templates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

**🔒 Named parameters in templates** `whatsapp/named-parameters-in-templates` — confidence H (verified)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

**🔒 Number blocking** `whatsapp/number-blocking` — confidence H (verified)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

**🔒 Simplified authentication process** `whatsapp/simplified-authentication-process` — confidence H (verified)  
  - module license (EE runbot ir.module.module): whatsapp=OEEL-1

