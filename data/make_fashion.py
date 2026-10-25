"""Build data/fashion10k.npz, the Fashion-MNIST subset used in unit 21 and 22_0.

Every notebook downloads this one file instead of the full dataset, so that all
students train and test on exactly the same images. From the 60,000 official
training images it takes 1,000 per class for training (10,000) and a separate
500 per class for validation (5,000). The test set is the official 10,000 test
images, unchanged. Images stay as 28 x 28 uint8 arrays (0-255).

Usage (from the 387 repo root):

    python data/make_fashion.py /path/to/download/folder

torchvision downloads the original files into that folder if they aren't there.

Fashion-MNIST: H. Xiao, K. Rasul and R. Vollgraf, "Fashion-MNIST: a Novel Image
Dataset for Benchmarking Machine Learning Algorithms", 2017. MIT License.
"""

import pathlib
import sys

import numpy as np
from torchvision import datasets

TRAIN_PER_CLASS = 1000
VAL_PER_CLASS = 500
SEED = 387

OUT = pathlib.Path(__file__).resolve().parent / "fashion10k.npz"


def main(root):
    train = datasets.FashionMNIST(root, train=True, download=True)
    test = datasets.FashionMNIST(root, train=False, download=True)
    images, labels = train.data.numpy(), train.targets.numpy()

    rng = np.random.default_rng(SEED)
    train_idx, val_idx = [], []
    for k in range(10):
        idx = rng.permutation(np.where(labels == k)[0])
        train_idx.append(idx[:TRAIN_PER_CLASS])
        val_idx.append(idx[TRAIN_PER_CLASS:TRAIN_PER_CLASS + VAL_PER_CLASS])
    train_idx = rng.permutation(np.concatenate(train_idx))
    val_idx = rng.permutation(np.concatenate(val_idx))

    np.savez_compressed(
        OUT,
        x_train=images[train_idx], y_train=labels[train_idx],
        x_val=images[val_idx], y_val=labels[val_idx],
        x_test=test.data.numpy(), y_test=test.targets.numpy(),
        classes=np.array(train.classes),
    )
    print(f"wrote {OUT} ({OUT.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main(sys.argv[1])
