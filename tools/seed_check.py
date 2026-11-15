#!/usr/bin/env python3
"""REVISION_PLAN.md step A3 and A4: check the single-run claims that survive the cuts, over five seeds.

Claims checked (old notebook numbering):
  21_1_1  dropout 0.5 on 1,000 images: validation loss ends well below no regularization;
          validation accuracy improves only a little.
  21_1_1  ten times the data (10,000 images, no regularization) raises validation accuracy
          by several points, far more than dropout does.
  22_0_2  the CNN without batch norm (Adam, best epoch) clearly beats the MLP on the test set,
          and loses much less accuracy than the MLP when test images are shifted 1 or 2 pixels.
          The CNN with batch norm is trained too, for reference.

Settings copy the notebooks, with the recipe changes the plan makes (plain Adam at 0.001,
keep the weights from the epoch with the lowest validation loss, no cosine schedule, no
weight decay). Runs on the CPU. Writes tools/seed_check_results.json and prints a summary.

Usage: python tools/seed_check.py [number_of_seeds]
"""

import json
import pathlib
import sys
import time

import numpy as np
import torch
from torch import nn

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEEDS = range(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
device = "cpu"
loss_fn = nn.CrossEntropyLoss()

data = np.load(ROOT / "data" / "fashion10k.npz")


def prepare(images, labels, flat):
    x = images.reshape(len(images), -1) if flat else images[:, None]
    return torch.tensor(x / 255, dtype=torch.float32), torch.tensor(labels, dtype=torch.long)


def evaluate(model, X, y):
    model.eval()
    with torch.no_grad():
        s = model(X)
        return loss_fn(s, y).item(), (s.argmax(1) == y).float().mean().item()


def fit(model, X, y, Xv, yv, epochs, keep_best=False):
    loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X, y), batch_size=64, shuffle=True)
    opt = torch.optim.Adam(model.parameters(), lr=0.001)
    hist = {"val_loss": [], "val_acc": []}
    best, best_state = float("inf"), None
    for _ in range(epochs):
        model.train()
        for xb, yb in loader:
            opt.zero_grad()
            loss_fn(model(xb), yb).backward()
            opt.step()
        vl, va = evaluate(model, Xv, yv)
        hist["val_loss"].append(vl)
        hist["val_acc"].append(va)
        if keep_best and vl < best:
            best, best_state = vl, {k: v.clone() for k, v in model.state_dict().items()}
    if keep_best:
        model.load_state_dict(best_state)
    return hist


def big_network(dropout=0.0):
    return nn.Sequential(nn.Linear(784, 512), nn.ReLU(), nn.Dropout(dropout),
                         nn.Linear(512, 512), nn.ReLU(), nn.Dropout(dropout),
                         nn.Linear(512, 10))


def make_cnn(batch_norm):
    def block(c_in, c_out):
        return [nn.Conv2d(c_in, c_out, 3, padding=1),
                nn.BatchNorm2d(c_out) if batch_norm else nn.Identity(),
                nn.ReLU(), nn.MaxPool2d(2)]
    return nn.Sequential(*block(1, 32), *block(32, 64), nn.Flatten(),
                         nn.Linear(64 * 7 * 7, 128), nn.ReLU(), nn.Dropout(0.3), nn.Linear(128, 10))


def make_mlp():
    return nn.Sequential(nn.Flatten(), nn.Linear(784, 512), nn.ReLU(), nn.Dropout(0.3),
                         nn.Linear(512, 512), nn.ReLU(), nn.Dropout(0.3), nn.Linear(512, 10))


def shift_right(X, pixels):
    if pixels == 0:
        return X
    s = torch.roll(X, shifts=pixels, dims=3)
    s[..., :pixels] = 0
    return s


results = {"21_1_1": [], "22_0_2": []}
start = time.time()

