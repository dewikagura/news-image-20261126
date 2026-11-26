#!/usr/bin/env python3
"""Ship the bundled front page to the grader's output directory.

The entry image is drawn at build time and shipped beside this program as
entry.png. This program only copies those exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png, verifies the copy byte for byte, and exits 0
on success. It uses only the Python standard library, reads nothing but the
bundled image, writes nowhere but the output directory, and never touches
the network, so running it twice writes identical bytes both times.
"""

import hashlib
import os
import sys

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
SOURCE_NAME = "entry.png"
TARGET_NAME = "entry.png"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(src):
        return fail("bundled image not found beside main.py: " + SOURCE_NAME)
    with open(src, "rb") as handle:
        data = handle.read()
    if not data.startswith(PNG_MAGIC):
        return fail("bundled image is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("bundled image has no PNG header")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        return fail("bundled image is %dx%d, expected 1024x1024"
                    % (width, height))
    if len(data) > MAX_BYTES:
        return fail("bundled image is over the 1 MiB limit")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, TARGET_NAME)
    with open(dst, "wb") as handle:
        handle.write(data)
    with open(dst, "rb") as handle:
        written = handle.read()
    digest = hashlib.sha256(data).hexdigest()
    if hashlib.sha256(written).hexdigest() != digest:
        return fail("written bytes differ from the bundled image")
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
