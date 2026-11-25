"""The Absurd Clause Contest entry.

Writes a single original English sentence, phrased as an absurd clause
buried deep inside a terms-of-service agreement, to /output/entry.txt.

Pure standard library, no network, fully deterministic: every run writes
the exact same bytes. The clause itself is original, written for this
competition, and is the only text the program produces.
"""

import hashlib
import os
import sys

CLAUSE = (
    "The User acknowledges that the Company may, at its sole discretion, "
    "replace the User's reflection in mirrors with a sponsored advertisement."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    clause = CLAUSE

    # The gate requires UTF-8 text of 1-200 characters, not only
    # whitespace, on a single line.
    if not clause or clause != clause.strip():
        print("error: clause is empty or has surrounding whitespace", file=sys.stderr)
        return 1
    if len(clause) > MAX_CHARS:
        print(
            "error: clause is %d characters, over the %d limit"
            % (len(clause), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in clause or "\r" in clause:
        print("error: clause must be a single line", file=sys.stderr)
        return 1

    data = clause.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write without a trailing newline: the file is exactly the sentence.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and confirm the bytes on disk match what we intended.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    if on_disk != data:
        print("error: bytes on disk do not match the clause", file=sys.stderr)
        return 1

    print("wrote %d characters (%d bytes) to %s" % (len(clause), len(data), OUTPUT_PATH))
    print("sha256: %s" % hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
