# hotel-sales-desk

Claude Code skills for hotel sales and events teams running **Amadeus Delphi** (the `nihrm__` managed package on Salesforce).

Built from real BEO, contract, resume and inbox workflows, generalized so no property, client, or staff data ships with the plugin. Every property-specific value lives in one config file you fill in.

## What it does

| Skill | Replaces |
|---|---|
| `delphi-beo` | Building, fixing, and generating Banquet Event Orders, packet assembly, sending for signature |
| `delphi-group-resume` | Producing the rooms/logistics resume from Delphi, filling what the template leaves blank |
| `delphi-contracts` | Generating contracts and addenda from your org's own Delphi templates, checking the revenue math |
| `sales-inbox-triage` | Sorting a day of inbox mail into action buckets and drafting on-brand replies |
| `property-setup` | Run once: discovers your org's Delphi IDs and template names, builds your config |

## Example property

The config example describes a fictional 400-room hotel with 40,000 sq ft of function space (an 18,000 sq ft divisible ballroom, an 8,000 sq ft junior ballroom, a 4,000 sq ft outdoor terrace, a boardroom, and 12 breakout rooms). Replace it with your own numbers.

## Install

```
/plugin marketplace add seven7rees/hotel-sales-desk
/plugin install hotel-sales-desk@hotel-sales-desk
```

## Setup

1. Authenticate your own Salesforce CLI to your Delphi org (`sf org login web`). Claude never handles your password.
2. Run the `property-setup` skill. It builds `.hotel-desk/property.yaml` from your org and a short interview.
3. Keep `.hotel-desk/property.yaml` out of source control if this repo is ever forked publicly. It describes a real property.

## Guardrails built into every skill

- Read-only until the user confirms. Live data before drafting, never invented rates or dates.
- Drafts only. Nothing sends or signs itself.
- Escalates legal, comp, discount, and above-threshold requests instead of acting on them.
- Never touches login pages or credentials.

## What this is not

Not a Delphi replacement, not a Salesforce admin tool, not legal advice. It automates the mechanical, repeatable parts of the job so a sales and events team spends less time on data entry and more time on the guest and the deal.

## License

See `LICENSE`.
