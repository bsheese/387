"""Build data/pets4.zip, the four-breed subset of Oxford-IIIT Pets used in 19_0 and 19_1.

The full dataset is about 800 MB, which is too slow to download at the start of
every class. This script takes four breeds, splits each into fixed train,
validation and test sets, shrinks every image so its shorter side is 256 pixels,
and writes the result as one small zip that the notebooks download from GitHub.
It also copies a few images of other breeds into other/ for the 19_0_2 section
on images outside the four classes.

Usage (from the 387 repo root, after downloading and extracting images.tar.gz
from https://www.robots.ox.ac.uk/~vgg/data/pets/):

    python data/make_pets4.py /path/to/pets/images

Oxford-IIIT Pets: Parkhi, Vedaldi, Zisserman and Jawahar, "Cats and Dogs",
CVPR 2012. Licensed CC BY-SA 4.0, so this subset is shared under the same license.
"""

import pathlib
import random
import shutil
import sys
import tempfile

from PIL import Image

BREEDS = ["Birman", "Ragdoll", "basset_hound", "beagle"]
SPLIT_SIZES = {"train": 100, "val": 50, "test": 50}
# Breeds that are not among the four, for showing what the model does with them.
OTHER = {"Siamese": 3, "Persian": 2, "pug": 2, "samoyed": 2, "keeshond": 1}
SHORT_SIDE = 256
SEED = 387

OUT = pathlib.Path(__file__).resolve().parent / "pets4.zip"


def shrink(src, dst):
    img = Image.open(src).convert("RGB")  # a few originals are grayscale or RGBA
    w, h = img.size
    scale = SHORT_SIDE / min(w, h)
    if scale < 1:
        img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    img.save(dst, "JPEG", quality=85)


def main(raw_dir):
    raw_dir = pathlib.Path(raw_dir)
    rng = random.Random(SEED)
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp) / "pets4"
        for breed in BREEDS:
            files = sorted(raw_dir.glob(f"{breed}_*.jpg"))
            rng.shuffle(files)
            start = 0
            for split, n in SPLIT_SIZES.items():
                folder = root / split / breed
                folder.mkdir(parents=True)
                for f in files[start:start + n]:
                    shrink(f, folder / f.name)
                start += n
        (root / "other").mkdir()
        for breed, n in OTHER.items():
            files = sorted(raw_dir.glob(f"{breed}_*.jpg"))
            for f in rng.sample(files, n):
                shrink(f, root / "other" / f.name)
        archive = shutil.make_archive(str(OUT.with_suffix("")), "zip", tmp, "pets4")
    print(f"wrote {archive} ({OUT.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main(sys.argv[1])
