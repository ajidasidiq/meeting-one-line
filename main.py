"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt.

The line is deliberately built as one sentence in three beats, because
that is exactly how a pointless meeting runs: first the status round
where nothing has moved, then the decision round where nothing gets
decided, then the scheduling round where the only concrete outcome is
another meeting. Naming all three in one breath leaves nothing for a
meeting to do, and the final clause turns the sentence itself into the
meeting, so after reading it there is no meeting left to hold.
"""

from pathlib import Path

LINE = (
    "There is no update, no decision has been made, "
    "and the next meeting is already booked, "
    "so this sentence was the whole meeting."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and the task requires a single line and a single
    sentence, so enforce all of that before writing anything."""
    if not line.strip():
        raise ValueError("entry must not be blank")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
