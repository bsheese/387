#!/usr/bin/env python3
"""One-off renumbering for REVISION_PLAN.md step B (2026-11-15).

Old 20_0_1 (Tensors) was merged into old 20_0_2 (Autograd) and deleted, so
  20_0_2 -> 20_0_1   and   20_0_3 -> 20_0_2.
Applies to every notebook (markdown, code and badge links) and to COURSE_MAP.md
and the TODO.md files. REVISION_PLAN.md, outlines and glossaries are left alone:
the plan names old and new numbers on purpose, and the outlines and glossaries
are rewritten in a later pass. Running it twice would renumber twice, so it is
kept only as a record. (The run on 2026-11-15 used an earlier version with a separate
file-name replacement that turned 20_0_3_Gradient_Descent into 20_0_1_; that was corrected by hand.)
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"\b20_0_([23])(?=\b|_)")
MAP = {"2": "1", "3": "2"}


def renumber(text):
    return PATTERN.sub(lambda m: "20_0_" + MAP[m.group(1)], text)


changed = []
for p in sorted(ROOT.rglob("*.ipynb")):
    if {"venv", "venv-colab", "extras", ".ipynb_checkpoints"} & set(p.relative_to(ROOT).parts):
        continue
    nb = json.loads(p.read_text())
    hit = False
    for c in nb["cells"]:
        old = "".join(c["source"])
        new = renumber(old)
        if new != old:
            c["source"] = new.splitlines(keepends=True)
            hit = True
    if hit:
        p.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
        changed.append(p.relative_to(ROOT))
for p in [ROOT / "COURSE_MAP.md", *sorted(ROOT.rglob("TODO.md"))]:
    if {"venv", "venv-colab", "extras"} & set(p.relative_to(ROOT).parts):
        continue
    old = p.read_text()
    new = renumber(old)
    if new != old:
        p.write_text(new)
        changed.append(p.relative_to(ROOT))
print("\n".join(str(c) for c in changed))
