# data/

Files the notebooks download from GitHub with their `fetch()` helper
(`https://raw.githubusercontent.com/bsheese/387/main/data/<name>`). A notebook
only works in Colab once the files it uses have been pushed.

## Oxford-IIIT Pets, four breeds (19_0, 19_1)

| File | Made by | Used in | What it is |
|---|---|---|---|
| `pets4.zip` | `make_pets4.py` | 19_0_1, 19_0_2 | Birman, Ragdoll, basset hound and beagle: 100 train, 50 val and 50 test photos per breed, shorter side shrunk to 256 px. `other/` has 10 photos of breeds outside the four (Siamese, Persian, pug, samoyed, keeshond). |
| `pets4_head.pt` | running 19_0_1 (`my_pets4_head.pt`) | 19_0_1 (shortcut), 19_0_2 | `state_dict` of the trained last layer, `nn.Linear(512, 4)`. Put it on an ImageNet-pretrained ResNet-18 kept in `eval()` mode to rebuild the model. |
| `pets4_history.csv` | running 19_0_1 (`my_pets4_history.csv`) | 19_1_1 | Training loss, training accuracy and validation accuracy after each of the 8 epochs. |
| `pets4_predictions.csv` | running 19_0_2 | 19_1 | One row per photo (800): `file`, `split`, `breed`, `predicted`, `score_<breed>` (the four raw scores) and `prob_<breed>` (softmax of the scores). |
| `pets4_features.npz` | running 19_0_2 | 19_1_3 | `features` (800 × 512 float32, the ResNet-18 output before the last layer), with `filename`, `split` and `breed` for each row, in the same order as `pets4_predictions.csv`. |

The last four files must come from the same run, and the 19_0 notebooks'
saved outputs show that run. If you change 19_0_1 or 19_0_2, re-execute
19_0_1, copy its two `my_` files here without the prefix, then re-execute
19_0_2 with `pets4_head.pt` in its working directory and copy its two output
files here. The committed versions were made on a CPU, where the run is
deterministic; a GPU gives slightly different numbers.

To rebuild `pets4.zip`, download and extract `images.tar.gz` from
<https://www.robots.ox.ac.uk/~vgg/data/pets/> and run
`python data/make_pets4.py /path/to/images`.

## Palmer penguins (20_0_3)

`penguins.csv` is the same file as cs377's `data/penguins.csv` (344 penguins; 342 have
flipper length and body mass). From the palmerpenguins package by Allison Horst, Alison Hill
and Kristen Gorman, released under CC0.

## Fashion-MNIST (unit 21, 22_0)

`fashion10k.npz` (made by `make_fashion.py`): `x_train`/`y_train` (10,000 images, 1,000 per
class), `x_val`/`y_val` (5,000, 500 per class, disjoint from train; both drawn from the
official training set) and `x_test`/`y_test` (the official 10,000 test images), as
28 × 28 uint8 arrays, plus `classes` (the 10 names). From H. Xiao, K. Rasul and
R. Vollgraf, "Fashion-MNIST" (Zalando Research, 2017), MIT License.

## IMDB movie reviews (unit 23)

`imdb_reviews.csv` (made by `make_imdb.py`): columns `split`, `label` (1 positive, 0 negative)
and `text`. 2,000 train and 1,000 val reviews (disjoint, from the official training set) and
2,000 test reviews (from the official test set), each half positive, with the raw `<br />`
line breaks replaced by spaces. From the Large Movie Review Dataset, A. L. Maas et al.,
"Learning Word Vectors for Sentiment Analysis", ACL 2011, released by the authors for
research use.

## Pets source and license

**Source and license.** O. M. Parkhi, A. Vedaldi, A. Zisserman and C. V. Jawahar,
"Cats and Dogs," CVPR 2012. The dataset is licensed CC BY-SA 4.0, and these
derived files are shared under the same license.
