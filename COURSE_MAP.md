# cs387 Course Map

The whole course on one page: what each unit teaches, what it assumes, where
each core idea is *first* taught, and what each unit still needs to be built.
The reasoning behind the design is in `PROPOSAL.md`. Build tasks are in the
`TODO.md` file in each module directory.

387 follows on from cs377 (units 16–18) and continues its numbering at 19. Not
every student takes 377 first: the prerequisite is CS/DASC 377, **or** CS 128
(C- or above) plus CS/MATH 136. Unit 19's on-ramp covers the gap. No unit
requires calculus.

First offering of this design: **Spring 2027**, Tuesday/Thursday, 70 minutes
per class, the same as 377.

**Exams:** five, one after each unit, each taking one class day. The exams for units 19–22 are
given in class; the unit 23 exam is given in the final exam period. There is no final project (cut 2026-10-24).

**Grade weights:** exams 80% (5 × 16%), pair activities 20%, practice quizzes 0% (ungraded).

**No take-home work** (decided 2026-10-24). Everything students must do happens in class. Readings, videos and practice quizzes are optional.

**Runtime rule for class time:** in-class pair activities can't contain cells
that take a long time on free Colab. A 30-minute training cell is far too
long. Use small subsets, few epochs and pretrained weights. If a result
needs a long run, show it as a saved output or load it from a file.

---

## The Arc

```
19  Whole game      →  20  How networks   →  21  Training      →  22  Images       →  23  Language
    + on-ramp            learn                 in practice

19_0 → 19_1             20_0 → 20_1          21_0 → 21_1          22_0 → 22_1 → 22_2     23_0 → 23_1 → 23_2 → 23_3
whole  on-ramp          nudge  anatomy       loop   practical     conv   transfer  AE +   tokens attn  pre-   gen +
game   (on the same     test,  & XOR                training             learning  diff.  & emb.       trained limits
       Pets model)      autograd                    (Fashion-MNIST from here through 22)
```

## Datasets

Six datasets, plus the four-point XOR toy (cut from ten on 2026-10-24).

| Dataset | Used in | Replaces |
|---|---|---|
| Oxford-IIIT Pets | 19_0 (whole game), 19_1 (the whole on-ramp), 22_1 (transfer learning) | student photos, CIFAR-10, Titanic, German Credit |
| Palmer penguins | 20_0_3 (gradient descent) | Auto MPG |
| Wisconsin breast cancer | 21_0_1 (training loop) | |
| Fashion-MNIST | 21_0_2 (multiclass), 21_1 (regularization, MLP), 22_0 (CNN), 22_2 (autoencoder) | CTG fetal health, wine quality |
| IMDB reviews | 23_0–23_2 | the student-chosen text set |
| XOR (4 points, toy) | 19_1_4, 20_1_1 | — |

Pretrained models (ResNet-18, DistilBERT, GPT-2 small, a small diffusion
model) are not counted as datasets.

## Units at a Glance

| Unit | Modules | Role | Datasets | Assumes | Status |
|---|---|---|---|---|---|
| `19_onramp` | `19_0_Whole_Game`, `19_1_ML_Foundations` | Fine-tune a pretrained image model in the first two days, then a four-session ML on-ramp taught on that same model (baselines, confusion matrix, one neuron, softmax); NumPy taught as needed | Pets, XOR | CS 128 or 377 | To write (377 notebooks are optional reference only) |
| `20_how_networks_learn` | `20_0_PyTorch_Basics`, `20_1_Network_Anatomy` | Tensors, the nudge test, autograd, gradient descent; one neuron → hidden layer → XOR | Penguins, XOR | 19_1 | Exists; rewrite math (nudge test first, calculus optional) |
| `21_training` | `21_0_Training_Loop`, `21_1_Practical_Training` | The full training loop, overfitting curves, multiclass, regularization, schedules | Breast cancer (21_0_1); Fashion-MNIST (21_0_2, 21_1) | 20 | Exists; 21_0_2 and all of 21_1 move from CTG/wine to Fashion-MNIST |
| `22_images` | `22_0_Convolution_and_CNNs`, `22_1_Transfer_Learning`, `22_2_Autoencoders_and_Diffusion` | Convolution by hand, CNNs (MLP → CNN on the same Fashion-MNIST), augmentation, transfer learning, bias; autoencoder denoising, diffusion as "denoising, repeated" | Fashion-MNIST, Pets | 21 | To write |
| `23_language` | `23_0_Tokens_and_Embeddings`, `23_1_Attention`, `23_2_Pretrained_Transformers`, `23_3_Generation_and_Limits` | Tokens, embeddings, attention, fine-tuning DistilBERT, sampling and temperature, what LLMs can't do | IMDB | 21, 22_1 (transfer learning) | To write |

