# 387 — repo-wide TODO

Target: first offering of the redesign in **Spring 2027** (Tuesday/Thursday, 70 min, same as 377). Exams: five, one after each unit; units 19–22 in class (one class day each), unit 23 in the final exam period. Weights: exams 80 (5 × 16%), pairs 20, practice quizzes 0. No final project (cut 2026-10-24). No take-home work (decided 2026-10-24): readings, videos and practice quizzes are optional.
Plan: `PROPOSAL.md`. Map: `COURSE_MAP.md`. Module-level tasks are in each module's `TODO.md`.

Note: `TODO.md` files are tracked in git (removed from `.gitignore` on 2026-10-24).

## Decide
- [x] **Grade weights** (decided 2026-10-24): exams 80 (5 × 16%), pair activities 20, practice quizzes 0.
- [ ] **Check the session budget against the Spring 2027 calendar** (break week, holidays, actual class-day count). Draft in `COURSE_MAP.md`: 26 teaching days + 4 in-class exam days; the unit 23 exam is in the final exam period. Unit 19 has 6 teaching days (19_0 gets 2), so unit 23 drops to 6.
- [x] Unit 23 exam: in the final exam period (decided 2026-10-24); unit 23 gets 7 teaching days.
- [ ] Proposal says "Units 21–24 need to be written". With the project cut and Fashion-MNIST moved, the writing list is: 19_0, 19_1 (trim + dataset swaps), 21_0_2 and 21_1 (move to Fashion-MNIST), 22, 23, plus the 20_0 math rewrite. Confirm.
- [ ] Ungraded practice quizzes (0%): keep the per-module `*_practice_quiz.ipynb` + quiz site, or quiz site only? (The three existing quiz notebooks are 16-word stubs.)

## Decide (from PLAN_CRITIQUE.md)
Suggested order: schedule (1, 3) → on-ramp (2) → the rest.

1. Schedule and scope
- [ ] **Fit content to 26 teaching days** (about 35 notebooks planned; about 1 notebook per class is realistic). Choose which notebooks become readings and which topics get cut. **Unit 21 decided 2026-10-25: 3 notebooks in 3 days (see below); the freed day went to unit 23.** With no take-home work, "becomes a reading" means optional material or class time, not homework. Candidates:
  - [x] Batch norm moves to 22_0 (21_1_1 explains only its train/eval behavior)
  - [x] Checkpointing: folded into 21_1_2 (early stopping with a checkpoint)
  - [x] Multiclass: folded into 21_0_1 (Fashion-MNIST is 10-class from the start)
  - [x] LR schedules: one cosine section in 21_1_2
  - [x] Exercises 21_0_9 and 21_1_9 cut (no take-home work; their job goes to pair activities)
  - [x] Breast cancer dropped from the course (5 datasets + XOR)
- [x] 19_0 gets 2 days (decided 2026-10-24)
- [ ] Test DistilBERT fine-tuning and the diffusion demo on free Colab in December, before writing units 22–23
  - `tools/colab_check.ipynb` (built by `tools/make_colab_check.py`, 2026-10-25) does this: Colab versions, every course notebook through `smoke_test.py --remote-data`, DDPM CIFAR-10 / BK-SDM-Small / SD 1.5, DistilBERT on 2,000 IMDB reviews, the SST-2 pipeline, GPT-2. Run once on a T4 GPU and once on CPU; paste back the last cell. Repeat on the GPU in January 2027.
  - [x] **T4 GPU run (2026-10-27):** all 20 course notebooks passed (603 s total; slowest cells 31–38 s: the 20_0_2 timing demo, the 22_1_1 Pets transforms, the 23_0_2 sentence-transformer download). DDPM CIFAR-10: 50 DDIM steps 2.1 s, 1,000 DDPM steps 29.8 s (4 images). BK-SDM-Small: load 53 s, 3.1 s per image, 2.7 GB. SD 1.5: load 128 s, 4.6 s per image, 3.4 GB. DistilBERT, 2,000 IMDB reviews, one epoch: 41 s, 86.3% on 1,000 test reviews. SST-2 pipeline with no training: 87.6% on 500 reviews in 14 s. GPT-2: 5 samples of 50 tokens in 0.7 s. Colab versions: Python 3.13, torch 2.11, numpy 2.1, pandas 2.2, scikit-learn 1.6, transformers 5.20, diffusers 0.42.
  - [ ] CPU run (Runtime → Change runtime type → CPU), to size things for a pair that doesn't get a GPU

2. On-ramp design
- [x] **Teach the on-ramp through the week-1 image model** (decided 2026-10-24). The 377 notebooks are optional reference only. See the 19_1 TODO.
- [ ] Enrollment estimate: how many 377 graduates vs. CS 128 + CS/MATH 136 students? Mixed pairs and the on-ramp design depend on it.

3. Dataset for units 21–22
- [x] **Move to Fashion-MNIST** (decided 2026-10-24): 21_0_2 (multiclass) and all of 21_1 (regularization, MLP), so 22_0 swaps in a CNN on the same data. Tasks are in the 21_0 and 21_1 TODOs.
- [x] **Cut to 6 datasets** (decided 2026-10-24), then 5 (breast cancer dropped 2026-10-25): Pets, penguins, Fashion-MNIST, IMDB, plus the XOR toy. Dropped: Titanic, CTG, wine, CIFAR-10, student photos, the student-chosen text set. The table is in `COURSE_MAP.md`.

