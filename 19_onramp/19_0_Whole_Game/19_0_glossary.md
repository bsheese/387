# 19_0 The Whole Game: Glossary

This document defines the terms used in the two 19_0 notebooks. Many of them are only
described in 19_0, because the model is treated as a black box on purpose. Where a later
notebook explains a term properly, the entry says which one.

---

## A

### Accuracy
The fraction of photos whose label the model gets right. With four breeds, guessing at
random gives an accuracy of about 0.25. 19_1_1 and 19_1_2 show why accuracy on its own
can be misleading.

---

## B

### Batch
A small group of training examples (32 photos in 19_0_1) that the model looks at before
its weights are nudged once. Training goes through the training set one batch at a time.

### Bias
An extra learned number that is added to a score, one per output. 19_0_1's new last layer
has 4 of them, one per breed, on top of its 2,048 weights.

---

## C

### Confidence
In these notebooks, the probability the model gives to the breed it predicts, which is the
highest of its four probabilities. With four breeds it is always at least 0.25. A high
confidence does not guarantee a right answer.

### Confusion matrix
A table that counts, for each true label (rows), how many examples got each predicted label
(columns). The diagonal holds the right answers. Introduced in 19_0_2 and covered in 19_1_2.

---

## E

### Epoch
One pass through all of the training examples. 19_0_1 trains for 8 epochs.

---

## F

### Features
The numbers a model computes from an example and passes to its last layer. For ResNet-18
there are 512 features per photo. They were learned on ImageNet and don't correspond to
anything we can name, such as ear length or fur color. 19_1_3 fits a model directly on them.

### Feature extraction
A way of reusing a pretrained model in which the whole pretrained network is frozen and only
a new last layer is trained on the features it computes. This is what 19_0_1 does. 22_1
compares it with fine-tuning.

### Fine-tuning
Reusing a pretrained model by letting training change some or all of its pretrained weights,
usually only a little. 19_0_1 does not do this (it uses feature extraction); 22_1 does.

### Freezing
Stopping some of a model's weights from changing during training. In PyTorch this is done by
setting `requires_grad = False` on them.

---

## G

### GPU (graphics processing unit)
A chip originally designed for graphics that can do thousands of multiplications at the same
time. Training and running neural networks is much faster on a GPU than on a CPU. Colab
offers a free T4 GPU when one is available.

---

## I

### ImageNet
A large collection of web photos labeled by crowd workers, first released in 2009. The full
collection has about 14 million photos in more than 20,000 categories. Most image models,
including the ResNet-18 used in 19_0, are pretrained on a smaller version made for a yearly
research competition: about 1.2 million photos in 1,000 categories (objects, animals, foods
and more). In this course, ImageNet means the 1,000-category version unless it says otherwise.

---

## L

### Layer
One stage of calculation in a neural network. It takes in a list of numbers, combines them
using learned numbers of its own, and passes a new list of numbers to the next layer.
ResNet-18 has 18 of them.

### Logistic regression
A model that multiplies each input number by a weight, adds the results up, and turns the
total into a probability. 19_1_3 shows that 19_0_1's new last layer is the same kind of
model.

### Label
The right answer for an example. In the Pets data, the label is the breed, given by the name
of the folder the photo is in.

### Last layer
The final step of a network, which turns the features into one score per possible answer.
ResNet-18's original last layer gives 1,000 scores (one per ImageNet category); 19_0_1
replaces it with one that gives 4. 19_1_3 shows that it is a weighted sum, the same as
logistic regression.

### Loss
A number that measures how wrong the model's answers are on a batch. Training changes the
weights to make the loss smaller. Explained in units 20 and 21.

---

## O

### Oxford-IIIT Pet dataset
About 7,400 photos of 37 cat and dog breeds, collected from the web and released by
researchers at Oxford and IIIT Hyderabad in 2012. 19_0 and 19_1 use four of its breeds.

---

## P

### Pretrained model
A model whose weights have already been learned, usually on a large dataset, and which can
be downloaded and reused. Most deep learning in practice starts from one.

### Probability (of a breed)
A number between 0 and 1 that the model outputs for each breed. The four probabilities for
a photo add up to 1. They come from the scores through softmax.

---

## R

### ResNet-18
A convolutional neural network with 18 layers and about 11.7 million weights, published by
researchers at Microsoft in 2015. Its family of models won the 2015 ImageNet competition.
Convolutional networks are covered in 22_0.

---

## S

### Score
One of the raw numbers the last layer outputs, one per breed. Higher means the model favors
that breed more. Scores can be any number, positive or negative; softmax turns them into
probabilities.

### Softmax
The function that turns a list of scores into probabilities that are all positive and add up
to 1. The highest score always gets the highest probability. Explained in 19_1_4.

---

## T

### Test set
Examples set aside until the very end and used once, for a final, fair measure of how well
the model works on examples it has never seen. 19_1_1 explains why it is kept separate from
the validation set.

### Training set
The examples the model learns from.

### Transfer learning
Using what a model learned on one task for another task, for example reusing a network
pretrained on ImageNet to tell pet breeds apart. Feature extraction and fine-tuning are two
ways to do it.

---

## V

### Validation set
Examples the model never learns from, used to check it during training (after each epoch in
19_0_1) and to make choices such as how long to train. Covered in 19_1_1.

---

## W

### Weights
The numbers inside a model that are learned during training. ResNet-18 has about 11.7
million of them. Strictly speaking, a few of these have other names, such as biases,
but "weights" is the usual word for all of a model's learned numbers. Unit 20 explains
what they do.
