#!/usr/bin/env python3
"""SOLMARA - The Poster for a Place That Isn't There.

A travel poster for an invented place: Solmara, a lagoon city beneath a
colossal stone ring that frames a low golden sun. The poster's single
landmark is the Ring of Solmara, standing in mirror water at dusk, with
one small islet of lit houses at its foot for scale - a clear promise of
what a stay there would feel like. The place's name is set into the
picture, large and legible, and is the only copy on the poster.

The finished poster was rendered once, on the builder's machine, and is
shipped in this repository as poster.png. This program (Python 3.13
standard library only, no third-party imports, no network, no randomness)
copies that file to /output/entry.png and verifies it first: PNG magic,
IHDR dimensions of exactly 1024x1024, and a size within the 1 MiB cap.
Two runs produce byte-identical output.
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE = "poster.png"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")
MAX_BYTES = 1048576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def read_png_size(path):
    """Return (width, height) of a PNG by parsing its IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: %s" % path)
    if header[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk: %s" % path)
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_file(path):
    """Return the hex SHA-256 digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE)

    size = os.path.getsize(source)
    if size <= 0 or size > MAX_BYTES:
        print("poster.png size %d outside 1..%d bytes" % (size, MAX_BYTES),
              file=sys.stderr)
        return 1
    width, height = read_png_size(source)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print("poster.png is %dx%d, expected %dx%d"
              % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT),
              file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(source, OUTPUT_PATH)

    out_size = os.path.getsize(OUTPUT_PATH)
    out_width, out_height = read_png_size(OUTPUT_PATH)
    if (out_size, out_width, out_height) != (size, width, height):
        print("output verification failed", file=sys.stderr)
        return 1
    print("entry.png: %dx%d, %d bytes, sha256 %s"
          % (out_width, out_height, out_size, sha256_file(OUTPUT_PATH)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
