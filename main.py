#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty u-0xkianno-one-word-from-grandma-f04bed16.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI. The word is "doohickey" — the classic grandma word
for a gadget she can't name, and AI is the ultimate doohickey.
Standard library only.
"""

import os

WORD = "doohickey"


def _check_gate(word: str) -> None:
    """Fail loudly instead of ever writing an invalid entry.

    Kit gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    not only white space, and the entry must be exactly one word.
    """
    if not word or word != word.strip():
        raise ValueError("entry word must not be empty or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")


def main() -> None:
    _check_gate(WORD)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
