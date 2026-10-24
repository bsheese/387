# 21_1 Practical Training — TODO

**Status:** exists (was 20_1); **moving from wine quality to Fashion-MNIST** (decided 2026-10-24). **Days:** part of unit 21 (4 teaching days, shared with 21_0). **Assumes:** 21_0 (including 21_0_2, where Fashion-MNIST is introduced).

Purpose: dropout, batch norm, LR schedules, saving/checkpointing and a full pipeline, all on a Fashion-MNIST MLP. Overfitting is easy to see on this data, and 22_0 then swaps the same MLP for a CNN on the same data.

## Notebooks (each one moves to Fashion-MNIST)
- [ ] `21_1_1_Dropout.ipynb`: an oversized MLP that overfits a Fashion-MNIST subset, then dropout; remove the `18_6` reference or add a recap
- [ ] `21_1_2_BatchNorm.ipynb`: or move to 22_0 (see the top-level TODO)
- [ ] `21_1_3_LR_Schedules.ipynb`: connect to the 20_0_3 learning-rate experiment; or fold into 21_1_5
- [ ] `21_1_4_Saving_and_Checkpointing.ipynb`: or make it a reading
- [ ] `21_1_5_Full_Pipeline.ipynb`: end with the MLP that 22_0_2 beats with a CNN; save its test accuracy so 22_0_2 can quote it
- [ ] `21_1_9_Exercise.ipynb`: rewrite off wine onto Fashion-MNIST. Q3 compared against XGBoost on wine, so replace it with a question that fits image data (for example, what an MLP on flattened pixels can't see, as a setup for 22_0).
- [ ] `21_1_outline.md`, `21_1_glossary.md`, `21_1_practice_quiz.ipynb`: update for Fashion-MNIST; fix the bare "20_1" / "19_0" / "19_1" references by hand

## Decide
- [ ] Is batch norm needed before 22 (CNNs use it), or can it move to 22_0?
- [ ] Unit 21 has 4 teaching days for 21_0 and 21_1 together. Choose which 21_1 notebooks become optional or are cut (no take-home work, so readings can't be assigned). Deferred.

## Runtime
- [ ] Each notebook's training run must fit in class (Fashion-MNIST subset, few epochs), or keep its output saved

## Exam
- [ ] Unit 21 exam: read train/val curves, diagnose overfitting, choose a fix
