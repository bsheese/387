# 20_0 PyTorch Basics — TODO

**Status:** exists (was 19_0); math to rewrite. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 19_1.

Purpose: tensors, then the nudge test, then autograd as "a fast, exact nudge test for every weight at once", then gradient descent. No calculus required; calculus goes in optional boxes.

## Notebooks
- [ ] `20_0_1_Tensors.ipynb`: open with "a tensor is a NumPy array that can track gradients" (callback to 19_1_0)
- [ ] `20_0_2_Autograd.ipynb`: **rewrite Section 1.** It currently checks against calculus ("Calculus tells us the answer is 2x", "dy/dx = 2x"). Instead:
  - [ ] Start with the nudge test: `(f(x + 0.001) - f(x)) / 0.001` → ≈ 6 at x = 3, then show `x.grad` gives 6
  - [ ] Move the dy/dx = 2x derivation into a collapsible "if you've taken calculus" box
  - [ ] Chain-rule section (z = (ax + b)²): add "rates multiply" with numbers, and check it with a nudge
  - [ ] The accumulation-trap cell says "dy/dx = 2x = 6, always". Reword so it doesn't need calculus.
- [ ] `20_0_3_Gradient_Descent.ipynb`: add one nudge-test step before the first `backward()`; references to 377's 17_0_5 (RSS bowl) need a recap for non-377 students
- [ ] `20_0_outline.md`, `20_0_glossary.md`: update for the nudge test; the old "19_0" in headings needs fixing by hand
- [ ] `20_0_practice_quiz.ipynb`: add nudge-test and rates-multiply questions; remove any that need calculus

## 377 references to fix
- 20_0_3, glossary, outline: `17_0`, `17_0_5`

## Activities
- [ ] TensorFlow Playground pair activity (predict, then test): no hidden layer on the circle data, learning rate 3, L2 turned up
- [ ] 3Blue1Brown chapters 1–2 (what a network is, gradient descent): show a short clip in class, or list as optional (no take-home work)
