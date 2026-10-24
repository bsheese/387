# 23_1 Attention — TODO

**Status:** new. **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 23_0.

Purpose: attention is a weighted average, and the weights come from how similar two words are, passed through softmax (callback to 19_1_4).

## Notebooks
- [ ] `23_1_1_Attention_by_Hand.ipynb`: 3–4 tokens with small embeddings; dot-product similarities, then softmax, then a weighted average, by hand in NumPy; then the same thing with `torch` matrix ops
- [ ] `23_1_outline.md`, `23_1_glossary.md`, `23_1_practice_quiz.ipynb`

## Activities
- [ ] 3Blue1Brown "But what is a GPT?" and "Attention in transformers" (2024): a short clip in class, or optional (no take-home work)
- [ ] Transformer Explainer pair activity: change the prompt and the temperature, and explain the attention weights and next-token probabilities
