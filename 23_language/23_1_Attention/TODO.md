# 23_1 Attention — TODO

**Status:** drafted 2026-10-25 (one notebook, no saved outputs; runs in ~10 s after the DistilBERT download). **Days:** 1 of unit 23's 7. **Assumes:** 23_0.

## Notebooks
- [x] `23_1_1_Attention_by_Hand.ipynb`: four made-up tokens (river, bank, money, loan) with 4-number vectors; scores, softmax, weighted average for one token by hand, then all tokens with matrix multiplication and a heatmap; queries, keys and values with `nn.Linear`; why divide by sqrt(d) (averaged over 2,000 random trials: largest weight 0.49 / 0.87 / 0.95 for d = 4 / 64 / 512 unscaled, 0.31–0.32 scaled); `scaled_dot_product_attention` matches; padding and causal masks; attention ignores order, so position embeddings (512 in DistilBERT); heads, feed-forward, residuals, layer norm, printed from DistilBERT's layer; the n² cost; DistilBERT's real attention from "it" ("tired" vs. "wide": animal 0.22 / 0.13, street 0.03 / 0.05, `[SEP]` 0.32 / 0.38), so attention weights aren't explanations (Clark et al., 2019); link to Transformer Explainer.
- [ ] `23_1_outline.md`, `23_1_glossary.md`, `23_1_practice_quiz.ipynb`: later pass.

## Activities
- [ ] 3Blue1Brown "But what is a GPT?" and "Attention in transformers" (2024): a short clip in class, or optional (no take-home work)
- [ ] Transformer Explainer pair activity: change the prompt and the temperature, and explain the attention weights and next-token probabilities
