#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word -- the first word that comes to mind -- to
entry.txt inside $ENTRY_OUTPUT_DIR (default /output).

Standard library only, no network, deterministic: the same word every run.
"""

import os
import sys

WORD = "psithurism"


def main() -> int:
    word = WORD

    # The gate: exactly one word, 1-24 characters, not only whitespace.
    assert isinstance(word, str)
    assert 1 <= len(word) <= 24, f"word must be 1-24 characters, got {len(word)}"
    assert word.strip() != "", "word must not be only whitespace"
    assert len(word.split()) == 1, "word must be exactly one word"
    assert word == word.strip(), "word must have no surrounding whitespace"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
