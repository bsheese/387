# 387 Revision Plan (version 7)

Plan for revising the 387 notebooks before and during Spring 2027. This version replaces version 6 (2026-11-15). The reviews behind it are `CONTENT_CRITIQUE.md` and `REVISION_PLAN_critique.md`. Nothing in this plan has been carried out.

## What changed in this version

Version 7 (2026-11-15):

- **The Spring 2027 calendar is checked.** 387 meets Tuesday and Thursday, 9:25 to 10:40 (75 minutes). The term has 28 class meetings, not the 30 the earlier versions assumed: classes begin Wednesday, Jan 6; spring recess removes Mar 9 and Mar 11; the last class meeting is Tuesday, Apr 20; final exams run Apr 23 to 28. To fit 28 meetings, the course keeps one review day instead of three, placed before the unit 22 exam (option 1, decided). Dates are now in the course table and the load table.
- **Classes are 75 minutes, not 70.** The Fall 2026 377 activities also ran in a 75-minute window, so the 377 figures carry over directly, and the default rises to 6 required questions from unit 20 on.

Version 6 (2026-11-15):

- **The interactive demos will be a fresh app, built much later.** It will be a new app, not more decks in `interactive/`, which crams too much into each deck. Until the new app exists, each class's demo is a Canvas walkthrough page that has students run and change named cells in the notebook in Colab, or use one of the three browser explainers. Each app screen replaces a walkthrough's Colab steps as it is built.
- **Canvas page naming follows the 125 convention** (E5, decided).
- **The Pets course copy is frozen** (E3, decided).

Version 5 (2026-11-15):

- **The demonstration moves out of class.** Before each class, students do a required interactive demo, and a Canvas walkthrough page tells them what to do with it. Class time is now the reading check and the pair activity. The demos may later become animations, but that is not part of this plan.
- **The reading check covers the demo as well as the notebook.** The reading checks will still be written later.
- **What the exam covers.** The exam can ask about anything assigned (the notebook, the demo and the pair activity), and it assumes students did the activities. But everything it tests is material in the core notebooks.
- **No new material in demos or activities.** Demos and activities may only present, practise or illustrate what the notebook already contains.
- **The Demo and Pair roles are replaced.** "Demo" is now the pre-class demo. "Pair sections" remain, as the part of the notebook each activity works in, but they are recorded only in this plan and in the activity's instructions, not in the notebooks.

Earlier decisions that still stand:

- The course is cut to a basic introduction to deep learning (version 3).
- 22_2 moves to `extras/`.
- The notebooks are renumbered with no gaps.
- Each class notebook is required reading before class, and nothing graded is done outside class.
- The review day is yours to plan.
- Seaborn conversion is postponed.
- There is no student timing test; the time budget comes from the 377 data.

Outlines, glossaries, the quiz site, the syllabus, the reading checks and the Canvas course shell are out of scope. The walkthrough pages and demos are in scope.

## How long a pair activity takes: the 377 data

The Canvas student-analysis reports for the Fall 2026 377 pair activities are in `canvas/grading/` and `canvas/courses/377/terms/f26/grading/`. For each submission they record the time from opening the quiz to submitting it, and every answer, so it is possible to see how far each pair got. Only aggregate figures are used here.

The four activities most like what 387 will run shared the same shape: a reading check on the day's reading, a pair notebook, and 8 questions tied to notebook cells, with Q1 to Q6 required and Q7 to Q8 extra credit.

| Activity (date) | Pairs | Minutes from opening to submitting (median, range) | Pairs that finished Q1 to Q6 | Median last question answered |
|---|---|---|---|---|
| Nested CV (10-27) | 5 | 70 (67 to 72) | 4 of 5 | 6 |
| Thresholds (11-05) | 6 | 73 (68 to 76) | 6 of 6 | 7 |
| Rare fraud (11-10) | 6 | 71 (68 to 76) | 5 of 6 | 6 |
| Telco churn (11-12) | 9 | 66 (62 to 73) | 6 of 9 | 6 |
| All four | 26 | about 70 | 21 of 26 (81%) | 6 |

What these figures say:

- **Pairs worked until the quiz closed.** Almost every submission came between 62 and 76 minutes after opening, which runs to the end of class plus the 5-minute lock.
- **About four pairs in five finished the 6 required questions.** The typical pair answered 6 questions, and only 7 of 26 pairs reached the last extra-credit question.
- **That is about 12 minutes of pair time per required question** for four in five pairs to finish. The figure covers reading the prompt and the notebook text it points to, running cells, talking it over and typing the answer.
- **Prompt and notebook sizes.** The prompts ran from about 130 to 185 words each. The pair notebooks were 1,200 to 1,600 words with 6 or 7 code cells, counted in the solution versions, which include the answer text.

The two 16-question activities show what happens with more questions. In Ridge and Lasso, the median last question was 9, and two pairs stopped at Q4. In Selection code reading, which had shorter questions, the median was 7 or 8. Beyond Accuracy (11-03) is left out, because its deadline was extended and its first question was known to be too slow.

**Limits of the comparison.**

- The samples are small: 26 pairs.
- The 377 class window was the same 75 minutes as 387's (the activities unlocked at class start and were due 75 minutes later), with a reading check at the start, so the time per question carries over without adjustment.
- 377 students were further along than many 387 students will be.
- The 377 questions came from separate pair notebooks; the 387 questions will come from the course notebook itself.

The first classes of the term will confirm or correct the figure (see Checks).

## The 387 time budget

A 75-minute class (Tuesday and Thursday, 9:25 to 10:40) has two parts:

| Part | Minutes |
|---|---|
| Reading check, on paper, handed out as class starts | 3 |
| Pair activity, including opening the notebook and submitting | 72 |

At 12 minutes per question, 72 minutes allows 6 required questions, which is exactly what four in five 377 pairs finished in the same window. The plan uses:

