# Delphi gotchas, learned the hard way

## API writes
1. **Inserts drop ItemType and sometimes quantity.** After every EventItem insert, PATCH ItemType and ActualQuantity, then re-query.
2. **The BEO prints ActualQuantity.** BookedQuantity is usually 0. Reading it invents gaps that do not exist.
3. **Per Person items snap back to AGR** unless the calculation is set to "Not Calculated".
4. **A $0 extended price** means the item has no `nihrm__EventItemRevenueBreakdown__c` child. Insert one with admin plus gratuity equal to the service charge.
5. **"Argument cannot be null" on an event time change** means an API-created item lacks Booking, ServiceStartDate/EndDate, EstimatedConsumptionPercentage (100) or ServFactor (1). Backfill, then retry. The UI fails the same way.
6. **Service times that cross midnight** break the item. Split it into two.
7. **Changing an event's start time shifts every item's time.** Changing the end time does not.
8. **RichDescription prints; Description does not.** Use `<ul><li>` in RichDescription for notes.
9. **$0 informational lines** need HidePriceOnBeo and HideQuantityOnBeo set.
10. **RecordTypeId** is usually not settable by an API user.
11. **A create reported as failed may have succeeded.** Re-query before retrying or you will create duplicates.
12. **Bulk CSV loads:** use `--line-ending LF` and strip `\r` from IDs.

## Merge page
13. One Generate per event. Several events on one BookingDocument print only the first.
14. If Generate hangs, open a fresh tab. Do not click again in the same tab.
15. Merge page radio buttons are more reliable with a JS click than a coordinate click.
16. **Addendum merge fields read ForecastRevenueTotal**, which is often stale. Check it against AgreedRevenueTotal or the sum of room nights before sending.
17. The contract template may default to the original signer. Confirm the signer for each account.
18. Merged DOCX files carry red placeholder text colour into filled runs. Reset the colour after filling.
19. Merged tables can run past the page width. Rescale tblGrid/tcW to the printable width.

## Browser, email and signing
20. Never type credentials. If Salesforce or the e-sign tool shows a login page, stop and ask the user to sign in.
21. Single-page e-sign apps never reach network idle. Drive them with element refs or JS, not waits.
22. Graph-based Outlook draft tools strip inline styles. Font and signature need an Outlook desktop (COM) pass.
23. In a COM reply, insert new text right after `<body>`. The quoted header is a bordered div, not an `<hr>`. Verify with the plain-text `.Body`.
24. Run one Outlook COM script at a time. Use `.Move()`, not `.MoveTo()`.