# 21_1_1: flattened images
Xtr, ytr = prepare(data["x_train"], data["y_train"], flat=True)
Xva, yva = prepare(data["x_val"], data["y_val"], flat=True)
small = torch.cat([torch.where(ytr == k)[0][:100] for k in range(10)])
for seed in SEEDS:
    row = {"seed": seed}
    for label, dropout, X, y, epochs in [("none_1k", 0.0, Xtr[small], ytr[small], 60),
                                         ("dropout_1k", 0.5, Xtr[small], ytr[small], 60),
                                         ("none_10k", 0.0, Xtr, ytr, 30)]:
        torch.manual_seed(seed)
        h = fit(big_network(dropout), X, y, Xva, yva, epochs)
        row[label] = {"final_val_loss": h["val_loss"][-1], "best_val_loss": min(h["val_loss"]),
                      "final_val_acc": h["val_acc"][-1], "best_val_acc": max(h["val_acc"])}
    results["21_1_1"].append(row)
    print(f"21_1_1 seed {seed} done ({time.time() - start:.0f} s)", flush=True)

# 22_0_2: images keep their shape
Xtr, ytr = prepare(data["x_train"], data["y_train"], flat=False)
Xva, yva = prepare(data["x_val"], data["y_val"], flat=False)
Xte, yte = prepare(data["x_test"], data["y_test"], flat=False)
for seed in SEEDS:
    row = {"seed": seed}
    for label, make, epochs in [("mlp", make_mlp, 30),
                                ("cnn_no_bn", lambda: make_cnn(False), 12),
                                ("cnn_bn", lambda: make_cnn(True), 12)]:
        torch.manual_seed(seed)
        model = make()
        fit(model, Xtr, ytr, Xva, yva, epochs, keep_best=True)
        row[label] = {"test_acc": evaluate(model, Xte, yte)[1],
                      "shift_acc": [evaluate(model, shift_right(Xte, p), yte)[1] for p in range(5)]}
    results["22_0_2"].append(row)
    print(f"22_0_2 seed {seed} done ({time.time() - start:.0f} s)", flush=True)

(ROOT / "tools" / "seed_check_results.json").write_text(json.dumps(results, indent=1))


def summary(values):
    v = np.array(values)
    return f"mean {v.mean():.3f}, range {v.min():.3f} to {v.max():.3f}"


r = results["21_1_1"]
print("\n21_1_1 (5 seeds)")
for key in ["none_1k", "dropout_1k", "none_10k"]:
    print(f"  {key:11} final val loss {summary([x[key]['final_val_loss'] for x in r])};  "
          f"final val acc {summary([x[key]['final_val_acc'] for x in r])};  best val acc {summary([x[key]['best_val_acc'] for x in r])}")
d_loss = [x["none_1k"]["final_val_loss"] - x["dropout_1k"]["final_val_loss"] for x in r]
d_acc = [x["dropout_1k"]["best_val_acc"] - x["none_1k"]["best_val_acc"] for x in r]
m_acc = [x["none_10k"]["best_val_acc"] - x["none_1k"]["best_val_acc"] for x in r]
print(f"  dropout lowers final val loss by: {[round(v, 3) for v in d_loss]}")
print(f"  dropout gain in best val acc:     {[round(v, 3) for v in d_acc]}")
print(f"  10x data gain in best val acc:    {[round(v, 3) for v in m_acc]}")

r = results["22_0_2"]
print("\n22_0_2 (5 seeds)")
for key in ["mlp", "cnn_no_bn", "cnn_bn"]:
    print(f"  {key:10} test acc {summary([x[key]['test_acc'] for x in r])};  "
          f"shift 0-4 px (mean) {[round(float(np.mean([x[key]['shift_acc'][p] for x in r])), 3) for p in range(5)]}")
print(f"  CNN (no BN) minus MLP, test acc: {[round(x['cnn_no_bn']['test_acc'] - x['mlp']['test_acc'], 3) for x in r]}")
print(f"  loss at 2 px shift, MLP vs CNN (no BN): "
      f"{[(round(x['mlp']['shift_acc'][0] - x['mlp']['shift_acc'][2], 3), round(x['cnn_no_bn']['shift_acc'][0] - x['cnn_no_bn']['shift_acc'][2], 3)) for x in r]}")
print(f"\ntotal time {time.time() - start:.0f} s")
