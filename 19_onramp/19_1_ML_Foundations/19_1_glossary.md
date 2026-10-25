# 19_1 The On-Ramp: Glossary

This document defines the terms introduced in the four 19_1 notebooks. Terms first used in
19_0 (accuracy, epoch, features, label, last layer, softmax, training/validation/test set,
weights) are defined in `19_0_glossary.md`; the entries below that repeat one of them add
what 19_1 says about it.

---

## A

### Accuracy paradox
When one class is rare, a model that never predicts that class can still have very high
accuracy, because almost every answer of "not that class" is right. In 19_1_2, on a set with
5 Ragdolls among 155 photos, a detector that never says "Ragdoll" has the same accuracy
(0.968) as the Pets model, which finds 4 of the 5.

### Activation function
The function a neuron applies to its weighted sum. Logistic regression uses sigmoid; the
hand-built XOR network in 19_1_4 uses a step function. Unit 20 introduces ReLU.

---

## B

### Baseline
The score of a simple method that doesn't learn from the data, used to judge whether a
model's score is any good. 19_1_1 uses three: always predicting the most common breed,
guessing at random, and telling cats from dogs and then guessing the breed.

### Bias (of a neuron)
The extra number added to a neuron's weighted sum. It shifts the sum up or down whatever the
features are. (Unrelated to bias in the sense of unfairness.)

### Broadcasting
NumPy's rule for combining arrays of different shapes, such as adding a bias of shape (4,)
to scores of shape (800, 4), or dividing an (800, 4) array by row totals of shape (800, 1).
The smaller array is repeated to match the larger one.

---

## C

### Confusion matrix
A table with one row for each true class and one column for each predicted class, where each
cell counts the examples with that combination. The diagonal holds the right answers.

### Cross-entropy loss
The loss used for classification: for each example, $-\log$ of the probability the model
gave to the true class, averaged over the examples. It is near 0 for confident right answers
and very large for confident wrong ones.

---

## D

### Decision boundary
The places where a model's answer changes from one class to another. For a single neuron it is
where the weighted sum equals 0, which is a straight line with two features.

### Dot product
Multiply two arrays of the same length element by element and add up the results. Written
`x @ w` in NumPy. A neuron's weighted sum is the dot product of the features and the weights,
plus the bias.

---

## F

### False negative (FN), false positive (FP)
For one class: a **false negative** is an example of that class the model missed; a **false
positive** is an example of another class that the model called that class (a false alarm).

---

## H

### Hidden layer
A layer of neurons between the inputs and the output layer. Its outputs are new features that
the network computes for itself. In 19_1_4, two hidden neurons turn XOR into a problem a
single straight line can separate.

---

## L

### Logarithm (natural log)
The inverse of $e^{x}$: $\log(e^{x}) = x$. `np.log` in NumPy. $\log(1) = 0$, and the log of a
number between 0 and 1 is negative, more so the closer the number is to 0.

### Logistic regression
A model for yes/no questions: one weighted sum of the features followed by sigmoid. It is a
single neuron.

### Loss
A number that measures how wrong a model's outputs are; training changes the weights to make
it smaller. See cross-entropy loss.

---

## M

### Mask
A `True`/`False` array used to select elements of another array of the same length, such as
`breed[split == 'test']`. Masks combine with `&` (and), `|` (or) and `~` (not).

### Matrix multiplication
Many dot products at once. `W @ x` takes the dot product of every row of the matrix `W` with
`x`. In `A @ B` the inner sizes must match, and the outer sizes give the shape of the result:
`(800, 512) @ (512, 4)` gives `(800, 4)`.

---

## N

### Neuron (artificial)
A weighted sum of its inputs plus a bias, passed through an activation function. Every network
in the course is built from neurons.

### NumPy array
A grid of numbers (or strings) of one type that supports operations on the whole array at
once. Has a `.shape`, such as `(800,)` for one dimension or `(800, 512)` for two.

---

## O

### Overfitting
When a model learns things that are specific to its training examples and don't carry over to
new ones. It shows as training accuracy that keeps rising while validation accuracy stops
improving, and validation loss that starts to rise.

---

## P

### Precision
For one class: TP / (TP + FP). When the model gives that answer, the fraction of the time it is
right. Read down the class's column of the confusion matrix.

---

## R

### Recall
For one class: TP / (TP + FN). Of the real examples of that class, the fraction the model
found. Read along the class's row of the confusion matrix.

---

## S

### Sigmoid
$1 / (1 + e^{-z})$. Turns any number into a probability between 0 and 1; sigmoid(0) = 0.5.
Equal to softmax with two classes when one score is 0.

### Softmax
Turns a list of scores into probabilities: raise $e$ to the power of each score, then divide
by the total. Only the differences between the scores matter.

---

## T

### Threshold
The probability above which a model's answer counts as "yes". Lowering it raises recall and
lowers precision; raising it does the opposite. Choose it from the costs of the two kinds of
mistake, on validation data.

### Transpose
Swapping the rows and columns of a matrix, written `.T`. A (4, 512) array transposed has
shape (512, 4).

### True positive (TP), true negative (TN)
For one class: a **true positive** is an example of that class the model found; a **true
negative** is an example of another class that the model correctly didn't call that class.

---

## V

### Validation set (what it's for)
Data used to compare options and make choices, such as how many epochs to train or which
threshold to use. Because the best option is picked on it, the winner's validation score is a
little optimistic, which is why a separate test set is kept for the final measurement.

---

## W

### Weighted sum
Each feature multiplied by its weight, added up, plus the bias. The first step of every
neuron.

---

## X

### XOR
"Exclusive or": the answer is 1 when exactly one of two inputs is 1. The four XOR points can't
be separated by a straight line, so no single neuron can learn them.
