"""Build data/imdb_reviews.csv, the IMDB subset used in unit 23.

Every notebook downloads this one file, so all students work with the same
reviews. It takes 2,000 training reviews (1,000 positive, 1,000 negative) and a
separate 1,000 validation reviews from the official training set, and 2,000
test reviews from the official test set, all balanced and chosen at random.

Usage (from the 387 repo root; needs the `datasets` package):

    python data/make_imdb.py

Large Movie Review Dataset: A. L. Maas, R. E. Daly, P. T. Pham, D. Huang,
A. Y. Ng and C. Potts, "Learning Word Vectors for Sentiment Analysis", ACL 2011.
Released by the authors for research use.
"""

import pathlib

import pandas as pd
from datasets import load_dataset

SEED = 387
SIZES = {"train": 2000, "val": 1000, "test": 2000}
OUT = pathlib.Path(__file__).resolve().parent / "imdb_reviews.csv"


def balanced(df, n, seed):
    per = n // 2
    return pd.concat([df[df.label == k].sample(per, random_state=seed) for k in (0, 1)])


def main():
    imdb = load_dataset("stanfordnlp/imdb")
    train_all = imdb["train"].to_pandas()
    test_all = imdb["test"].to_pandas()
    train = balanced(train_all, SIZES["train"], SEED)
    val = balanced(train_all.drop(train.index), SIZES["val"], SEED)
    test = balanced(test_all, SIZES["test"], SEED)
    parts = []
    for split, df in [("train", train), ("val", val), ("test", test)]:
        df = df.sample(frac=1, random_state=SEED).assign(split=split)
        parts.append(df)
    out = pd.concat(parts)[["split", "label", "text"]]
    out["text"] = out["text"].str.replace("<br />", " ", regex=False)   # the raw reviews contain HTML line breaks
    out.to_csv(OUT, index=False)
    print(f"wrote {OUT} ({OUT.stat().st_size / 1e6:.1f} MB): {out.split.value_counts().to_dict()}")


if __name__ == "__main__":
    main()
