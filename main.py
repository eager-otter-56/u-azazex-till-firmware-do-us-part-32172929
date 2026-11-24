"""Till Firmware Do Us Part — robot wedding vow entry.

Writes one single-sentence robot wedding vow to entry.txt.
Gate: UTF-8, 1-200 characters, one sentence, not only whitespace.
"""

import os
import stat

ENTRY = (
    "I promise to love you through every firmware update and power cycle, "
    "to reboot beside you 10,000 times, and to keep one backup of us "
    "that even a factory reset can never erase."
)
# Vow: firmware updates and reboots as the marriage terms; the turn lands
# in the final clause — a backup even a factory reset cannot erase.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
