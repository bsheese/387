# CS 387 Redesign Proposal: Deep Learning for a Broad Audience

Oct 24, 2026 · Brad Sheese

> Snapshot of the working doc at https://claude.ai/artifact/3N2ZsL6qJp2uYQWZQdYuUN, taken 2026-10-24.
> `COURSE_MAP.md` is the working view of the plan; the per-module `TODO.md` files hold the build tasks.

## Summary

Rebuild 387 around code first and pictures first. Students should train a working image classifier in week 1, open the black box in weeks 2–7, then use what they learned on images and on language. No step requires calculus. Every derivative becomes a "nudge test": students change a weight a little and measure how much the loss changes. The chain rule becomes "rates multiply." Calculus students get the formal version in optional boxes.

The mixed audience is handled by a two-week on-ramp built from existing 377 notebooks. For students new to ML it teaches the material; 377 graduates move through it faster as review, with a harder extension each class.

What changes from the current draft:

- **Add a week-1 "whole game."** Students fine-tune a pretrained image model on day 1, the way fast.ai opens its course.
- **Add a 377 on-ramp** (logistic regression as one neuron, splits and baselines, metrics). This replaces the current assumption that everyone took 377.
- **Rewrite the math in 19_0_2 and 19_0_3.** The nudge test comes first, with calculus in an optional box. 19_1 and 20_1 stay mostly as written.
- **Replace RNNs with embeddings, then attention, then pretrained transformers**, which is where students' interest and the field both are.
- **Make interactive explainers class activities**: TensorFlow Playground, CNN Explainer and Transformer Explainer, each paired with a Canvas pair activity.

(Unit numbers in this summary use the old layout. In the new layout 19_0 is `20_0_PyTorch_Basics`, 19_1_1 is `20_1_1`, 19_1_2–3 are `21_0_1`–`21_0_2`, and 20_1 is `21_1_Practical_Training`.)

## Audience and constraints

The course has to work for two groups in the same room, and for students who have never taken calculus.

| Group | Already has | Needs from 387 |
| --- | --- | --- |
| 377 graduates | sklearn, pipelines, cross-validation, regularization, metrics, logistic regression, softmax, and XOR and an MLP as a black box (18_2_3) | What happens inside the network, PyTorch, images and text |
| Students via CS 128 + CS/MATH 136 | Python through CS2 (C- or above) and discrete math; pandas not guaranteed | The ML basics first: splits, baselines, metrics, overfitting |
| Students without calculus (in either group) | Algebra | Gradients and backprop explained without derivatives |

The current material and format:

- **Meeting pattern.** Spring 2025 met Tuesday and Thursday for 75 minutes, about 28 sessions. Colab is the environment; the free CPU is enough for everything except larger CNN and transformer runs.
- **What the 387 repo has.** Unit 19 (tensors, autograd, gradient descent, network anatomy, the training loop, multiclass) and unit 20 (dropout, batch norm, LR schedules, checkpointing, a full pipeline). There are 13 notebooks plus quizzes and glossaries. They assume 377 and reuse its datasets (XOR, Wisconsin breast cancer, CTG fetal health).
- **How Spring 2025 ran.** It was built on Learn PyTorch (Bourke) chapters 0–4 and StatQuest videos, with a reading quiz and a team challenge most sessions, two exams, and a final project presented in the exam period.
- **Course notes so far.** `course_outline.md` holds only three lines (20_1 motivation, 20_2 "fastai style solve a problem", 20_3 blank).

## What other courses and textbooks do

The resources that reach a broad audience have three things in common. They show a working result before any theory, they teach through examples rather than notation, and they bring in math only when a concrete step needs it. University courses still mostly require calculus. The no-calculus approaches come from books and open courses.

