# 23_0 Tokens and Embeddings — TODO

**Status:** drafted 2026-10-25 (two notebooks, no saved outputs; each runs in under 20 s on a laptop CPU after the model downloads). **Days:** 2 of unit 23's 7. **Assumes:** 21, 22_1.

Data: `data/imdb_reviews.csv` (2,000 train / 1,000 val / 2,000 test, balanced), the unit's one dataset.

## Notebooks
- [x] `23_0_1_Tokens.ipynb`: the reviews; characters vs. words (49,708 different "words" in the training reviews, 30,423 seen once) vs. subwords; DistilBERT's WordPiece tokenizer (30,522 tokens, `##`, uncased); IDs and `[CLS]`/`[SEP]`; padding, truncation, attention mask, (batch, tokens) tensors; token lengths (median 220; 41% over 256, 14% over 512); GPT-2's tokenizer (50,257, `Ġ`, cased) and why IDs don't transfer; tokens per word (1.26) and English vs. Spanish (10 vs. 21 tokens).
- [x] `23_0_2_Embeddings.ipynb`: `nn.Embedding` as a lookup and as one-hot @ W; DistilBERT's (30522, 768) table (35% of its weights); cosine similarity (and why unrelated words still score ~0.4); nearest neighbors ("good" → "bad", "terrible" → "terrific": embeddings capture use, not meaning); a PCA plot (people separate, praise/criticism mixed); contextual embeddings for "bank" (money–loan 0.91 vs. money–river 0.65); MiniLM sentence embeddings with mean pooling and semantic search over 500 reviews (honestly uneven).
- [ ] `23_0_outline.md`, `23_0_glossary.md`, `23_0_practice_quiz.ipynb`: later pass.

## Notes
- RNNs/LSTMs: one historical slide only (decided). Not in the notebooks.
- MiniLM sentence embeddings + logistic regression get only 0.777 on IMDB sentiment (TF-IDF + logistic regression: 0.833), measured while building 23_0_2. Use that comparison in 23_2_2.
- Source: Hugging Face LLM course ch. 1–2 (free)
