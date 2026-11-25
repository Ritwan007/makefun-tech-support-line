#!/usr/bin/env python3
"""make.fun entry: Have You Tried Turning It Off?

Writes one funny line a hopeless tech support agent says to a
desperate customer to /output/entry.txt.
"""
import os

LINE = "Have you tried turning it off and on again? It worked for my marriage. Well \u2014 half of it did."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
