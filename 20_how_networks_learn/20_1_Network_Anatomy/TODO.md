# 20_1 Network Anatomy — TODO

**Status:** 20_1_1 rewritten 2026-10-25 (no saved outputs). Was 19_1_1. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 20_0, 19_1_3–4.

Purpose: `nn.Module`, logistic regression as a one-layer network, and a hidden layer that solves XOR.

## Notebooks
- [x] `20_1_1_Anatomy_of_a_Network.ipynb` ("Building a Network"): builds on 19_1_3, 19_1_4 and 20_0 instead of 377's 18_2_3 (linked as optional reference). `nn.Linear` checked against `X @ W.T + b`; `nn.Module`; a single neuron trained on XOR ends at 0.5 everywhere (loss = -log 0.5); the nudge test shows the step activation has slope 0, so ReLU; XORNet (17 numbers) trained with BCE + SGD, decision boundary (a band) and its learned hidden features; nudge check of the largest hidden-weight slope against autograd; 20 random starts (15 solve XOR, 5 stuck at 2 of 4; dead ReLUs explained); `nn.Sequential`, `state_dict` (ties to `pets4_head.pt`), and ResNet-18 introspection (11.7M numbers, `fc` = `nn.Linear(512, 1000)`, `conv1` preview of unit 22).
- [x] "Rates multiply" backprop check on XORNet: folded into 20_1_1 Section 5 (unit 20 has one day for 20_1).
- [ ] Optional extension for the 377 track: micrograd-style tiny autograd in plain Python (after Karpathy)
- [ ] **Create** `20_1_outline.md`, `20_1_glossary.md`, `20_1_practice_quiz.ipynb` in the later pass. The anatomy sections are still inside `21_0_outline.md`, `21_0_glossary.md` and `21_0_practice_quiz.ipynb` (the old 19_1 files); move them here then.

## Exam
- [ ] Unit 20 exam: tensor shapes, nudge-test reasoning, reading a loss curve, parameter counts
