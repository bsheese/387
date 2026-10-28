# 22_2 Autoencoders and Diffusion — TODO

**Status:** new. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 22_0.

Decided: generative models get two sessions in the course, not a unit. This is the image one; 23_3 is the text one. Exams test them by reading and reasoning only.

## Notebooks
- [ ] `22_2_1_Denoising_Autoencoder.ipynb`: a small autoencoder that denoises Fashion-MNIST (add noise, train it to remove the noise, look at the bottleneck)
- [ ] `22_2_2_Diffusion_Demo.ipynb`: a pretrained diffusion model (Hugging Face `diffusers`, a small model that fits free Colab), shown as "denoising, repeated"; step through the intermediate images
- [ ] `22_2_outline.md`, `22_2_glossary.md`, `22_2_practice_quiz.ipynb`

## Decide
- [ ] Which diffusion model fits free Colab memory and time. T4 results (2026-10-27): DDPM CIFAR-10 (`google/ddpm-cifar10-32`) loads in 3 s and makes 4 images in 2.1 s with 50 DDIM steps or 29.8 s with all 1,000 steps; BK-SDM-Small loads in 53 s and makes one 512 × 512 image in 3.1 s (2.7 GB); SD 1.5 takes 128 s to load and 4.6 s per image (3.4 GB), so it adds nothing over BK-SDM-Small. Suggested: DDPM CIFAR-10 with a hand-written loop for "denoising, repeated" (the intermediate images are cheap to show), and BK-SDM-Small for one text-to-image cell. Still needs the CPU numbers; if BK-SDM is slow on CPU, show its intermediate steps as saved output.

## Exam
- [ ] Unit 22 exam covers 22_0–22_2
