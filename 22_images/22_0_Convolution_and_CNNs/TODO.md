# 22_0 Convolution and CNNs — TODO

**Status:** drafted 2026-10-25 (two notebooks). **Days:** 2 of unit 22's 6. **Assumes:** 21 (reuses 21_1_2's recipe).

Decided 2026-10-25: augmentation is a section of 22_0_2, not its own notebook (unit 22 = 22_0_1, 22_0_2, 22_1_1, 22_1_2, 22_2_1, 22_2_2, one day each). Batch norm moved here from 21_1.

## Notebooks
- [x] `22_0_1_Convolution_by_Hand.ipynb` (no saved outputs; runs in seconds): a 6×6 edge image and a 3×3 vertical-edge filter by hand (feature map of 0s and 3s); `nn.Conv2d` gives the same; vertical/horizontal edge and blur filters on a Fashion-MNIST ankle boot; channels and weight shapes (ties to ResNet's (64, 3, 7, 7)); padding, stride and the output-size formula; max pooling; weight count Conv2d(1, 32, 3) = 320 vs. Linear = 19.7M; link to CNN Explainer.
- [x] `22_0_2_First_CNN.ipynb` (saved outputs; ~3 min on a laptop CPU): two conv blocks (conv, BN, ReLU, pool) + MLP head, 421,834 weights; layer-by-layer shape printout; 12 epochs with 21_1_2's recipe: **test 0.897 vs. MLP 0.869**, per-class gains (coat +0.09, T-shirt +0.05, shirt +0.04); learned first-layer filters and feature maps; shift test (MLP 0.869 → 0.53 at 2 px; CNN 0.897 → 0.818 at 2 px, 0.587 at 3 px); batch norm explained, with/without over 5 epochs (val loss 0.297 vs. 0.376); augmentation (shift + flip) on 1,000 images with a constant LR (train 0.895 vs. 0.999, final val loss 0.485 vs. 0.661, best val acc 0.833 vs. 0.846).
- [ ] `22_0_outline.md`, `22_0_glossary.md`: later pass.

## Activities
- [ ] CNN Explainer pair activity: trace one 3×3 filter by hand, then find it in the tool
- [ ] Optional: Learn PyTorch ch. 03 (Computer Vision) as reference reading (Spring 2025 used it)

## Runtime
- [x] Time 22_0_2 in Colab. T4 GPU (2026-10-27): passed, no cell over 38 s. Colab CPU (2026-11-02, session D): **did not finish within the 15-minute cap**. Local M2 cell times are 53 s (cell 11, the 12-epoch CNN), 11 s (cell 13, the MLP), 40 s (cell 19, batch norm on/off) and 48 s (cell 23, augmentation), 160 s in all; Colab's CPU ran 7 to 11 times slower than the M2 in sessions B to D, so the whole notebook would take roughly 20 to 30 minutes there, with each of those three cells taking 5 to 10 minutes.
- [x] CPU-only pairs (decided 2026-11-02): students use Colab's free GPU. The intro of 22_0_2 says the notebook needs a GPU, to switch to the partner's account if Colab refuses one, and otherwise to read the saved outputs for the training cells. No CPU switch.
- [ ] Pair activity: keep the required questions off cells 11, 19 and 23 (the long training cells), so a pair stuck on the CPU can still finish the required part.
