# 19_0 Whole Game — TODO

**Status:** drafted 2026-10-25 (both notebooks, outline, glossary); not yet tested in Colab. **Days:** 2 (decided 2026-10-24). **Assumes:** nothing beyond Python.

Purpose: on day one students fine-tune a pretrained image model and use it, before they know what a weight is (fast.ai's order). Say it's a black box on purpose. The 19_1 on-ramp then teaches the ML basics **on this same model** (decided 2026-10-24), and 22_1 opens up the box.

What 19_0 leaves behind for 19_1 (all in `data/`, see `data/README.md`):
- `pets4_head.pt`: the trained last layer, so the model can be rebuilt without training
- `pets4_history.csv`: train loss, train accuracy and validation accuracy per epoch (8 epochs)
- `pets4_predictions.csv`: predicted breed, 4 scores and 4 probabilities for all 800 photos
- `pets4_features.npz`: the 512 ResNet-18 features for all 800 photos

## Notebooks
- [x] `19_0_1_Your_First_Image_Model.ipynb` (day 1): Colab setup, the photos, the pretrained ResNet-18's own ImageNet guesses, freeze + replace the last layer, train 8 epochs, test accuracy, `predict()`, upload your own photo, save.
- [x] `19_0_2_What_Just_Happened.ipynb` (day 2): rebuild from the course copy, the 512 features, test results table and crosstab, the mistakes, confidence, other breeds, save outputs for 19_1, history timeline, where the photos came from (ethics).
- [x] `19_0_outline.md`, `19_0_glossary.md` (practice quiz notebook removed 2026-11-02)

## Decided
- [x] Dataset: Oxford-IIIT Pets (decided 2026-10-24).
- [x] **Classes** (decided 2026-10-25): 4 breeds, in look-alike pairs: Birman, Ragdoll, basset hound, beagle. Saved run: test accuracy 0.90; mistakes are 12 Ragdoll→Birman, 4 Birman→Ragdoll, 4 basset→beagle, no cat/dog confusions.
- [x] **Training code is shown** (decided 2026-10-25), with comments, labeled as code to run and watch rather than study.
- [x] **Saved predictions and features go in `data/`** (decided 2026-10-25), made by running the notebooks. 19_1 downloads them, so every student sees the same numbers.
- [x] Both notebooks keep their saved outputs (listed in `KEEP_OUTPUTS` in `smoke_test.py`). They are the CPU fallback, and 19_1 refers to the same numbers.

## Design notes
- The model stays in `eval()` mode the whole time, including during training. In `train()` mode the frozen ResNet would still update its batch-norm statistics, and then saving only the last layer would not reproduce the model. 21_1 explains train vs. eval mode.
- Data comes from `data/pets4.zip` (17 MB, built by `data/make_pets4.py`) rather than the 800 MB full dataset.
- The notebooks only work in Colab after `data/` is pushed to GitHub.

## Runtime
- [x] CPU path: the notebook works on a CPU, and `USE_COURSE_COPY = True` loads the trained last layer if training is too slow.
- [ ] **Time it in Colab**, on both the free GPU and the CPU runtime. Locally (M2 CPU), one epoch is about 7 s as a script; as a guess, free Colab's CPU is 3–5 times slower, which puts 8 epochs at a few minutes. 19_0_2's slowest cell (features for 800 photos) takes 14 s locally. Local timings of the training cell were inconsistent: about 1 minute in most runs, but 6 and 17 minutes in two nbconvert runs. Per-batch timing inside a kernel later showed the normal speed, so the slow runs look like a problem with this machine, not with the notebook. That is one more reason to time it in Colab.
  - **Colab CPU (2026-11-02, session B):** 19_0_1 runs in 646 s in total; the training cell (`EPOCHS = 8`, `IMAGES_PER_BREED = 100`) takes 581 s, about 73 s per epoch; the test-accuracy cell 31 s. 19_0_2 runs in 144 s. On the T4 (2026-10-27) no 19_0 cell took more than 31 s. So day 1 works on the CPU but has about 10 minutes of waiting, and the `IMAGES_PER_BREED` pair activity below would cost up to 10 minutes per retrain on the CPU. Options for the activity: have CPU pairs use fewer epochs (3 is probably enough for a frozen backbone), or compute the ResNet features once and train only the last layer on them, as 19_0_2 does, so each retrain takes seconds. Still to time: the GPU numbers for this notebook alone.
- [ ] **Near-duplicate photos across splits** (found by a blind review, 2026-11-02). Validation `Birman_199.jpg` is the same photo as training `Birman_25.jpg` (feature cosine similarity 0.997), and test `basset_hound_121.jpg` is a back-to-back shot of training `basset_hound_120.jpg` (0.956); the highest similarity between two training photos is 0.932. `make_pets4.py` shuffles each breed separately, so near-duplicates can land in different splits. Fix: group photos whose features are nearly identical and keep each group in one split, then rebuild `pets4.zip`, `pets4_head.pt`, `pets4_history.csv`, `pets4_predictions.csv` and `pets4_features.npz`, re-execute 19_0, and re-check every number quoted in 19_0 and 19_1. 19_0_1 says the test photos are ones the model "has never seen", and 19_1_1 teaches splits, so this matters more than its small effect on accuracy.
- [x] Review fixes (2026-11-02): re-running training now starts from the same random layer (so the `IMAGES_PER_BREED` activity trains from scratch); the `USE_COURSE_COPY` shortcut works without running the training cell and also loads the course history; "fine-tuning" renamed to feature extraction (matching 22_1); ImageNet versions, layers, biases, softmax and logistic regression defined; out-of-breed confidence claims match the outputs; day references removed; seaborn plots; HEIC/EXIF handling for uploads; `fetch()` no longer leaves half-downloaded files. Re-executed: the run reproduces the course copy exactly.
- [ ] `fetch()` in the other notebooks still writes straight to the final file name; copy the 19_0 version (download to `name + '.part'`, then `os.replace`) when each is next revised.
- [ ] The 19_0_2 mistakes grid makes the notebook about 4 MB. Shrink the figures if that becomes a problem.

## Activities
- [ ] Pair activity (day 1 or 2): change `IMAGES_PER_BREED` (for example 5, 20, 100), retrain, and compare accuracy and the mistakes. Changing the breeds would need more breeds in `pets4.zip`.
- [ ] Ethics prompt: 19_0_2 Section 9 explains the issues (purebreds only, web photos, ImageNet labels, how test examples are chosen); the discussion questions go in the pair activity.

Notebooks stand on their own: no "discuss with your partner" prompts in them (decided 2026-10-25). Discussion questions live in the pair activities.

## Exam
- [ ] Unit 19 exam covers 19_0 + 19_1, asked about this model (see the 19_1 TODO)
