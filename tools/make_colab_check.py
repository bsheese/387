"""Build tools/colab_check.ipynb, the notebook that times the course in Colab.

It is not course material. It records Colab's library versions, runs every
course notebook through smoke_test.py, and times the candidate models for
22_2 (diffusion) and unit 23 (DistilBERT, GPT-2). The last cell prints one
block of text to paste back.

    python tools/make_colab_check.py
"""

import pathlib

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

OUT = pathlib.Path(__file__).resolve().parent / "colab_check.ipynb"
BADGE = ('<a href="https://colab.research.google.com/github/bsheese/387/blob/main/tools/colab_check.ipynb" '
         'target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>')

cells = [
("md", BADGE),
("md", r"""
# 387 Colab Check

Not course material. This notebook times the course on Colab and tests the models planned for 22_2 and unit 23.

**Run it twice:**

1. **GPU:** Runtime → Change runtime type → **T4 GPU** → Save. Then Runtime → **Run all**. About 20–30 minutes.
2. **CPU:** Runtime → Change runtime type → **CPU** → Save. Then Runtime → **Run all** again. Up to about an hour; it can run unattended. Parts that need a GPU are skipped automatically.

After each run, copy everything printed by the **last cell** and paste it back to Claude.

If Colab warns that a Hugging Face token (`HF_TOKEN`) isn't set, ignore it; nothing here needs one. Each part records its own errors, so a failure in one part doesn't stop the rest.
"""),
("code", r"""
import importlib.metadata, json, os, platform, subprocess, sys, time, traceback
os.environ['HF_HUB_DISABLE_XET'] = '1'      # the classic download path; the newer one hung in testing
import torch

RESULTS = {}
GPU = torch.cuda.is_available()
device = 'cuda' if GPU else 'cpu'

def record(section, **values):
    RESULTS.setdefault(section, {}).update(values)

def run_part(section, fn):
    # Run one part, recording its time and any error instead of stopping the notebook.
    start = time.time()
    try:
        fn()
        record(section, status='ok')
    except Exception as e:
        record(section, status='ERROR', error=f'{type(e).__name__}: {e}'[:500])
        traceback.print_exc()
    record(section, seconds=round(time.time() - start, 1))
    print(f"\n[{section}] {RESULTS[section].get('status')} in {RESULTS[section]['seconds']} s")

print('device:', device)
"""),
("md", "## Part 1: Environment"),
("code", r"""
def environment():
    versions = {}
    for pkg in ['torch', 'torchvision', 'numpy', 'pandas', 'scikit-learn', 'matplotlib', 'seaborn',
                'transformers', 'datasets', 'diffusers', 'accelerate', 'ipywidgets', 'nbconvert']:
        try:
            versions[pkg] = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            versions[pkg] = 'not installed'
    record('environment', python=platform.python_version(), cpus=os.cpu_count(),
           torch_threads=torch.get_num_threads(), versions=versions)
    if GPU:
        props = torch.cuda.get_device_properties(0)
        record('environment', gpu=props.name, gpu_memory_gb=round(props.total_memory / 1e9, 1))
    else:
        record('environment', gpu=None)
    try:
        mem = subprocess.run(['free', '-g'], capture_output=True, text=True).stdout.split('\n')[1].split()[1]
        record('environment', ram_gb=mem)
    except Exception:
        pass

run_part('environment', environment)
print(json.dumps(RESULTS['environment'], indent=1))
"""),
("md", r"""
## Part 2: Every course notebook

Clones the course repo and runs `smoke_test.py`, which executes each notebook in a fresh folder the way a student would, downloading data from GitHub. The 19_0_1 cell that asks for a photo upload is replaced first, because it would wait forever with nobody to click. This is the longest part, especially on the CPU.
"""),
("code", r"""
RUN_COURSE_NOTEBOOKS = os.environ.get('COLAB_CHECK_SKIP_COURSE') != '1'

def course_notebooks():
    if not RUN_COURSE_NOTEBOOKS:
        record('course_notebooks', skipped='COLAB_CHECK_SKIP_COURSE=1')
        return
    subprocess.run(['rm', '-rf', '387_check'])
    subprocess.run(['git', 'clone', '--depth', '1', '-q', 'https://github.com/bsheese/387', '387_check'], check=True)

    import nbformat
    path = '387_check/19_onramp/19_0_Whole_Game/19_0_1_Your_First_Image_Model.ipynb'
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if 'files.upload()' in cell.source:
            cell.source = "print('photo upload skipped in the Colab check')"
    nbformat.write(nb, path)

    proc = subprocess.run([sys.executable, 'smoke_test.py', '--remote-data', '--slow', '30', '--timeout', '1800'],
                          cwd='387_check', capture_output=True, text=True)
    lines = [l for l in proc.stdout.splitlines() if l.strip() and '#' not in l]
    print('\n'.join(lines))
    record('course_notebooks', exit_code=proc.returncode,
           report=[l for l in lines if ' ... ' in l or ' s  ' in l or 'passed' in l or 'FAIL' in l][:60])
    if proc.returncode != 0:
        record('course_notebooks', stderr_tail=proc.stdout[-1500:])

run_part('course_notebooks', course_notebooks)
"""),
("md", r"""
## Part 3: Diffusion models for 22_2

Three candidates:

- **DDPM on CIFAR-10** (`google/ddpm-cifar10-32`): small and unconditional, making 32 × 32 images of objects and animals. Timed with its full 1,000 steps and with a 50-step DDIM schedule, using a hand-written loop like the one 22_2_2 would show.
- **BK-SDM-Small** (`nota-ai/bk-sdm-small`): a compressed Stable Diffusion that makes 512 × 512 images from text. Timed on both GPU and CPU.
- **Stable Diffusion 1.5** (`stable-diffusion-v1-5/stable-diffusion-v1-5`): the standard text-to-image model, GPU only.
"""),
("code", r"""
import subprocess
try:
    import diffusers
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'diffusers'], check=True)
    import diffusers
import matplotlib.pyplot as plt

def ddpm():
    from diffusers import DDIMScheduler, DDPMScheduler, UNet2DModel
    t0 = time.time()
    unet = UNet2DModel.from_pretrained('google/ddpm-cifar10-32').to(device).eval()
    record('ddpm_cifar10', load_seconds=round(time.time() - t0, 1),
           weights=sum(p.numel() for p in unet.parameters()))
    snapshots = {}
    for name, scheduler, steps in [('ddim_50', DDIMScheduler.from_pretrained('google/ddpm-cifar10-32'), 50),
                                   ('ddpm_1000', DDPMScheduler.from_pretrained('google/ddpm-cifar10-32'), 1000)]:
        scheduler.set_timesteps(steps)
        torch.manual_seed(0)
        n_images = 4 if GPU else 1
        x = torch.randn(n_images, 3, 32, 32, device=device)
        t0 = time.time()
        saved = []
        with torch.no_grad():
            for i, t in enumerate(scheduler.timesteps):
                noise = unet(x, t).sample                  # the network's guess at the noise
                x = scheduler.step(noise, t, x).prev_sample  # remove a little of it
                if i % max(1, steps // 5) == 0 or i == steps - 1:
                    saved.append(x[0].clamp(-1, 1).cpu())
        record('ddpm_cifar10', **{f'{name}_seconds': round(time.time() - t0, 1), 'images_per_run': n_images})
        snapshots[name] = saved
    fig, axes = plt.subplots(2, 6, figsize=(12, 4.4))
    for row, (name, saved) in enumerate(snapshots.items()):
        for ax, img in zip(axes[row], saved[-6:]):
            ax.imshow((img.permute(1, 2, 0) + 1) / 2); ax.axis('off')
        axes[row, 0].set_title(name, fontsize=9)
    plt.show()

run_part('ddpm_cifar10', ddpm)
"""),
("code", r"""
def text_to_image(section, repo, steps, dtype):
    def part():
        from diffusers import StableDiffusionPipeline
        t0 = time.time()
        pipe = StableDiffusionPipeline.from_pretrained(repo, torch_dtype=dtype).to(device)
        pipe.set_progress_bar_config(disable=True)
        record(section, load_seconds=round(time.time() - t0, 1))
        if GPU:
            torch.cuda.reset_peak_memory_stats()
        latents_seen = []
        def keep(pipeline, step, timestep, kwargs):
            latents_seen.append(step)
            return kwargs
        t0 = time.time()
        image = pipe('a watercolor painting of a beagle in a field of flowers', num_inference_steps=steps,
                     generator=torch.Generator(device).manual_seed(0),
                     callback_on_step_end=keep).images[0]
        record(section, steps=steps, seconds_for_1_image=round(time.time() - t0, 1),
               step_callback_calls=len(latents_seen))
        if GPU:
            record(section, peak_gpu_memory_gb=round(torch.cuda.max_memory_allocated() / 1e9, 2))
        plt.figure(figsize=(4, 4)); plt.imshow(image); plt.axis('off'); plt.title(section); plt.show()
        del pipe
        if GPU:
            torch.cuda.empty_cache()
    return part

run_part('bk_sdm_small', text_to_image('bk_sdm_small', 'nota-ai/bk-sdm-small', 25 if GPU else 10,
                                       torch.float16 if GPU else torch.float32))
if GPU:
    run_part('stable_diffusion_1_5', text_to_image('stable_diffusion_1_5',
                                                   'stable-diffusion-v1-5/stable-diffusion-v1-5', 30, torch.float16))
else:
    record('stable_diffusion_1_5', skipped='no GPU')
"""),
("md", r"""
## Part 4: Language models for unit 23

- **DistilBERT fine-tuned on IMDB reviews** (23_2): 2,000 training reviews, 1,000 test reviews, 256 tokens each, one epoch, with a plain PyTorch loop like unit 21's. On the CPU only 10 training steps are timed, to estimate a full epoch.
- **A ready-made sentiment model** (`distilbert-base-uncased-finetuned-sst-2-english`) on 500 test reviews, with no training.
- **GPT-2 small** (23_3): next-token probabilities and sampled text.
"""),
("code", r"""
def distilbert():
    from datasets import load_dataset
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    t0 = time.time()
    imdb = load_dataset('stanfordnlp/imdb')
    train = imdb['train'].shuffle(seed=0).select(range(2000))
    test = imdb['test'].shuffle(seed=0).select(range(1000))
    record('distilbert_imdb', dataset_seconds=round(time.time() - t0, 1))

    tok = AutoTokenizer.from_pretrained('distilbert-base-uncased')
    model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2).to(device)
    def batches(split, size, limit=None):
        n = len(split) if limit is None else min(len(split), limit * size)
        for i in range(0, n, size):
            rows = split[i:i + size]
            enc = tok(rows['text'], truncation=True, max_length=256, padding=True, return_tensors='pt')
            yield {k: v.to(device) for k, v in enc.items()}, torch.tensor(rows['label'], device=device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
    limit = None if GPU else 10
    model.train()
    t0 = time.time()
    steps = 0
    for x, y in batches(train, 16, limit):
        optimizer.zero_grad()
        loss = model(**x, labels=y).loss
        loss.backward()
        optimizer.step()
        steps += 1
    train_seconds = time.time() - t0
    record('distilbert_imdb', train_steps=steps, train_seconds=round(train_seconds, 1),
           estimated_epoch_seconds=round(train_seconds / steps * (len(train) / 16), 1))

    model.eval()
    correct, t0 = 0, time.time()
    eval_limit = None if GPU else 5
    seen = 0
    with torch.no_grad():
        for x, y in batches(test, 32, eval_limit):
            correct += (model(**x).logits.argmax(dim=1) == y).sum().item()
            seen += len(y)
    record('distilbert_imdb', eval_reviews=seen, eval_seconds=round(time.time() - t0, 1),
           test_accuracy_after_training=round(correct / seen, 3))

def ready_made():
    from transformers import pipeline
    from datasets import load_dataset
    test = load_dataset('stanfordnlp/imdb')['test'].shuffle(seed=0).select(range(500))
    clf = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english',
                   device=0 if GPU else -1)
    t0 = time.time()
    out = clf(list(test['text']), truncation=True, max_length=256, batch_size=32)
    labels = [1 if o['label'] == 'POSITIVE' else 0 for o in out]
    record('sst2_pipeline', reviews=len(labels), seconds=round(time.time() - t0, 1),
           accuracy=round(sum(int(a == b) for a, b in zip(labels, list(test['label']))) / len(labels), 3))

def gpt2():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained('gpt2')
    model = AutoModelForCausalLM.from_pretrained('gpt2').to(device).eval()
    prompt = 'The best thing about a beagle is'
    ids = tok(prompt, return_tensors='pt').to(device)
    with torch.no_grad():
        probs = model(**ids).logits[0, -1].softmax(dim=0)
    top = probs.topk(5)
    record('gpt2', top_next_tokens=[(tok.decode(int(i)), round(p.item(), 3)) for p, i in zip(top.values, top.indices)])
    t0 = time.time()
    with torch.no_grad():
        outs = model.generate(**ids, max_new_tokens=50, do_sample=True, temperature=0.8, top_k=50,
                              num_return_sequences=5, pad_token_id=tok.eos_token_id)
    record('gpt2', seconds_for_5_samples_of_50_tokens=round(time.time() - t0, 1),
           sample=tok.decode(outs[0], skip_special_tokens=True)[:300])

run_part('distilbert_imdb', distilbert)
run_part('sst2_pipeline', ready_made)
run_part('gpt2', gpt2)
"""),
("md", "## Summary: copy everything below and paste it back"),
("code", r"""
print('===== 387 COLAB CHECK =====')
print(json.dumps(RESULTS, indent=1, default=str))
print('===== END =====')
"""),
]

nb = new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
               "language_info": {"name": "python"}, "accelerator": "GPU", "colab": {"provenance": []}}
for i, (kind, src) in enumerate(cells):
    cell = new_markdown_cell(src.strip("\n")) if kind == "md" else new_code_cell(src.strip("\n"))
    cell["id"] = f"c{i:03d}"
    nb.cells.append(cell)
nbformat.write(nb, OUT)
print("wrote", OUT)
