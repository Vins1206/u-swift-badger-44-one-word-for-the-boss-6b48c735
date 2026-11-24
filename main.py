"""One Word for the Boss -- entry program.

Writes exactly one word to /output/entry.txt: "teflon".

Why this word: the boss nothing sticks to. Blame, missed deadlines,
bad calls -- everything slides off him while it sticks to everyone
else. One word, no caption needed, and every office, kitchen and
warehouse has met him. It is also short on purpose: at 6 bytes it
wins the size tie-break against any longer word that ties on rate.
"""

import os

WORD = "teflon"


def main() -> None:
    word = WORD.strip().lower()
    assert word, "word must not be empty"
    assert len(word) <= 30, "word must be at most 30 characters"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert word.isalpha(), "entry must be a single alphabetic word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
