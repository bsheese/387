# 20_0 PyTorch Basics — TODO

**Status:** rewritten 2026-10-25 (all three notebooks; no saved outputs). Was 19_0. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 19_1.

Purpose: tensors, then the nudge test, then autograd as "a fast, exact nudge test for every weight at once", then gradient descent. No calculus required; calculus goes in optional boxes.

## Notebooks
- [x] `20_0_1_Tensors.ipynb`: a tensor as a NumPy array that can live on a GPU and track gradients. Redoes 19_1_3's `features @ W.T + bias` with tensors; four differences from NumPy (with the real dtype error); a shapes section (the `@` shape error message, `reshape`, the batch dimension, `unsqueeze(0)` from 19_0_1's `predict`, image shape (3, 224, 224)); devices; `requires_grad` first look. Penguins dropped from this notebook.
- [x] `20_0_2_Autograd.ipynb`: the nudge test first, with the central difference (6.000 at x = 3), and a plot of slopes on y = x²; `x.grad` agrees; slopes for a neuron's w1, w2, bias by nudging and by autograd (37.8, 25.2, 12.6); "rates multiply" (3 × 14 = 42) checked by nudging and autograd; a timing demo nudging every weight of layers with 1k / 10k / 50k weights vs. one `.backward()` (50k: about 5 s vs. under a millisecond), then the ResNet-18 arithmetic (23M passes, nearly three days per step); zeroing gradients; `torch.no_grad()`; mapping to 19_0_1's loop. Calculus in `<details>` boxes.
- [x] `20_0_3_Gradient_Descent.ipynb`: penguins from `data/penguins.csv` (342 rows); standardizing explained from scratch; the loss bowl; one step by hand with the slope from both the nudge test and autograd; 100-step loop with the path drawn on the bowl; matches `LinearRegression`; learning rates 0.001 / 0.1 / 1.05 (diverges); `torch.optim.SGD` reproduces the hand loop; Adam mentioned for unit 21.
- [ ] `20_0_outline.md`, `20_0_glossary.md`, `20_0_practice_quiz.ipynb`: stale (old 19_0 numbering, calculus-based questions). Left for the later pass on outlines, quizzes and glossaries (decided 2026-10-25).

## 377 references
- [x] Notebooks: none assumed. 20_0_3 links 377's 17_0_5 as optional reference only.
- [ ] Glossary and outline still mention `17_0` and `17_0_5` (later pass).

## Activities
- [ ] TensorFlow Playground pair activity (predict, then test): no hidden layer on the circle data, learning rate 3, L2 turned up
- [ ] 3Blue1Brown chapters 1–2 (what a network is, gradient descent): show a short clip in class, or list as optional (no take-home work)
