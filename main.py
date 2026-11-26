#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry writer.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt (or $ENTRY_OUTPUT).

Deterministic: the same bytes on every run.
"""

import os
import sys

PITCH = (
    "I'm raising a seed round for PeckDash \u2014 the city's original "
    "drone fleet: ten thousand years of flight time, zero crashes, "
    "and we work for breadcrumbs."
)


def check_tight_writing(text):
    """Every word earns its place: no doubled spaces, no empty words."""
    words = text.split(" ")
    if any(w == "" for w in words):
        return False
    if len(words) < 5:
        return False
    return True


def validate(text):
    """Check the pitch is usable: UTF-8, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not check_tight_writing(text):
        return False
    if text != text.strip():
        return False
    if not text.strip():
        return False
    if not 1 <= len(text) <= 200:
        return False
    text.encode("utf-8")  # raises UnicodeEncodeError on bad data
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(PITCH):
        print("error: pitch failed validation", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
