#!/usr/bin/env python3
"""Measure each class's Pair path against the REVISION_PLAN.md time budget.

Reads tools/core_paths.csv: one row per class (a class can have more than one
row when its Pair path draws on two notebooks). For every class it prints
the words and code cells in its Pair sections, the words of the whole
notebook (the student's required reading before class), and the required and
extra-credit question counts, and flags anything over the plan's limits.

Sections are the notebooks' own "## Section N:" headings, written S1, S2, ...
A section runs from its heading to the next "## " heading, so it includes the
interpretation text after its code cells. Words in <details> boxes are left
out, since the boxes are optional.

Until REVISION_PLAN.md step B is done, the CSV points at the current
notebooks with their current section numbers, so the counts are before the
cuts and the additions. Step B updates the CSV to the new files and numbers.

Usage:
    python tools/check_core.py            # table for every class
    python tools/check_core.py 19_1 22    # only classes starting with these
"""

import csv
import json
import pathlib
import re
import sys
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV = ROOT / "tools" / "core_paths.csv"

# Limits from REVISION_PLAN.md ("The 387 time budget").
MAX_PAIR_WORDS = 1300      # about the size of a 377 pair notebook
GUIDE_PAIR_CELLS = 7       # rough guide only; 387 cells are shorter
MAX_REQUIRED = 6           # 72 pair minutes at about 12 minutes a question


def words(text):
    text = re.sub(r"<details>.*?</details>", " ", text, flags=re.S)   # optional boxes
    text = re.sub(r"<[^>]+>", " ", text)                                 # leftover HTML
    return len(text.split())


def sections(path):
    """Map 'S1', 'S2', ... (and 'intro', 'summary', ...) to [words, code cells]."""
    cells = json.loads(path.read_text())["cells"]
    out = OrderedDict(intro=[0, 0])
    current = "intro"
    for cell in cells:
        src = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            for line in src.splitlines():
                m = re.match(r"^## (.*)", line)
                if m:
                    title = m.group(1).strip()
                    sec = re.match(r"Section (\d+)\b", title)
                    current = f"S{sec.group(1)}" if sec else title.lower()
                    out.setdefault(current, [0, 0])
                else:
                    out[current][0] += words(line)
        else:
            out[current][1] += 1
    return out


def main(filters):
    classes = OrderedDict()
    for row in csv.DictReader(CSV.open()):
        if filters and not any(row["class"].startswith(f) for f in filters):
            continue
        c = classes.setdefault(row["class"], {"parts": [], "required": "", "ec": ""})
        c["parts"].append(row)
        c["required"] = row["required"] or c["required"]
        c["ec"] = row["extra_credit"] or c["ec"]

    print(f"{'class':8} {'pair words':>10} {'pair cells':>10} {'reading':>8} {'req+EC':>7}  flags")
    problems = 0
    for name, c in classes.items():
        pw = pc = reading = 0
        flags, seen = [], set()
        for row in c["parts"]:
            path = ROOT / row["notebook"]
            if not path.exists():
                flags.append(f"missing {row['notebook']}")
                continue
            secs = sections(path)
            if row["notebook"] not in seen:          # count each notebook's reading once
                reading += sum(w for w, _ in secs.values())
                seen.add(row["notebook"])
            for s in row["pair_sections"].split():
                if s not in secs:
                    flags.append(f"no {s} in {path.name}")
                    continue
                pw += secs[s][0]
                pc += secs[s][1]
        if pw > MAX_PAIR_WORDS:
            flags.append(f"pair words over {MAX_PAIR_WORDS}")
        if pc > GUIDE_PAIR_CELLS:
            flags.append(f"cells over the guide of {GUIDE_PAIR_CELLS}")
        if c["required"] and int(c["required"]) > MAX_REQUIRED:
            flags.append(f"more than {MAX_REQUIRED} required")
        problems += any(f.startswith(("missing", "no ")) for f in flags)
        req = f"{c['required']}+{c['ec']}" if c["required"] else "?"
        print(f"{name:8} {pw:10,} {pc:10} {reading:8,} {req:>7}  {'; '.join(flags)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
