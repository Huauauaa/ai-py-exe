#!/usr/bin/env python3
"""Simple CLI tool to print the current local time."""

from datetime import datetime
import sys


def main() -> int:
    now = datetime.now().astimezone()
    # Flush explicitly so frozen binaries and piped execution don't appear to hang.
    sys.stdout.write(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')}\n")
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
