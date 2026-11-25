"""Write one funny 4 a.m. agent bug-fix commit message to /output/entry.txt.

Pure Python stdlib only. Deterministic: same bytes on every run.
"""

import os

# The message is composed from fragments so each beat of the joke is
# visible in the code; the joined result is the single commit line.
_FRAGMENTS = [
    "fix: reverted my 3am fix,",
    "which fixed my 2am fix,",
    "which broke the thing my 1am fix was fixing;",
    "the bug was me all along",
]

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def compose_message():
    """Join the fragments into one line and validate the gate."""
    text = " ".join(_FRAGMENTS).strip()
    if not text or text.isspace():
        raise ValueError("message must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("message exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("message must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def main():
    text = compose_message()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
