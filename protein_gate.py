#!/usr/bin/env python3
"""Main-agent gate for protein-scout runs.

This command rebuilds the summary, runs the legacy fixer/checker, then runs the
strict non-mutating validator for the requested batch.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def run(cmd: list[str]) -> int:
    print("\n$ " + " ".join(cmd))
    proc = subprocess.run(cmd, cwd=BASE)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run protein-scout rebuild and validation gates")
    parser.add_argument("--batch", type=Path, help="Batch manifest JSON")
    parser.add_argument("--gene", action="append", default=[], help="Gene symbol to validate; repeatable")
    parser.add_argument("--all", action="store_true", help="Validate every report")
    parser.add_argument("--skip-legacy", action="store_true", help="Skip legacy validate.py")
    parser.add_argument("--fail-on-warnings", action="store_true")
    args = parser.parse_args()

    if not args.batch and not args.gene and not args.all:
        raise SystemExit("Provide --batch, --gene, or --all")

    rc = run([sys.executable, "rebuild_summary.py"])
    if rc:
        return rc

    if not args.skip_legacy:
        rc = run([sys.executable, "validate.py"])
        if rc:
            return rc

    strict_cmd = [sys.executable, "validate_strict.py"]
    if args.batch:
        strict_cmd += ["--batch", str(args.batch)]
    for gene in args.gene:
        strict_cmd += ["--gene", gene]
    if args.all:
        strict_cmd.append("--all")
    if args.fail_on_warnings:
        strict_cmd.append("--fail-on-warnings")
    return run(strict_cmd)


if __name__ == "__main__":
    sys.exit(main())
