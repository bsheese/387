# 23_2 Pretrained Transformers — TODO

**Status:** new. **Days:** part of unit 23 (6 teaching days). **Assumes:** 23_1, 22_1 (transfer learning).

Purpose: the text version of transfer learning. Use pretrained transformers through `pipeline`, then fine-tune DistilBERT as a classifier.

## Notebooks
- [ ] `23_2_1_Using_Pretrained_Models.ipynb`: Hugging Face `pipeline` for sentiment, zero-shot classification and summarization; read the model card
- [ ] `23_2_2_Fine_Tuning_DistilBERT.ipynb`: IMDB (decided 2026-10-24; no student-chosen text set), compared against a TF-IDF + logistic regression baseline (377 habit: beat a baseline); confusion matrix; error analysis
- [ ] `23_2_outline.md`, `23_2_glossary.md`, `23_2_practice_quiz.ipynb`

## Decide
- [ ] Dataset size so fine-tuning fits in class. If it can't, keep the full run as a saved output and have pairs run only evaluation and error analysis. T4 results (2026-10-27): 2,000 reviews × 256 tokens, batch 16, one epoch with a plain PyTorch loop takes 41 s and reaches 86.3% on 1,000 test reviews, so this fits in class on the GPU with room for a larger training set. Still needs the CPU number.
- [ ] Use the comparison the check turned up: the off-the-shelf SST-2 `pipeline` scores 87.6% on IMDB with no training, about the same as our one-epoch fine-tune. That makes a good discussion point in 23_2_2 (a model fine-tuned on a related task can already be as good as a quick fine-tune of our own).
- [ ] HF Trainer API vs. the 21_0 training loop (the loop shows continuity; Trainer is what students will meet outside class)
