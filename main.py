#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji for a dream vacation to /output/entry.txt.
"""

ENTRY = "\U0001F30C"


import os


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 8, f"entry is {len(text)} chars"
    assert len(text) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
