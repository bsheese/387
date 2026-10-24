# 22_0 Convolution and CNNs — TODO

**Status:** new. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 21 (reuses the 21_0 training loop unchanged).

Purpose: convolution as "slide a 3×3 grid of numbers over the image and multiply-add", then a first CNN.

## Notebooks
- [ ] `22_0_1_Convolution_by_Hand.ipynb`: a 5×5 image, a 3×3 edge filter, by hand in NumPy, then `nn.Conv2d` gives the same numbers; pooling; what a feature map is
- [ ] `22_0_2_First_CNN.ipynb`: the same Fashion-MNIST data as 21_1. Swap the 21_1_5 MLP for a small CNN and show the accuracy jump; parameter counts; train/val curves
- [ ] `22_0_3_Augmentation.ipynb`: torchvision transforms as a regularizer (connect to 21_1)
- [ ] `22_0_outline.md`, `22_0_glossary.md`, `22_0_practice_quiz.ipynb`

## Activities
- [ ] CNN Explainer pair activity: trace one 3×3 filter by hand, then find it in the tool
- [ ] Optional: Learn PyTorch ch. 03 (Computer Vision) as reference reading (Spring 2025 used it)

## Notes
- Runtime rule: no long-running cells in class. Use a Fashion-MNIST subset and few epochs; show longer runs as saved outputs.
