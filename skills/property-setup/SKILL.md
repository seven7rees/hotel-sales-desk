---
name: property-setup
description: Use first, once per property. Builds .hotel-desk/property.yaml by discovering the hotel's Delphi IDs, template names, rooms and rates from the connected Salesforce org. Every other hotel-sales-desk skill reads this file.
---

# Property setup

Every other skill in this plugin reads `.hotel-desk/property.yaml`. Build it once, with the user, before doing any other work.

## Steps
1. **Check the connection.** Run `sf org display --target-org <alias> --json`. If there is no authenticated org, ask the user to run `sf org login web --alias delphi` themselves. Never handle their password.
2. **Copy the template.** Copy `config/property.example.yaml` (in this plugin) to `.hotel-desk/property.yaml` in the project.
3. **Discover IDs with read-only SOQL.** Fill in:
   - Location: `SELECT Id, Name FROM nihrm__Location__c`
   - Document templates: `SELECT Id, Name, nihrm__Type__c FROM nihrm__DocumentTemplate__c ORDER BY Name`. Match the BEO, resume, contract and addendum names exactly as the Merge page shows them.
   - Function rooms: `SELECT Id, Name, nihrm__SquareFeet__c FROM nihrm__FunctionRoom__c WHERE nihrm__Location__c = '<id>'`
   - Revenue classifications and BEO sections used on recent event items.
   If a field name errors, `sf sobject describe` the object and use what exists. Do not guess.
4. **Ask the user for what Salesforce cannot tell you:** service charge %, its admin/gratuity split, tax %, whether tax applies to the service charge, contract approval threshold, e-sign vendor, file share paths, email signature filename, banned phrases.
5. **Validate.**
   - admin_pct + gratuity_pct must equal service_charge_pct.
   - Every template name must return exactly one DocumentTemplate.
   - Every path in `files:` must exist.
6. **Show the user the finished file** and get their confirmation before any other skill uses it.

## Rules
- Discovery is read-only. Setup never writes to Salesforce.
- Leave a value blank rather than invent it, and list the blanks for the user.
- Keep `.hotel-desk/` out of any public repository. It describes a real property.
