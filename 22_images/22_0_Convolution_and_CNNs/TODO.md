# 22_0 Convolution and CNNs — TODO

**Status:** new. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 21 (reuses the 21_0 training loop unchanged).

Purpose: convolution as "slide a 3×3 grid of numbers over the image and multiply-add", then a first CNN.

## Notebooks
- [ ] `22_0_1_Convolution_by_Hand.ipynb`: a 5×5 image, a 3×3 edge filter, by hand in NumPy, then `nn.Conv2d` gives the same numbers; pooling; what a feature map is
- [ ] `22_0_2_First_CNN.ipynb`: the same Fashion-MNIST data as 21_1 (`data/fashion10k.npz`). Swap 21_1_2's MLP for a small CNN and show the accuracy jump against the MLP's **test accuracy 0.869** (21_1_2's full recipe; Shirt 0.62 was its weakest class); parameter counts; train/val curves. Reuse 21_1_2's `fit` (early stopping, checkpoint, cosine).
- [ ] **Batch norm** (moved here from 21_1 on 2026-10-25): `nn.BatchNorm2d` in the CNN. 21_1_1 already explained its train/eval behavior (running averages) and the 19_0 connection; here cover what it does to training.
- [ ] `22_0_3_Augmentation.ipynb`: torchvision transforms as a regularizer (connect to 21_1)
- [ ] `22_0_outline.md`, `22_0_glossary.md`, `22_0_practice_quiz.ipynb`

## Activities
- [ ] CNN Explainer pair activity: trace one 3×3 filter by hand, then find it in the tool
- [ ] Optional: Learn PyTorch ch. 03 (Computer Vision) as reference reading (Spring 2025 used it)

## Notes
- Runtime rule: no long-running cells in class. Use a Fashion-MNIST subset and few epochs; show longer runs as saved outputs.
