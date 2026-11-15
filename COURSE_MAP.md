# cs387 Course Map

The whole course on one page: what each unit teaches, what it assumes, where each core idea is first taught, and how the term is laid out. The reasoning behind the original design is in `PROPOSAL.md` (an October 2026 snapshot). The current plan, including the cuts made on 2026-11-15 and the order of the remaining work, is in `REVISION_PLAN.md`. Build tasks are in the `TODO.md` file in each module directory.

387 follows on from cs377 (units 16 to 18) and continues its numbering at 19. Not every student takes 377 first: the prerequisite is CS/DASC 377, **or** CS 128 (C- or above) plus CS/MATH 136. Unit 19's on-ramp covers the gap. No unit requires calculus. Since 2026-11-15 the course is a basic introduction to deep learning, and material that is mainly about training models well, or about mechanisms practitioners tune, has been cut (`REVISION_PLAN.md`, "What is cut").

First offering of this design: **Spring 2027**, Tuesday/Thursday, 9:25 to 10:40 (75 minutes), 28 class meetings.

**Exams:** five, one after each unit. The exams for units 19 to 22 are given in class; the unit 23 exam is given in the final exam period. There is no final project (cut 2026-10-24). An exam can ask about anything assigned (the notebook, the pre-class demo and the pair activity) and assumes the activities were done, but everything it tests is material in the core notebooks.

**Grade weights:** exams 80% (5 × 16%), pair activities 20%, practice quizzes 0% (ungraded).

**Required reading, no graded take-home work** (decided 2026-10-24, revised 2026-11-15). Before each class that has a pair activity, students read that class's notebook and do its pre-class demo. A reading check at the start of class checks both. Nothing graded is done outside class: the reading check, the pair activity and the exams all happen in class. Videos, the cs377 reference notebooks and practice quizzes are optional.

**A class:** a 3-minute paper reading check, then about 72 minutes of pair activity. Unit 19 activities have 5 required and 2 extra-credit questions, units 20 to 23 have 6 and 2 by default, and the first class has 3 and 2 (sized from the Fall 2026 377 activities; see `REVISION_PLAN.md`).

**Pre-class demos:** each class except the first has a required demo with a Canvas walkthrough page ("To Do:" naming, as in 125). For now a demo is a set of steps in Colab using the notebook's own cells, or a walkthrough of TensorFlow Playground, CNN Explainer or Transformer Explainer. A separate interactive demo app will be built later. Demos and activities introduce no new material: everything in them must already be in the notebook.

**Runtime rule for class time:** in-class pair activities can't contain cells that take a long time on free Colab. Use small subsets, few epochs and pretrained weights. If a result needs a long run, show it as a saved output or load it from a file.

---

## The Arc

```
19  Whole game      →  20  How networks   →  21  Training      →  22  Images       →  23  Language
    + on-ramp            learn                 in practice

19_0 → 19_1             20_0 → 20_1          21_0 → 21_1          22_0 → 22_1            23_0 → 23_1 → 23_2 → 23_3
whole  on-ramp          tensors, anatomy     loop   overfitting   conv   transfer        tokens attn  pre-   gen +
game   (on the same     nudge,   & XOR              & early              learning,       & emb.       trained limits
       Pets model)      autograd                    stopping             failures
                                                    (Fashion-MNIST from here through 22_0)
```

## Datasets

Four datasets, plus the four-point XOR toy.

| Dataset | Used in | Replaces |
|---|---|---|
| Oxford-IIIT Pets | 19_0 (whole game), 19_1 (the whole on-ramp), 22_1 (transfer learning, failures) | student photos, CIFAR-10, Titanic, German Credit |
| Palmer penguins | 20_0_2 (gradient descent) | Auto MPG |
| Fashion-MNIST (`data/fashion10k.npz`: 10k train / 5k val / 10k test) | 21_0_1 (training loop), 21_1_1 (overfitting), 22_0 (CNN), 22_1_2 (planted shortcut) | Wisconsin breast cancer, CTG fetal health, wine quality |
| IMDB reviews | 23_0 to 23_2 | the student-chosen text set |
| XOR (4 points, toy) | 19_1_5, 20_1_1 | none |

