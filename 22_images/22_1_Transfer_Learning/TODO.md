# 22_1 Transfer Learning — TODO

**Status:** drafted 2026-10-25 (two notebooks, both with saved outputs). **Days:** 2 of unit 22's 6. **Assumes:** 22_0, 19_0.

Purpose: open up the 19_0 black box, then show how image models fail.

## Notebooks
- [x] `22_1_1_Transfer_Learning.ipynb` (~2.5 min on a laptop CPU): ResNet-18's path with shapes (224 → 7, 3 → 512 channels, global average pooling → the 512 features); residual blocks and why the `+ x` path helps (rates multiply); conv1's 64 filters as color images; layer1 vs. layer4 feature maps on a beagle; a CNN from scratch on the 400 Pets photos at 112 px with augmentation (**test 0.655**); feature extraction from 19_0 (**0.900**); fine-tuning layer4 (lr 1e-4 vs. 1e-3 for the head, frozen layers kept in eval mode, augmentation; **0.920**), with the point that 1–2 points on 200 test photos can't be told from chance; a table for choosing an approach.
- [x] `22_1_2_What_CNNs_Get_Wrong.ipynb` (~1.5 min): shortcut learning with a class-coded 2×2 marker on Fashion-MNIST (marked 1.000, clean 0.508, wrong marker 0.265 and follows the marker 0.701), Zech et al. 2018 and the ruler example (Narla et al. 2018); distribution shift on the 19_0 model (grayscale 0.93, darker 0.87, zoomed out 0.82, upside down 0.69, blurred 0.62); adversarial examples by FGSM using autograd on the pixels (1.2 brightness levels → accuracy 0.02); bias: Gender Shades (Buolamwini and Gebru 2018) and the follow-up audit (Raji and Buolamwini 2019), tied to 19_0_2 and 19_1_2.
- [ ] `22_1_outline.md`, `22_1_glossary.md`, `22_1_practice_quiz.ipynb`: later pass.

## Runtime
- [ ] Time both in Colab (GPU and CPU). Fine-tuning and the from-scratch CNN are the long cells.
