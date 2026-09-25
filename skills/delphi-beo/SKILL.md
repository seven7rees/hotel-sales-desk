---
name: delphi-beo
description: Use to build, edit, generate or send Banquet Event Orders (BEOs) in Amadeus Delphi. Covers adding menu and text items, fixing $0 prices, room moves, generating PDFs on the Merge page, assembling a packet, and sending it for client signature.
---

# Delphi BEOs

Read `.hotel-desk/property.yaml` first. If it does not exist, run the `property-setup` skill.
Keep `reference/gotchas.md` open. Most failures are listed there.

## 1. Read the current state
Query the booking, its events, and every event item before changing anything:
- `nihrm__BookingEvent__c`: times, room, AGR, guarantee, `nihrm__Beo__c`
- `nihrm__EventItem__c`: ItemType, ActualQuantity, UnitPrice, BeoSection, RevenueClassification, Location, RichDescription, hide flags
Report the gaps to the user before writing anything.

## 2. Add or edit items
- **Menu items:** ItemType `Simple Menu` or `Item`. Price comes from the menu file the client was actually sent (`files.menus`). If two menu versions disagree, ask.
- **Every food line lists its contents** in RichDescription (for example, what a buffet includes). A bare menu name is not enough for the kitchen.
- **Notes and setup:** ItemType `Text`, RichDescription as `<ul><li>` bullets, HidePriceOnBeo and HideQuantityOnBeo set to true.
- **Every item** needs BeoSection, RevenueClassification and Location, or it prints nowhere.
- **After every insert:** PATCH ItemType and ActualQuantity, then re-query to confirm. Inserts drop them.
- **After every priced insert:** confirm a `nihrm__EventItemRevenueBreakdown__c` child exists. If not, create one using `financials.service_charge_split`.
- **Allergies:** a plated meal only needs the allergy guest's own selections to be safe. A buffet needs the entire menu to be safe. Never tell a client a guest "can eat" something without checking the ingredients.
- **House setup** (cocktail tables, standard linens, staging included with the room) is not billed. Leave it off the BEO.

## 3. Room moves
Update the event's function room field AND its `nihrm__EventFunctionroomDate__c` join together. Outdoor rooms get a weather backup line naming the backup room from the config.

## 4. Generate PDFs
1. The user must be logged in to Salesforce in the browser. If you see a login page, stop and ask.
2. Open `https://<vf_domain>/apex/nihrm__Merge?id=<bookingId>`.
3. Select the `templates.beo` radio (JS click), tick exactly ONE event, click the top Generate.
4. Repeat per event in a fresh tab if the page hangs. One event per Generate.
5. If an event has no BookingDocument, create one (Type BEO, `templates.beo_document_template_id`), link it on `nihrm__Beo__c`, and increment the BEO number counter.
6. Merge the PDFs in event order: `python scripts/merge_pdfs.py out.pdf beo1.pdf beo2.pdf ...`
7. Extract the packet text and check it: names, dates, times, rooms, quantities, prices, no staff shorthand, no internal notes.

## 5. Send
- The client email attaches the PDF "for reference" and includes the e-sign link as "the copy to sign". State the event dates and room plainly.
- Build the email with the `sales-inbox-triage` drafting rules (threaded reply, configured font, signature).
- A fresh-context review of the email and the PDF happens BEFORE the draft is created, not after. People send drafts quickly.

## Never
- Never change prices, comps or minimums without the user's approval.
- Never send. Create drafts only.
- Never enter credentials into Salesforce or the e-sign tool.