Pretrained models (ResNet-18, DistilBERT, GPT-2 small, SmolLM2) are not counted as datasets.

## Units at a Glance

| Unit | Modules | Notebooks | Role | Datasets | Assumes |
|---|---|---|---|---|---|
| `19_onramp` | `19_0_Whole_Game`, `19_1_ML_Foundations` | 19_0_1, 19_0_2; 19_1_1 to 19_1_5 | Fine-tune a pretrained image model in the first two classes, then a five-class ML on-ramp taught on that same model (baselines and the three-way split, the confusion matrix, one neuron, softmax and the loss, XOR and the hidden layer); NumPy taught as needed | Pets, XOR | CS 128 or 377 |
| `20_how_networks_learn` | `20_0_PyTorch_Basics`, `20_1_Network_Anatomy` | 20_0_1, 20_0_2; 20_1_1 | Tensors, the nudge test, autograd, gradient descent; `nn.Module`, ReLU and a network that learns XOR | Penguins, XOR | 19_1 |
| `21_training` | `21_0_Training_Loop`, `21_1_Practical_Training` | 21_0_1; 21_1_1 | The training loop built line by line; overfitting, dropout, more data, early stopping, a checklist | Fashion-MNIST | 20 |
| `22_images` | `22_0_Convolution_and_CNNs`, `22_1_Transfer_Learning` | 22_0_1, 22_0_2; 22_1_1, 22_1_2 | Convolution by hand, a CNN against the MLP on the same Fashion-MNIST, transfer learning on Pets, what image models get wrong (shortcuts, distribution shift, bias) | Fashion-MNIST, Pets | 21 |
| `23_language` | `23_0_Tokens_and_Embeddings`, `23_1_Attention`, `23_2_Pretrained_Transformers`, `23_3_Generation_and_Limits` | 23_0_1, 23_0_2; 23_1_1; 23_2_1, 23_2_2; 23_3_1, 23_3_2 | Tokens, embeddings, attention as a weighted average, pretrained pipelines and fine-tuning DistilBERT, sampling and temperature, what LLMs get wrong | IMDB (`data/imdb_reviews.csv`) | 21, 22_1 (transfer learning) |

The autoencoder and diffusion notebooks (formerly 22_2) are in `extras/` as optional, unassessed reading.

**Session budget** (Spring 2027 calendar checked 2026-11-15). 28 meetings: 23 notebook classes, 1 review day and 4 in-class exams. Spring recess removes Mar 9 and 11. The dated, class-by-class layout is in `REVISION_PLAN.md`.

| Unit | Meetings | Notebook classes | Review | Exam |
|---|---|---|---|---|
| 19 | 1 to 8 (Jan 7 to Feb 2) | 7 | none | meeting 8, Feb 2 |
| 20 | 9 to 12 (Feb 4 to Feb 16) | 3 | none | meeting 12, Feb 16 |
| 21 | 13 to 15 (Feb 18 to Feb 25) | 2 | none | meeting 15, Feb 25 |
| 22 | 16 to 21 (Mar 2 to Mar 25, recess inside) | 4 | meeting 20, Mar 23 | meeting 21, Mar 25 |
| 23 | 22 to 28 (Mar 30 to Apr 20) | 7 | none | final exam period, Apr 23 to 28 |
| **Total** | 28 | **23** | 1 | 4 in class + 1 in the exam period |

**Sequencing notes.**
- 19_0 is deliberately a black box: students fine-tune a pretrained model before they know what a weight is, and 19_0_2 points forward to the units that open it up.
- 19_1 runs entirely on 19_0's saved predictions and cached features. The Pets course copy (`data/pets4_*`) is frozen; see the 19_0 TODO.
- 22_1 opens up the black box from 19_0, on the same Pets data. 23_2 does the same thing for text.
- 21 must come before 22: 22_0 reuses unit 21's Fashion-MNIST MLP and training loop, and swaps in a CNN on the same data.
- 23_3 (generation) is tested by reading and reasoning only.

## Where Concepts Are First Taught (and Reprised)

