#!/usr/bin/env python3
"""Local verification for the Houseplant Out-of-Office entry.

Runs main.py twice (the grader runs it twice for determinism) and checks
the sealed gate: /output/entry.txt must be UTF-8 text of 1-120
characters, not only whitespace, and both runs must write identical bytes.

Usage: python3 test_entry.py
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = Path("/output/entry.txt")


def run_once() -> bytes:
    result = subprocess.run(
        [sys.executable, str(HERE / "main.py")],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise SystemExit(f"main.py failed:\n{result.stdout}\n{result.stderr}")
    print(result.stdout.strip())
    return OUTPUT.read_bytes()


def main() -> None:
    first = run_once()
    second = run_once()
    assert first == second, "runs differ — entry is not deterministic"
    text = first.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only whitespace"
    print(f"OK: {len(text)} characters, deterministic across 2 runs")
    print(f"Entry: {text}")


if __name__ == "__main__":
    main()
