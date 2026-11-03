# 23_3 Generation and Limits — TODO

**Status:** both notebooks drafted 2026-11-03, with saved outputs (the text describes specific generated text). **Days:** see the unit row in the `COURSE_MAP.md` session budget. **Assumes:** 23_2.

Decided: text generation (sampling, temperature) goes next to the LLM-limits session. Exams test it by reading and reasoning only.

## Notebooks
- [x] `23_3_1_Text_Generation.ipynb` (drafted 2026-11-03; GPT-2 pinned to the CPU so seeded samples match the saved ones; next-token table, loss by hand 3.079, reversed sentence 7.361 and perplexity, greedy repetition, temperature table and samples at 0.3 / 1.0 / 1.6, top-k with `generate`) (GPT-2 runs fine live on either runtime: on the CPU it loads in about 15 s and makes 5 samples of 50 tokens in 13.2 s; on the T4, 0.7 s): GPT-2 (small) next-token probabilities; greedy vs. sampling; temperature and top-k; the next-token loss is cross-entropy again (callback to 19_1_4 and 21_0_1)
- [x] `23_3_2_What_LLMs_Get_Wrong.ipynb` (drafted 2026-11-03; `HuggingFaceTB/SmolLM2-360M-Instruct`, greedy, on the CPU): the chat template; facts it gets right; invented Nobel Prize in Basket Weaving and a made-up novel; token probabilities drop to 0.08–0.18 where it invents; "strawberry" has 10 r's (tokens); 10 easy questions: letters 4/10 and 2/10 by option order (9 of 10 answers changed), open answers 3/10 exact match, 8/10 contains, 9/10 by a person; memorization by loss (famous openings 0.945 / 0.562 vs. reworded 2.582 / 3.143) and benchmark contamination; ends the course with a look back.
- [ ] `23_3_outline.md`, `23_3_glossary.md` (later pass)
- [ ] Pair activities: 23_3_1 (temperature and top-k on their own prompts; compare the loss of texts); 23_3_2 (write new trick questions; shuffle multiple-choice options; score open answers with their own rule). Check that SmolLM2's answers are the same in Colab's transformers version in January 2027.

## Exam
- [ ] Unit 23 exam covers 23_0–23_3
