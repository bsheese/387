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

**Source and license.** O. M. Parkhi, A. Vedaldi, A. Zisserman and C. V. Jawahar,
"Cats and Dogs," CVPR 2012. The dataset is licensed CC BY-SA 4.0, and these
derived files are shared under the same license.
