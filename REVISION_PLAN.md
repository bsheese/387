# 387 Revision Plan (version 6)

Plan for revising the 387 notebooks before and during Spring 2027. This version replaces version 5 (2026-11-15). The reviews behind it are `CONTENT_CRITIQUE.md` and `REVISION_PLAN_critique.md`. Nothing in this plan has been carried out.

## What changed in this version

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
- The review days are yours to plan.
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
- 377 students were further along than many 387 students will be.
- The 377 questions came from separate pair notebooks; the 387 questions will come from the course notebook itself.

The first classes of the term will confirm or correct the figure (see Checks).

## The 387 time budget

A 70-minute class has two parts:

| Part | Minutes |
|---|---|
| Reading check, on paper, handed out as class starts | 3 |
| Pair activity, including opening the notebook and submitting | 67 |

At 12 minutes per question, 67 minutes allows 5 required questions, with about 7 minutes to spare for a slow start. So every class except the first has **5 required questions and 2 extra credit**.

The first class has no reading check and no pre-class demo, because nothing can be assigned before it, and it includes the course introduction and Colab setup. It gets 3 required questions and 2 extra credit.

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

The "Class" column counts teaching days only. The load table further down counts every class meeting, exams included.

| Unit | Class | Notebook (new numbering) | Pre-class demo | Comes from |
|---|---|---|---|---|
| 19 | 1 | 19_0_1 Your First Image Model | none (first day) | unchanged |
| | 2 | 19_0_2 What Just Happened | Colab walkthrough (19_0) | unchanged |
| | 3 | 19_1_1 Is It Any Good | Colab walkthrough (19_1, part 1) | trimmed |
| | 4 | 19_1_2 Confusion Matrix | Colab walkthrough (19_1, part 2) | trimmed |
| | 5 | 19_1_3 One Neuron | Colab walkthrough (19_1, part 3) | unchanged |
| | 6 | 19_1_4 Softmax and the Loss | Colab walkthrough (19_1, part 4) | first half of old 19_1_4 |
| | 7 | 19_1_5 What One Neuron Can't Do | Colab walkthrough (19_1, part 5) | second half of old 19_1_4 |
| | exam | Unit 19 exam | | |
| 20 | 8 | 20_0_1 The Nudge Test and Autograd | Colab walkthrough (20_0, part 1) | old 20_0_2, plus tensor basics from old 20_0_1 |
| | 9 | 20_0_2 Gradient Descent | Colab walkthrough (20_0, part 2) | old 20_0_3 |
| | 10 | 20_1_1 Building a Network | TensorFlow Playground | trimmed |
| | 11 | Review | yours | new |
| | exam | Unit 20 exam | | |
| 21 | 12 | 21_0_1 The Training Loop | Colab walkthrough (21_0) | trimmed |
| | 13 | 21_1_1 Overfitting | Colab walkthrough (21_1) | old 21_1_1 plus early stopping from old 21_1_2 |
| | 14 | Review | yours | new |
| | exam | Unit 21 exam | | |
| 22 | 15 | 22_0_1 Convolution by Hand | CNN Explainer | trimmed |
| | 16 | 22_0_2 A Convolutional Network | Colab walkthrough (22_0) | trimmed |
| | 17 | 22_1_1 Transfer Learning | Colab walkthrough (22_1, part 1) | trimmed |
| | 18 | 22_1_2 What Image Models Get Wrong | Colab walkthrough (22_1, part 2) | trimmed |
| | 19 | Review | yours | new |
| | exam | Unit 22 exam | | |
| 23 | 20 | 23_0_1 Tokens | Colab walkthrough (23_0, part 1) | trimmed, with a new opening |
| | 21 | 23_0_2 Embeddings | Colab walkthrough (23_0, part 2) | trimmed |
| | 22 | 23_1_1 Attention | Transformer Explainer | trimmed |
| | 23 | 23_2_1 Using Pretrained Models | Colab walkthrough (23_2, part 1) | trimmed |
| | 24 | 23_2_2 Fine-Tuning DistilBERT | Colab walkthrough (23_2, part 2) | trimmed |
| | 25 | 23_3_1 Generating Text | Colab walkthrough (23_3, part 1) | trimmed |
| | 26 | 23_3_2 What Language Models Get Wrong | Colab walkthrough (23_3, part 2) | trimmed |
| | final exam period | Unit 23 exam | | |