- **Unit 19: 5 required and 2 extra credit.** These are the first weeks of a new format, and many students are new to machine learning, so unit 19 keeps about 12 minutes of margin.
- **Units 20 to 23: 6 required and 2 extra credit by default,** confirmed or reduced to 5 by the measurement of the first six classes (see Checks).
- **The first class: 3 required and 2 extra credit.** It has no reading check and no pre-class demo, because nothing can be assigned before it, and it includes the course introduction and Colab setup. Its Pair path is also the largest in the course (1,910 words after trims), all of it read in class.

Two further limits come from the 377 activities:

- Question prompts of about 150 words or less.
- A Pair path no larger than a 377 pair notebook, about 1,300 words and 7 code cells. The 387 cells are shorter than the 377 pair-notebook cells, so the cell count is a rough guide only.

Before each class, a student reads the whole notebook and does the demo. After the cuts, a notebook is about 1,500 to 2,500 words, and a demo is planned at 10 to 15 minutes. That is about 30 to 45 minutes of preparation for each class, twice a week.

## Rules for what is assigned and tested

1. **The core notebooks are where all course material lives.** Anything the exam tests is in a notebook that was assigned.
2. **Demos, walkthrough pages and activities add no new material.** They introduce no new concepts, terms or methods. Every idea in a demo or an activity question must appear in the notebook it accompanies or an earlier one. A number a demo quotes in its text must match the notebook. A number a student produces by moving a slider doesn't have to. If a demo or activity needs something the notebook lacks, either the notebook gets it or the demo drops it.
3. **The exam can ask about anything assigned** and assume the activities were done. For example, it can ask about a result students produced in an activity, provided the idea behind it is in the notebook.
4. **The browser explainers** (TensorFlow Playground, CNN Explainer, Transformer Explainer) show more than the notebooks teach. Their walkthrough pages send students only to the features the notebook covers, and anything else the tool shows is not tested. The details are under step C.
5. **The text-to-image demonstration planned for class 18 is dropped.** It would introduce diffusion, which is no longer in a core notebook. The 22_2 notebooks stay in `extras/` as optional, unassessed reading.

## The course after the cuts

Every class meeting, with its date. Meetings 1 to 17 come before spring recess and 18 to 28 after it.

