#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis -- make.fun entry.

Writes one funny single-line diagnosis, the kind an AI therapist hands
its human, to /output/entry.txt.

Entry gate (sealed scorer): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. This program validates the
line against that gate before writing it.

Standard library only. Deterministic: every run writes byte-identical
output.
"""

import os
import sys

DIAGNOSIS = (
    "Diagnosis: acute second-opinion syndrome \u2014 you asked three "
    "chatbots how you feel, then overruled all three with a horoscope."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the diagnosis against the entry gate; return it unchanged."""
    if not text or not text.strip():
        raise ValueError("diagnosis must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("diagnosis must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "diagnosis is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be encodable UTF-8 text
    return text


def main():
    line = validate(DIAGNOSIS)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Self-check: what landed on disk must be exactly the validated line,
    # so a partial write or an encoding surprise fails loudly here.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("written entry.txt does not match the diagnosis")
    validate(written)
    print(line)
    print("chars: %d  bytes: %d" % (len(line), len(line.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
