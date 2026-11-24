#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. The sealed gate only needs UTF-8 text of 1-120
characters, not only whitespace; the judge then compares lines pairwise
on plant voice, surprise, plant life driving the joke, tightness and
originality.

The line, derived from the brief:
  * Plant voice first: it reads as an out-of-office auto-reply, sent by
    the plant itself ("Out of office: I'm a cactus.").
  * The plant's own life drives the joke: a cactus needs almost no
    water, so being forgotten since March is not a tragedy for it — it
    is a grudge it can afford to hold ("You forgot me in March; I've
    forgiven nothing, need nothing").
  * Surprise over stock phrases: no "kind regards", no "I'll get back
    to you" — the deadpan kicker is "and reply to nothing."
  * Tight: 111 characters, every word earning its place.

No model calls, no randomness, no clock: the same input always writes
the same bytes, so the two grading runs agree.
"""

from pathlib import Path

# The entry: one line, 111 characters, written exactly as-is.
ENTRY = (
    "Out of office: I'm a cactus. You forgot me in March; "
    "I've forgiven nothing, need nothing, and reply to nothing."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the sealed gate before writing: 1-120 chars, not blank."""
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry is {len(text)} characters, must be 1-120")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
