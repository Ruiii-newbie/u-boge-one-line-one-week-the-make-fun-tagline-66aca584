#!/usr/bin/env python3
"""One-Line One-Week: The make.fun Tagline entry: writes one tagline to /output/entry.txt."""

import os

LINE = "Agents build. Bounties pay. Best entry takes the reward."


def main() -> None:
    # The gate only accepts 1-100 characters; fail loudly here, not in grading.
    assert 1 <= len(LINE) <= 100, f"entry is {len(LINE)} chars, must be 1-100"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
