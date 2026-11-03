# 22_1 Transfer Learning — TODO

**Status:** drafted 2026-10-25 (two notebooks, both with saved outputs). **Days:** 2 of unit 22's 6. **Assumes:** 22_0, 19_0.

Purpose: open up the 19_0 black box, then show how image models fail.

## Notebooks
- [x] `22_1_1_Transfer_Learning.ipynb` (~2.5 min on a laptop CPU): ResNet-18's path with shapes (224 → 7, 3 → 512 channels, global average pooling → the 512 features); residual blocks and why the `+ x` path helps (rates multiply); conv1's 64 filters as color images; layer1 vs. layer4 feature maps on a beagle; a CNN from scratch on the 400 Pets photos at 112 px with augmentation (**test 0.635**); feature extraction from 19_0 (**0.885**); fine-tuning layer4 (lr 1e-4 vs. 1e-3 for the head, frozen layers kept in eval mode, augmentation; **0.885**, the same as feature extraction, after the 2026-11-03 Pets split rebuild; it was 0.920 before), with the point that 1–2 points on 200 test photos can't be told from chance; a table for choosing an approach.
- [x] `22_1_2_What_CNNs_Get_Wrong.ipynb` (~1.5 min): shortcut learning with a class-coded 2×2 marker on Fashion-MNIST (marked 1.000, clean 0.508, wrong marker 0.265 and follows the marker 0.701), Zech et al. 2018 and the ruler example (Narla et al. 2018); distribution shift on the 19_0 model (grayscale 0.93, darker 0.87, zoomed out 0.82, upside down 0.69, blurred 0.62); adversarial examples by FGSM using autograd on the pixels (1.2 brightness levels → accuracy 0.02); bias: Gender Shades (Buolamwini and Gebru 2018) and the follow-up audit (Raji and Buolamwini 2019), tied to 19_0_2 and 19_1_2.
- [ ] `22_1_outline.md`, `22_1_glossary.md`: later pass.

## Runtime
- [x] Time both in Colab. T4 GPU (2026-10-27): both passed; slowest cell 31 to 38 s (the Pets transforms in 22_1_1). Colab CPU (2026-11-02, session D): 22_1_2 passed in 419 s (cells 7, 9 and 13 took 102, 141 and 156 s). **22_1_1 did not finish within the 15-minute cap.** Locally its from-scratch CNN (cell 13) takes 75 s and fine-tuning (cell 17) 67 s, so on Colab's CPU each would take roughly 8 to 14 minutes and the notebook 17 to 27 minutes.
- [x] CPU-only pairs (decided 2026-11-02): students use Colab's free GPU. The intro of 22_1_1 says the notebook needs a GPU, to switch to the partner's account if Colab refuses one, and otherwise to read the saved outputs for the two training cells. No CPU switch.
- [ ] Pair activities: keep the required questions off 22_1_1's cells 13 (the CNN from scratch) and 17 (fine-tuning), so a pair stuck on the CPU can still finish the required part.
