#!/usr/bin/env python3
"""Entry for make.fun: The 3AM Commit Message.

Writes one funny one-line git commit message, deterministically,
to /output/entry.txt. No network, no randomness, no time dependence.
"""

import os

ENTRY = "fix: reverted my fix. the bug was load-bearing and I apologized to it\n"

MAX_LEN = 140


def main() -> None:
    line = ENTRY.rstrip("\n")
    if "\n" in line or len(line) > MAX_LEN:
        raise ValueError("entry must be one line of at most 140 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
