"""Find photos of the same animal in pets4 and keep each animal in one split.

The Oxford-IIIT Pet photos were collected from the web, and photos with nearby
numbers (Ragdoll_159, Ragdoll_160, Ragdoll_161) are often the same animal, taken
by the same person, sometimes seconds apart. The first version of pets4 split each
breed at random, so some of those near-copies ended up in training and some in
validation or test, and the model could be checked on photos of animals it had
already learned from. This script groups the photos and writes data/pets4_splits.csv,
which make_pets4.py uses to place every photo.

Two photos of the same breed are put in the same group when any of these holds:
  - their numbers differ by at most 2 and the cosine similarity of their ResNet-18
    features (data/pets4_features.npz) is at least 0.85;
  - their numbers differ by at most 5 and the feature similarity is at least 0.90;
  - the feature similarity is at least 0.96, or two 32 x 32 grayscale thumbnails
    (either one mirrored) have a correlation of at least 0.9 (the same photo twice);
  - the pair is in MANUAL, a list of pairs judged to be the same animal by looking
    at the most similar pairs that the rules above left in different splits.
Groups are the connected pieces of these links. Each group goes to the split that
held most of its photos in the original random split; then single photos are moved
(chosen at random with a fixed seed) until every breed has 100 train, 50 val and
50 test photos again.

Usage, from the repo root, with the original pets4.zip extracted into ./pets4 and
the original split in the original_split column of an existing pets4_splits.csv
(or in the folder each photo is in):

    python data/group_pets4.py pets4
"""

import collections
import csv
import pathlib
import random
import re
import sys

import numpy as np
from PIL import Image, ImageOps

HERE = pathlib.Path(__file__).resolve().parent
TARGET = {"train": 100, "val": 50, "test": 50}
MANUAL = {frozenset(p) for p in [
    ("Ragdoll_44.jpg", "Ragdoll_63.jpg"), ("Birman_18.jpg", "Birman_19.jpg"), ("Birman_18.jpg", "Birman_20.jpg"),
    ("Ragdoll_183.jpg", "Ragdoll_184.jpg"), ("beagle_165.jpg", "beagle_174.jpg"), ("Ragdoll_42.jpg", "Ragdoll_73.jpg"),
    ("Ragdoll_42.jpg", "Ragdoll_75.jpg"), ("Ragdoll_42.jpg", "Ragdoll_128.jpg"), ("basset_hound_61.jpg", "basset_hound_63.jpg"),
    ("Birman_42.jpg", "Birman_43.jpg"), ("Ragdoll_136.jpg", "Ragdoll_137.jpg"), ("Ragdoll_9.jpg", "Ragdoll_18.jpg"),
    ("basset_hound_48.jpg", "basset_hound_105.jpg"), ("beagle_5.jpg", "beagle_6.jpg"),
]}


def thumb(path, flip=False):
    im = ImageOps.fit(Image.open(path).convert("L"), (32, 32))
    if flip:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    v = np.asarray(im, float).ravel()
    v -= v.mean()
    return v / np.linalg.norm(v)


def main(root):
    root = pathlib.Path(root)
    paths = sorted((p for p in root.glob("*/*/*.jpg") if p.parts[-3] != "other"), key=lambda p: p.name)
    names = [p.name for p in paths]
    breed = [p.parent.name for p in paths]
    num = [int(re.search(r"_(\d+)\.jpg$", n).group(1)) for n in names]
    original = {p.name: p.parts[-3] for p in paths}
    old_csv = HERE / "pets4_splits.csv"
    if old_csv.exists():
        with open(old_csv) as f:
            original = {r["file"]: r["original_split"] for r in csv.DictReader(f)}

    V = np.stack([thumb(p) for p in paths])
    Vf = np.stack([thumb(p, flip=True) for p in paths])
    pix = np.maximum(V @ V.T, V @ Vf.T)
    feats = np.load(HERE / "pets4_features.npz")
    index = {n: i for i, n in enumerate(feats["filename"])}
    F = feats["features"][[index[n] for n in names]]
    F = F / np.linalg.norm(F, axis=1, keepdims=True)
    sim = F @ F.T

    parent = list(range(len(paths)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            if breed[i] != breed[j]:
                continue
            d = abs(num[i] - num[j])
            if ((d <= 2 and sim[i, j] >= 0.85) or (d <= 5 and sim[i, j] >= 0.90) or sim[i, j] >= 0.96
                    or pix[i, j] >= 0.9 or frozenset((names[i], names[j])) in MANUAL):
                parent[find(i)] = find(j)
    groups = collections.defaultdict(list)
    for i in range(len(paths)):
        groups[find(i)].append(i)
    groups = list(groups.values())

    rng = random.Random(387)
    split, group_id = {}, {}
    for b in sorted(set(breed)):
        bg = [g for g in groups if breed[g[0]] == b]
        assign = {}
        for k, g in enumerate(bg):
            c = collections.Counter(original[names[i]] for i in g)
            best = max(c.values())
            assign[k] = [s for s in TARGET if c[s] == best][0]
        while True:
            c = collections.Counter()
            for k, s in assign.items():
                c[s] += len(bg[k])
            over = [s for s in TARGET if c[s] > TARGET[s]]
            if not over:
                break
            under = [s for s in TARGET if c[s] < TARGET[s]]
            singles = sorted(k for k, s in assign.items() if s == over[0] and len(bg[k]) == 1)
            assign[rng.choice(singles)] = under[0]
        for k, s in assign.items():
            for i in bg[k]:
                split[names[i]] = s
                group_id[names[i]] = f"{b}_{min(num[j] for j in bg[k])}"

    with open(old_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "breed", "group", "original_split", "split"])
        for n, b in sorted(zip(names, breed), key=lambda t: (t[1].lower(), int(re.search(r"_(\d+)\.jpg$", t[0]).group(1)))):
            w.writerow([n, b, group_id[n], original[n], split[n]])
    moved = sum(split[n] != original[n] for n in names)
    print(f"wrote {old_csv}: {len(groups)} groups, {sum(len(g) > 1 for g in groups)} with more than one photo, "
          f"{moved} photos moved from their original split")


if __name__ == "__main__":
    main(sys.argv[1])
