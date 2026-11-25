#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the bundled poster (entry.png, drawn for Tuesday 24 November 2026)
to $MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, no network,
deterministic: both runs write the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("error: bundled entry.png not found next to main.py",
              file=sys.stderr)
        return 1
    with open(src, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("error: bundled entry.png is not a valid PNG", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
