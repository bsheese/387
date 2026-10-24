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
- [ ] **Fit content to 26 teaching days** (about 35 notebooks planned; about 1 notebook per class is realistic). Choose which notebooks become readings and which topics get cut. **Deferred for unit 21 ("later").** With no take-home work, "becomes a reading" means optional material or class time, not homework. Candidates:
  - [ ] Batch norm (21_1_2) moves to 22_0
  - [ ] Checkpointing (21_1_4) becomes a reading
  - [ ] Multiclass (21_0_2) becomes a short reading (softmax is already in 19_1_4)
  - [ ] LR schedules (21_1_3) folded into 21_1_5
- [x] 19_0 gets 2 days (decided 2026-10-24)
- [ ] Test DistilBERT fine-tuning and the diffusion demo on free Colab in December, before writing units 22–23

2. On-ramp design
- [x] **Teach the on-ramp through the week-1 image model** (decided 2026-10-24). The 377 notebooks are optional reference only. See the 19_1 TODO.
- [ ] Enrollment estimate: how many 377 graduates vs. CS 128 + CS/MATH 136 students? Mixed pairs and the on-ramp design depend on it.

3. Dataset for units 21–22
- [x] **Move to Fashion-MNIST** (decided 2026-10-24): 21_0_2 (multiclass) and all of 21_1 (regularization, MLP), so 22_0 swaps in a CNN on the same data. Tasks are in the 21_0 and 21_1 TODOs.
- [x] **Cut to 6 datasets** (decided 2026-10-24): Pets, penguins, breast cancer, Fashion-MNIST, IMDB, plus the XOR toy. Dropped: Titanic, CTG, wine, CIFAR-10, student photos, the student-chosen text set. The table is in `COURSE_MAP.md`.

4. Assessment
- [x] ~~Project weight~~: the project is cut (decided 2026-10-24). See "Grade weights without the project" above.
- [x] **Unit 19 exam:** keep as is, in class after unit 19 (decided 2026-10-24). Any head start for 377 graduates is acceptable; CS-route students often have their own advantages.
- [x] ~~Project proposal timing~~: no project.
- [x] ~~AI coding-assistant policy~~: not needed; there's no take-home work and exams are under lockdown (decided 2026-10-24).

5. Content gaps (find each a home)
- [ ] Logs and exponentials (before cross-entropy and softmax)
- [ ] Vectors and the dot product (before embeddings and attention)
- [ ] Matrix and tensor shapes as an explicit lesson (exams test it)
- [x] ~~Loading your own images for project track 1~~: no project. (`ImageFolder` may still be worth a cell in 22_1 if Pets is loaded from folders.)
- [ ] Debugging: shape and device errors, NaN loss, seeds, reading a stack trace
- [ ] Day-one Colab setup, with a CPU or saved-output fallback for the whole game (now in 19_0_1)
- [ ] Ethics: tie each unit's ethics item to a pair activity so it gets class time

6. Small fixes
- [ ] Nudge test: use a central difference `(f(x+h) - f(x-h)) / 2h` (20_0_2)
- [ ] Motivate backprop with cost: nudging every weight means about 11M forward passes for ResNet-18 (20_0_2 or 20_1)
- [ ] `PROPOSAL.md`: correct "about half the notebooks already exist" (about 13 exist, about 22 are new or trimmed) and the old unit numbers in the summary, or leave the snapshot as is

## Repo infrastructure (port from public/377)
- [ ] `requirements.txt` (torch, torchvision, transformers, datasets, scikit-learn, pandas, seaborn, matplotlib) pinned to the Colab versions of Jan 2027
- [ ] `smoke_test.py`: run every notebook in a temp dir (the 377 version). **Saved outputs are decided notebook by notebook**, so replace 377's "no outputs" check with an allowlist of notebooks that keep theirs.
- [ ] **Review outputs, notebook by notebook.** All 13 existing notebooks (20_*, 21_*) have saved outputs. Decide which keep them (long runs, results students should see first) and clear the rest.
- [ ] **Time every cell used in a pair activity** on free Colab (CPU and the free GPU). A cell that runs for anything like 30 minutes can't be in class: cut the data, the epochs or the model, or show a saved output. The smoke test could report the slowest cells.
- [ ] `venv/` locally (gitignored already)
- [ ] `data/` vendored datasets + raw-GitHub loading pattern (377 Maintenance Notes)
- [ ] Quiz site: `quizzes/*.md` + `quiz_site/build.py` + GitHub Pages workflow (`_site/` already gitignored)
- [ ] `README.md` for students (course description, how to open notebooks in Colab)
- [ ] `supplemental/` for pair-activity notebooks (377 convention); pair-activity sources go in `canvas/private/387_*` (instructor-only)
- [ ] Consider a `CLAUDE.md` for this repo (it's gitignored here too)

## Cross-cutting content
- [ ] **377 references.** The moved notebooks cite 377 notebooks that non-377 students have not seen (17_0_5, 18_1, 18_2_3, 18_5_x, 18_6). Point each one at its 19_1 on-ramp equivalent, or add a one-line recap. Per-file lists are in the 20_* and 21_* TODOs.
- [ ] **Sub-unit references.** The bare IDs `19_0`, `19_1` and `20_1` in outlines, glossaries and quizzes were not renumbered automatically, because the old 19_1 is now split across 20_1 and 21_0. Fix them by hand (`grep -rnE '\b(19_0|19_1|20_1)\b'`).
- [ ] "If you've taken calculus" collapsible-box convention: pick one HTML/markdown pattern and use it everywhere
- [ ] Glossary per module (377 convention); one course-wide glossary?
- [ ] Canvas: create `canvas/courses/387/terms/s27/` (doctor.py → dates.yaml, modules), one module per unit, 5 exams (units 19–22 in class; unit 23 in the final exam period), weekly pair-activity New Quizzes
- [ ] Syllabus: prereqs (377, or CS 128 C- + CS/MATH 136), weights (exams 80 = 5 × 16%, pairs 20, practice quizzes 0), free materials list
- [ ] Interactive companion decks in `interactive/` for nudge test, convolution, attention? (registry `sourceUnit` → 387 units)
