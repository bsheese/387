# 19_1 ML Foundations (on-ramp) — TODO

**Status:** drafted 2026-10-25 (all four notebooks, outline, glossary, practice quiz), kept without saved outputs (every cell runs in seconds). Redesigned 2026-10-24. **Days:** 4. **Assumes:** 19_0, CS 128 (CS2) Python; pandas NOT guaranteed.

Decided 2026-10-24: **teach the on-ramp through the week-1 image model.** Every session works on the Pets model from 19_0: its predictions, probabilities, training curves and cached features. Newcomers learn the ML basics on something they just built. 377 graduates recognize the ideas but see them on new material instead of redoing Titanic and penguins.

The trimmed 377 notebooks are **not** class time. With no take-home work, they're optional reference for newcomers who want more (link the cs377 sources from each notebook's header).

NumPy/pandas: no separate primer (it would have been pre-work). Teach the few NumPy operations each session needs inside that session (predictions as arrays, `argmax`, comparing arrays, counting). 377's 16_3 / 16_4_1 / 16_5 are optional reference.

## Notebooks (all on the 19_0 Pets model)
- [x] `19_1_1_Is_It_Any_Good.ipynb`: baseline = always predict the most common breed; train / validation / test split; overfitting by fine-tuning too long (the 19_0 per-epoch curves). Concepts from 377 16_1, 17_0_1, 17_1_6. 377 extension: why a validation set exists.
- [x] `19_1_2_Confusion_Matrix.ipynb`: confusion matrix of the model's predictions; per-breed precision and recall; the accuracy paradox, by making one breed rare in a subset. Concepts from 377 18_1_1, 18_1_2. Extension: choose a threshold for one breed under a stated cost.
- [x] `19_1_3_One_Neuron.ipynb`: the model's last layer is a weighted sum of the 512 features. Fit sklearn `LogisticRegression` on the cached features (for 2 of the breeds), then reproduce one image's `predict_proba` by hand: weighted sum, then sigmoid. Concepts from 377 18_2_0_1, 18_2_1, 18_2_3 §1. Extension: fit the neuron with the nudge test in NumPy.
- [x] `19_1_4_Softmax_and_XOR.ipynb`: softmax turns the model's breed scores into probabilities (a table of numbers); then the XOR toy shows what one neuron can't separate, which leads into hidden layers in 20_1. Concepts from 377 18_5_1, 18_2_3 §2. Extension: softmax by hand; predict the hidden layer XOR needs.
- [x] `19_1_outline.md`, `19_1_glossary.md`, `19_1_practice_quiz.ipynb`

## Runtime
- [x] Every cell runs on the saved predictions or cached features from 19_0, so nothing is retrained in class. The overfitting and selection demos in 19_1_1 train a last layer on the cached features, which takes seconds.
- [ ] Time all four in Colab (expected: seconds per cell).

## Notes
- **19_0 outputs are ready** in `data/` (see `data/README.md`): `pets4_predictions.csv` (800 rows with split, breed, prediction, 4 scores, 4 probabilities), `pets4_features.npz` (800 × 512), `pets4_history.csv` (8 epochs) and `pets4_head.pt`. Breeds: Birman, Ragdoll, basset_hound, beagle. Test accuracy 0.90 (Ragdoll 38/50, Birman 46, basset 46, beagle 50).
- The classes are balanced (100 / 50 / 50 per breed), so the "always predict the most common breed" baseline in 19_1_1 is 0.25 on every split. To make the baseline more interesting, use the accuracy-paradox subset (one breed made rare) or a cat-vs-dog framing.
- 19_0's history only runs 8 epochs, where validation accuracy levels off but doesn't drop, so 19_1_1's overfitting demo trains a last layer on the cached features instead (full batch, Adam lr 0.003, 300 epochs). Overfitting on frozen features is mild: validation accuracy stays near 0.9, so the loss plot carries the point.
- 19_1_1 extension: what happens with fewer training photos (the 19_0 `IMAGES_PER_BREED` setting).
- 19_1_4's XOR points must match 20_1_1's XOR data exactly.
- Datasets: Pets (from 19_0) and the XOR toy. Penguins and breast cancer are no longer used in the on-ramp; they first appear in 20_0_3 and 21_0_1.

## As built (2026-10-25)
- **19_1_1**: NumPy arrays, masks and accuracy; three baselines (most common 0.25, random about 0.25, species-then-guess about 0.5); the memorizer; train/val/test accuracy; 300 epochs on cached features (val loss lowest at epoch 32); the selection demo (30 versions, winner +0.041 over average on validation, +0.006 on test).
- **19_1_2**: confusion matrix by hand and with sklearn; precision/recall (Ragdoll 0.905 / 0.76); accuracy paradox (5 Ragdolls in 155 photos, both detectors 0.968); thresholds; cost-based choice on validation (0.35 when false alarms cost 3, 0.15 when misses cost 3; both below 0.5 because this model under-predicts Ragdoll).
- **19_1_3**: weighted sum and dot product; LogisticRegression Birman vs. Ragdoll (test 0.89); `predict_proba` by hand via sigmoid; the neuron; the last layer as a (4, 512) matrix; matrix multiplication and the shape rule; broadcasting.
- **19_1_4**: softmax by hand and for all rows; scaling scores; sigmoid as two-class softmax; cross-entropy loss with logs (test loss 0.255); XOR (best line 3 of 4; LogisticRegression gives weights 0 and 0.5 everywhere); hand-built hidden layer with step activations.
- The 377 extensions listed above are not in the notebooks. They can go in the pair activities (notebooks stand on their own; no partner prompts).

## Activities
- [ ] One pair activity per notebook (4), in `canvas/private/387_*`, sized for a 70-minute class.

## Exam (unit 19)
- [ ] Exam questions are about the Pets model's own outputs (its confusion matrix, its baseline, one image's weighted sum), so recalling 377 isn't enough to answer them.
