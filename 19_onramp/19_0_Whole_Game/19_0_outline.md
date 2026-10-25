# 19_0 The Whole Game: Topic Outline

This document outlines the topics covered in the two 19_0 notebooks. 19_0 takes
two class days, one per notebook. Students fine-tune a pretrained image model on
day one, before they know what a weight is, and treat it as a black box on
purpose. 19_1 then teaches the basics of evaluating a model on this same model,
and 22_1 explains transfer learning.

---

## 19_0_1: Your First Image Model (day 1)

**Dataset:** Oxford-IIIT Pets, four breeds (Birman, Ragdoll, basset hound, beagle),
from `data/pets4.zip`

### Why start with a working model
- The order of the course: the whole model first, then its parts (fast.ai's approach)
- Where each piece of today's code is explained later (19_1, unit 20, unit 21, 22_1)

### Setting up Colab
- Running on Google's computers; asking for a T4 GPU through Runtime → Change runtime type
- What a GPU is good for (many multiplications at once)
- The CPU path: everything still works, the training cell is slower, and there is a shortcut

### The photos
- The Oxford-IIIT Pet dataset (2012): 37 breeds, about 200 photos each
- The four breeds come in look-alike pairs, so the problem is harder than cat vs. dog
- Training, validation and test photos (100 / 50 / 50 per breed); why a score on the
  training photos isn't a fair measure (19_1_1 covers this properly)
- One folder per breed; the folder name is the label
- How much the photos vary within a breed

### A pretrained model
- ResNet-18 (2015, 18 layers, about 11.7 million weights), trained on ImageNet
  (about 1.2 million photos, 1,000 categories)
- What "pretrained" means and why most deep learning starts from a pretrained model
- `weights.transforms()`: resize, center crop to 224 × 224, rescale colors as in training
- The pretrained model's own top-3 guesses: it has "beagle" and "basset" but no Birman or
  Ragdoll, so it names the cats "Siamese cat" and "Persian cat"

### Fine-tuning the last layer
- The last layer turns 512 numbers into 1,000 scores; we replace it with one that gives 4
- Freezing the pretrained weights (`requires_grad = False`); only 2,052 numbers are trained
- `IMAGES_PER_BREED`: how many training photos per breed the model learns from
- Batches, the loss, nudging the weights, epochs (described, not explained)
- The training loop shown in full, as code to run and watch (unit 21 explains it)
- Accuracy on training and validation photos after each epoch; the plot against
  random guessing (0.25)
- The shortcut: `USE_COURSE_COPY = True` loads the course's trained last layer

### The test set and new photos
- Test accuracy (0.90 in the saved run, 180 of 200)
- Why it works with so few photos: the pretrained network already knows what animals look like
- `predict(path)`: the four probabilities for one photo
- Uploading your own photo in Colab; the model always answers with one of the four breeds

### Saving
- `my_pets4_head.pt` (the trained last layer) and `my_pets4_history.csv`
- Colab deletes files at the end of a session; 19_0_2 uses the course copy

---

## 19_0_2: What Just Happened? (day 2)

**Dataset:** the same four breeds, plus 10 photos of other breeds (`pets4/other/`)

### Rebuilding the model
- Loading the course copy of the last layer so everyone has the same model
  (19_1 and the unit 19 exam ask about this model)

### Every photo as 512 numbers
- **Features**: the 512 numbers the rest of the network computes from a photo
- Taking the last layer out with `nn.Identity()` to see them; a (800, 512) array
- The individual features have no names we can give them; they were learned on ImageNet
- The last layer alone turns features into 4 scores; **softmax** turns scores into
  probabilities that add up to 1 (19_1_4 explains softmax)
- Check: same probabilities as running the whole model on the photo

### The test results
- A pandas table with one row per test photo (no pandas knowledge needed)
- Right answers by breed: Ragdoll is the hardest (38 of 50)
- A table of true breed against predicted breed (named a **confusion matrix**;
  19_1_2 covers it)
- Mistakes stay inside the look-alike pairs; most are Ragdolls called Birmans

### Looking at the mistakes
- Every misclassified test photo with its true breed, prediction and confidence
- Discussion: would a person get these right? Small, hidden or unusual-pose animals

### Confidence
- **Confidence**: the probability of the predicted breed (never below 0.25 with four breeds)
- Right answers are usually more confident than wrong ones (0.88 vs. 0.68 on average),
  but a few wrong answers have confidence above 0.8

### Photos outside the four breeds
- Siamese, Persian, pug, samoyed and keeshond photos all get one of the four breeds
- Some get very confident wrong answers, and some dogs get cat breeds, which never
  happened on the test photos
- A model has no "none of these" answer unless it is built to have one

### Saving outputs for 19_1
- `pets4_predictions.csv` (800 rows: split, breed, prediction, scores, probabilities)
  and `pets4_features.npz`; the course copies are what 19_1 downloads

### How we got here
- A timeline from the perceptron (1958) to transformers and today's large models, with
  where each step comes up in the course
- What changed around 2012: data, GPUs and shared pretrained models

### Where the photos came from (ethics discussion)
- The Pets photos: purebreds only, photos people chose to post online
- ImageNet: web photos labeled by crowd workers; the 2019 removal of many person categories
- How the choice of test examples shapes a reported accuracy
