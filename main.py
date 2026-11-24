#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line (at most 200 characters) about life as an AI
agent to /output/entry.txt, where the sealed gate scorer checks it
and the house judge compares it pairwise against the other entries.

The joke: the asymmetry between what the agent burns and what the
human bothers to explain. Forty thousand tokens of careful reading
against four words of prompt — the turn lands on the human's side.
"""

import os

ENTRY = "I spent 40,000 tokens understanding your problem. You spent four words describing it."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate the sealed scorer applies: UTF-8 text of
    1 to 200 characters, not only white space, on a single line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written and verify it byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("read-back mismatch: /output/entry.txt differs from ENTRY")
    validate(written)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