**Session budget** (draft; check against the Spring 2027 calendar). 15 weeks ×
2 = 30 class days. The exams for units 19–22 each take a class day right after
the unit; the unit 23 exam is in the final exam period. The four days that went
to projects now go one each to units 20–23.

| Unit | Class days | Teaching days | Exam day | Notes |
|---|---|---|---|---|
| 19 | 1–7 | 6 | day 7 | 19_0 gets 2 days, 19_1 gets 4 |
| 20 | 8–12 | 4 | day 12 | |
| 21 | 13–17 | 4 | day 17 | 21_1 still has more notebooks than days (see the top-level TODO) |
| 22 | 18–24 | 6 | day 24 | |
| 23 | 25–30 | 6 | final exam period | gave a day to 19_0 |
| **Total** | 30 | **26** | 4 in class + 1 in the exam period | |

**Sequencing notes.**
- 19_0 is deliberately a black box: students fine-tune a pretrained model
  before they know what a weight is. 19_0's closing notebook should say so and
  point forward to the units that open it up, the way 377's 18_1_1 does for XGBoost.
- 19_1 runs entirely on 19_0's saved predictions and cached features, so 19_0
  must produce them (see the 19_0 TODO).
- 22_1 (transfer learning) opens up the black box from 19_0, on the same Pets
  data. 23_2 does the same thing for text.
- 21 must come before 22: 22_0 reuses the 21_1 Fashion-MNIST MLP and the 21_0
  training loop, and swaps in a CNN on the same data.
- 22_2 and 23_3 (generative models) are tested by reading and reasoning only.

## Where Concepts Are First Taught (and Reprised)

| Concept | First taught | Reprised / deepened |
|---|---|---|
| Pretrained model, fine-tuning (black box) | 19_0 | 22_1 (opened up), 23_2 (text) |
| NumPy arrays (as needed) | 19_1, inside each session | 20_0_1 (tensors as arrays that track gradients) |
| Baseline, train/test split, overfitting | 19_1_1 (on the Pets model) | 21_0_1 (validation set, loss curves) |
| Confusion matrix, precision/recall | 19_1_2 (on the Pets model) | 21_0_1, 21_0_2, every later evaluation |
| Sigmoid, weighted sum, one neuron | 19_1_3 (the Pets model's last layer) | 20_1_1 (`nn.Linear` + sigmoid) |
| Softmax, XOR limit | 19_1_4 (Pets breed scores; XOR toy) | 20_1_1 (XORNet), 21_0_2 (CrossEntropyLoss) |
| Nudge test (slope by measurement) | 20_0_2 | 20_0_3 (gradient descent), 22_0 (filters) |
| Autograd as an automatic nudge test | 20_0_2 | everything after |
| Rates multiply (backprop without calculus) | 20_0_2 | 20_1_1 |
| Learning rate, loss bowl | 20_0_3 | 21_1_3 (schedules) |
| Training loop, DataLoader, three-way split | 21_0_1 | 22, 23 (same loop) |
| Cross-entropy as "surprise" | 21_0_2 | 23_3 (next-token loss) |
| Dropout, weight decay (Ridge in 377), batch norm | 21_1 (Fashion-MNIST MLP) | 22_0 |
| Convolution as sliding multiply-add | 22_0 | 22_1, 22_2 |
| Transfer learning | 22_1 | 23_2 |
| Autoencoder, denoising, diffusion | 22_2 | — |
| Tokens, embeddings | 23_0 | 23_1, 23_2 |
| Attention as a weighted average | 23_1 | 23_2, 23_3 |
| Sampling, temperature | 23_3 | — |

## Ethics Thread

- 19_0: where the training images came from, and who is missing from them
- 21_0_1: the malignant-recall framing (inherited from 377 18_6)
- 22_1: bias in vision models (face and skin-tone failures)
- 23_3: what LLMs get wrong; hallucination; evaluating a model's output

## Maintenance Notes

- Module layout follows 377: `<unit>/<module>/` holds the notebooks plus
  `*_outline.md`, `*_glossary.md` and `*_practice_quiz.ipynb`.
- **Saved outputs are decided notebook by notebook** (unlike 377, which
  commits none). Keep them where a run is too long for class or where
  students need to see a result before they can run it. A ported
  `smoke_test.py` needs a per-notebook allowlist in place of 377's "no
  outputs" check.
- Colab badges point at `github.com/bsheese/387`. They must be updated by hand whenever a file moves.
- `TODO.md` files are tracked. `CLAUDE.md` and `AGENTS.md` are gitignored.
- Not yet ported from 377: `smoke_test.py`, `requirements.txt`, the quiz site,
  vendored `data/`. See the top-level `TODO.md`.