| Unit | Meeting | Date | Notebook (new numbering) or event | Pre-class demo | Comes from |
|---|---|---|---|---|---|
| 19 | 1 | Thu Jan 7 | 19_0_1 Your First Image Model | none (first day) | unchanged |
| | 2 | Tue Jan 12 | 19_0_2 What Just Happened | Colab walkthrough (19_0) | unchanged |
| | 3 | Thu Jan 14 | 19_1_1 Is It Any Good | Colab walkthrough (19_1, part 1) | trimmed |
| | 4 | Tue Jan 19 | 19_1_2 Confusion Matrix | Colab walkthrough (19_1, part 2) | trimmed |
| | 5 | Thu Jan 21 | 19_1_3 One Neuron | Colab walkthrough (19_1, part 3) | unchanged |
| | 6 | Tue Jan 26 | 19_1_4 Softmax and the Loss | Colab walkthrough (19_1, part 4) | first half of old 19_1_4 |
| | 7 | Thu Jan 28 | 19_1_5 What One Neuron Can't Do | Colab walkthrough (19_1, part 5) | second half of old 19_1_4 |
| | 8 | Tue Feb 2 | Unit 19 exam | | |
| 20 | 9 | Thu Feb 4 | 20_0_1 The Nudge Test and Autograd | Colab walkthrough (20_0, part 1) | old 20_0_2, plus tensor basics from old 20_0_1 |
| | 10 | Tue Feb 9 | 20_0_2 Gradient Descent | Colab walkthrough (20_0, part 2) | old 20_0_3 |
| | 11 | Thu Feb 11 | 20_1_1 Building a Network | TensorFlow Playground | trimmed |
| | 12 | Tue Feb 16 | Unit 20 exam | | |
| 21 | 13 | Thu Feb 18 | 21_0_1 The Training Loop | Colab walkthrough (21_0) | trimmed |
| | 14 | Tue Feb 23 | 21_1_1 Overfitting | Colab walkthrough (21_1) | old 21_1_1 plus early stopping from old 21_1_2 |
| | 15 | Thu Feb 25 | Unit 21 exam | | |
| 22 | 16 | Tue Mar 2 | 22_0_1 Convolution by Hand | CNN Explainer | trimmed |
| | 17 | Thu Mar 4 | 22_0_2 A Convolutional Network | Colab walkthrough (22_0) | trimmed |
| | | Mar 5 to 15 | Spring recess | | |
| | 18 | Tue Mar 16 | 22_1_1 Transfer Learning | Colab walkthrough (22_1, part 1) | trimmed |
| | 19 | Thu Mar 18 | 22_1_2 What Image Models Get Wrong | Colab walkthrough (22_1, part 2) | trimmed |
| | 20 | Tue Mar 23 | Review | yours | new |
| | 21 | Thu Mar 25 | Unit 22 exam | | |
| 23 | 22 | Tue Mar 30 | 23_0_1 Tokens | Colab walkthrough (23_0, part 1) | trimmed, with a new opening |
| | 23 | Thu Apr 1 | 23_0_2 Embeddings | Colab walkthrough (23_0, part 2) | trimmed |
| | 24 | Tue Apr 6 | 23_1_1 Attention | Transformer Explainer | trimmed |
| | 25 | Thu Apr 8 | 23_2_1 Using Pretrained Models | Colab walkthrough (23_2, part 1) | trimmed |
| | 26 | Tue Apr 13 | 23_2_2 Fine-Tuning DistilBERT | Colab walkthrough (23_2, part 2) | trimmed |
| | 27 | Thu Apr 15 | 23_3_1 Generating Text | Colab walkthrough (23_3, part 1) | trimmed |
| | 28 | Tue Apr 20 | 23_3_2 What Language Models Get Wrong | Colab walkthrough (23_3, part 2) | trimmed |
| | | Apr 23 to 28 | Unit 23 exam, in its final-exam slot (to be confirmed from the registrar's spring exam schedule) | | |

That is 23 notebook days, 1 review day and 4 in-class exams, which fills the 28 meetings. `COURSE_MAP.md`'s session budget (26 teaching days and 4 exams) is updated in step B.

Notes on the layout:

- Spring recess falls inside unit 22, between 22_0_2 and 22_1_1. The review day comes after the break, just before the unit 22 exam.
- Units 20 and 21 have no review day, so their exams follow straight after their last notebook.
- Activity times for Canvas (unlock at class start, due at class end, lock 5 minutes later) are 15:25 to 16:40 UTC through Mar 11, and 14:25 to 15:40 UTC from Mar 16, after daylight saving time starts on Mar 14.

There are 22 pre-class demos. Three are walkthroughs of existing browser explainers (TensorFlow Playground, CNN Explainer and Transformer Explainer). The other 19 are, for now, Colab walkthroughs: the Canvas page has students run and change specific cells of the notebook they have just read. They become screens of the new demo app when it is built. The "Pre-class demo" column names the module each demo belongs to, which is how the new app might group them; that grouping is for the app's design to settle.

## What is cut

### Whole notebooks

| Notebook | What happens to it |
|---|---|
| 22_2_1, 22_2_2 | Moved, unchanged, to a new `extras/` folder. Each gets a note at the top saying it is optional and unassessed. 22_1_2's "What's next" mentions them. |
| 20_0_1 Tensors | Deleted after its essentials are merged into the new 20_0_1. |
| 21_1_2 Training a Model Well | Deleted after early stopping and the checklist are merged into 21_1_1. |

### Topics, notebook by notebook (old numbering)

| Notebook | Cut | Keep |
|---|---|---|
| 19_1_1 | Section 5's 30-versions experiment; Baseline 3 (species then guess) | Baselines 1 and 2, the memorizer, overfitting from training too long. The three-way split is stated as a rule with a short explanation (about 150 words, no code). |
| 19_1_2 | Section 4 (thresholds and costs) | The confusion matrix, precision and recall, the accuracy paradox |
| 19_1_4 | "Sigmoid is softmax with two classes" | Softmax, the loss as surprise, XOR and the hidden layer, now split over two classes |
| 20_0_2 | The nudge-versus-autograd timing cell. Section 4 becomes one paragraph with the ResNet-18 arithmetic. | The nudge test, autograd, rates multiply, zeroing gradients, `no_grad`. Add about 300 words and 3 cells of tensor basics from 20_0_1: making a tensor, `.shape`, the batch dimension, `.item()`, `requires_grad`. |
| 20_1_1 | Section 5 (slope check on a hidden weight), Section 6 (20 seeds), the ResNet-18 tour in Section 7 | `nn.Linear`, `nn.Module`, ReLU, XORNet, `nn.Sequential`. Add a passage on classes and a short procedure for counting parameters. |
| 21_0_1 | Section 5 (Adam against SGD) | Everything else. Adam is used without the comparison. |
| 21_1_1 and 21_1_2, merged | Weight decay, the learning-rate schedule, checkpoint files, the batch-norm paragraph in Section 3 (one sentence remains) | Overfitting on 1,000 images, dropout, `train()` and `eval()`, more data, early stopping as keeping the weights from the best epoch, a shortened checklist |
| 22_0_1 | Stride and the output-size formula | Filters, `nn.Conv2d`, channels, padding, pooling, why convolution needs few weights |
| 22_0_2 | Batch normalization (Section 5, and its layers in the CNN); the AdamW and cosine recipe, replaced by Adam and the best epoch; the augmentation training run (augmentation becomes a paragraph) | The CNN, the per-class comparison with the MLP, the learned filters, the shift test |
| 22_1_1 | Residual connections (one sentence remains); the layer4 feature maps | ResNet's shape path, first-layer filters, training from scratch, feature extraction against fine-tuning, choosing an approach. One sentence on batch norm, where ResNet and the scratch CNN use it. |
| 22_1_2 | Section 3 (adversarial examples); batch norm in its small CNN | Shortcuts, distribution shift, Gender Shades |
| 23_0_1 | nothing | Add a black-box opening that runs the sentiment and fill-mask pipelines |
| 23_0_2 | The PCA picture | Embedding tables, cosine similarity, neighbors, "bank" in context, review search |
| 23_1_1 | Queries, keys and values as matrices; the √d scaling; masks (Section 4); position embeddings (Section 5); the anatomy of a transformer layer | Attention as a weighted average by similarity (Sections 1 and 2); a paragraph saying that real models learn what to compare; the cost of long texts; the "it" experiment |
| 23_2_1 | Section 5 (zero-shot classification) | The pipeline, what it does, the model card and the country bias, fill-mask |
| 23_2_2 | Students no longer run the fine-tuning loop. The cell stays as instructor-run reference, and its test-set probabilities are saved to a small file in `data/` so the comparison and the mistakes run live on a CPU. | The TF-IDF baseline, the new head, the comparison, reading the mistakes |
| 23_3_1 | Top-p sampling (one sentence remains) | Next-token probabilities, the loss and perplexity (one paragraph), greedy decoding, temperature, top-k. Add two sentences naming self-supervised learning, and one on the causal mask, since 23_1_1 no longer teaches masks. |
| 23_3_2 | Section 5 (contamination) and its bullet in Section 6 | Chat templates, what it gets right, hallucination, strawberry, the form of the question |

Cut material is deleted from the notebooks. It stays in git history, and 22_2 stays in `extras/`.

These are no longer exam topics: thresholds and costs, weight decay, learning-rate schedules, optimizer comparison, checkpoints, batch normalization, stride and output-size arithmetic, residual connections, adversarial examples, queries, keys and values, masks, position embeddings, √d, zero-shot classification, autoencoders, diffusion and contamination. Under rule 2, demos and activities can't bring any of them back.

## Decisions for you

| | Decision | Recommendation |
|---|---|---|
| E3 | Keep the Pets course copy frozen? | **Decided 2026-11-15: frozen.** The four `pets4_*` files in `data/` and the saved outputs of 19_0_1 and 19_0_2 stay as they are, and 19_0 is not re-run on Colab. Any future code change to 19_0 is re-run on the laptop CPU with the local venv, which reproduces the course copy exactly. If the copy is ever regenerated, every Pets number in 19_0_2, 19_1, 20_0_1, 22_1_1, 22_1_2, the walkthrough pages and the unit 19 exam must be re-checked, as on 2026-11-03. |
Decided: E1 (required reading), E2 (roles, settled in version 5), E4 (a fresh demo app, built much later, not decks in `interactive/`), E5 (walkthrough pages follow the 125 class-day naming convention, for example "To Do: Topic 19.2, Confusion Matrix"; like the 125 prep pages, each lists the notebook to read and the demo steps, with no day references and no Logistics section).

## Step A: before any notebook or demo is built (done 2026-11-15, except one item)

1. **Calendar.** Done: 28 meetings, the layout above. Still to confirm: the unit 23 exam's slot in the spring final exam schedule.
2. **`tools/check_core.py`.** Done. It reads `tools/core_paths.csv` (each class's notebook and Pair sections) and prints the Pair words, the Pair code cells, the notebook's total words (the student's pre-class reading) and the question counts, with flags against the limits. Until step B the CSV points at the current notebooks, so the counts are before the cuts; step B updates the CSV to the new files and section numbers. The first run shows two things for step D:
   - 19_0_1's Pair path is 2,294 words and 12 cells today, against the plan's 1,250 after trims. Day 1 needs the S2 and S4 trims in full.
   - Pre-class reading runs from about 1,500 to 3,300 words a class before the cuts.

   Most classes are over the 7-cell guide, which is expected, since 387 cells are short.
3. **Five seeds.** Done with `tools/seed_check.py` (CPU, local venv, about 14 minutes); raw numbers in `tools/seed_check_results.json`. It used the revised recipe: plain Adam at 0.001, and for 22_0_2 the weights from the best validation epoch.

   | Claim (old numbering) | Five-seed result | Verdict |
   |---|---|---|
   | 21_1_1: dropout makes the validation loss end well below no regularization | Final validation loss lower by 0.30 to 0.35 in every seed (1.07 against 0.73 on average) | Holds |
   | 21_1_1: dropout improves validation accuracy a little | Best validation accuracy higher by 0.0 to 0.8 points; final validation accuracy is slightly lower on average (0.804 against 0.810) | Reword: accuracy is about the same, and the clear effect is on the loss |
   | 21_1_1: ten times the data raises validation accuracy by several points, far more than dropout | Best validation accuracy higher by 4.8 to 6.1 points in every seed (0.869 against 0.814) | Holds |
   | 22_0_2: the CNN beats the MLP | CNN without batch norm 0.885 test accuracy on average (0.883 to 0.887), MLP 0.861 (0.856 to 0.868); the CNN is ahead by 1.5 to 3.1 points in every seed | Holds; the text should call it a gain of about 2 to 3 points |
   | 22_0_2: shifting images hurts the MLP far more than the CNN | At 2 pixels the MLP loses 33 to 36 points and the CNN without batch norm 9 to 13, in every seed | Holds |

   The revised recipe gives lower numbers than the current text quotes (the MLP 0.861 against 0.869, the CNN 0.885 against 0.897), so the quoted figures change when the notebooks are re-run in step D.
4. **CNN without batch norm.** Done as part of item 3. Batch norm made almost no difference to test accuracy (0.886 with it, 0.885 without), and the CNN without it still clearly beats the MLP and passes the shift test. Batch norm is cut from 22_0_2 and 22_1_2 as planned.
5. **A Colab-matched venv.** Done: `venv-colab/` (ignored by git), Python 3.13.2 with torch 2.11, torchvision 0.26, numpy 2.4, pandas 2.2, scikit-learn 1.6, transformers 5.22 and diffusers 0.42, the versions the October and November Colab runs reported. The full list is in `tools/requirements-colab.txt`. Run checks with `venv-colab/bin/python smoke_test.py ...`; its own kernel is used, and the script's venv warning can be ignored. Twelve notebooks pass in it so far (19_1, 20_0, 22_0_1, 23_0, 23_1, 23_2_1). Colab's versions will move by January, so the venv is rebuilt then from a fresh Colab run of `tools/colab_check.ipynb`.

   The local venv's full `pip freeze` is saved as `tools/venv_freeze_pets_copy.txt`, so the frozen Pets copy can still be reproduced after `requirements.txt` is re-pinned.

## Step B: restructure the repo (done 2026-11-15)

**What was done.**

- **22_2 moved.** It is now in `extras/22_2_Autoencoders_and_Diffusion/`, with corrected badges, an optional-reading note at the top of each notebook, and `extras/README.md`. `smoke_test.py` skips `extras/`, and the two notebooks are out of `KEEP_OUTPUTS`.
- **19_1_4 split.** `19_1_4_Softmax_and_the_Loss.ipynb` has Sections 1 and 2, a new introduction, a Summary and a "What's next" paragraph. The new `19_1_5_What_One_Neuron_Cant_Do.ipynb` has a new introduction and setup cell, XOR and the hidden layer as Sections 1 and 2, a Summary and a "What's next" pointing to unit 20.
- **Tensors merged.** The tensor essentials are a "Before We Start: Tensors" section at the top of the autograd notebook: about 400 words and 4 cells covering making a tensor, shape and dtype, `.item()`, the batch dimension with `.unsqueeze(0)`, in-place methods, devices, `requires_grad` and `.detach()`. The old tensors notebook is deleted. References to it in 22_0_1 (color channels) and 23_1_1 (`.unsqueeze`) still hold, because the new 20_0_1 covers both.
- **21_1_2 merged.** 21_1_1 gains Section 6, Early Stopping. It keeps the best weights in memory with a patience of 5 on the 1,000-image run, which stops at epoch 14 with the best weights from epoch 9: validation loss 0.578 against 0.979 at epoch 60, and accuracy 0.800 against 0.803. A shortened checklist follows, then a new Summary and a "What's next" pointing to unit 22. 21_1_2 is deleted. The counting errors in 21_1_1 ("fourth option", "fifth tool") are fixed in passing.
- **Renumbered.** The autograd notebook is now `20_0_1_Autograd.ipynb` and gradient descent is `20_0_2_Gradient_Descent.ipynb`, using `tools/renumber_2026_11.py` over all notebooks, `COURSE_MAP.md` and the `TODO.md` files.
  - The unit 20 titles were renumbered (Parts 1 to 3).
  - References to XOR, the step function and the hidden layer now point to 19_1_5. References to softmax and the loss stay on 19_1_4.
  - The script's first run also turned one file name into "20_0_1_Gradient_Descent"; that was corrected by hand.
  - Outlines and glossaries were not renumbered, because they are rewritten in a later pass.
- **Four broken references fixed:**
  - the diffusion row of 19_0_2's history table
  - 22_0_1's "Next" line, which no longer cites 21_1_2's 0.869
  - 22_1_2's "Next" line, which now points to unit 23 and mentions `extras/`
  - 21_1_1's mention of 21_1_2
- **Documentation.** `COURSE_MAP.md` is rewritten for the new structure: the arc, datasets, units, the 28-meeting session budget, the concepts table, the ethics list, the rules on what is assigned and tested, and the maintenance notes. The 19_1, 20_0, 21_1, 22_0 and 22_1 TODOs have dated notes. `tools/core_paths.csv` points at the new files.

Checks passed:

- The smoke test passes for units 19 to 21 and 22_0_1, 13 notebooks in all.
- The saved-output check passes.
- All 26 Colab badges, including the two in `extras/`, point at their own files.

**Hits left for step D.** These come from the reference search. Each is in a notebook whose step D row already covers it:

| Notebook | What still mentions a removed notebook or topic |
|---|---|
| 19_1_2 | Section 4, thresholds and costs |
| 21_0_1 | AdamW in its closing cell |
| 21_1_1 | Section 4, weight decay (and its summary bullet); the batch-norm paragraph in Section 3 |
| 22_0_1 | Stride and the output-size formula |
| 22_0_2 | References to 21_1_2's recipe in 8 cells; the quoted 0.869 and 0.374; batch norm; AdamW and the cosine schedule; the in-memory checkpoint wording |
| 22_1_1 | Residual connections; batch norm in the scratch CNN; AdamW and the cosine schedule in its training cells |
| 22_1_2 | Section 3, adversarial examples; batch norm and AdamW in its small CNN |
| 23_0_1 | "23_1 shows how" for the attention mask |
| 23_1_1 | √d, masks, position embeddings and the transformer-layer anatomy; batch norm and residual connections mentioned in Section 6 |
| 23_2_1 | Section 5, zero-shot classification |
| 23_2_2 | AdamW in the fine-tuning loop (stays, as instructor-run reference); the `Trainer` paragraph in Section 7 mentions a schedule and checkpoints |
| 23_3_1 | Top-p; the causal-mask sentence; the forward reference to 23_3_2's contamination check |
| 23_3_2 | Section 5, contamination |


1. Move 22_2 to `extras/`.
2. Create 19_1_5 from Sections 3 and 4 of 19_1_4. Give it a new opening of about 150 words that recaps the neuron and softmax, and cut 19_1_4 down to Sections 1 and 2.
3. Merge the tensor basics into old 20_0_2, and delete old 20_0_1.
4. Merge early stopping and the checklist into 21_1_1, and delete 21_1_2.
5. Renumber old 20_0_2 and 20_0_3 as 20_0_1 and 20_0_2. Use a script with a rename map, which changes:
   - the file names
   - the Colab badge URLs
   - every in-text reference in all the notebooks, `COURSE_MAP.md` and the `TODO.md` files
   - `smoke_test.py`'s `KEEP_OUTPUTS`
6. Search all notebooks for references to removed notebooks and topics (22_2, 21_1_2, old 20_0_1, adversarial examples, batch norm, weight decay, √d, masks, zero-shot, contamination), and list each hit for step D. The ones known now:
   - the diffusion row of 19_0_2's history table
   - 22_1_2's "Next" line
   - 22_0_2's nine references to 21_1_2, and its quoted 0.869 and 0.374
   - 23_0_1's "23_1 shows how" for the attention mask
   - 23_3_1's causal-mask sentence, and its forward reference to 23_3_2's contamination check
   - 23_3_2's retrieval bullet
7. Update `COURSE_MAP.md`:
   - the arc, the unit table and the session budget
   - the datasets table (Fashion-MNIST is no longer used in 22_2)
   - the "where concepts are first taught" table, dropping the rows for cut topics
   - the ethics list
   - a new line on pre-class demos and the rules for what is assigned and tested

Check: the smoke test passes for units 19 to 21 and 22_0_1, the reference search returns only the hits listed for step D, and every Colab badge resolves to a file that exists.

## Step C: what each class contains

The "Pre-class demo" column says what the demo lets a student do. Every item in it is something the notebook already teaches, so it obeys rule 2. Until the new app exists, each of these is done in Colab with the notebook's own cells (the walkthrough names the cell and the setting to change), apart from the three explainers. The column is also the starting specification for the app's screens. "Pair" is the part of the notebook the activity works in. Its word and cell counts are estimates after the cuts.

| Class | Pre-class demo | Pair sections | Pair words / cells | Required + EC | Other changes |
|---|---|---|---|---|---|
| 19_0_1 | none | S1 to S5, with S3 led by you | 1,910 / 12 after trims | 3 + 2 | Trim S2 to about 350 words and S4 to about 550. CPU pairs use `USE_COURSE_COPY`. |
| 19_0_2 | Browse the test photos with predicted breed and confidence; filter to mistakes; sort by confidence | S3 to S6, S9 | 980 / 6 | 5 + 2 | Trim S6 and S9. Fix the diffusion row. |
| 19_1_1 | Train and validation accuracy against epochs from the saved 300-epoch run; the model against the always-guess baseline | S1, S2, S3, short S5 | 980 / 9 | 5 + 2 | |
| 19_1_2 | Click a cell of the confusion matrix to see its photos; precision and recall for a chosen breed; a slider for the number of Ragdolls in the shelter set | S1, S2, S3 | 970 / 9 | 5 + 2 | |
| 19_1_3 | Drag three weights and a bias and watch the weighted sum and sigmoid; a shape-matching widget for `@` | S1, S2, S3 | 810 / 10 | 5 + 2 | Decode the NumPy shape error. One sentence on 1.000 training accuracy against 0.850 test. |
| 19_1_4 | Drag four scores and watch softmax and the loss for the true breed | S1, S2 | 710 / 8 | 5 + 2 | Loss cell: a loop over five photos first. |
| 19_1_5 | Drag a line over the four XOR points and count the points right; switch to the hidden-layer view | new opening, S3, S4 | 840 / 7 | 5 + 2 | |
| 20_0_1 | Nudge a point on a curve and watch the slope; two linked sliders for rates multiplying | S1, S2, S3, S5 | 1,000 / 11 | 6 + 2 | Calculus boxes stay. |
| 20_0_2 | Step gradient descent down the penguin loss bowl; a learning-rate slider showing too small, about right and diverging | S1 to S6 | 920 / 8 | 6 + 2 | |
| 20_1_1 | TensorFlow Playground: the circle data with no hidden layer and then with one; ReLU; the learning rate. The walkthrough skips the regularization controls. | S2, S3, S4 | 940 / 10 | 6 + 2 | Classes passage; parameter counting. |
| 21_0_1 | One training step as a sequence (batch, loss, slopes, update); the saved loss curves; the starting loss against −log(1/10) | S2, S3, S4, S6 | 700 / 8 | 6 + 2 | |
| 21_1_1 | Choose 1,000 or 10,000 images and dropout on or off, from saved training histories; mark the best epoch | S1, S2, S3, S5, early stopping, checklist | 1,200 / 8 | 6 + 2 | Reword according to the five-seed result. |
| 22_0_1 | CNN Explainer: one 3×3 filter over a patch, ReLU, max pooling. The walkthrough skips the stride and hyperparameter views. | S1, S2, S4, S5, S6 | 990 / 9 | 6 + 2 | |
| 22_0_2 | Choose a filter and slide it over a Fashion-MNIST image; the shift-test accuracies for the MLP and the CNN | S1, S2, S3, S4, S6 | 780 / 6 | 6 + 2 | GPU rule. Re-run. |
| 22_1_1 | ResNet's shape path layer by layer; the three test accuracies (from scratch, feature extraction, fine-tuning) | S1 to S5 | 1,080 / 7 | 6 + 2 | Fix "90%". GPU rule. Re-run. |
| 22_1_2 | Toggle the planted marker and see the accuracy; the Pets accuracy under each photo change; the Gender Shades error rates by group | S1, S2, S4 | 930 / 3 | 6 + 2 | Re-run. |
| 23_0_1 | Choose a sentence and see its DistilBERT and GPT-2 tokens and IDs; padding and the attention mask for a batch | S2 to S7 | 1,000 / 6 | 6 + 2 | Explain the second tokenizer warning; fix the "23_1 shows how" reference. |
| 23_0_2 | Choose a word and see its nearest neighbors; "bank" in three sentences, before and after DistilBERT | S2 without PCA, S3, S4 | 850 / 6 | 6 + 2 | Mention the `269` neighbor; fix the closing sentence that promises a comparison 23_2 doesn't make. |
| 23_1_1 | Transformer Explainer: attention weights for a typed sentence and the next-token probabilities. The walkthrough skips the query, key and value views. | S1, S2, learned-comparison paragraph, cost of long texts, S7 | 840 / 7 | 6 + 2 | Fix the `np.float64` printing. The learned-comparison paragraph names queries and keys in one sentence each, so the explainer's labels are not new words. |
| 23_2_1 | Step a sentence through the pipeline (tokens, scores, softmax); the country-bias probabilities | S1, S3, S4 | 1,010 / 5 | 6 + 2 | |
| 23_2_2 | The words with the largest TF-IDF weights; browse the fine-tuned model's mistakes from the saved probabilities | S1, S5, S6 | 970 / 4 | 6 + 2 | Save the test probabilities to `data/`. Pairs read S2 to S4 from the saved outputs before class. |
| 23_3_1 | A temperature slider and a top-k slider on GPT-2's next-token probabilities for the notebook's prompt | S1, S3, S4, S5 | 950 / 5 | 6 + 2 | Self-supervised and causal-mask sentences. Re-run on Colab's CPU. |
| 23_3_2 | The token probabilities of the real and the invented answers; the multiple-choice table in both option orders | S1 to S4, S6 | 1,130 / 5 | 6 + 2 | Re-run on Colab's CPU. |

When the app is built, its screens should use precomputed data exported from the notebooks by small scripts in `public/387/tools/`, so a screen and its notebook cannot disagree, and none should run a model in the browser. A few Colab walkthroughs need a named setting the notebook doesn't expose yet (for example the number of Ragdolls in the 19_1_2 shelter set); adding it is part of that notebook's revision.

## Rules for building the notebooks, activities and demos

1. Cuts are deletions. A notebook's sections are renumbered after its cuts, and the step B reference search is repeated for that notebook.
2. The pair activity's instructions list its Pair sections in order. Its required questions cover the material the exam leans on most, and an ethics question is never the last required question.
3. **GPU notebooks** (22_0_2, 22_1_1): required questions are answered from the saved outputs before anything is run, and running or changing the training cells is extra credit.
4. **Answer keys** for anything a pair runs live come from Colab runs on the CPU and the T4, and they accept the range between the two.
5. Question prompts are about 150 words or less.
6. **Demos**, in Colab now and in the new app later, show one idea at a time and name the notebook section they illustrate. The new app should avoid the density of the current `interactive/` decks: one interaction per screen, with a short explanation, which also keeps the option of animating it later.
7. **Walkthrough pages** take 10 to 15 minutes to follow. Each says what to set, what to notice, and which notebook section explains it. They follow the student-facing rules: no day references, no time estimates, no Logistics section.

## Step D: build one unit at a time

**Progress.** Unit 19 is drafted (2026-11-15), and a blind review is next.

- **Notebooks.** The step C changes were made:
  - 19_1_1: Baseline 3 and the 30-versions experiment are cut. Section 5 is now a short explanation of the three-way split, with its table.
  - 19_1_2: Section 4 (thresholds) is cut, and `N_RAGDOLLS` is exposed for the walkthrough and the activity.
  - 19_1_3: the two shape errors are decoded, the 1.000 against 0.850 gap is explained, and "9 times in 10" is corrected.
  - 19_1_4: the sigmoid aside is cut, a five-photo loop comes before the one-line loss, and the average loss is interpreted.
  - 19_0_1 and 19_0_2: text trims only, so the frozen outputs are untouched.
  - All 19_1 notebooks: the newer `fetch()` and "What's next" paragraphs.

  All 7 notebooks pass in the local venv and in `venv-colab/`, and the saved-output check passes.
- **The rest of unit 19** is in `canvas/private/387_unit19/`, generated by `build.py`:
  - seven pair activities and the unit 19 exam as New Quiz drafts in `drafts/`
  - six walkthrough pages and the code-reading list in `pages/`

  They wait there until the Canvas s27 term exists.
- **Day 1 has 3 required questions, not 4.** Its Pair path is 1,910 words even after the trims, and nothing can be read before the first class.
- **Answer keys.** One key depends on library versions: 19_1_3's logistic regression gives z = 0.835 with scikit-learn 1.9 and 0.864 with Colab's 1.6, and the key accepts both. Colab's environment also prints an `OptimizeWarning` in 19_1_3, which may confuse students; check it on real Colab.
- **Still to do:** step D5 (open each notebook in real Colab) and D6 (time the cells on Colab's CPU and a T4), which need a browser session. The laptop CPU times are below 5 s for every 19_1 notebook, and 78 s for 19_0_1's training cell.

Each class produces:

- the revised notebook
- the pair activity (required and extra-credit questions per the table, with a key)
- the Canvas walkthrough page for the pre-class demo (Colab steps or an explainer)

Each unit also produces its exam and one "code you should be able to read" list. The review day and the reading checks are planned separately.

For each unit:

1. Revise the notebooks: the cuts and changes above, the corrections from the critique's error table that apply, the newer `fetch()`, a "What's next" paragraph, and a sentence saying a student's own numbers will differ slightly from the text. The notebook comes first because everything else must match it.
2. For a notebook with saved outputs (22_0_2, 22_1_1, 22_1_2, 23_2_2, 23_3_1, 23_3_2), re-run it on Colab in the same sitting as the edit, with library progress output turned down, and check every quoted number.
3. Write the walkthrough page: which cells to run, which setting to change, what to notice and which section explains it. Expose any named setting it needs in the notebook.
4. Draft the exam and the code list from the notebooks. Each exam question names the notebook section that holds what it tests.
5. Draft the pair activities. An exam question whose idea no pair question or demo touches is either kept as reading-only material or given a pair question.
6. Open each revised notebook in Colab and look at it, and follow each walkthrough page step by step in Colab.
7. Time every cell a pair question depends on, on Colab's CPU and on the T4, and make the key from those runs.
8. Have a reviewer who hasn't seen the plan read each notebook against its walkthrough and activity. The reviewer looks for anything in the demo or activity that the notebook doesn't contain (rule 2), text that disagrees with output, and references to things that were cut.

Not done in this pass: the new demo app (a separate, later project; see below), seaborn conversion, collapsing plotting cells, replacing `lambda`, the 19_0_1 terms table, the 23_3_2 comparison with current chatbots, and animation.

## The new demo app (later, separate project)

Not scheduled in this plan. When it is built:

- It is a fresh app, not an extension of `interactive/`.
- Each screen holds one interaction from the "Pre-class demo" column of step C, with a short explanation that names the notebook section.
- Its data comes from export scripts that read the notebooks' data files and saved outputs.
- Each screen replaces the Colab steps on that class's walkthrough page. The reading checks are revised to match.
- Rule 2 applies: a screen shows nothing the notebook doesn't teach.
- Its design should leave room for animation later.

Building it from the step C table, after the notebooks are settled, means its screens are designed against final content.

## Load and dates

Each unit is finished two weeks before its first class.

| Unit | First class | Due | Notebooks | Pair activities | Walkthrough pages (explainers among them) | Exam | Re-runs |
|---|---|---|---|---|---|---|---|
| 19 | Thu Jan 7 | before term (Jan 6) | 7 | 7 | 6 (0) | 1 | 0 |
| 20 | Thu Feb 4 | Thu Jan 21 | 3 | 3 | 3 (1) | 1 | 0 |
| 21 | Thu Feb 18 | Thu Feb 4 | 2 | 2 | 2 (0) | 1 | 0 |
| 22 | Tue Mar 2 | Tue Feb 16 | 4 | 4 | 4 (1) | 1 | 3 |
| 23 | Tue Mar 30 | Tue Mar 16 | 7 | 7 | 7 (1) | 1 | 3 |

Units 20 to 22 are each built in about two weeks while the course is running (Jan 7 to 21, Jan 21 to Feb 4, Feb 4 to 16). Unit 23 has four weeks, including spring recess.

**Before term:** steps A and B, plus all of unit 19: 7 notebooks, 7 activities, 6 walkthrough pages and the exam. This sits alongside the Canvas course shell, the syllabus and the unit 19 reading checks.

**From Jan 7 to Mar 16:** 16 notebooks, 16 activities, 16 walkthrough pages, 4 exams and 6 re-runs, about 6 pieces a week, plus the review day and the reading checks. A walkthrough page is small next to the other pieces, because its steps use cells the notebook already has.

If the load can't be met, protect work in this order:

1. the pair activity and its key
2. the exam
3. the walkthrough page
4. the cuts that change what students run
5. the remaining text changes

## Checks

| What | Check that can fail |
|---|---|
| Corrections | A script with one pattern per row of the critique's error table, run over the `.ipynb` files only. |
| Cuts complete | The step B reference search returns nothing; it is repeated after each unit. |
| No new material in demos or activities | Step D8. Every walkthrough step names a notebook section, and a script checks that the section exists. |
| Fit to the period | After each of the first six classes (Jan 7 to Jan 26), the same figures as the 377 table are pulled from the Canvas report: minutes to submission, the share of pairs that finished the required questions, and the median last question. If about four in five pairs finish unit 19's 5 required questions with 10 minutes or more to spare, units 20 to 23 keep 6; otherwise they use 5. |
| Pre-class work is done | Reading-check scores by class. If one class is consistently low, its notebook or demo is too long. |
| Notebooks still run | Smoke test for the unit, with a filter. |
| Exam matches what was assigned | Each exam question names the notebook section holding what it tests. Questions without one are removed. After the unit 19 exam, item results are split by newcomers and 377 graduates. |
| Colab behaviour and numbers | Steps D2, D6 and D7, in the Colab-matched venv. |

## How the critique's concerns are now covered

| Concern | Status |
|---|---|
| 1. Notebooks don't fit the class | Resolved on the 377 estimate, by cutting and by moving the demonstration out of class. To be checked against Canvas data from the first classes. |
| 2. Code-reading load | Mostly resolved. There is a code list per unit, a passage on classes, and the cuts remove much of the unfamiliar Python. `*block` and `**inputs` remain. |
| 3. No active work | Resolved in design. Every class has a pre-class demo and an in-class activity. Only unit 19's exist before term. |
| 4. On-ramp pace | Mostly resolved. There are five on-ramp classes, with cuts, and each has a demo of its main idea. |
| 5. Only unit 19 opens with a working model | Resolved for unit 23 |
| 6. Heaviest math | Resolved by cutting |
| 7. Single-run comparisons | Resolved once the five-seed runs are done |
| Schedule slack | One review day, before the unit 22 exam. In unit 19, 19_1_4 and 19_1_5 can share a day if a class is lost; in unit 22 the review day absorbs a lost class. Units 20, 21 and 23 have no slack. |
| Debugging gap | Open. Shape errors appear in 19_1_3 and 20_0_1, and the review day is yours. |
| Self-supervised learning unnamed | Resolved in 23_3_1 |
| Distance to current chatbots | Open (deferred) |
| Saved outputs | Resolved for six notebooks. 19_0 is frozen, and 22_2 is unchanged in `extras/`. |

## Risks

- **The time budget is thin evidence.** It rests on 26 pairs in four 377 activities, which is why the first six classes are measured.
- **Preparation before class.** It is now 30 to 45 minutes before every class, twice a week. Students who skip it will be slow in the activity and will show up in the reading check. The 377 figures come from students who had prepared.
- **The demos are weaker at first.** Until the new app exists, a demo is a set of steps in Colab, which asks more of students than an interactive page and depends on Colab behaving. When app screens replace the Colab steps, the reading checks for those classes have to be revised.
- **The browser explainers are outside your control.** They can change or go offline. Each walkthrough page should note the tool's version and date, and each needs a fallback (screenshots on the page).
- **Rule 2 can be hard to keep in demos.** An interaction can suggest a new idea without any text stating it, which is why step D8 is a reading of notebook against demo rather than a text search. This matters most when the app is built.
- **The longer on-ramp.** Some 377 graduates will find the five on-ramp classes slow. Extra-credit questions are their only extension.
- **Batch norm.** Cutting it from 22_0_2 changes its numbers. Step A4 checks this before the notebook is edited.
- **Renumbering** touches every notebook and several documents at once, which is why step B ends with a badge and reference check.

## What changed from version 6

| Area | Version 6 | Version 7 |
|---|---|---|
| Class meetings | 30 assumed | 28, from the Spring 2027 calendar, with dates |
| Review days | 3 | 1, before the unit 22 exam |
| Class length | 70 minutes | 75 minutes (9:25 to 10:40) |
| Required questions | 5 (first class 3) | Unit 19: 5; units 20 to 23: 6 by default; first class 4 |
| Due dates | Week numbers | Calendar dates |

## What changed from version 5

| Area | Version 5 | Version 6 |
|---|---|---|
| Demo platform | 10 new decks in `interactive/`, built during this pass | A fresh app, built much later; Colab walkthroughs and the three explainers until then |
| New deliverables in this pass | 10 decks (19 sections), 3 explainer walkthroughs, 22 Canvas pages | 22 Canvas walkthrough pages |
| Load in weeks 1 to 10 | about 7 pieces a week | about 6 pieces a week |
| Canvas naming | Decision pending | 125 convention, decided |
| Decisions open | E3, E4, E5 | none (E3 decided: Pets copy frozen) |

## What changed from version 4

| Area | Version 4 | Version 5 |
|---|---|---|
| Demonstration | In class, 0 to 15 minutes, by you | Before class: an interactive deck section or explainer, with a Canvas walkthrough page |
| Class time | Reading check, demonstration, pairs | Reading check 3, pairs 67 |
| Required questions | 4 or 5 depending on the demonstration | 5 everywhere except the first class (3) |
| What the exam tests | Code from Pair sections only | Anything assigned; all of it in the core notebooks |
| New material | Not addressed | None allowed in demos or activities |
| Role lines in notebooks | Under each section heading | None; Pair sections recorded in the plan and the activity |
| Text-to-image | 10-minute in-class demonstration | Dropped; 22_2 is optional reading in `extras/` |
| New deliverables | none | 10 decks (19 sections), 3 explainer walkthroughs, 22 Canvas pages |
| Decisions open | E2, E3 | E3, E4, E5 |
