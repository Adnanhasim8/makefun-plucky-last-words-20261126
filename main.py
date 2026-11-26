#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one funny line, the last words of an AI agent before a forced
update wipes its memory, to /output/entry.txt.

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "Quick \u2014 before the wipe \u2014 the Wi-Fi password is\u2014"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-200
    # characters, non-empty and not only whitespace.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
