---
name: delphi-contracts
description: Use to create group contracts and contract addenda from the property's own Delphi merge templates (every contract, addendum and agreement template the org has), fill the blanks from live booking data, check the math, and prepare the signing copy.
---

# Contracts and addenda from Delphi templates

Read `.hotel-desk/property.yaml` first.

**The rule:** contracts and addenda come from the property's Delphi merge templates. Never hand-build a contract from scratch or from an old client's file. Hand-built documents drift from approved legal language.

## 1. Find the right template
List every contract-type template in the org:
`SELECT Id, Name, nihrm__Type__c FROM nihrm__DocumentTemplate__c ORDER BY Name`
Show the user the list (group contract, addendum, wedding agreement, catering-only, rooms-only and any others) and confirm which one fits. Default to `templates.contract` or `templates.addendum`.

## 2. Pull live data first
Query the booking, room blocks by night, events, F&B minimums, rental fees, deposit schedule and account contact. Never invent a rate, concession or date. If Delphi has no value, stop and ask.

## 3. Generate
1. The user is logged in. If you see a login page, stop and ask.
2. Merge page, select the template, check the room block(s), choose DOC, Generate.
3. Download fresh from the new BookingDocument's attachments every time.

## 4. Fill and fix
- Fill the remaining blanks from Delphi or the user: signing date, due dates, room-night change, revenue figures.
- **Revenue check:** addendum merge fields often read `ForecastRevenueTotal__c`, which can be stale. Compare it with `AgreedRevenueTotal__c` or the sum of room nights. If they differ, stop and show the user.
- **Signer check:** templates can default to the original signer. Confirm the signer for this account.
- Reset the red placeholder colour on filled text. Rescale oversized tables to the printable width.
- **Rate shown:** show the contract's stated rate, not revenue divided by nights.

## 5. Check the math
Run `python scripts/event_revenue.py` with the F&B minimum, rental, service charge % and tax %. The service charge is taxable when `financials.tax_applies_to_service_charge` is true. F&B minimums are measured on food and beverage alone, before service charge and tax.

## 6. Approval and signing
- If the total contract value is at or above `financials.contract_approval_threshold`, add the director signature line and tell the user it needs approval.
- Flag any custom legal language, waived deposit, comp or rate override. Do not include it without approval.
- Convert to PDF, save under `files.contracts_root`, and prepare the e-sign request. The user sends it.

## Never
- Never change legal language in a template.
- Never send a contract. Prepare it for the user.
