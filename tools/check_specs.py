#!/usr/bin/env python3
"""Check that the spec map (specs/README.md) still matches the tree.

Two checks, both cheap and offline:

1. Every path in the "Files it maps" column of the spec table exists on disk,
   or is git-ignored (derived artefacts such as data/talks.db are not present
   in a fresh checkout). Brace sets and globs are expanded.
2. Every script in tools/ (*.py, *.sh) is named by at least one spec, so a
   new tool cannot go unmapped.

Exit 1 with one line per problem; exit 0 silently.
"""
import glob
import itertools
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = ROOT / "specs"


def brace_expand(pattern: str):
    m = re.search(r"\{([^{}]*)\}", pattern)
    if not m:
        return [pattern]
    head, tail = pattern[: m.start()], pattern[m.end() :]
    return list(
        itertools.chain.from_iterable(
            brace_expand(head + alt + tail) for alt in m.group(1).split(",")
        )
    )


def ignored(path: str) -> bool:
    r = subprocess.run(
        ["git", "check-ignore", "-q", path], cwd=ROOT, capture_output=True
    )
    return r.returncode == 0


def mapped_paths():
    text = (SPECS / "README.md").read_text()
    for line in text.splitlines():
        if not line.startswith("| [") or "](" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        for p in re.findall(r"`([^`]+)`", cells[2]):
            yield cells[0], p


def main() -> int:
    problems = []
    for spec, raw in mapped_paths():
        for pat in brace_expand(raw):
            if any(ch in pat for ch in "*?["):
                if glob.glob(str(ROOT / pat), recursive=True):
                    continue
            elif (ROOT / pat).exists() or ignored(pat):
                continue
            problems.append(f"{spec}: mapped path does not exist: {raw}")

    spec_text = "\n".join(p.read_text() for p in SPECS.glob("*.md"))
    for tool in sorted(itertools.chain((ROOT / "tools").glob("*.py"), (ROOT / "tools").glob("*.sh"))):
        if tool.name not in spec_text:
            problems.append(f"no spec names tools/{tool.name}")

    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
