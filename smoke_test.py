#!/usr/bin/env python3
"""Execute every teaching notebook and report failures and slow cells.

Adapted from cs377's smoke_test.py. Two differences:

1. Saved outputs. 377 commits every notebook without outputs. In 387 that is
   decided notebook by notebook: notebooks whose results students should see
   before running anything (or whose runs are too long for class) keep their
   outputs. Those are listed in KEEP_OUTPUTS below. Every other notebook must
   be committed without outputs, and this script checks that statically
   before running anything.

2. Data. The notebooks download files from the course repo on GitHub with a
   fetch() helper that skips the download if the file is already in the
   working directory. By default this script copies data/ into each
   notebook's temp directory, so it tests the files as they are on disk,
   including ones not pushed yet. Use --remote-data to make the notebooks
   download from GitHub instead, which checks that the pushed copies are there.

Each notebook is copied into its own temp subdirectory and executed there,
so committed outputs stay untouched and files the notebooks write (saved
models, CSVs) don't leak into the source tree.

Usage:
    python smoke_test.py                  # check outputs, then run everything
    python smoke_test.py 19_0 21_1        # only paths containing a pattern
    python smoke_test.py --list           # show what would run, don't run
    python smoke_test.py --check-only     # only the saved-output check
    python smoke_test.py --slow 30        # report cells slower than 30 s (default 60)
    python smoke_test.py --timeout 900    # per-notebook timeout in seconds

Cell times are measured on this machine. A cell that is slow here will be
slower on free Colab's CPU, and in-class cells can't take long (see TODO.md).

Exit status is non-zero if any notebook fails, times out, or has saved
outputs without being listed in KEEP_OUTPUTS.
"""

import argparse
import datetime
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parent
VENV_DIR = ROOT / "venv"
DATA_DIR = ROOT / "data"

# tools/ holds colab_check.ipynb, which runs this script itself.
EXCLUDE_DIR_PARTS = {"venv", ".ipynb_checkpoints", "old", "old_material", "_site", ".ignore", "tools"}

# Notebooks that are committed with their outputs (paths relative to the repo root).
KEEP_OUTPUTS = {
    # 19_0: the saved outputs are the CPU fallback for day one, and 19_1 refers to the same numbers.
    "19_onramp/19_0_Whole_Game/19_0_1_Your_First_Image_Model.ipynb",
    "19_onramp/19_0_Whole_Game/19_0_2_What_Just_Happened.ipynb",
    # 22: several minutes of training each on a CPU; students read the results before running.
    "22_images/22_0_Convolution_and_CNNs/22_0_2_First_CNN.ipynb",
    "22_images/22_1_Transfer_Learning/22_1_1_Transfer_Learning.ipynb",
    "22_images/22_1_Transfer_Learning/22_1_2_What_CNNs_Get_Wrong.ipynb",
}

# Moved from the old 387 with outputs and not yet reviewed (TODO.md, "Review outputs,
# notebook by notebook"). Each one either moves to KEEP_OUTPUTS or gets cleared.
NOT_YET_REVIEWED = set()   # all reviewed as of 2026-10-25


def venv_warning():
    """None if running from ./venv; otherwise a banner to print.

    Jupyter picks a kernel via sys.prefix, which is set by which python ran
    this script, not by whether `source venv/bin/activate` was typed. If this
    process isn't running with ./venv's prefix, notebooks execute against
    whatever kernel is registered elsewhere on the machine, and failures from
    that mismatch look exactly like real notebook bugs.
    """
    try:
        running = pathlib.Path(sys.prefix).resolve()
        expected = VENV_DIR.resolve()
    except OSError:
        return None
    if running == expected:
        return None
    return (
        "\n"
        "############################################################\n"
        "#  WARNING: not running from this project's venv.\n"
        f"#  Expected prefix: {expected}\n"
        f"#  Actual prefix:   {running}\n"
        "#  Run `source venv/bin/activate` first. Otherwise notebooks\n"
        "#  execute against whatever Jupyter kernel is registered\n"
        "#  elsewhere, and failures below may be environment artifacts,\n"
        "#  not real bugs.\n"
        "############################################################\n"
    )


def collect(patterns):
    nbs = []
    for p in sorted(ROOT.rglob("*.ipynb")):
        rel = p.relative_to(ROOT)
        if EXCLUDE_DIR_PARTS & set(rel.parts):
            continue
        if "practice_quiz" in p.name:
            continue
        if patterns and not any(pat in str(rel) for pat in patterns):
            continue
        nbs.append(rel)
    return nbs


def has_outputs(path):
    nb = json.loads(path.read_text())
    return any(c.get("outputs") for c in nb["cells"] if c["cell_type"] == "code")


