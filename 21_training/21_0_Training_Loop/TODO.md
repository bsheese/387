# 21_0 Training Loop — TODO

**Status:** rewritten 2026-10-25 as one notebook (no saved outputs). **Days:** 1 of unit 21's 3. **Assumes:** 20.

Decided 2026-10-25: unit 21 is 3 notebooks in 3 days. 21_0_1 builds the loop on Fashion-MNIST and absorbs the old multiclass notebook (21_0_2). Breast cancer is no longer used in the course. The old exercise (21_0_9, wine) is cut.

## Notebooks
- [x] `21_0_1_Training_Loop.ipynb`: Fashion-MNIST introduced (`data/fashion10k.npz`); flattening and scaling (and what flattening loses); `TensorDataset` + `DataLoader` (157 batches of 64); MLP 784-128-10 outputs logits; `nn.CrossEntropyLoss` checked by hand against 19_1_4 and the -log(1/10) starting-loss check; `train_one_epoch` / `evaluate` / `fit` line by line, with `model.train()` / `model.eval()`; Adam (val 0.857) vs. SGD lr 0.01 (0.768) and 0.1 (0.834); test accuracy 0.850 and confusion matrix (Shirt hardest, 0.57).
- [ ] `21_0_outline.md`, `21_0_glossary.md`, `21_0_practice_quiz.ipynb`: stale (old 19_1 content, includes anatomy sections that belong in 20_1). Later pass.

## Activities
- [ ] One pair activity (in `canvas/private/387_*`)