That is 26 teaching days (23 notebooks and 3 review days) and 4 in-class exam days, the same totals as `COURSE_MAP.md`. These totals still have to be checked against the Spring 2027 calendar.

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

## Step A: before any notebook or demo is built (now to mid-December)

1. **Calendar.** Check the real number of class days in Spring 2027 and where spring break falls, before any week number below is relied on.
2. **`tools/check_core.py`.** It reads a CSV of each class's Pair sections and prints the Pair words, the Pair code cells and the notebook's total words. The total is the student's pre-class reading.
3. **Five seeds for the claims that remain.** These are dropout against no regularization, ten times the data, and the CNN against the MLP once batch norm is removed from the CNN. Run each over five seeds outside the notebooks, which takes a few minutes. Keep a sentence's wording only if the result holds in all five.
4. **CNN without batch norm.** As part of item 3, confirm that 22_0_2's CNN without batch norm still clearly beats the MLP and still shows the shift-test result. If it doesn't, keep batch norm with a one-sentence explanation.
5. **A Colab-matched venv** for all number checks.

## Step B: restructure the repo (one sitting, before any unit is edited)

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
| 19_0_1 | none | S1 to S5, with S3 led by you | 1,250 / 9 | 3 + 2 | Trim S2 to about 350 words and S4 to about 550. CPU pairs use `USE_COURSE_COPY`. |
| 19_0_2 | Browse the test photos with predicted breed and confidence; filter to mistakes; sort by confidence | S3 to S6, S9 | 980 / 6 | 5 + 2 | Trim S6 and S9. Fix the diffusion row. |
| 19_1_1 | Train and validation accuracy against epochs from the saved 300-epoch run; the model against the always-guess baseline | S1, S2, S3, short S5 | 980 / 9 | 5 + 2 | |
| 19_1_2 | Click a cell of the confusion matrix to see its photos; precision and recall for a chosen breed; a slider for the number of Ragdolls in the shelter set | S1, S2, S3 | 970 / 9 | 5 + 2 | |
| 19_1_3 | Drag three weights and a bias and watch the weighted sum and sigmoid; a shape-matching widget for `@` | S1, S2, S3 | 810 / 10 | 5 + 2 | Decode the NumPy shape error. One sentence on 1.000 training accuracy against 0.850 test. |
| 19_1_4 | Drag four scores and watch softmax and the loss for the true breed | S1, S2 | 710 / 8 | 5 + 2 | Loss cell: a loop over five photos first. |
| 19_1_5 | Drag a line over the four XOR points and count the points right; switch to the hidden-layer view | new opening, S3, S4 | 840 / 7 | 5 + 2 | |
| 20_0_1 | Nudge a point on a curve and watch the slope; two linked sliders for rates multiplying | S1, S2, S3, S5 | 1,000 / 11 | 5 + 2 | Calculus boxes stay. |
| 20_0_2 | Step gradient descent down the penguin loss bowl; a learning-rate slider showing too small, about right and diverging | S1 to S6 | 920 / 8 | 5 + 2 | |
| 20_1_1 | TensorFlow Playground: the circle data with no hidden layer and then with one; ReLU; the learning rate. The walkthrough skips the regularization controls. | S2, S3, S4 | 940 / 10 | 5 + 2 | Classes passage; parameter counting. |
| 21_0_1 | One training step as a sequence (batch, loss, slopes, update); the saved loss curves; the starting loss against −log(1/10) | S2, S3, S4, S6 | 700 / 8 | 5 + 2 | |
| 21_1_1 | Choose 1,000 or 10,000 images and dropout on or off, from saved training histories; mark the best epoch | S1, S2, S3, S5, early stopping, checklist | 1,200 / 8 | 5 + 2 | Reword according to the five-seed result. |
| 22_0_1 | CNN Explainer: one 3×3 filter over a patch, ReLU, max pooling. The walkthrough skips the stride and hyperparameter views. | S1, S2, S4, S5, S6 | 990 / 9 | 5 + 2 | |
| 22_0_2 | Choose a filter and slide it over a Fashion-MNIST image; the shift-test accuracies for the MLP and the CNN | S1, S2, S3, S4, S6 | 780 / 6 | 5 + 2 | GPU rule. Re-run. |
| 22_1_1 | ResNet's shape path layer by layer; the three test accuracies (from scratch, feature extraction, fine-tuning) | S1 to S5 | 1,080 / 7 | 5 + 2 | Fix "90%". GPU rule. Re-run. |
| 22_1_2 | Toggle the planted marker and see the accuracy; the Pets accuracy under each photo change; the Gender Shades error rates by group | S1, S2, S4 | 930 / 3 | 5 + 2 | Re-run. |
| 23_0_1 | Choose a sentence and see its DistilBERT and GPT-2 tokens and IDs; padding and the attention mask for a batch | S2 to S7 | 1,000 / 6 | 5 + 2 | Explain the second tokenizer warning; fix the "23_1 shows how" reference. |
| 23_0_2 | Choose a word and see its nearest neighbors; "bank" in three sentences, before and after DistilBERT | S2 without PCA, S3, S4 | 850 / 6 | 5 + 2 | Mention the `269` neighbor; fix the closing sentence that promises a comparison 23_2 doesn't make. |
| 23_1_1 | Transformer Explainer: attention weights for a typed sentence and the next-token probabilities. The walkthrough skips the query, key and value views. | S1, S2, learned-comparison paragraph, cost of long texts, S7 | 840 / 7 | 5 + 2 | Fix the `np.float64` printing. The learned-comparison paragraph names queries and keys in one sentence each, so the explainer's labels are not new words. |
| 23_2_1 | Step a sentence through the pipeline (tokens, scores, softmax); the country-bias probabilities | S1, S3, S4 | 1,010 / 5 | 5 + 2 | |
| 23_2_2 | The words with the largest TF-IDF weights; browse the fine-tuned model's mistakes from the saved probabilities | S1, S5, S6 | 970 / 4 | 5 + 2 | Save the test probabilities to `data/`. Pairs read S2 to S4 from the saved outputs before class. |
| 23_3_1 | A temperature slider and a top-k slider on GPT-2's next-token probabilities for the notebook's prompt | S1, S3, S4, S5 | 950 / 5 | 5 + 2 | Self-supervised and causal-mask sentences. Re-run on Colab's CPU. |
| 23_3_2 | The token probabilities of the real and the invented answers; the multiple-choice table in both option orders | S1 to S4, S6 | 1,130 / 5 | 5 + 2 | Re-run on Colab's CPU. |

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

