#!/usr/bin/env python3
"""One Emoji, One Dream Vacation entry (make.fun).

Writes exactly one emoji to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).

The pick is Mount Fuji (U+1F5FB): a single, instantly readable
postcard of one specific dream trip — sunrise over Japan's most
famous peak — rather than a generic beach or plane. Stdlib only;
no network, no files read, no secrets.
"""

import os
import sys

EMOJI = "\U0001f5fb"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EMOJI
    # The gate allows 1 to 8 UTF-8 characters; one emoji is exactly 1.
    assert 1 <= len(text) <= 8, f"entry is {len(text)} chars, must be 1-8"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the grader's gate reads UTF-8 text, so confirm the
    # file on disk decodes to exactly the one emoji we meant to write.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, f"round-trip mismatch: {written!r} != {text!r}"
    print(f"wrote {text!r} ({len(text)} char) to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