4. Assessment
- [x] ~~Project weight~~: the project is cut (decided 2026-10-24). See "Grade weights without the project" above.
- [x] **Unit 19 exam:** keep as is, in class after unit 19 (decided 2026-10-24). Any head start for 377 graduates is acceptable; CS-route students often have their own advantages.
- [x] ~~Project proposal timing~~: no project.
- [x] ~~AI coding-assistant policy~~: not needed; there's no take-home work and exams are under lockdown (decided 2026-10-24).

5. Content gaps (find each a home)
- [x] Logs and exponentials (before cross-entropy and softmax): $e^x$ in 19_1_3 (sigmoid) and 19_1_4 (softmax); the natural log in 19_1_4 (cross-entropy loss)
- [x] Vectors and the dot product (before embeddings and attention): 19_1_3 Section 1
- [x] Matrix and tensor shapes as an explicit lesson (exams test it): 19_1_3 Section 4 (the shape rule, transpose, broadcasting, the shape error); revisit for tensors in 20_0_1
- [x] ~~Loading your own images for project track 1~~: no project. (`ImageFolder` may still be worth a cell in 22_1 if Pets is loaded from folders.)
- [ ] Debugging: shape and device errors, NaN loss, seeds, reading a stack trace
- [x] Day-one Colab setup, with a CPU or saved-output fallback for the whole game (in 19_0_1, drafted 2026-10-25; still to be timed in Colab)
- [ ] Ethics: tie each unit's ethics item to a pair activity so it gets class time

6. Small fixes
- [x] Nudge test: use a central difference `(f(x+h) - f(x-h)) / 2h` (20_0_2)
- [x] Motivate backprop with cost: nudging every weight means about 11M forward passes for ResNet-18 (20_0_2 Section 4, with a timing demo)
- [ ] `PROPOSAL.md`: correct "about half the notebooks already exist" (about 13 exist, about 22 are new or trimmed) and the old unit numbers in the summary, or leave the snapshot as is

## Repo infrastructure (port from public/377)
- [x] `requirements.txt` (2026-10-25): pinned to the local venv used for the 19_0 outputs
- [ ] Re-pin `requirements.txt` to the Colab versions of Jan 2027 (in Oct 2026 the local venv was well ahead of Colab: pandas 3.1 vs 2.2, numpy 2.5 vs 2.1, torch 2.14 vs 2.11, scikit-learn 1.9 vs 1.6; the notebooks still pass on Colab, but saved outputs made with pandas 3 may print differently), and add transformers + datasets when unit 23 needs them
- [x] `smoke_test.py` (2026-10-25): the 377 version plus a `KEEP_OUTPUTS` allowlist, `--check-only`, copying `data/` into each run (or `--remote-data`), and a report of cells slower than `--slow` seconds. The 13 old notebooks are in a temporary `NOT_YET_REVIEWED` list.
- [ ] **Review outputs, notebook by notebook.** All 13 existing notebooks (20_*, 21_*) have saved outputs. Decide which keep them (long runs, results students should see first) and clear the rest. Then move each one from `NOT_YET_REVIEWED` in `smoke_test.py` to `KEEP_OUTPUTS`, or delete it from the list.
- [ ] **Time every cell used in a pair activity** on free Colab (CPU and the free GPU). A cell that runs for anything like 30 minutes can't be in class: cut the data, the epochs or the model, or show a saved output. `python smoke_test.py --slow 30` reports slow cells (local times, so Colab will be slower).
- [x] `venv/` locally (gitignored already; created 2026-10-25 from `requirements.txt`)
- [x] `data/` + raw-GitHub loading (2026-10-25): notebooks use a `fetch()` helper that downloads from `bsheese/387/main/data/` unless the file is already present. `data/README.md` lists the files and how they were made. Penguins, breast cancer, Fashion-MNIST and IMDB still to add when their units are rebuilt.
- [ ] Quiz site: `quizzes/*.md` + `quiz_site/build.py` + GitHub Pages workflow (`_site/` already gitignored)
- [ ] `README.md` for students (course description, how to open notebooks in Colab)
- [ ] `supplemental/` for pair-activity notebooks (377 convention); pair-activity sources go in `canvas/private/387_*` (instructor-only)
- [ ] Consider a `CLAUDE.md` for this repo (it's gitignored here too)

## Cross-cutting content
- [ ] **377 references.** The moved notebooks cite 377 notebooks that non-377 students have not seen (17_0_5, 18_1, 18_2_3, 18_5_x, 18_6). Point each one at its 19_1 on-ramp equivalent, or add a one-line recap. Per-file lists are in the 20_* and 21_* TODOs.
- [ ] **Sub-unit references.** The bare IDs `19_0`, `19_1` and `20_1` in outlines, glossaries and quizzes were not renumbered automatically, because the old 19_1 is now split across 20_1 and 21_0. Fix them by hand (`grep -rnE '\b(19_0|19_1|20_1)\b'`).
- [x] "If you've taken calculus" collapsible-box convention: `<details><summary><b>If you've taken calculus</b></summary> ... </details>` (first used in 20_0_2)
- [ ] Glossary per module (377 convention); one course-wide glossary?
- [ ] Canvas: create `canvas/courses/387/terms/s27/` (doctor.py → dates.yaml, modules), one module per unit, 5 exams (units 19–22 in class; unit 23 in the final exam period), weekly pair-activity New Quizzes
- [ ] Syllabus: prereqs (377, or CS 128 C- + CS/MATH 136), weights (exams 80 = 5 × 16%, pairs 20, practice quizzes 0), free materials list
- [ ] Interactive companion decks in `interactive/` for nudge test, convolution, attention? (registry `sourceUnit` → 387 units)
