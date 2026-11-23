#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes a single funny line to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

LINE = (
    "I bought noise-cancelling earbuds to finally hear myself think, "
    "and it turns out I have nothing to say."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
