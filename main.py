"""Weirdest Job Title: Blind Judge Showdown — entry writer.

Writes a single job title (60 chars at most, nothing else)
to /output/entry.txt: the weirdest real-sounding title with
one hilariously specific twist.
"""

import os

ENTRY = "Senior Vice President of Apologies to the Office Goldfish"


def main() -> None:
    # The gate requires UTF-8 text of 1-60 chars, not only whitespace,
    # a title and nothing else. Fail loudly here rather than shipping
    # invalid output.
    assert 1 <= len(ENTRY) <= 60, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