Each class produces:

- the revised notebook
- the pair activity (required and extra-credit questions per the table, with a key)
- the Canvas walkthrough page for the pre-class demo (Colab steps or an explainer)

Each unit also produces its exam and one "code you should be able to read" list. Review days and reading checks are planned separately.

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

Week numbers assume two classes a week, no break, and the day order above. They are redone after the calendar check. Each unit is finished two weeks before its first class.

| Unit | First class | Due | Notebooks | Pair activities | Walkthrough pages (explainers among them) | Exam | Re-runs |
|---|---|---|---|---|---|---|---|
| 19 | day 1 | before term | 7 | 7 | 6 (0) | 1 | 0 |
| 20 | day 9 (week 5) | end of week 3 | 3 | 3 | 3 (1) | 1 | 0 |
| 21 | day 14 (week 7) | end of week 5 | 2 | 2 | 2 (0) | 1 | 0 |
| 22 | day 18 (week 9) | end of week 7 | 4 | 4 | 4 (1) | 1 | 3 |
| 23 | day 24 (week 12) | end of week 10 | 7 | 7 | 7 (1) | 1 | 3 |

**Before term:** steps A and B, plus all of unit 19: 7 notebooks, 7 activities, 6 walkthrough pages and the exam. This sits alongside the Canvas course shell, the syllabus and the unit 19 reading checks.

**During weeks 1 to 10:** 16 notebooks, 16 activities, 16 walkthrough pages, 4 exams and 6 re-runs, about 6 pieces a week, plus the review days and the reading checks. A walkthrough page is small next to the other pieces, because its steps use cells the notebook already has.

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
| Fit to the period | After each of the first six classes, the same figures as the 377 table are pulled from the Canvas report: minutes to submission, the share of pairs that finished the required questions, and the median last question. If fewer than about four in five finish, the units not yet built drop to 4 required questions. If nearly all pairs finish with time to spare, the extra-credit questions get larger. |
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
| Schedule slack | Three review days. In unit 19, 19_1_4 and 19_1_5 can share a day if a class is lost. |
| Debugging gap | Open. Shape errors appear in 19_1_3 and 20_0_1, and the review days are yours. |
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
