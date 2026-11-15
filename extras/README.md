# Extras

Notebooks that are not part of CS 387 as it is taught in Spring 2027. They aren't assigned, the pair activities don't use them, and the exams don't test them. They are kept for students who want to go further.

- `22_2_Autoencoders_and_Diffusion/`: a denoising autoencoder on Fashion-MNIST (22_2_1) and diffusion as repeated denoising, ending with a text-to-image model (22_2_2). Removed from the course on 2026-11-15 when it was cut to a basic introduction (see `REVISION_PLAN.md`). The notebooks are unchanged apart from a note at the top, so their references to other notebooks use the numbering from before that reorganization.

`smoke_test.py` skips this folder. To check these notebooks, run them directly, for example `python -m nbconvert --to notebook --execute --output /tmp/out.ipynb extras/22_2_Autoencoders_and_Diffusion/22_2_1_Denoising_Autoencoder.ipynb`.
