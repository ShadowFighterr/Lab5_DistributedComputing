#!/usr/bin/env python3
import sys
import re

WORD_RE = re.compile(r"[A-Za-z0-9']+")

def main():
    for line in sys.stdin:
        line = line.strip().lower()
        for word in WORD_RE.findall(line):
            # emit word \t 1
            print(f"{word}\t1")

if __name__ == "__main__":
    main()
