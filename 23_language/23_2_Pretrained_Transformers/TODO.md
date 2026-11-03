# 23_2 Pretrained Transformers — TODO

**Status:** new. **Days:** part of unit 23 (6 teaching days). **Assumes:** 23_1, 22_1 (transfer learning).

Purpose: the text version of transfer learning. Use pretrained transformers through `pipeline`, then fine-tune DistilBERT as a classifier.

## Notebooks
- [ ] `23_2_1_Using_Pretrained_Models.ipynb`: Hugging Face `pipeline` for sentiment, zero-shot classification and summarization; read the model card
- [ ] `23_2_2_Fine_Tuning_DistilBERT.ipynb` (needs a GPU: open with the same "This notebook needs a GPU" paragraph as 22_0_2 and 22_1_1, keep saved outputs, and keep the pair activity's required questions off the fine-tuning cell): IMDB (decided 2026-10-24; no student-chosen text set), compared against a TF-IDF + logistic regression baseline (377 habit: beat a baseline); confusion matrix; error analysis
- [ ] `23_2_outline.md`, `23_2_glossary.md`

## Decide
- [ ] Dataset size so fine-tuning fits in class. If it can't, keep the full run as a saved output and have pairs run only evaluation and error analysis. T4 results (2026-10-27): 2,000 reviews × 256 tokens, batch 16, one epoch with a plain PyTorch loop takes 41 s and reaches 86.3% on 1,000 test reviews, so this fits in class on the GPU with room for a larger training set. CPU results (2026-11-02, free Colab, 2 vCPUs, 1 torch thread): about 26 s per training step of 16 reviews, so a projected 55 minutes (3,282 s) for one epoch on 2,000 reviews; evaluation takes about 0.46 s per review (160 reviews in 73.5 s). Fine-tuning can't run live on the CPU, so 23_2_2 keeps the full GPU run as a saved output, and a pair without a GPU works from saved predictions for the error analysis. Evaluation should stay at about 100 reviews on the CPU.
- [ ] Use the comparison the check turned up: the off-the-shelf SST-2 `pipeline` scores 87.6% on IMDB with no training, about the same as our one-epoch fine-tune. On the CPU the pipeline took 255 s for 500 reviews (about 0.5 s per review), so use about 100 reviews for a live cell. That makes a good discussion point in 23_2_2 (a model fine-tuned on a related task can already be as good as a quick fine-tune of our own).
- [ ] HF Trainer API vs. the 21_0 training loop (the loop shows continuity; Trainer is what students will meet outside class)
