# 22_2 Autoencoders and Diffusion — TODO

**Status:** both notebooks drafted 2026-11-03, with saved outputs (made on a laptop CPU). **Days:** 2, one per notebook. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 22_0.

Decided: generative models get two sessions in the course, not a unit. This is the image one; 23_3 is the text one. Exams test them by reading and reasoning only.

## Notebooks
- [x] `22_2_1_Denoising_Autoencoder.ipynb` (drafted 2026-11-03; ~30 s on a laptop CPU, so about 3 to 4 minutes on Colab's CPU): conv encoder to a 32-number code, transposed-conv decoder (108,881 weights); noise 0.5, fresh noise every batch, MSE against the clean image, 10 epochs (val MSE 0.0198); baselines on the noisy test images: unchanged 0.1178, 3 × 3 blur 0.0462, autoencoder 0.0198; nearest code is the same class 77.6% of the time with no labels (mix-ups among upper-body classes); interpolation trouser → sneaker and random codes (blends and smudges, not new garments); heavier noise and pure noise give a grey average blur, which motivates diffusion.
- [x] `22_2_2_Diffusion.ipynb` (drafted 2026-11-03; ~2.5 min on a laptop CPU): the noise schedule on a 32 × 32 Pets beagle (a and b at steps 0 to 999); training explained (predict the noise, MSE); one denoising step at steps 100/250/500/750 (guess MSE 0.009 / 0.029 / 0.140 / 0.349, the 22_2_1 blur again); a hand-written DDIM loop on `google/ddpm-cifar10-32` with the image and the guess of the end result every 10 steps; 5 / 10 / 50 steps and seeds (same seed, same images); BK-SDM-Small text-to-image as latent diffusion, with the latent decoded every 5 steps (GPU only in class; read the saved output on a CPU); training data, lawsuits, memorization, fabricated images, the safety checker.
- [ ] `22_2_outline.md`, `22_2_glossary.md` (later pass, with the other outlines and glossaries)

## Decide
- [ ] Which diffusion model fits free Colab memory and time. T4 results (2026-10-27): DDPM CIFAR-10 (`google/ddpm-cifar10-32`) loads in 3 s and makes 4 images in 2.1 s with 50 DDIM steps or 29.8 s with all 1,000 steps; BK-SDM-Small loads in 53 s and makes one 512 × 512 image in 3.1 s (2.7 GB); SD 1.5 takes 128 s to load and 4.6 s per image (3.4 GB), so it adds nothing over BK-SDM-Small. Suggested: DDPM CIFAR-10 with a hand-written loop for "denoising, repeated" (the intermediate images are cheap to show), and BK-SDM-Small for one text-to-image cell. CPU results (2026-11-02, free Colab, 2 vCPUs, 1 torch thread): DDPM CIFAR-10 loads in 2 s and makes 1 image in 18.9 s with 50 DDIM steps, or 370 s with all 1,000 steps; BK-SDM-Small loads in 68 s and takes 329 s for one image with only 10 steps. Decision this suggests: the DDIM 50-step loop runs live for every pair, on the GPU or the CPU; the 1,000-step run and the BK-SDM text-to-image cell are shown as saved outputs (or run live only on a GPU).

## Pair activity
- [ ] One pair activity per notebook. 22_2_1: change `NOISE` or the code size (`Autoencoder(code_size=...)`) and compare the test MSE and the pictures; the training cell is short enough to rerun on a CPU. 22_2_2: change the seed and the number of steps in `generate`; keep the required questions off Section 5 (text to image), which needs a GPU.
- [ ] Check whether `pred_original_sample` and the `dtype=` argument still work in Colab's `diffusers` in January 2027.

## Exam
- [ ] Unit 22 exam covers 22_0–22_2