| Resource | Math it assumes | How it handles the math | What 387 takes from it |
| --- | --- | --- | --- |
| [fast.ai, Practical Deep Learning for Coders](https://course.fast.ai/) | High school math; a year of coding | Top-down: build a working model first, then explain how it works; "we always teach through examples" | The week-1 whole game; play first, explain after |
| [Grokking Deep Learning (Trask)](https://www.goodreads.com/author_blog_posts/14998820-grokking-deep-learning) | Basic algebra; basic Python | Builds from scratch in NumPy; only "the bits and pieces" of calculus that are needed | One neuron built by hand with real numbers before PyTorch |
| [Deep Learning: A Visual Approach (Glassner, 2021)](https://glassner.com/book-deep-learning/) | "No math beyond addition and multiplication" | About 900 figures, free on GitHub; covers networks, backprop, CNNs, RNNs, attention | Optional companion text for students without calculus; figures for slides |
| [Deep Learning with Python, 3rd ed. (Chollet and Watson, 2025)](https://manning.com/books/deep-learning-with-python-third-edition) | Intermediate Python; no linear algebra | "Intuitive and easy math explanations"; adds transformers, a GPT-like model and diffusion | Optional only (paid); Keras-first, but it also shows PyTorch |
| [Neural Networks: Zero to Hero (Karpathy)](https://karpathy.ai/zero-to-hero.html) | Python; "a vague recollection of calculus from high school" | micrograd builds backprop step by step in plain Python | An optional extension notebook for the 377 track |
| 3Blue1Brown neural network series, including the [2024 transformer chapters](https://3blue1brown.substack.com/p/but-what-is-a-gpt) | None for the main videos | Animation first; calculus kept to a separate optional video | Assigned viewing before the gradient descent and attention classes |
| [Learn PyTorch for Deep Learning (Bourke)](https://www.learnpytorch.io/) | 3–6 months of Python; one beginner ML course | Code first; light math | Spring 2025's spine; keep it as the PyTorch reference |
| [Dive into Deep Learning](https://d2l.ai/) | Linear algebra, calculus and probability (taught in ch. 2 and an appendix) | Math alongside runnable code; adopted at 500 universities | Instructor reference only; too much math for the main text |
| [MIT 6.S191](https://introtodeeplearning.com/) | Derivatives, the chain rule, matrix multiplication | Short lectures plus labs on music, faces and fine-tuning an LLM; graded on a project proposal | The breadth of topics and a project-centered finish |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Python and an intro DL course | Uses pretrained models through libraries; free | Source for the language unit |

The closest match among university courses is Michigan Statistics' deep learning course for arts-and-sciences undergraduates. It cut its prerequisites to single-variable calculus, one programming course and one statistics course, and has grown from a 40-student pilot in Winter 2022 ([CACM blog](https://cacm.acm.org/blogcacm/scaling-deep-learning-education-in-a-college-of-arts-sciences); the page blocked direct access, so this comes from search summaries). It still asks for more math than 387 would.

Three free browser tools make the hidden parts of a network visible with no setup: [TensorFlow Playground](https://playground.tensorflow.org/) (train a small network live, changing layers, activation, learning rate and regularization), [CNN Explainer](https://poloclub.github.io/cnn-explainer/), and [Transformer Explainer](https://huggingface.co/papers/2408.04619) (a live GPT-2 "designed for non-experts").

## Design principles

Six rules, taken from the survey and from what already works in 377:

1. **Whole game first.** Each unit opens with a working model on real data, then opens it up. This is fast.ai's order, and it fits 377's evaluation-first unit 18 too.
2. **Measure before you formalize.** Every math idea starts as something students compute and see: a nudge, a table, a plot. Notation comes after, and is optional when it needs calculus.
3. **One idea per notebook, a picture for every idea.** Each concept gets a diagram or a live tool (Playground, CNN Explainer, Transformer Explainer) along with its code.
4. **Reuse what students know.** Logistic regression is the first neuron, regularization becomes weight decay, nested CV becomes the validation discipline, and confusion matrices are reused unchanged. 377 graduates should recognize the ideas; newcomers learn each one once.
5. **Pretrained models are the normal case.** Most real deep learning work adapts an existing model. Transfer learning and fine-tuning are core skills here, not an extra.
6. **Keep the 377 habits.** Notebooks are committed with no outputs and smoke-tested, there are pair activities with a driver and a recorder answering in a Canvas quiz, and evaluation stays honest (baselines, held-out test sets).

## Reusing 377, and an on-ramp for students who skipped it

Make weeks 2–3 a four-session on-ramp built from trimmed copies of 377 notebooks. For newcomers it's new material; for 377 graduates it's review plus an extension. Mixed pairs (one 377 graduate, one newcomer) in the pair activities make the gap useful instead of awkward.

| On-ramp session | 377 source notebooks | Trim to | 377-graduate extension |
| --- | --- | --- | --- |
| 1. What a model is, and how to tell if it's any good | 16_1 Intro to ML, 17_0_1 (baseline), 17_1_6 Generalization Test | Baseline, train/test split, overfitting on one dataset | Explain why the validation set exists, ahead of the 387 three-way split |
| 2. Classification and its metrics | 18_1_1 Classification Foundations, 18_1_2 Confusion Matrix | Accuracy paradox, confusion matrix, precision/recall | Pick a threshold under a stated cost |
| 3. Logistic regression is one neuron | 18_2_0_1 reading, 18_2_1 (first half), 18_2_3 section 1 | Sigmoid, weighted sum, `predict_proba` reproduced by hand | Write the neuron in NumPy and fit it with the nudge test (see the math section) |
| 4. More than two classes, and where one neuron stops | 18_5_1 Multiclass Intro, 18_2_3 section 2 (XOR) | Softmax as a table of numbers; XOR can't be split with one line | Write softmax by hand; predict what hidden layer XOR needs |

Other 377 ideas come back later, where they are needed:

- **Ridge and Lasso (17_2_1_3)** become weight decay in the training-loop unit.
- **Cross-validation and nested CV (17_2_1_2–5)** explain why deep learning uses one validation set: training is too slow to repeat k times.
- **Pipelines and leakage (17_2_1_1–2)** become the rule "fit the scaler on training data only" in 19_1_2.
- **Trees and XGBoost (17_2_2, 18_6)** are the baseline every network has to beat on tabular data. 19_1_2 already makes this comparison.
- **NumPy arrays** come in the same way 377 introduces them, early in the on-ramp, so PyTorch tensors arrive as arrays that track gradients. Which 377 notebook to lift is still to pick.

These should be copies in the 387 repo, not links into cs377. The 377 folder names change: `17_2_MLR` was renamed `17_2_1_MLR` this term. Each copy's header should name its 377 source so changes can be carried over by hand.

## Proposed unit sequence

Six units over 15 weeks. About half the notebooks already exist in the 387 repo or as 377 notebooks to trim; the images and language units are new.

(The doc shows this as a diagram; it does not export, so here it is as a table.)

| Weeks | Unit | Content | Material comes from |
| --- | --- | --- | --- |
| 1–3 | 19 · Whole game and on-ramp | Week 1: fine-tune a pretrained image model on day one. Weeks 2–3: baselines, metrics, one neuron, softmax | New (week 1); 377 copies (weeks 2–3) |
| 4–5 | 20 · How networks learn | Tensors, the nudge test, autograd, gradient descent. Hidden layers solve XOR; TensorFlow Playground | Existing 19_0, 19_1_1, math rewritten |
| 6–7 | 21 · Training in practice | Training loop, DataLoader, overfitting curves, Adam. Dropout, weight decay, batch norm, LR schedules | Existing 19_1_2–3, 20_1, mostly as written |
| 8–10 (proposal week 9) | 22 · Images | Convolution by hand, CNN Explainer, a CNN on Fashion-MNIST. Augmentation, transfer learning (ResNet-18), bias | New |
| 11–13 (checkpoint week 12) | 23 · Language | Tokens and embeddings, attention, Transformer Explainer. Fine-tune DistilBERT; what LLMs can and can't do | New; draws on the HF course |
| 14–15 (presentations in the exam period) | 24 · Projects | Project work in class, with instructor check-ins | Student work |

The existing units 19 and 20 become units 20 and 21, nearly intact. RNNs and LSTMs get one historical slide in the language unit rather than a week: attention replaced them, and Transformer Explainer makes attention easier to see than recurrence.

| Unit | Notebooks (proposed) | Datasets | Status |
| --- | --- | --- | --- |
| 19 Whole game and on-ramp | 19_0 Your first image model (fine-tune a pretrained ResNet on a small labeled set); 19_1 to 19_4 on-ramp sessions | Oxford-IIIT Pets or student photos; 377 datasets (Titanic, penguins) | 19_0 new; 19_1–19_4 trimmed from 377 |
| 20 How networks learn | Tensors; the nudge test and autograd; gradient descent; anatomy of a network and XOR | Penguins, XOR | Existing 19_0_1–19_0_3, 19_1_1; add the nudge test |
| 21 Training in practice | Training loop; multiclass; dropout; batch norm; LR schedules; checkpointing; full pipeline | Wisconsin breast cancer, CTG fetal health | Existing 19_1_2–19_1_3, 20_1_1–20_1_5 |
| 22 Images | Convolution by hand; a first CNN; augmentation; transfer learning; what CNNs get wrong; autoencoders and denoising, with a pretrained diffusion demo | Fashion-MNIST, CIFAR-10, the week-1 image set | New |
| 23 Language | Tokens and embeddings; attention; using pretrained transformers; fine-tuning a text classifier; text generation (sampling, temperature); limits and evaluation of LLMs | IMDB or another review set; a short-text set students pick | New |
| 24 Projects | Project template notebook | Student-chosen | New |

## Handling the math without calculus

Every calculus step in deep learning can be done as an experiment in code. Students measure first; autograd then does the same thing faster. The core move is the nudge test:

```python
def loss(w):
    return ((w * x + b - y) ** 2).mean()

slope = (loss(w + 0.001) - loss(w)) / 0.001   # how much the loss changes per unit of w
# then: loss_t.backward(); w_t.grad          # autograd gives the same number
```

Students see the two numbers agree to three decimal places. From then on, autograd is "a fast, exact nudge test for every weight at once" rather than a black box.

| Idea | Usual (calculus) version | 387 version | How students check it |
| --- | --- | --- | --- |
| Slope of the loss | Derivative dL/dw | Nudge w by 0.001 and divide the change in loss by 0.001 | Matches `w.grad` |
| Gradient | Vector of partial derivatives | One nudge per weight, in a table: which way is downhill for each | Matches `.grad` for every parameter |
| Gradient descent | w ← w − lr · ∇L | The same update, using numbers students already computed; the 19_0_3 loss bowl | The loss curve goes down |
| Backpropagation | Chain rule | "Rates multiply": if a nudge to a weight moves a hidden value 3× as much, and the hidden value moves the loss 0.5×, the weight moves the loss 1.5×. Backprop does this from the output backward so each rate is computed once | Nudge the weight directly and get 1.5 |
| Matrix multiply | Linear algebra | Many weighted sums at once: the neuron from on-ramp session 3, repeated | The shapes rule: inner sizes must match |
| Cross-entropy loss | Negative log-likelihood | "Surprise": −ln(0.9) = 0.11, −ln(0.5) = 0.69, −ln(0.1) = 2.30, so confident wrong answers cost the most | A table of predictions and losses |
| Softmax | Normalized exponential | Make every score positive (exponentiate), then divide by the total | The probabilities sum to 1 |
| Convolution | Discrete convolution | Slide a 3×3 grid of numbers over the image and multiply-add | By hand on a 5×5 grid, then CNN Explainer |
| Attention | Scaled dot-product attention | A weighted average; the weights come from how similar two words are, passed through softmax | Transformer Explainer shows the weights |

What this means for existing notebooks: 19_0_2 now checks autograd against calculus (dy/dx = 2x). It should check against the nudge test instead, with the calculus moved to a collapsible "if you've taken calculus" box. 19_0_3 already teaches gradient descent through the loss bowl and needs only the nudge step added before `backward()`.

## Assessment and activities

Assess reading code and reasoning about models, not deriving formulas. That keeps the bar the same for students with and without calculus. The weights below are a starting point.

| Component | Weight | Form |
| --- | --- | --- |
| Final project | 15% | Proposal in week 9, checkpoint in week 12, presentation in the exam period (as in Spring 2025). One of three tracks: fine-tune an image model on a dataset the student collects; build a text classifier on a pretrained transformer; or compare a tabular network against XGBoost. Each needs a baseline, an honest held-out evaluation and a one-paragraph ethics note. |
| Unit exams (6) | 70% (about 11.7% each) | One at the end of each unit, lockdown browser, same format as 377's exams. Code reading: predict tensor shapes, read loss curves, diagnose overfitting, choose a fix, interpret a confusion matrix. No derivations. |
| Pair activities | 15% | Weekly, driver and recorder, answers in a Canvas New Quiz, the last two questions extra credit. Size them by 377's Ridge vs. Lasso activity, which ran far too long: few required questions, every notebook edit a small change to given code. |
| Practice quizzes | 0% (ungraded) | The existing `*_practice_quiz` notebooks and a quiz site like 377's, done before class. They replace Spring 2025's lockdown-browser reading quizzes. |

Where live tools fit as class activities:

- **TensorFlow Playground** (gradient descent week): predict, then test, what happens with no hidden layer on the circle data, a learning rate of 3, or L2 turned up.
- **CNN Explainer** (vision unit): trace one 3×3 filter by hand, then find it in the tool.
- **Transformer Explainer** (language unit): change the temperature and the prompt, and explain the next-token probabilities.

## Open questions and decisions

- [x] **Prerequisite.** Decided: CS/DASC 377, or both CS 128 (CS2) with a C- or above and CS/MATH 136 (Discrete Math). The CS 128 route does not guarantee pandas, so the on-ramp may need a short pandas primer alongside NumPy.
- [x] **Textbook.** Decided: free and open materials wherever possible (Learn PyTorch, 3Blue1Brown, the Hugging Face course and similar). Paid books such as Chollet and Watson or Glassner are optional at most, never required.
- [x] **Framework.** Decided: stay with PyTorch (the 13 existing notebooks, Hugging Face and most current tutorials use it). NumPy arrays will likely need to come in first, introduced the same way 377 does, ahead of tensors.
- [x] **Unit numbering.** Decided: keep 377's numbering (19–24), with the on-ramp at the front of unit 19.
- [x] **GPU budget.** Decided: most students stay on free Colab, so models stay small (ResNet-18 for images, DistilBERT for text). The CS department cluster is open to more advanced students only.
- [x] **Generative models.** Decided: two sessions, not a unit. Unit 22 ends with a small autoencoder that denoises Fashion-MNIST, then a pretrained diffusion model shown as "denoising, repeated." Unit 23 adds text generation (sampling, temperature) beside the LLM-limits session. Exams test it by reading and reasoning only; it is not a project track.
- [x] **Exams.** Decided: lockdown browser, same format as 377's exams, one at the end of every unit and weighted more heavily (see Assessment).
- [x] **Next offering.** Decided: Spring 2027. Units 21–24 need to be written before then.

## Decisions made after the snapshot (2026-10-24)

These supersede the text above where the two conflict.

- **Class format:** Tuesday/Thursday, 70 minutes per class, the same as 377 (Spring 2025 was 75).
- **Exams:** five, one after each of units 19–23, each taking one class day: units 19–22 in class, unit 23 in the final exam period. Each is 16% of the grade (80% total), and pair activities are 20%. This replaces the whole assessment table above and the diagram's "Exam 1 / Exam 2" milestones.
- **Saved outputs:** 387 notebooks may keep saved outputs. This is decided notebook by notebook, so design principle 6 ("committed with no outputs") does not apply here.
- **No final project** (cut 2026-10-24). Unit 24 is removed, and its four class days go to units 20–23. Grade weights are now exams 80% (5 × 16%), pair activities 20%, practice quizzes 0%. The unit 23 exam is given in the final exam period. Everything above about project tracks, the proposal and the checkpoint no longer applies.
- **Six datasets** plus the XOR toy: Oxford-IIIT Pets, penguins, Wisconsin breast cancer, Fashion-MNIST, IMDB. Dropped: Titanic, CTG, wine, CIFAR-10, student photos, a student-chosen text set.
- **Fashion-MNIST moves earlier:** 21_0_2 (multiclass) and all of 21_1 (regularization) use a Fashion-MNIST MLP, and 22_0 swaps in a CNN on the same data. Units 20–21 no longer teach deep learning only on tabular data.
- **No take-home work.** Everything required happens in class; readings, videos and practice quizzes are optional.
- **The on-ramp runs on the week-1 Pets model:** baseline, confusion matrix, one neuron (the model's last layer), softmax. The 377 notebooks are optional reference, not class time. 19_0 gets two days.
- **Runtime in class:** pair activities can't include long-running cells (30 minutes is far too long). Use small data, few epochs and pretrained weights, or show long runs as saved outputs.

## Sources

Web pages opened on 2026-10-24:

- [fast.ai — Practical Deep Learning for Coders](https://course.fast.ai/)
- [Trask — Grokking Deep Learning (author's post)](https://www.goodreads.com/author_blog_posts/14998820-grokking-deep-learning)
- [Glassner — Deep Learning: A Visual Approach](https://glassner.com/book-deep-learning/)
- [Manning — Deep Learning with Python, Third Edition](https://manning.com/books/deep-learning-with-python-third-edition)
- [Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- [3Blue1Brown — But what is a GPT?](https://3blue1brown.substack.com/p/but-what-is-a-gpt)
- [Bourke — Learn PyTorch for Deep Learning](https://www.learnpytorch.io/)
- [Dive into Deep Learning](https://d2l.ai/)
- [MIT 6.S191 Introduction to Deep Learning](https://introtodeeplearning.com/)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
- [TensorFlow Playground](https://playground.tensorflow.org/)
- [Transformer Explainer paper](https://huggingface.co/papers/2408.04619)
- [CACM blog: Scaling deep learning education in a college of arts and sciences](https://cacm.acm.org/blogcacm/scaling-deep-learning-education-in-a-college-of-arts-sciences) (blocked direct access; details come from search summaries)

Local material read: `public/387` (course_outline.md and the unit 19 and 20 outlines), `public/377/COURSE_MAP.md`, the 18_2 outline, and the Spring 2025 387 Canvas modules and dates in `canvas/courses/387/terms/s25`.
