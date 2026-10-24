# 22_1 Transfer Learning — TODO

**Status:** new. **Days:** part of unit 22 (6 teaching days). **Assumes:** 22_0, 19_0.

Purpose: open up the 19_0 black box. A pretrained ResNet-18 is a stack of learned filters; replace the head and fine-tune. Then: what CNNs get wrong.

## Notebooks
- [ ] `22_1_1_Transfer_Learning.ipynb`: re-run the 19_0 task with every piece now explained (frozen backbone, new head, fine-tuning); compare against a small CNN trained from scratch on the same Pets data (CIFAR-10 dropped, decided 2026-10-24)
- [ ] `22_1_2_What_CNNs_Get_Wrong.ipynb`: shortcut learning, distribution shift, bias in vision models (face and skin-tone failures); look at misclassified examples
- [ ] `22_1_outline.md`, `22_1_glossary.md`, `22_1_practice_quiz.ipynb`

## Runtime
- [ ] Fine-tuning a ResNet-18 on Pets can be long on CPU. Use a small subset, or keep the full run as a saved output.

