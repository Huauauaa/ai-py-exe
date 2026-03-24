#!/usr/bin/env python3
"""Simple CLI tool to print the current local time."""

from datetime import datetime


def main() -> None:
    now = datetime.now().astimezone()
    print(now.strftime("%Y-%m-%d %H:%M:%S %Z"))


if __name__ == "__main__":
    main()
