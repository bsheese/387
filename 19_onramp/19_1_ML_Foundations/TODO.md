# 19_1 ML Foundations (on-ramp) — TODO

**Status:** new; redesigned 2026-10-24. **Days:** 4. **Assumes:** 19_0, CS 128 (CS2) Python; pandas NOT guaranteed.

Decided 2026-10-24: **teach the on-ramp through the week-1 image model.** Every session works on the Pets model from 19_0: its predictions, probabilities, training curves and cached features. Newcomers learn the ML basics on something they just built. 377 graduates recognize the ideas but see them on new material instead of redoing Titanic and penguins.

The trimmed 377 notebooks are **not** class time. With no take-home work, they're optional reference for newcomers who want more (link the cs377 sources from each notebook's header).

NumPy/pandas: no separate primer (it would have been pre-work). Teach the few NumPy operations each session needs inside that session (predictions as arrays, `argmax`, comparing arrays, counting). 377's 16_3 / 16_4_1 / 16_5 are optional reference.

## Notebooks (all on the 19_0 Pets model)
- [ ] `19_1_1_Is_It_Any_Good.ipynb`: baseline = always predict the most common breed; train / validation / test split; overfitting by fine-tuning too long (the 19_0 per-epoch curves). Concepts from 377 16_1, 17_0_1, 17_1_6. 377 extension: why a validation set exists.
- [ ] `19_1_2_Confusion_Matrix.ipynb`: confusion matrix of the model's predictions; per-breed precision and recall; the accuracy paradox, by making one breed rare in a subset. Concepts from 377 18_1_1, 18_1_2. Extension: choose a threshold for one breed under a stated cost.
- [ ] `19_1_3_One_Neuron.ipynb`: the model's last layer is a weighted sum of the 512 features. Fit sklearn `LogisticRegression` on the cached features (for 2 of the breeds), then reproduce one image's `predict_proba` by hand: weighted sum, then sigmoid. Concepts from 377 18_2_0_1, 18_2_1, 18_2_3 §1. Extension: fit the neuron with the nudge test in NumPy.
- [ ] `19_1_4_Softmax_and_XOR.ipynb`: softmax turns the model's breed scores into probabilities (a table of numbers); then the XOR toy shows what one neuron can't separate, which leads into hidden layers in 20_1. Concepts from 377 18_5_1, 18_2_3 §2. Extension: softmax by hand; predict the hidden layer XOR needs.
- [ ] `19_1_outline.md`, `19_1_glossary.md`, `19_1_practice_quiz.ipynb`

## Runtime
- [ ] Every cell runs on the saved predictions or cached features from 19_0, so nothing is retrained in class. The only exception is the overfitting demo, which can use the saved curves.

## Notes
- 19_1_4's XOR points must match 20_1_1's XOR data exactly.
- Datasets: Pets (from 19_0) and the XOR toy. Penguins and breast cancer are no longer used in the on-ramp; they first appear in 20_0_3 and 21_0_1.

## Exam (unit 19)
- [ ] Exam questions are about the Pets model's own outputs (its confusion matrix, its baseline, one image's weighted sum), so recalling 377 isn't enough to answer them.