| Concept | First taught | Reprised / deepened |
|---|---|---|
| Pretrained model, transfer learning (black box) | 19_0 | 22_1 (opened up), 23_2 (text) |
| NumPy arrays (as needed) | 19_1, inside each class | 20_0_1 (tensors as arrays that track how they were computed) |
| Baseline, three-way split, overfitting | 19_1_1 (on the Pets model) | 21_0_1 (validation set, loss curves), 21_1_1 |
| Confusion matrix, precision and recall | 19_1_2 (on the Pets model) | 21_0_1, every later evaluation |
| Sigmoid, weighted sum, one neuron, matrix shapes | 19_1_3 (the Pets model's last layer) | 20_1_1 (`nn.Linear` + sigmoid) |
| Softmax | 19_1_4 (Pets breed scores) | 21_0_1 (`CrossEntropyLoss` on logits), 23_1 (attention weights), 23_3 (temperature) |
| Cross-entropy as "surprise" | 19_1_4 | 20_1_1 (BCE), 21_0_1 (`nn.CrossEntropyLoss`), 23_3 (next-token loss) |
| XOR limit, hidden layer | 19_1_5 (XOR toy) | 20_1_1 (XORNet learns it) |
| Tensors, batch dimension, device | 20_0_1 | everything after |
| Nudge test (slope by measurement) | 20_0_1 | 20_0_2 (gradient descent) |
| Autograd as an automatic nudge test | 20_0_1 | everything after |
| Rates multiply (backprop without calculus) | 20_0_1 | 20_1_1 |
| Learning rate, loss bowl | 20_0_2 | 21_0_1 |
| Training loop, DataLoader | 21_0_1 | 22, 23 (same loop) |
| Dropout, train/eval mode, more data | 21_1_1 (Fashion-MNIST MLP) | 22_0 |
| Early stopping | 21_1_1 | 22_0_2 |
| Convolution as sliding multiply-add | 22_0_1 | 22_0_2, 22_1 |
| Transfer learning, feature extraction against fine-tuning | 22_1_1 | 23_2 |
| Shortcuts, distribution shift, bias by group | 22_1_2 | 23_2_1 (model card bias), 23_3_2 |
| Tokens, embeddings | 23_0 | 23_1, 23_2 |
| Attention as a weighted average | 23_1_1 | 23_2, 23_3 |
| Sampling, temperature | 23_3_1 | 23_3_2 |

## Ethics Thread

- 19_0_2: where the training images came from, and who is missing from them (purebreds only, web photos, ImageNet's person categories)
- 21: none (the malignant-recall item left with breast cancer)
- 22_1_2: shortcut learning, distribution shift, Gender Shades and disaggregated evaluation
- 23_0_1: tokenizer cost by language
- 23_2_1: the model card's country bias, pronoun associations in fill-mask
- 23_3_2: hallucination, answers that change with the form of the question

## Maintenance Notes

- Module layout follows 377: `<unit>/<module>/` holds the notebooks plus `*_outline.md` and `*_glossary.md`. The outlines and glossaries are out of date and are rewritten in a later pass. There are no practice quiz notebooks (dropped 2026-11-02); practice quizzes, if any, live on the quiz site only.
- Notebooks were renumbered on 2026-11-15 (`REVISION_PLAN.md`, step B): old 20_0_1 (tensors) was merged into the autograd notebook, which became 20_0_1, and gradient descent became 20_0_2; 19_1_4 was split into 19_1_4 and 19_1_5; 21_1_2 was merged into 21_1_1. Documents dated before then use the old numbers.
- **Saved outputs are decided notebook by notebook** (unlike 377, which commits none). `smoke_test.py` lists the notebooks that keep them in `KEEP_OUTPUTS` and skips `extras/`.
- `tools/check_core.py` measures each class's Pair path against the time budget, from `tools/core_paths.csv`. `venv-colab/` is a venv on Colab's library versions for number checks (`tools/requirements-colab.txt`).
- Colab badges point at `github.com/bsheese/387`. They must be updated by hand whenever a file moves.
- `TODO.md` files are tracked. `CLAUDE.md` and `AGENTS.md` are gitignored.
- Not yet ported from 377: the quiz site. See the top-level `TODO.md`.
