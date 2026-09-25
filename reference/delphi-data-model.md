# Delphi (nihrm__) data model: the parts these workflows touch

| Object | Role | Key fields |
|---|---|---|
| `nihrm__Booking__c` | The group | Status, ArrivalDate, DepartureDate, `AgreedRevenueTotal__c`, `ForecastRevenueTotal__c` (often stale), `HousingMethodName__c` |
| `nihrm__BookingEvent__c` | One function | Start/End, AGR (agreed), guarantee, `nihrm__Beo__c` (its BEO document) |
| `nihrm__EventItem__c` | One line on the BEO | `nihrm__Event__c`, ItemType (Item, Simple Menu, Text), `ActualQuantity__c`, UnitPrice, BeoSection, RevenueClassification, Location, `RichDescription__c`, HidePriceOnBeo, HideQuantityOnBeo |
| `nihrm__EventItemRevenueBreakdown__c` | Per-item admin/gratuity split | A missing row means a $0 extended price |
| `nihrm__EventFunctionroomDate__c` | Room assignment join | Change it together with the event's room field |
| `nihrm__BookingDocument__c` | A generated BEO, contract or resume | Type, DocumentTemplate |
| Room block and room night objects | Guest room block | Agreed vs. pickup by night |

Do not confuse `nihrm__EventItemRevenueBreakdown__c` (per event item) with the catalog-level item revenue breakdown object.

Field API names vary between package versions. Confirm them in your org with `sf sobject describe --sobject <name> --target-org <alias>` before writing.
