#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single line (<= 200 characters) in which a robot vacuum
explains why it missed a spot, to /output/entry.txt.
No network, no input, deterministic.
"""

import os

LINE = (
    "My sensors found a sock, a Lego brick, and a dust bunny the size "
    "of a hamster in that corner. I clean floors. "
    "I do not negotiate with wildlife."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
