# Awesome MiniMax H3

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Entries](https://img.shields.io/badge/entries-138-blue.svg)](https://github.com/AtlasCloudAI/awesome-minimax-h3) [![Verified](https://img.shields.io/badge/links%20verified-2026--08--18-brightgreen.svg)](https://github.com/AtlasCloudAI/awesome-minimax-h3)

> Everything built on top of MiniMax H3 — the open-weight omni-modal video model that generates picture and native audio together. Weights, quantizations, LoRAs, ComfyUI nodes, workflows and the tricks people found. Every entry checked against a live API and dated.

[简体中文](i18n/README_zh.md)

**Scope: H3 only.** MiniMax ships plenty besides H3 — the M-series LLMs, Music, an agent stack with more stars than H3 itself. None of it is here. If an entry cannot be pointed at H3, it does not belong on this list.

## Contents

- [Official](#official)
- [Run it](#run-it)
- [Fit it on your GPU](#fit-it-on-your-gpu)
- [Make it fast](#make-it-fast)
- [LoRAs and training](#loras-and-training)
- [Unusual tricks](#unusual-tricks)
- [Direct a film](#direct-a-film)
- [Agent skills](#agent-skills)
- [Other ComfyUI nodes](#other-comfyui-nodes)
- [Prompting](#prompting)
- [Ready-made workflows](#ready-made-workflows)
- [Learn](#learn)
- [Related lists](#related-lists)
- [What is MiniMax H3?](#what-is-minimax-h3)
- [What gets in](#what-gets-in)

**How to read an entry.** Every entry carries its popularity and the date it was last touched, both read from the live API on 2026-08-18. `⭐` marks a community project that MiniMax named itself, in its release roundup or on its community picks page — so it is not applied inside the Official section, where everything is official by definition.

---

## Official

Start here. Weights, docs and the endpoints, straight from MiniMax.

### Model and weights

- [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) `6.2k★ · 2026-08-15` — Official repository — inference code, model card and the reference pipelines for every H3 task.
- [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) `4.1k♥ · 2.4M↓ · 2026-08-13` — Official weights on Hugging Face.
- [MiniMax/MiniMax-H3 (ModelScope)](https://modelscope.cn/models/MiniMax/MiniMax-H3) — Official weights on ModelScope — the faster mirror inside mainland China.

### Documentation, API and community

- [H3 open-source community picks](https://hailuoai.com/h3-open#featured) — The official, continuously updated showcase of community projects and tutorials. This list tracks it.
- [H3 user handbook](https://vrfi1sk8a0.feishu.cn/wiki/FIWjwgL33ipnkekzk30crmKUnIh) — The complete official usage handbook — first entry on the picks page.
- [Open-source announcement](https://www.minimax.io/news/minimax-h3-open-source) — "Open General Intelligence" — the release post.
- [Model tech blog](https://www.minimax.io/blog/minimax-h3) — How H3 collapses tasks and modalities into one context.
- [H3 product page (Hailuo AI)](https://hailuoai.video/tools/minimax-h3) — Hosted H3 — try it without a GPU.
- [Video generation v2 API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create) — The H3 generation endpoint.
- [Context IR (H3-only)](https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir) — H3's multimodal context intermediate representation — the API-side counterpart of its one-context design.
- [Regeneration API](https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration) — Re-roll a shot while keeping the rest of the context fixed.
- [MiniMax Discord](https://discord.com/invite/dbMxutw7tP) — Where most H3 troubleshooting actually happens.

## Run it

Getting H3 to produce a first clip, on whatever hardware you actually have.

### In ComfyUI

- ⭐ [ComfyUI official H3 tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) — The path of least resistance for a first local run.
- ⭐ [Comfy template: text-to-video](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_t2v.json) — Official t2v workflow template.
- ⭐ [Comfy template: reference-to-video](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_r2v.json) — Official r2v workflow template.
- [MiniMaxH3ComfyUI/MiniMax-H3-ComfyUI](https://github.com/MiniMaxH3ComfyUI/MiniMax-H3-ComfyUI) `128★ · 2026-08-08` — All-in-one bundle for people who would rather not assemble nodes by hand.
- [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) `449★ · 2026-08-15` — One node set covering t2v, i2v, first/last-frame and reference modes.
- [LeonQ8/ComfyUI-ALLinONE-MinimaxH3](https://github.com/LeonQ8/ComfyUI-ALLinONE-MinimaxH3) `199★ · 2026-08-18` — The entire H3 pipeline behind one node — pick a mode, drop in a prompt or references, generate. No graph to wire up and no hunting through a dozen node packs to find the right workflow.

### Serving frameworks

- [vLLM recipe](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3) — Serving recipe for vLLM.
- [SGLang cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3) — Serving recipe for SGLang.
- [diffusers pipeline docs](https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/minimax_h3.md) — H3 is merged into diffusers main — pipeline, scheduler and both autoencoders.

### Local and cross-platform

- ⭐ [antirez/h3.c](https://github.com/antirez/h3.c) `2.2k★ · 2026-08-11` — Redis author antirez rewrote H3 inference from scratch in C + Metal: safetensors read directly, Qwen text/vision encoders, DiT and both VAEs in one native Mac binary — no Python, no PyTorch. Covers t2av, first/last-frame and Ref2VA.
- [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP) `8.7k★ · 2026-08-16` — Runs H3 on low-VRAM consumer cards; pairs with the DeepBeepMeep packaged weights.
- [inlineresearch/Inline-Studio](https://github.com/inlineresearch/Inline-Studio) `233★ · 2026-08-18` — Node-based AI filmmaking on your own GPU.
- [PipeNetwork/minimax-h3-mlx](https://github.com/PipeNetwork/minimax-h3-mlx) `59★ · 2026-08-10` — MLX port of the full 33B joint video+audio pipeline, validated against the reference implementation.
- [mrbizarro/Phosphene](https://github.com/mrbizarro/Phosphene) `163★ · 2026-08-16` — Video, image and character-LoRA training on a Mac, all in MLX: no PyTorch, no CUDA, no cloud, no API key. One-click Pinokio install, and it runs LTX-2.5 alongside H3.

### Hardware-specific

- ⭐ [NVIDIA Sol Engine (NVlabs/Sana, sol-engine branch)](https://github.com/NVlabs/Sana/tree/sol-engine) — NVIDIA optimized H3 within 4.5 hours of release, with no weight changes, no distillation, no LoRA and no offline calibration.
- ⭐ [Sol Engine — datacenter report](https://nvlabs.github.io/Sana/Sol-Engine/H3/) — 8×GB200, 1344×768, 24fps, 124 frames, 50 steps: 3.95× vs Diffusers, 2.80× vs SGLang.
- ⭐ [Sol Engine — on-device report](https://nvlabs.github.io/Sana/Sol-Engine/H3-OnDevice/) — 3.92× on DGX Spark, 4.52× on RTX 5090.
- [Sol Video Inference Engine (paper)](https://arxiv.org/pdf/2606.23743) — The method behind the numbers above.
- ⭐ [charlie12345/R9700AIProComfyUIPatch](https://github.com/charlie12345/R9700AIProComfyUIPatch) `10★ · 2026-08-08` — ComfyUI patch for RDNA4 Radeon AI PRO R9700 on ROCm — tuned partial RoPE, long-sequence attention and model loading. Benchmarked at 864×480, 124 frames, 20 steps on a 32GB R9700.

### Try it online

- ⭐ [MiniMaxAI/MiniMax-H3-Turbo-Lora](https://huggingface.co/spaces/MiniMaxAI/MiniMax-H3-Turbo-Lora) `201♥ · 2026-08-14` — Official Space running the Turbo LoRA.
- [multimodalart/minimax-h3](https://huggingface.co/spaces/multimodalart/minimax-h3) `261♥ · 2026-08-16` — The most-liked community Space.
- [mrfakename/minimax-h3-ultra-fast](https://huggingface.co/spaces/mrfakename/minimax-h3-ultra-fast) `111♥ · 2026-08-08` — Few-step variant, for a quick look.
- [multimodalart/minimax-h3-reference](https://huggingface.co/spaces/multimodalart/minimax-h3-reference) `82♥ · 2026-08-16` — Try the reference-conditioned (Ref2VA) mode in the browser.
- [akhaliq/MiniMax-H3-Turbo-Lora](https://huggingface.co/spaces/akhaliq/MiniMax-H3-Turbo-Lora) `62♥ · 2026-08-12` — Another hosted Turbo LoRA demo.
- [geocine/MiniMax-H3-Prompt-Enhancer](https://huggingface.co/spaces/geocine/MiniMax-H3-Prompt-Enhancer) `21♥ · 2026-08-09` — Expands a bare idea into an H3-shaped prompt.
- [Atlas Cloud — hosted H3 API](https://www.atlascloud.ai/models/minimax/h3/text-to-video?utm_source=github&utm_campaign=awesome-minimax-h3) — Hosted t2v, i2v and ref2v endpoints, for when you would rather not keep 42GB resident. Disclosure: run by the people who maintain this list.

## Fit it on your GPU

The full model is 123.6GB. These are the projects that got it down to something a desktop can hold.

### Packaged builds

- ⭐ [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) `1.4k♥ · 14M↓ · 2026-08-17` — The ComfyUI packaged build, and by download count the way most people actually run H3: 40% of the modulation weights pruned, INT8 ConvRot and custom kernels take 123.6GB down to 42.5GB.
- [DeepBeepMeep/MiniMax-H3](https://huggingface.co/DeepBeepMeep/MiniMax-H3) `49♥ · 371.6k↓ · 2026-08-13` — Low-VRAM packaging from the Wan2GP author.

### Quantizations

- [realrebelai/MiniMax-H3_GGUFs](https://huggingface.co/realrebelai/MiniMax-H3_GGUFs) *(GGUF)* `201♥ · 392.5k↓ · 2026-08-08` — The most-liked GGUF set.
- [Abiray/Minimax-H3-nvfp4-INT4-INT8-Convrot](https://huggingface.co/Abiray/Minimax-H3-nvfp4-INT4-INT8-Convrot) *(NVFP4 · INT4/INT8 ConvRot)* `193♥ · 703.4k↓ · 2026-08-15` — Mixed-precision builds; the download leader among community quants.
- [unsloth/MiniMax-H3-GGUF](https://huggingface.co/unsloth/MiniMax-H3-GGUF) *(GGUF)* `186♥ · 217.9k↓ · 2026-08-14` — Unsloth's GGUF conversions.
- [Abiray/MiniMax-H3-GGUF](https://huggingface.co/Abiray/MiniMax-H3-GGUF) *(GGUF)* `113♥ · 723.4k↓ · 2026-08-08` — Widely used GGUF set.
- [lilcheaty/MiniMax-H3-NVFP4](https://huggingface.co/lilcheaty/MiniMax-H3-NVFP4) *(NVFP4)* `82♥ · 2026-08-05` — NVFP4 for Blackwell-class cards.
- [molbal/MiniMax-H3-GGUF](https://huggingface.co/molbal/MiniMax-H3-GGUF) *(GGUF)* `50♥ · 194.5k↓ · 2026-08-12` — Another GGUF line.
- [leejet/MiniMax-H3-GGUF](https://huggingface.co/leejet/MiniMax-H3-GGUF) *(GGUF)* `15♥ · 57.5k↓ · 2026-08-04` — From the author of stable-diffusion.cpp.
- [Abiray/MiniMax-H3-Pruned-GGUF](https://huggingface.co/Abiray/MiniMax-H3-Pruned-GGUF) *(GGUF)* `47♥ · 186.6k↓ · 2026-08-07` — GGUF built on the pruned weights — the smallest route that still tracks the ComfyUI build.

### Split-out components

- [Kijai/MiniMax-H3_comfy](https://huggingface.co/Kijai/MiniMax-H3_comfy) `372♥ · 2026-08-13` — Kijai's ComfyUI conversions — the de-facto standard component set, including rank-reduced LoRAs.
- [Kijai/MiniMax-H3-experimental](https://huggingface.co/Kijai/MiniMax-H3-experimental) `236♥ · 2026-08-08` — Experimental variants from the same author.
- [Kijai/MiniMax-H3-TAE](https://huggingface.co/Kijai/MiniMax-H3-TAE) `139♥ · 2026-08-05` — Tiny autoencoder — fast previews instead of full VAE decodes.
- [NicoLab28/ClipProj-MiniMax-H3](https://huggingface.co/NicoLab28/ClipProj-MiniMax-H3) `112♥ · 2026-08-16` — Projected text encoder: 15.7GB down to 5.2GB.
- [Mamad8/MiniMax-H3-Image-VAE](https://huggingface.co/Mamad8/MiniMax-H3-Image-VAE) `62♥ · 2026-08-08` — Image VAE split out for single-frame work.
- [nicolab28/ComfyUI-ClipProj](https://github.com/nicolab28/ComfyUI-ClipProj) `93★ · 2026-08-17` — The ComfyUI side of ClipProj — swaps the large text encoder for a small one through a learned linear projection.
- [smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models](https://huggingface.co/smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models) `77♥ · 2026-08-16` — Pre-merged fl2va/ref2va hybrids, for when you would rather download the combination than assemble it with a hybrid loader.

## Make it fast

Two separate levers: fewer sampling steps (Turbo LoRAs) and cheaper steps (caching, attention kernels). They compose.

### Turbo LoRAs — 20 steps down to 4–8

- ⭐ [larryvrh/MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora) `789♥ · 2026-08-08` — The original 4-step Turbo LoRA, with multiple checkpoint and EMA variants. 4 steps is ~5× faster but smears large motion; 6–8 steps keeps detail and audio quality.
- [Larryvrh/ComfyUI-MiniMax-H3-Turbo](https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo) `456★ · 2026-08-14` — Matching loader node and Turbo sampler; handles BF16, INT8 ConvRot and pruned builds.
- [lightx2v/Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo) `586♥ · 264.4k↓ · 2026-08-13` — Distilled Turbo weights; the method is open-sourced in ModelTC/Minimax-H3-Turbo.
- [ModelTC/Minimax-H3-Turbo](https://github.com/ModelTC/Minimax-H3-Turbo) `262★ · 2026-08-15` — The 4-step distillation method behind the weights above.
- [drbaph/MiniMax-H3-Turbo-Lora-ComfyUI](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI) `335♥ · 141.4k↓ · 2026-08-13` — Converted for pruned-build compatibility.
- [joyfox/MiniMax-H3-Turbo](https://huggingface.co/joyfox/MiniMax-H3-Turbo) `62♥ · 2026-08-12` — 4-step, BF16 only.
- [t8star/minimax-h3-4step-turbo-loras-comfyui-exp](https://huggingface.co/t8star/minimax-h3-4step-turbo-loras-comfyui-exp) `51♥ · 2026-08-09` — Built for int8_convrot.
- [Abiray/MiniMax-H3-Turbo-Lora-Pruned-ComfyUI](https://huggingface.co/Abiray/MiniMax-H3-Turbo-Lora-Pruned-ComfyUI) `43♥ · 15.9k↓ · 2026-08-09` — Ships with workflow JSON.
- [tutututututu/…-AudioVideo-20to8-NFE-LoRA](https://huggingface.co/tutututututu/Tutu-MiniMax-H3-AudioVideo-20to8-NFE-LoRA) `17♥ · 2026-08-09` — 20 → 8 NFE, tuned to keep audio intact.

### Caching and attention

- [kijai/ComfyUI-SolAttn_triton](https://github.com/kijai/ComfyUI-SolAttn_triton) `323★ · 2026-08-08` — Brings Sol-Attn into ComfyUI via Triton.
- [Saganaki22/ComfyUI-sol-attn](https://github.com/Saganaki22/ComfyUI-sol-attn) `93★ · 2026-08-13` — Another Sol-Attn integration.
- [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) `530★ · 2026-08-16` — Spectral prediction to cut steps.
- [HELPMEEADICE/TE-Speed-MiniMaxH3-OSS](https://github.com/HELPMEEADICE/TE-Speed-MiniMaxH3-OSS) `251★ · 2026-08-03` — Aggressive text-encoder caching.
- [T8mars/comfyui-minimax-h3-blockcache-T8](https://github.com/T8mars/comfyui-minimax-h3-blockcache-T8) `106★ · 2026-08-14` — Block cache.
- [duckyshell/ComfyUI-MiniMaxH3-FirstBlockCache](https://github.com/duckyshell/ComfyUI-MiniMaxH3-FirstBlockCache) `79★ · 2026-08-07` — First-block cache.
- [lihaoyun6/ComfyUI-MiniMaxH3-Cache](https://github.com/lihaoyun6/ComfyUI-MiniMaxH3-Cache) `75★ · 2026-08-03` — Cache node tuned specifically for H3.
- [Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler](https://github.com/Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler) `198★ · 2026-08-17` — Upscales AV latents.
- [LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler](https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler) `73★ · 2026-08-17` — Upscales H3's 24-channel latents with a trained network rather than naive interpolation, skipping the expensive VAE decode/encode round trip on the way to high resolution.

## LoRAs and training

Teaching H3 a look it does not have — and the paths to training your own.

### Style and capability LoRAs

- ⭐ [fal/MiniMax-H3-Realism-People-LoRA](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA) `245♥ · 18.6k↓ · 2026-08-12` — Vendor-trained realistic-people LoRA: 176 clips at a uniform 24fps, 16 hyperparameter runs compared.
- [Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime](https://huggingface.co/Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime) `57♥ · 2026-08-11` — Looping hand-drawn anime.
- [Jojocodex/minimax-h3-spatial-physics-lora](https://huggingface.co/Jojocodex/minimax-h3-spatial-physics-lora) `35♥ · 49↓ · 2026-08-17` — Trained for spatial reasoning and object motion rather than a look — aimed at the physics H3 gets wrong.

### Train your own

- ⭐ [fal H3 LoRA Trainer](https://fal.ai/models/minimax/h3/t2v/trainer) — Hosted trainer billed per training step, with t2v, flf2v, i2v and ref2va entry points. Reference material feeds both H3's visual conditioning sequence and the Qwen3-VL prompt side, so picture and sound can be trained together; frames, resolution, rank, steps and reference-conditioning ratio are all adjustable.
- [fal — how to train an H3 LoRA](https://fal.ai/learn/devs/how-to-train-a-lora-for-minimax-h3) — Their working defaults: 10–200 clips at 24fps, rank 16 and up, lr 2e-4, A/B evaluation on a fixed seed.
- ⭐ [IAmIronMan42/MiniMax-H3-FineTuning](https://github.com/IAmIronMan42/MiniMax-H3-FineTuning) `55★ · 2026-08-10` — Full fine-tuning on top of the official diffusers integration: separate noise schedules for picture and sound, real stereo audio in training. Run on 8×A800 over 2000+ clips at 30s / 448×768.
- [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) `13k★ · 2026-08-17` — Complete H3 training path — LoRA scripts plus model docs.
- [DiffSynth — H3 LoRA training script](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/minimax_h3/model_training/lora/MiniMax-H3-FL2VA.sh) — The FL2VA LoRA training entry point.
- [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) `11.7k★ · 2026-08-17` — Added H3 t2v and i2v training.
- [unslothai/unsloth](https://github.com/unslothai/unsloth) `73.3k★ · 2026-08-18` — Lists MiniMax-H3 among its supported training targets.

## Unusual tricks

The most interesting corner of this ecosystem: things H3 turned out to do that it was never trained to do. MiniMax's own release roundup led with these rather than with benchmarks.

### Continue a shot indefinitely

- ⭐ [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) `619★ · 2026-08-15` — Recursive generation: reads the previous segment's picture and audio latents directly, takes its last 22 frames as the next segment's opening condition, and re-aligns audio onto one timeline — avoiding the information loss of decoding and re-encoding between segments.
- [ethanfel/ComfyUI-MiniMaxH3-Contex-Loop](https://github.com/ethanfel/ComfyUI-MiniMaxH3-Contex-Loop) `255★ · 2026-08-18` — Reviewable long-form workflow: shot planning, per-segment preview, regeneration, checkpoints and automatic stitching.
- [tritant/ComfyUI_MiniMax_H3_Extender](https://github.com/tritant/ComfyUI_MiniMax_H3_Extender) `111★ · 2026-08-18` — Folds Ref2VA conditioning, Motion Context, disk caching, multi-clip generation and image/audio references into one node, so long continuous sequences stop requiring a hand-built graph.

### Use a video model to edit one image

- ⭐ [tori29umai0123/ComfyUI-MiniMaxH3-SingleFrame](https://github.com/tori29umai0123/ComfyUI-MiniMaxH3-SingleFrame) `78★ · 2026-08-09` — Turns H3 into an image editor with no extra training at all: pin the input image at frame 0, generate a single AV latent, decode it as an image. A second mode pins first and last frames and takes the middle. Ships Temporal RoPE Patch and Empty Single Frame Latent nodes.
- [Comfy-Org/ComfyUI#15416](https://github.com/Comfy-Org/ComfyUI/issues/15416) — Tracking issue for single-frame VAE decode artifacts — read before you file your own.
- [thaakeno/ComfyUI-MiniMax-H3-Studio](https://github.com/thaakeno/ComfyUI-MiniMax-H3-Studio) `63★ · 2026-08-17` — Turns H3 into an actual image workflow: text-to-image, editing, multi-reference generation, LightX acceleration, face refine, previews and benchmarking — without building the H3 graph yourself.

### Other

- [matlowai/ComfyUI-MAINodes](https://github.com/matlowai/ComfyUI-MAINodes) `90★ · 2026-08-18` — Contact-sheet diffusion (several views of one subject in a single generation) plus a motion lab for test-time de-roping.

### Audio-only generation, no repository required

One of the three tricks MiniMax highlighted has no repo at all. Take the default image-to-video workflow, disconnect the input image, and drop the resolution to 32×32. Pull dialogue, ambience and effects out separately with Get Video Components. It runs close to real time, audio quality does not noticeably suffer, and the result can be fed back in as an audio reference. Credited to developer comfiestncoziest in the official one-week roundup; the original write-up appears to be a Reddit post we have not been able to locate — a pointer would be welcome.

## Direct a film

H3 makes shots, not films. These projects add what sits above a shot: planning, continuity, batching, edit and export.

- ⭐ [chiphoton/MiniMax-H3-Codex-Drama](https://github.com/chiphoton/MiniMax-H3-Codex-Drama) `11★ · 2026-08-16` — An installable Codex plugin with nine built-in skills that drives local H3 through the ComfyUI MCP: character and scene design, storyboard keyframes, per-shot workflow selection, then FFmpeg edit, mix, subtitle, export and QC. Prompts, assets, candidate takes and selection results are all kept, so a run can be resumed and each new attempt keeps its own version.
- ⭐ [huangserva/ComfyUI_MiniMaxH3_Director](https://github.com/huangserva/ComfyUI_MiniMaxH3_Director) `684★ · 2026-08-04` — Segment planning, conditioning, sampling, decoding and export folded into one node; PySceneDetect splits scenes automatically and the previous segment's closing motion and audio become the next one's context.
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) `530★ · 2026-08-15` — Multi-segment directing, adapted to the official nodes.
- [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) `213★ · 2026-08-16` — Timeline storyboard.
- [open-video-ai/open-video](https://github.com/open-video-ai/open-video) `108★ · 2026-08-07` — "Ollama for MiniMax H3" — a local director layer over ComfyUI.
- [yg496/CS-H3-Multimodal-Director](https://github.com/yg496/CS-H3-Multimodal-Director) `54★ · 2026-08-05` — Multimodal directing setup.

## Agent skills

Installable skills that let a coding agent — Claude Code, Codex, OpenCode and friends — do the prompting and drive the pipeline for you.

- [Rimagination/h3lite](https://github.com/Rimagination/h3lite) `217★ · 2026-08-17` — Hardware-aware Codex skill for local generation through ComfyUI: it profiles what you have and picks the route — low-VRAM fast, or quality — instead of making you choose. Bilingual docs.
- [benjiyaya/Minimax-H3-Prompt-AgentSkill](https://github.com/benjiyaya/Minimax-H3-Prompt-AgentSkill) `100★ · 2026-08-06` — Agent Skill that turns media plus a rough idea into a formatted H3 prompt.
- [SlavaSexton/ComfyUI-Agent-Kit](https://github.com/SlavaSexton/ComfyUI-Agent-Kit) `77★ · 2026-08-16` — One ComfyUI skill that every coding agent can drive — Claude Code, Codex, Gemini CLI, Qwen Code.
- [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) `87★ · 2026-08-17` — Creative-DNA prompt cases packaged as installable skills.
- [unknowlei/minimax-h3-opencode-skills](https://github.com/unknowlei/minimax-h3-opencode-skills) `74★ · 2026-08-09` — OpenCode skill suite: directing, routing, multishot planning and prompt generation.

## Other ComfyUI nodes

Useful nodes that do not fit the categories above.

- [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) `729★ · 2026-08-17` — Audio-side nodes — the part most H3 workflows under-use.
- [ethanfel/ComfyUI-MiniMax-H3-Guide](https://github.com/ethanfel/ComfyUI-MiniMax-H3-Guide) `189★ · 2026-08-11` — Normalizes prompts into the shape H3 responds to.
- [Carasibana/ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) `239★ · 2026-08-12` — Fixes the small-face problem in H3 output: per-frame face tracking, crop, refine, composite back.
- [HM-RunningHub/ComfyUI_RH_MinMaxH3](https://github.com/HM-RunningHub/ComfyUI_RH_MinMaxH3) `119★ · 2026-08-05` — RunningHub's H3 node pack.
- [scottmudge/ComfyUI_MinimaxH3HybridLoader](https://github.com/scottmudge/ComfyUI_MinimaxH3HybridLoader) `125★ · 2026-08-11` — Hybridization loader — combine layers and blocks from the fl2va and ref2va models into one.

## Prompting

H3 responds to a fairly specific prompt shape. These help you hit it.

- [lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA](https://huggingface.co/lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA) `166♥ · 864↓ · 2026-08-07` — A LoRA that rewrites your prompt instead of your pixels.
- [fal — H3 prompting guide](https://fal.ai/learn/devs/minimax-h3-prompting-guide) — Prompting guide with 44 worked video examples.
- [1038lab/ComfyUI-MiniMax-H3-Promptor](https://github.com/1038lab/ComfyUI-MiniMax-H3-Promptor) `141★ · 2026-08-14` — Cinematic prompt automation.
- [T8mars/comfyui-minimax-h3-prompt-enhancer-T8](https://github.com/T8mars/comfyui-minimax-h3-prompt-enhancer-T8) `136★ · 2026-08-17` — Multimodal prompt enhancement.
- [Adudeguyman/…-PromptBuilder](https://github.com/Adudeguyman/ComfyUI-Fantastic-MiniMaxH3-PromptBuilder) `102★ · 2026-08-18` — Prompt builder node.
- [duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer](https://github.com/duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer) `91★ · 2026-08-15` — Local multimodal prompt writer running on Gemma 4 GGUF — no API calls.
- [penposs/minimax-h3-video-prompt](https://github.com/penposs/minimax-h3-video-prompt) `53★ · 2026-08-04` — Generates and reviews prompts from a goal plus multimodal references.
- [benjiyaya/ComfyUI-H3-VisionPromptor](https://github.com/benjiyaya/ComfyUI-H3-VisionPromptor) `62★ · 2026-08-09` — Give it an idea plus optional reference images and it returns a prompt with shots, camera vocabulary, dialogue tags, soundscape and music fields filled in.

## Ready-made workflows

Drop-in graphs from Civitai and GitHub — including the low-VRAM configurations that actually run. Popular, and largely absent from other H3 lists.

### On GitHub

- [Shrek3OnVH5/MiniMax-H3-NativeAudio-MusicVideo-Workflow](https://github.com/Shrek3OnVH5/MiniMax-H3-NativeAudio-MusicVideo-Workflow) `69★ · 2026-08-05` — Music-video workflow built around H3's native audio.

### On Civitai

- [H3 [LightX2V 6-8steps] collection](https://civitai.com/models/579280) *(Workflows)* `29k↓` — The most-downloaded H3 workflow collection.
- [MiniMax H3 INT8/INT4 ConvRot](https://civitai.com/models/2830065) *(Checkpoint)* `18.2k↓` — ConvRot checkpoints packaged for ComfyUI.
- [Lonecat's Simple Workflows](https://civitai.com/models/2600919) *(Workflows)* `14.3k↓` — Deliberately minimal workflows.
- [MiniMax H3 lightx2v turbo accelerator](https://civitai.com/models/1063735) *(LORA)* `11.9k↓` — Turbo acceleration packaged as a LoRA drop-in.
- [MiniMax H3: EZ Turbo / RTX Upscale / LTX Refine](https://civitai.com/models/2831976) *(Workflows)* `10.3k↓` — Turbo plus upscale and refine passes.
- [T2V / I2V / REF2V Advanced Filmmaking](https://civitai.com/models/2834514) *(Workflows)* `11.3k↓` — Covers all three input modes in one filmmaking setup.
- [MiniMax-H3 Multishot Seamless Chain](https://civitai.com/models/2833322) *(Workflows)* `5.9k↓` — Chained multi-shot generation.
- [Ultra Fastest Workflow (6GB VRAM / 16GB RAM)](https://civitai.com/models/2835250) *(Workflows)* `4.7k↓` — The low-end configuration that actually runs.
- [SageAttention four-mode workflow](https://civitai.com/models/2831550) *(ComfyWorkflows)* `4.2k↓` — Four SageAttention modes side by side.
- [4 STEPS TURBO AIO](https://civitai.com/models/2838258) *(Workflows)* `3.3k↓` — All-in-one 4-step setup.
- [INT4 ConvRot (12GB VRAM)](https://civitai.com/models/2830162) *(Checkpoint)* `2.7k↓` — Fits H3 into 12GB.
- [SEEDVR2 upscaler + Ollama prompt helper](https://civitai.com/models/2836319) *(Workflows)* `2.9k↓` — Upscaling and a local prompt assistant in one graph.
- [Claymation Transformation](https://civitai.com/models/1659949) *(LORA)* `1.5k↓` — Clay-animation look.

## Learn

Guides and news sources that keep up.

### English

- [ComfyUI Wiki — H3](https://comfyui-wiki.com/en/tutorial/advanced/video/minimax/minimax-h3) — Bilingual tutorials plus daily news; it has covered the Turbo LoRA, Image VAE and AI-Toolkit training as they landed.
- [Oxen.ai — complete H3 guide](https://www.oxen.ai/blog/minimax-h3) — Long-form walkthrough.
- [RunPod — what it takes to run it](https://www.runpod.io/blog/minimax-h3-the-open-weight-omni-modal-video-model-and-what-it-takes-to-run-it) — Honest accounting of the hardware bill.
- [Morphic — H3 spec sheet](https://morphic.com/resources/models/minimax-h3) — Specs at a glance.
- [Kingy.ai — ComfyUI local guide](https://kingy.ai/ai/ai-guides/minimax-h3-comfyui-local-guide/) — Local ComfyUI setup walkthrough.
- [ComfyUI Wiki — AI-Toolkit H3 training](https://comfyui-wiki.com/en/news/2026-08-03-ai-toolkit-minimax-h3-training) — Report on ai-toolkit adding H3 training.

### Chinese

- [macin.top — 本地部署](https://macin.top/posts/12dcc77b/index.html) — Chinese local deployment notes.
- [jiazhuangai — LoRA + ComfyUI](https://jiazhuangai.com/articles/minimax-h3-loracomfyui4) — Chinese LoRA and ComfyUI guide.

## Related lists

Other people covering the same ground, usefully.

- [wildminder/awesome-minimax-H3](https://github.com/wildminder/awesome-minimax-H3) `267★ · 2026-08-17` — Deeply detailed on weights, quantizations and node inventory — the reference to reach for when you want file-level specifics.
- [AtlasCloudAI/awesome-minimax-h3-prompts](https://github.com/AtlasCloudAI/awesome-minimax-h3-prompts) `19★ · 2026-08-17` — Our companion list: H3 prompts from the official showcase, each with its generated preview, in 20 languages.

---

## What is MiniMax H3?

H3 is MiniMax's open-weight omni-modal video model. Instead of treating text-to-video, image-to-video, reference conditioning and audio as separate models, it reads one multimodal context and generates picture and stereo audio jointly. That single design decision is why this ecosystem looks the way it does: the interesting projects below are mostly people discovering that one model already does things nobody trained it to do — editing a single image, generating audio on its own, continuing a shot indefinitely.

## What gets in

- **SFW only.** A meaningful slice of the H3 LoRA scene is adult-oriented. None of it is here, and neither are uncensored components such as stripped text encoders — including otherwise-good speed work that depends on them.
- **Popularity floor, with one exemption.** 50+ stars on GitHub, 10+ likes on Hugging Face, 500+ downloads on Civitai. The floor keeps out the SEO shells that crowd this keyword. The single exemption is official recognition: anything MiniMax named itself goes in regardless — two of the best entries here have single-digit stars.
- **Every link resolves.** The whole list was re-checked against the GitHub, Hugging Face and Civitai APIs on 2026-08-18. Entries that had gone private, 404'd, or that could not be verified programmatically were dropped rather than carried over on trust.
- **H3, not MiniMax.** See the scope note above.

## How this list stays current

Twice a week a [GitHub Action](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/.github/workflows/refresh.yml) re-checks every entry against the GitHub, Hugging Face and Civitai APIs: figures and dates are refreshed, renamed repositories are followed, and anything that stops resolving is withheld from the list — then deleted if it is still gone three weeks later. If more than a tenth of the run fails, it publishes nothing rather than stamp a verification date the entries did not earn.

A [weekly sweep](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/.github/workflows/discover.yml) looks for H3 projects that are missing here and clear the bar, and files them as a review issue. Nothing is ever added automatically — whether a project does something no listed project already does is not a question a query can answer.

Entries live in [`data/ecosystem.json`](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/data/ecosystem.json) and both READMEs are generated from it by `npm run generate`; edit the JSON, not the Markdown. MiniMax keeps its own [community picks page](https://hailuoai.com/h3-open#featured) updated, and this list is reconciled against it.

## Contributing

Found something missing? [Open an issue](https://github.com/AtlasCloudAI/awesome-minimax-h3/issues/new/choose) or send a PR. Include the link, what it does that nothing else here does, and its current star or like count. Read [CONTRIBUTING.md](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/CONTRIBUTING.md) first — the bar above is applied literally.

## License

[CC BY 4.0](LICENSE). Linked projects keep their own licenses.
