# 19_0 Whole Game — TODO

**Status:** new. **Days:** 2 (decided 2026-10-24). **Assumes:** nothing beyond Python.

Purpose: on day one students fine-tune a pretrained image model and use it, before they know what a weight is (fast.ai's order). Say it's a black box on purpose. The 19_1 on-ramp then teaches the ML basics **on this same model** (decided 2026-10-24), and 22_1 opens up the box.

Because 19_1 builds on it, 19_0 must leave behind:
- a fine-tuned model, its predictions and probabilities on a held-out set, and its train/validation accuracy per epoch (for 19_1_1 and 19_1_2);
- the ResNet-18 features (512 numbers per image), computed once and cached, so 19_1_3 can fit a single neuron on them in seconds.

## Notebooks
- [ ] `19_0_1_Your_First_Image_Model.ipynb` (day 1): load a pretrained ResNet-18 (torchvision), fine-tune the last layer on Oxford-IIIT Pets, and predict on new images. Includes day-one Colab setup.
- [ ] `19_0_2_What_Just_Happened.ipynb` (day 2): what the model got right and wrong, with misclassified images; save the predictions, probabilities and cached features for 19_1. Short course intro / history of deep learning, and the ethics prompt.
- [ ] `19_0_outline.md`, `19_0_glossary.md`, `19_0_practice_quiz.ipynb`

## Decide
- [x] Dataset: Oxford-IIIT Pets (decided 2026-10-24).
- [ ] **Classes:** 19_1_4 needs more than 2 classes for softmax, so use a few breeds (3–5) rather than cat vs. dog. All 37 breeds is probably too many to read a confusion matrix.
- [ ] Hide the training code in a helper module, or show it uncommented? (fast.ai shows it; 377's 18_1 used XGBoost as a black box)
- [ ] Where the saved predictions and features live: computed live in class (runtime), or saved in `data/` so 19_1 loads them

## Runtime
- [ ] Day one has setup plus fine-tuning in 70 minutes. It needs a CPU path (fine-tune on a small subset, or load a fine-tuned checkpoint) in case the free GPU isn't available.

## Activities
- [ ] Pair activity (day 1 or 2): change the breeds or the number of training images, then predict and observe the effect on accuracy
- [ ] Ethics prompt: where the images came from and who is missing from them

## Exam
- [ ] Unit 19 exam covers 19_0 + 19_1, asked about this model (see the 19_1 TODO)
