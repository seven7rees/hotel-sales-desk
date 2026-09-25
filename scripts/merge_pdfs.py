#!/usr/bin/env python3
"""Merge per-event BEO PDFs into one packet, in the given order.

Usage: python merge_pdfs.py OUTPUT.pdf INPUT1.pdf INPUT2.pdf ...
"""
import sys

from pypdf import PdfWriter


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 1

    output_path, *input_paths = argv[1:]
    writer = PdfWriter()
    for path in input_paths:
        writer.append(path)
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Wrote {output_path} from {len(input_paths)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
