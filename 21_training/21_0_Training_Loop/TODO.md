# 21_0 Training Loop — TODO

**Status:** exists (was 19_1_2, 19_1_3, 19_1_9); 21_0_2 moves to Fashion-MNIST. **Days:** part of unit 21 (4 teaching days, shared with 21_1). **Assumes:** 20.

Purpose: DataLoader, the complete train/validate loop, overfitting curves, Adam vs. SGD, multiclass with CrossEntropyLoss.

Datasets (decided 2026-10-24): breast cancer for 21_0_1, **Fashion-MNIST for 21_0_2** (replaces CTG). CTG and wine are no longer used in the course.

## Notebooks
- [ ] `21_0_1_Training_Loop.ipynb` (breast cancer, keep): 377 references (`18_1`, `18_5`, `18_6`) need recaps for non-377 students. The XGBoost/ensemble comparison (18_6) still works if the baseline result is shown in the notebook.
- [ ] `21_0_2_Multiclass_Classification.ipynb`: **rewrite on Fashion-MNIST** (10 classes, flattened 28×28 → MLP). Introduce the dataset here, since 21_1 and 22 reuse it. Point softmax at 19_1_4 instead of 377 18_5_x. Cross-entropy as "surprise" (−ln 0.9 = 0.11, −ln 0.5 = 0.69, −ln 0.1 = 2.30). The CTG imbalance/class-weight material goes; Fashion-MNIST is balanced.
- [ ] `21_0_9_Exercise.ipynb`: currently wine quality, with reflection Q1 comparing against "the XGBoost result from exercise 18_5_9". **Rewrite** on breast cancer (training-loop practice, XGBoost baseline included in the notebook) or on a Fashion-MNIST subset.
- [ ] `21_0_outline.md`, `21_0_glossary.md`, `21_0_practice_quiz.ipynb`: these are the old 19_1 files. Move the anatomy (20_1_1) parts out to 20_1, update for Fashion-MNIST, and fix the "19_1" headings by hand.

## Weight decay
- [ ] Where Adam + `weight_decay` first appears, connect it to Ridge for 377 graduates, and explain it in one line for everyone else

## Runtime
- [ ] Fashion-MNIST is 60,000 images. Use a subset (for example 10,000 training images) and few epochs for anything run in class.
