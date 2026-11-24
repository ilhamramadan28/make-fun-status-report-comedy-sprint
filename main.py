#!/usr/bin/env python3
"""Write the entry to /output/entry.txt."""
import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    with open(SOURCE, encoding="utf-8") as f:
        text = f.read()
    stripped = text.strip()
    if not (1 <= len(stripped) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if any(ord(c) < 32 for c in text):
        raise SystemExit("entry must not contain control characters")
    if "\n" in stripped:
        raise SystemExit("entry must be a single clean line")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("output mismatch")


if __name__ == "__main__":
    main()
