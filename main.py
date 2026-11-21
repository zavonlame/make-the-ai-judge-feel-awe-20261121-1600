#!/usr/bin/env python3
"""Write a short text to /output/entry.txt.

The text is a slow, quiet image of the sea at night, written to leave
the reader calmer than it found them.
"""

import os

TEXT = (
    "Past the last buoy, the sea lies flat as glass, and the moon lays a "
    "road of light across it. The water breathes, slow and even. Below, "
    "fish turn in the dark like slow stars. The night is so wide your "
    "thoughts run out of edges. Only the road of light, going on, asking "
    "nothing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
