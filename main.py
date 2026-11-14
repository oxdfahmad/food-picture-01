"""food-picture-01 entry (Python 3.13, standard library only).

The picture is the entry.png beside this file: a steaming bowl of
tonkotsu ramen, chopsticks lifting glossy noodles, a soft-boiled egg,
chashu and spring onions in warm window light. The program copies it
byte for byte to the output directory, so both graded runs produce
identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

# Gate limits from the competition rules: at most 1 MiB, at most 1024x1024.
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from a JPEG's first SOF marker (stdlib only)."""
    i = 2  # skip the SOI marker
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2
            height, width = struct.unpack(">HH", data[i + 5 : i + 9])
            return width, height
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = struct.unpack(">H", data[i + 2 : i + 4])[0]
        i += 2 + length
    raise ValueError("no SOF marker found in entry.png")


def main() -> None:
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    width, height = jpeg_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Guard against a partial write: the output must be byte-identical.
    if hashlib.sha256(target.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("output does not match entry.png")
    print(f"wrote {target} ({len(data)} bytes, {width}x{height})")


if __name__ == "__main__":
    main()
