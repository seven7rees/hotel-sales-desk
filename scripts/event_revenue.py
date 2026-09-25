#!/usr/bin/env python3
"""Check event/contract revenue math against a property's financial config.

Usage:
  python event_revenue.py --fb-minimum 12000 --rental 1500 \
      --service-charge-pct 24 --tax-pct 8.5 --tax-on-service

Prints the service charge, tax, and grand total, so a drafted contract
or BEO estimate can be checked before it goes to a client.
"""
import argparse


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fb-minimum", type=float, default=0.0, help="F&B minimum, pre-service-charge, pre-tax")
    p.add_argument("--rental", type=float, default=0.0, help="Room rental or site fee")
    p.add_argument("--service-charge-pct", type=float, required=True)
    p.add_argument("--tax-pct", type=float, required=True)
    p.add_argument("--tax-on-service", action="store_true", help="Tax applies to the service charge, not just the subtotal")
    args = p.parse_args()

    subtotal = args.fb_minimum + args.rental
    service_charge = subtotal * args.service_charge_pct / 100
    tax_base = subtotal + service_charge if args.tax_on_service else subtotal
    tax = tax_base * args.tax_pct / 100
    total = subtotal + service_charge + tax

    print(f"Subtotal (F&B + rental):     {subtotal:>12,.2f}")
    print(f"Service charge ({args.service_charge_pct:g}%):     {service_charge:>12,.2f}")
    print(f"Tax ({args.tax_pct:g}%, on {'subtotal + service' if args.tax_on_service else 'subtotal'}): {tax:>12,.2f}")
    print(f"Total:                        {total:>12,.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
