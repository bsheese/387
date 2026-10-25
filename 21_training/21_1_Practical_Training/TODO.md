# 21_1 Practical Training — TODO

**Status:** rewritten 2026-10-25 as two notebooks (no saved outputs). **Days:** 2 of unit 21's 3. **Assumes:** 21_0_1.

Decided 2026-10-25: the five old notebooks (dropout, batch norm, LR schedules, checkpointing, full pipeline) and the exercise (21_1_9, wine) became two. Batch norm moved to 22_0; 21_1_1 only explains its train/eval behavior (and why 19_0 kept ResNet-18 in eval mode).

## Notebooks
- [x] `21_1_1_Overfitting_and_Regularization.ipynb`: big MLP (784-512-512-10, 670k weights) on 1,000 images for 60 epochs (train 0.997, val 0.803, val loss 0.578 at epoch 9 -> 0.979); `nn.Dropout` demo in train/eval mode; dropout 0.5 (val loss 0.678, acc 0.814); train vs. eval measurement demo; batch norm's running averages and the 19_0 connection; weight decay with AdamW 1.0 (val loss 0.732) and the Ridge connection; more data (10,000 images: best val acc 0.870); early stopping previewed.
- [x] `21_1_2_Training_a_Model_Well.ipynb`: `fit` with checkpointing and patience (stops at epoch 19, restores epoch 14); `torch.save` / `load_state_dict(torch.load(..., weights_only=True))`; the architecture-mismatch error; cosine annealing (plot of the rate; constant vs. cosine final val loss 0.408 vs. 0.384); the full recipe (dropout 0.3, AdamW 0.05, cosine, early stopping): **test accuracy 0.869, the MLP number 22_0 compares against**; a 7-step training checklist.
- [ ] `21_1_outline.md`, `21_1_glossary.md`, `21_1_practice_quiz.ipynb`: stale (old wine-based 20_1 content). Later pass.

## Runtime
- [x] Every training run fits in class: locally 8 s (21_0_1), 18 s (21_1_1) and 34 s (21_1_2) for whole notebooks on CPU. Still to time in Colab.

## Activities
- [ ] Pair activities for 21_1_1 and 21_1_2 (in `canvas/private/387_*`). Candidates from the cut exercises: dropout rate sweep, patience choice, reading curves to diagnose over/underfitting.

## Exam
- [ ] Unit 21 exam: read train/val curves, diagnose overfitting, choose a fix
