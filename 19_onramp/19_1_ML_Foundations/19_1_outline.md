# 19_1 The On-Ramp: Topic Outline

This document outlines the topics covered in the four 19_1 notebooks, one per class day.
Every notebook works with the Pets model from 19_0, using the files 19_0 saved in `data/`
(`pets4_predictions.csv`, `pets4_features.npz`, `pets4_head.pt`), plus the four-point XOR
toy in 19_1_4. Nothing retrains the network, and every cell runs in seconds on a CPU. The
NumPy each session needs is taught in that session. The cs377 notebooks that cover the same
ideas are linked from each notebook as optional reference.

---

## 19_1_1: Is It Any Good?

**Data:** `pets4_predictions.csv`, `pets4_features.npz`

### The model's predictions as arrays
- Reading the CSV with pandas, then taking columns out with `.to_numpy()`
- Arrays vs. lists: one type, operations on the whole array at once; `.shape`
- Element-by-element comparison (`predicted == breed`), `.sum()` and `.mean()` of a
  `True`/`False` array; **accuracy**
- **Masks**: selecting the test rows with `split == 'test'`

### Baselines
- What a **baseline** is and why a score means little without one
- Most common breed with `np.unique(..., return_counts=True)` and `np.argmax`: 0.25 here,
  because the classes are balanced; with unbalanced data it can be very high
- Random guessing with `np.random.default_rng(...).choice`: about 0.25
- Tell cats from dogs, then guess the breed: about 0.5
- The model's 0.90 against all three

### Measured on which photos?
- The memorizer: 1.0 on training photos, nothing on new ones
- The model's own accuracy on train / val / test (0.94 / 0.89 / 0.90)
- **Overfitting** defined as a gap between training and new photos

### Training too long
- Training a fresh last layer directly on the cached 512 features (fast)
- 300 epochs: training accuracy reaches 1.0 and training loss approaches 0, while
  validation accuracy levels off near 0.9 and validation loss rises after about epoch 32
- Stopping where validation loss is lowest
- The **loss** introduced informally (19_1_4 defines it)

### Why a separate test set
- Choosing on the validation photos makes the winner's validation score optimistic
- Demo: 30 versions trained on different random 10 photos per breed; the winner is 0.041
  above average on validation but only 0.006 above average on test
- Table: training / validation / test photos, what each is for, and the rule for each

---

## 19_1_2: The Confusion Matrix

**Data:** `pets4_predictions.csv`

### Building the confusion matrix
- Counting by hand into `np.zeros((4, 4), dtype=int)`; two-dimensional indexing
- `confusion_matrix` and `ConfusionMatrixDisplay` from scikit-learn
- Reading rows (true breed), columns (predicted breed) and the diagonal (right answers)
- The Pets model: mistakes only within look-alike pairs; 12 Ragdolls called Birmans
- Accuracy as the diagonal sum over the total (`np.diag`)

### Precision and recall
- The adoption-site example: "Ragdoll or not?"
- TP, FN, FP, TN read from the matrix (`matrix[k, :]`, `matrix[:, k]`)
- **Recall** (along the row) and **precision** (down the column): Ragdoll recall 0.76,
  precision 0.905; Birman is the mirror image
- `classification_report`; F1 and support mentioned; one mistake lowers one breed's recall
  and another breed's precision

### The accuracy paradox
- A shelter-like set: 150 other photos and 5 Ragdolls (`np.where`, `~`)
- Our model and a detector that never says "Ragdoll" both score 0.968
- Recall tells them apart (0.8 vs. 0); with a rare class, look at precision and recall

### Thresholds
- Saying "Ragdoll" when its probability is above a threshold; table of thresholds from
  0.1 to 0.9 with precision and recall
- Choosing a threshold by cost, on validation photos: false alarm costs 3 (adoption site)
  gives 0.35; miss costs 3 (lost-pet service) gives 0.15
- Why both are below 0.5: this model says "Ragdoll" too rarely; 0.5 is only a default

---

## 19_1_3: One Neuron

**Data:** `pets4_features.npz`, `pets4_head.pt`, `pets4_predictions.csv`

### A weighted sum
- Features, **weights** and a **bias** in a three-feature example, by hand
- What positive, negative and near-zero weights mean
- The **dot product** and `@`; arrays must have the same length (the shape error)

### A neuron that tells Birmans from Ragdolls
- Selecting the two cat breeds with `|` and `&`
- `LogisticRegression` on the 512 features: test accuracy 0.89 (the four-breed model got
  84 of the 100 test cats right)
- `coef_` (512 weights) and `intercept_`

### One prediction by hand
- `predict_proba` for one test photo
- The weighted sum `x @ w + b`, then **sigmoid**, $1 / (1 + e^{-z})$; how $e^{-z}$ behaves;
  sigmoid(0) = 0.5
- The two steps reproduce `predict_proba` exactly
- An artificial **neuron**: weighted sum plus an **activation function**; the perceptron (1958)

### The Pets model's last layer
- `pets4_head.pt`: a (4, 512) weight matrix and 4 biases, one neuron per breed
- The four scores for one photo, one at a time, matching the saved scores
- **Matrix multiplication**: `W @ x + bias` gives all four at once
- **The shape rule**: inner sizes must match, outer sizes give the result;
  `(800, 512) @ (512, 4)` gives `(800, 4)`; transposing with `.T`; broadcasting the bias
- The shape error when the inner sizes don't match

---

## 19_1_4: Softmax, and What One Neuron Can't Do

**Data:** `pets4_predictions.csv`; the XOR toy (the same four points as 20_1_1)

### Softmax
- Scores can be negative and don't add up to 1
- $e^{x}$: always positive, 1 at 0, grows quickly
- The two steps (exponentiate, divide by the total) reproduce the saved probabilities
- Softmax for all 800 photos with `.sum(axis=1, keepdims=True)`
- Only differences between scores matter; scaling the scores makes the model more or less
  confident (used again for text generation in unit 23)
- Sigmoid is softmax with two classes

### The loss
- The natural log as the inverse of $e^{x}$; the penalty $-\log(p)$ for a range of $p$
- **Cross-entropy loss** as the average penalty; confident wrong answers cost the most
- The test loss of the Pets model (0.255)

### XOR
- The four points and the target pattern
- A single neuron's **decision boundary** is a straight line
- Three lines that each get 3 of 4 right; a search over 15,625 weight settings never gets 4
- Logistic regression sets both weights to 0 and answers 0.5 everywhere
- Minsky and Papert (1969)

### A hidden layer
- Step activation; hidden neurons for "at least one" and "both"; the output neuron
  "at least one, but not both"
- All four points right
- The hidden layer's features make the points separable by a line
- The same idea in the Pets model: its hidden layers turn photos into 512 features the last
  layer can separate with straight boundaries; unit 20 learns the hidden weights