def check_outputs(nbs):
    """Notebooks with saved outputs that aren't allowed to have them."""
    allowed = KEEP_OUTPUTS | NOT_YET_REVIEWED
    return [nb for nb in nbs if nb.as_posix() not in allowed and has_outputs(ROOT / nb)]


def slow_cells(executed_path, threshold):
    """(cell number, seconds, first line) for each code cell slower than threshold."""
    nb = json.loads(executed_path.read_text())
    slow = []
    for i, cell in enumerate(nb["cells"]):
        timing = cell.get("metadata", {}).get("execution", {})
        if cell["cell_type"] != "code" or "iopub.execute_input" not in timing:
            continue
        start = datetime.datetime.fromisoformat(timing["iopub.execute_input"].replace("Z", "+00:00"))
        end = datetime.datetime.fromisoformat(timing["shell.execute_reply"].replace("Z", "+00:00"))
        seconds = (end - start).total_seconds()
        if seconds > threshold:
            source = "".join(cell["source"]).strip().splitlines()
            slow.append((i, seconds, source[0] if source else ""))
    return slow


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("patterns", nargs="*", help="only run notebooks whose path contains one of these substrings")
    ap.add_argument("--list", action="store_true", help="list notebooks that would run, then exit")
    ap.add_argument("--check-only", action="store_true", help="only check saved outputs; don't execute")
    ap.add_argument("--remote-data", action="store_true", help="don't copy data/; notebooks download from GitHub")
    ap.add_argument("--slow", type=float, default=60, help="report cells slower than this many seconds (default 60)")
    ap.add_argument("--timeout", type=int, default=2400, help="per-notebook timeout in seconds (default 2400)")
    args = ap.parse_args()

    nbs = collect(args.patterns)
    if not nbs:
        print("No notebooks matched.")
        return 1
    if args.list:
        for nb in nbs:
            marker = "  (keeps outputs)" if nb.as_posix() in KEEP_OUTPUTS else ""
            print(f"{nb}{marker}")
        print(f"\n{len(nbs)} notebooks")
        return 0

    bad_outputs = check_outputs(nbs)
    for nb in bad_outputs:
        print(f"HAS OUTPUTS: {nb}  (clear them, or add it to KEEP_OUTPUTS)")
    if args.check_only:
        print("Saved-output check:", "FAILED" if bad_outputs else "ok")
        return 1 if bad_outputs else 0

    warning = venv_warning()
    if warning:
        print(warning)

    failures, slow_report = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for i, nb in enumerate(nbs, 1):
            print(f"[{i}/{len(nbs)}] {nb} ... ", end="", flush=True)
            start = time.time()
            work_dir = pathlib.Path(tmp) / str(nb).replace("/", "__")
            work_dir.mkdir()
            nb_copy = work_dir / nb.name
            shutil.copy(ROOT / nb, nb_copy)
            if not args.remote_data and DATA_DIR.is_dir():
                for f in DATA_DIR.iterdir():
                    if f.is_file() and f.suffix != ".py":
                        shutil.copy(f, work_dir / f.name)
            try:
                proc = subprocess.run(
                    [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook",
                     "--execute", str(nb_copy), "--output-dir", str(work_dir),
                     "--ExecutePreprocessor.timeout", str(args.timeout)],
                    capture_output=True, text=True, timeout=args.timeout + 60,
                )
                ok = proc.returncode == 0
                err = proc.stderr
            except subprocess.TimeoutExpired:
                ok, err = False, f"hard timeout after {args.timeout}s"
            elapsed = time.time() - start
            if ok:
                print(f"ok ({elapsed:.0f}s)")
                for cell, seconds, first_line in slow_cells(nb_copy, args.slow):
                    slow_report.append((nb, cell, seconds, first_line))
            else:
                print(f"FAIL ({elapsed:.0f}s)")
                # keep the last relevant traceback lines for the summary
                tail = "\n".join(line for line in err.splitlines() if line.strip())[-2000:]
                failures.append((nb, tail))

    print(f"\n{len(nbs) - len(failures)}/{len(nbs)} notebooks passed.")
    if slow_report:
        print(f"\nCells slower than {args.slow:g} s:")
        for nb, cell, seconds, first_line in slow_report:
            print(f"  {seconds:6.0f} s  {nb} cell {cell}: {first_line[:60]}")
    for nb, tail in failures:
        print(f"\n=== FAILED: {nb} ===\n{tail}")
    if bad_outputs:
        print(f"\n{len(bad_outputs)} notebook(s) have saved outputs but aren't in KEEP_OUTPUTS (listed at the top).")
    if failures and warning:
        print(warning)
    return 1 if failures or bad_outputs else 0


if __name__ == "__main__":
    sys.exit(main())
