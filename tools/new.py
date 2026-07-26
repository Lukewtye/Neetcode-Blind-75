#!/usr/bin/env python3
"""Scaffold a new practice file with the required header.

    python3 tools/new.py neetcode/arrays-hashing two-sum
    python3 tools/new.py exercism bob
"""
import pathlib
import sys

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

folder, slug = sys.argv[1], sys.argv[2]
root = pathlib.Path(__file__).resolve().parent.parent
path = root / folder / f"{slug}.py"

if path.exists():
    print(f"exists already: {path}")
    sys.exit(1)

path.parent.mkdir(parents=True, exist_ok=True)
path.write_text((root / "tools" / "template.py").read_text())
print(path)
