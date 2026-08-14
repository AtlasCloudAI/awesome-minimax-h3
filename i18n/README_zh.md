# Awesome MiniMax H3

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Entries](https://img.shields.io/badge/entries-129-blue.svg)](https://github.com/AtlasCloudAI/awesome-minimax-h3) [![Verified](https://img.shields.io/badge/links%20verified-2026--08--14-brightgreen.svg)](https://github.com/AtlasCloudAI/awesome-minimax-h3)

> 围绕 MiniMax H3 长出来的一切——这是一个开放权重的全模态视频模型，画面与原生音频一起生成。权重、量化、LoRA、ComfyUI 节点、现成工作流，以及社区挖出来的各种玩法。每条都实测过、带日期。

[English](../README.md)

**收录范围：只收 H3。** MiniMax 的产品线不止 H3——M 系列 LLM、Music、星数比 H3 还高的 Agent 那条线，这里一概不收。一条目如果落不到 H3 上，就不属于这个清单。

## 目录

- [官方](#官方)
- [跑起来](#跑起来)
- [塞进你的显卡](#塞进你的显卡)
- [提速](#提速)
- [LoRA 与训练](#lora-与训练)
- [冷门玩法](#冷门玩法)
- [Agent 制片](#agent-制片)
- [Agent Skills](#agent-skills)
- [其他 ComfyUI 节点](#其他-comfyui-节点)
- [提示词](#提示词)
- [现成工作流](#现成工作流)
- [教程与资讯](#教程与资讯)
- [相关清单](#相关清单)
- [MiniMax H3 是什么？](#minimax-h3-是什么)
- [收录标准](#收录标准)

**条目怎么读。** 每条都带热度与最后更新时间，均为 2026-08-14 从官方 API 实测读取。`⭐` 表示这个社区项目被 MiniMax 官方点过名（开源一周盘点或社区精选页）——所以「官方」那一节里不标，那节本来就整节都是官方的。

---

## 官方

从这里开始。权重、文档与接口，全部来自 MiniMax 官方。

### 模型与权重

- [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) `5.9k★ · 2026-08-13` — 官方仓库——推理代码、模型卡与各任务参考管线。
- [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) `3.9k♥ · 2M↓ · 2026-08-13` — Hugging Face 官方权重。
- [MiniMax/MiniMax-H3（ModelScope）](https://modelscope.cn/models/MiniMax/MiniMax-H3) — ModelScope 官方权重——中国大陆访问更快的镜像。

### 文档、API 与社区

- [H3 开源社区精选页](https://hailuoai.com/h3-open#featured) — 官方持续更新的社区项目与教程精选页。本清单以它为对齐基准。
- [H3 官方使用手册](https://vrfi1sk8a0.feishu.cn/wiki/FIWjwgL33ipnkekzk30crmKUnIh) — 官方完整使用手册——精选页第一条。
- [开源发布公告](https://www.minimax.io/news/minimax-h3-open-source) — 《Open General Intelligence》——开源发布稿。
- [官方模型技术博客](https://www.minimax.io/blog/minimax-h3) — H3 如何打破任务与模态边界的技术解读。
- [H3 产品页（Hailuo AI）](https://hailuoai.video/tools/minimax-h3) — 官方托管版 H3，无需显卡即可试用。
- [视频生成 v2 API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create) — H3 生成接口。
- [Context IR（H3 专有）](https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir) — H3 专有的多模态上下文中间表示——一套上下文设计在 API 侧的对应物。
- [重生成 API](https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration) — 固定其余上下文，只重掷某一镜头。
- [MiniMax Discord](https://discord.com/invite/dbMxutw7tP) — H3 疑难杂症的主要讨论地。

## 跑起来

在你手头这台机器上，让 H3 出第一条片子。

### 在 ComfyUI 里

- ⭐ [ComfyUI 官方 H3 教程](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) — 本地首次跑通阻力最小的路径。
- ⭐ [Comfy 官方模板：文生视频](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_t2v.json) — 官方 t2v 工作流模板。
- ⭐ [Comfy 官方模板：参考生视频](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_r2v.json) — 官方 r2v 工作流模板。
- [MiniMaxH3ComfyUI/MiniMax-H3-ComfyUI](https://github.com/MiniMaxH3ComfyUI/MiniMax-H3-ComfyUI) `93★ · 2026-08-08` — 整合包，省去手动拼节点。
- [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) `360★ · 2026-08-13` — 一套节点覆盖 t2v / i2v / 首尾帧 / 参考四种模式。

### 推理框架

- [vLLM 部署配方](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3) — vLLM 部署配方。
- [SGLang cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3) — SGLang 部署配方。
- [diffusers 管线文档](https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/minimax_h3.md) — H3 已合入 diffusers main——管线、调度器与两个自编码器齐备。

### 本地与跨平台

- ⭐ [antirez/h3.c](https://github.com/antirez/h3.c) `1.8k★ · 2026-08-11` — Redis 作者 antirez 用 C + Metal 从零重写的 Apple Silicon 原生推理引擎：直读 safetensors，Qwen 文/视编码器 + DiT + 双 VAE 全装进一个原生 Mac 程序，不依赖 Python/PyTorch。支持文生音视频、首尾帧与 Ref2VA。
- [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP) `8.4k★ · 2026-08-13` — 在低显存消费级显卡上跑 H3，配套 DeepBeepMeep 打包权重。
- [inlineresearch/Inline-Studio](https://github.com/inlineresearch/Inline-Studio) `217★ · 2026-08-13` — 节点式 AI 影视创作，跑本地 GPU。
- [PipeNetwork/minimax-h3-mlx](https://github.com/PipeNetwork/minimax-h3-mlx) `54★ · 2026-08-10` — 33B 视频+音频联合管线的 MLX 移植，与参考实现做过对齐验证。

### 特定硬件

- ⭐ [NVIDIA Sol Engine（NVlabs/Sana 的 sol-engine 分支）](https://github.com/NVlabs/Sana/tree/sol-engine) — NVIDIA 在开源首日 4.5 小时内完成 H3 优化：不改权重、无蒸馏、无 LoRA、无离线校准。
- ⭐ [Sol Engine — 数据中心部署报告](https://nvlabs.github.io/Sana/Sol-Engine/H3/) — 8×GB200 / 1344×768 / 24fps / 124 帧 / 50 步：3.95× vs Diffusers、2.80× vs SGLang。
- ⭐ [Sol Engine — 桌面级部署报告](https://nvlabs.github.io/Sana/Sol-Engine/H3-OnDevice/) — DGX Spark 3.92×、RTX 5090 4.52×。
- [Sol 视频推理引擎（论文）](https://arxiv.org/pdf/2606.23743) — 上述数字背后的方法论。
- ⭐ [charlie12345/R9700AIProComfyUIPatch](https://github.com/charlie12345/R9700AIProComfyUIPatch) `9★ · 2026-08-08` — 面向 RDNA4 Radeon AI PRO R9700 + ROCm 的 ComfyUI 补丁：优化 partial RoPE、长序列注意力与模型加载。在 32GB R9700 上按 864×480 / 124 帧 / 20 步实测提速。

### 在线试玩

- ⭐ [MiniMaxAI/MiniMax-H3-Turbo-Lora](https://huggingface.co/spaces/MiniMaxAI/MiniMax-H3-Turbo-Lora) `107♥ · 2026-08-14` — 官方 Space，跑 Turbo LoRA。
- [multimodalart/minimax-h3](https://huggingface.co/spaces/multimodalart/minimax-h3) `251♥ · 2026-08-12` — 社区 likes 最高的 Space。
- [mrfakename/minimax-h3-ultra-fast](https://huggingface.co/spaces/mrfakename/minimax-h3-ultra-fast) `98♥ · 2026-08-08` — 少步数版本，适合快速尝鲜。
- [multimodalart/minimax-h3-reference](https://huggingface.co/spaces/multimodalart/minimax-h3-reference) `78♥ · 2026-08-07` — 在浏览器里试参考条件（Ref2VA）模式。
- [akhaliq/MiniMax-H3-Turbo-Lora](https://huggingface.co/spaces/akhaliq/MiniMax-H3-Turbo-Lora) `51♥ · 2026-08-12` — 另一个托管的 Turbo LoRA demo。
- [geocine/MiniMax-H3-Prompt-Enhancer](https://huggingface.co/spaces/geocine/MiniMax-H3-Prompt-Enhancer) `13♥ · 2026-08-09` — 把粗略想法扩写成适配 H3 的提示词。
- [Atlas Cloud — 托管 H3 API](https://www.atlascloud.ai/models/minimax/h3/text-to-video?utm_source=github&utm_campaign=awesome-minimax-h3) — 托管的 t2v / i2v / ref2v 接口，适合不想让 42GB 常驻本地的情况。利益相关：由维护本清单的团队运营。

## 塞进你的显卡

完整模型 123.6GB。这一节是把它压到台式机装得下的那些项目。

### 打包版

- ⭐ [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) `1.3k♥ · 11.8M↓ · 2026-08-09` — ComfyUI 官方打包版，按下载量看多数人实际就是这样跑 H3 的：裁掉 4 成调制权重 + INT8 ConvRot + 定制 kernel，123.6GB → 42.5GB。
- [DeepBeepMeep/MiniMax-H3](https://huggingface.co/DeepBeepMeep/MiniMax-H3) `45♥ · 345.9k↓ · 2026-08-13` — Wan2GP 作者的低显存打包。

### 量化

- [realrebelai/MiniMax-H3_GGUFs](https://huggingface.co/realrebelai/MiniMax-H3_GGUFs) *(GGUF)* `200♥ · 317.9k↓ · 2026-08-08` — likes 最高的 GGUF 合集。
- [Abiray/Minimax-H3-nvfp4-INT4-INT8-Convrot](https://huggingface.co/Abiray/Minimax-H3-nvfp4-INT4-INT8-Convrot) *(NVFP4 · INT4/INT8 ConvRot)* `181♥ · 680.6k↓ · 2026-08-11` — 混合精度构建；社区量化里下载量最高。
- [unsloth/MiniMax-H3-GGUF](https://huggingface.co/unsloth/MiniMax-H3-GGUF) *(GGUF)* `152♥ · 136.8k↓ · 2026-08-11` — Unsloth 出品的 GGUF 转换。
- [Abiray/MiniMax-H3-GGUF](https://huggingface.co/Abiray/MiniMax-H3-GGUF) *(GGUF)* `102♥ · 667.7k↓ · 2026-08-08` — 使用面很广的 GGUF 合集。
- [lilcheaty/MiniMax-H3-NVFP4](https://huggingface.co/lilcheaty/MiniMax-H3-NVFP4) *(NVFP4)* `80♥ · 2026-08-05` — 面向 Blackwell 级显卡的 NVFP4。
- [molbal/MiniMax-H3-GGUF](https://huggingface.co/molbal/MiniMax-H3-GGUF) *(GGUF)* `49♥ · 186.3k↓ · 2026-08-12` — 另一条 GGUF 线。
- [leejet/MiniMax-H3-GGUF](https://huggingface.co/leejet/MiniMax-H3-GGUF) *(GGUF)* `14♥ · 50.8k↓ · 2026-08-04` — 出自 stable-diffusion.cpp 作者之手。

### 分离组件

- [Kijai/MiniMax-H3_comfy](https://huggingface.co/Kijai/MiniMax-H3_comfy) `329♥ · 2026-08-13` — Kijai 的 ComfyUI 转换合集——事实标准组件集，含降 rank 的 LoRA。
- [Kijai/MiniMax-H3-experimental](https://huggingface.co/Kijai/MiniMax-H3-experimental) `226♥ · 2026-08-08` — 同作者的实验版本。
- [Kijai/MiniMax-H3-TAE](https://huggingface.co/Kijai/MiniMax-H3-TAE) `129♥ · 2026-08-05` — 微型自编码器——用快速预览替代整段 VAE 解码。
- [NicoLab28/ClipProj-MiniMax-H3](https://huggingface.co/NicoLab28/ClipProj-MiniMax-H3) `91♥ · 2026-08-12` — 投影后的文本编码器：15.7GB → 5.2GB。
- [Mamad8/MiniMax-H3-Image-VAE](https://huggingface.co/Mamad8/MiniMax-H3-Image-VAE) `46♥ · 2026-08-08` — 拆出的图像 VAE，配合单帧玩法。
- [nicolab28/ComfyUI-ClipProj](https://github.com/nicolab28/ComfyUI-ClipProj) `63★ · 2026-08-12` — ClipProj 的 ComfyUI 端——用一个学出来的线性投影把大文本编码器换成小的。

## 提速

两条互不冲突的路子：减少采样步数（Turbo LoRA）和让每步更便宜（缓存、注意力 kernel）。两者可以叠加。

### Turbo LoRA——20 步降到 4–8 步

- ⭐ [larryvrh/MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora) `729♥ · 2026-08-08` — 最早的 4 步 Turbo LoRA，含多个 ckpt / EMA 变体。4 步提速约 5×，但大动作易拖影；6–8 步能保住细节与音质。
- [Larryvrh/ComfyUI-MiniMax-H3-Turbo](https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo) `430★ · 2026-08-12` — 配套 LoRA 加载节点与 Turbo 采样器，适配 BF16 / INT8 ConvRot / pruned。
- [lightx2v/Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo) `477♥ · 149.9k↓ · 2026-08-13` — 蒸馏 Turbo 权重；方法开源在 ModelTC/Minimax-H3-Turbo。
- [ModelTC/Minimax-H3-Turbo](https://github.com/ModelTC/Minimax-H3-Turbo) `176★ · 2026-08-13` — 上述权重背后的 4 步蒸馏方法。
- [drbaph/MiniMax-H3-Turbo-Lora-ComfyUI](https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI) `317♥ · 113k↓ · 2026-08-13` — 为 pruned 构建做的兼容转换。
- [joyfox/MiniMax-H3-Turbo](https://huggingface.co/joyfox/MiniMax-H3-Turbo) `58♥ · 2026-08-12` — BF16 专用 4 步。
- [t8star/minimax-h3-4step-turbo-loras-comfyui-exp](https://huggingface.co/t8star/minimax-h3-4step-turbo-loras-comfyui-exp) `47♥ · 2026-08-09` — 针对 int8_convrot 的版本。
- [Abiray/MiniMax-H3-Turbo-Lora-Pruned-ComfyUI](https://huggingface.co/Abiray/MiniMax-H3-Turbo-Lora-Pruned-ComfyUI) `41♥ · 14k↓ · 2026-08-09` — 附带工作流 JSON。
- [tutututututu/…-AudioVideo-20to8-NFE-LoRA](https://huggingface.co/tutututututu/Tutu-MiniMax-H3-AudioVideo-20to8-NFE-LoRA) `17♥ · 2026-08-09` — 20→8 NFE，针对保住音频做了调校。

### 缓存与注意力

- [kijai/ComfyUI-SolAttn_triton](https://github.com/kijai/ComfyUI-SolAttn_triton) `273★ · 2026-08-08` — 用 Triton 把 Sol-Attn 落到 ComfyUI。
- [Saganaki22/ComfyUI-sol-attn](https://github.com/Saganaki22/ComfyUI-sol-attn) `83★ · 2026-08-13` — 另一个 Sol-Attn 集成。
- [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) `506★ · 2026-08-14` — 频谱预测加速。
- [HELPMEEADICE/TE-Speed-MiniMaxH3-OSS](https://github.com/HELPMEEADICE/TE-Speed-MiniMaxH3-OSS) `236★ · 2026-08-03` — 文本编码器超级缓存加速。
- [T8mars/comfyui-minimax-h3-blockcache-T8](https://github.com/T8mars/comfyui-minimax-h3-blockcache-T8) `100★ · 2026-08-14` — Block cache。
- [duckyshell/ComfyUI-MiniMaxH3-FirstBlockCache](https://github.com/duckyshell/ComfyUI-MiniMaxH3-FirstBlockCache) `77★ · 2026-08-07` — First-block cache。
- [lihaoyun6/ComfyUI-MiniMaxH3-Cache](https://github.com/lihaoyun6/ComfyUI-MiniMaxH3-Cache) `75★ · 2026-08-03` — 专为 H3 优化的缓存加速节点。

## LoRA 与训练

教会 H3 它本来没有的调性——以及自己动手训练的几条路。

### 风格 / 能力 LoRA

- ⭐ [fal/MiniMax-H3-Realism-People-LoRA](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA) `163♥ · 9.1k↓ · 2026-08-12` — 厂商训练的真人写实 LoRA：176 条视频、统一 24fps、16 组超参对比。
- [Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime](https://huggingface.co/Inner-Reflections/MiniMax-H3-Looping-Sketch-Anime) `52♥ · 2026-08-11` — 循环动漫手绘。

### 自己练一个

- ⭐ [fal H3 LoRA 训练器](https://fal.ai/models/minimax/h3/t2v/trainer) — 按训练步计费的托管训练器，有 t2v / flf2v / i2v / ref2va 四个入口。参考素材同时进入 H3 视觉条件序列与 Qwen3-VL 提示词侧，因此画面与声音可联合训练；帧数、分辨率、rank、步数、参考条件比例均可调。
- [fal — 怎么训一个 H3 LoRA](https://fal.ai/learn/devs/how-to-train-a-lora-for-minimax-h3) — 他们给的实用默认值：10–200 条 24fps 短片、rank 16 起、lr 2e-4、固定 seed 做 A/B 评估。
- ⭐ [IAmIronMan42/MiniMax-H3-FineTuning](https://github.com/IAmIronMan42/MiniMax-H3-FineTuning) `552★ · 2026-08-10` — 基于官方 diffusers 集成的完整微调：画面与声音分别处理噪声日程，真实立体声入训。已在 8×A800 上用 2000+ 条 30s / 448×768 素材跑通。
- [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) `12.9k★ · 2026-08-14` — H3 完整训练链路——LoRA 训练脚本 + 模型文档。
- [DiffSynth — H3 LoRA 训练脚本](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/minimax_h3/model_training/lora/MiniMax-H3-FL2VA.sh) — FL2VA 的 LoRA 训练入口脚本。
- [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) `11.7k★ · 2026-08-13` — 已加入 H3 t2v / i2v 训练。
- [unslothai/unsloth](https://github.com/unslothai/unsloth) `71.3k★ · 2026-08-14` — 支持的训练目标中明确列出 MiniMax-H3。

## 冷门玩法

整个生态最有意思的一角：H3 被发现能干一些它从没被训练去干的事。MiniMax 官方的开源一周盘点，开篇讲的正是这些而不是跑分。

### 把镜头无限续下去

- ⭐ [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) `531★ · 2026-08-12` — 递归生成：直读上一段的画面与音频 latent，截末尾 22 帧作下一段的开头条件，音频重对齐到同一条时间线——避开「解码再编码」的信息损失。
- [ethanfel/ComfyUI-MiniMaxH3-Contex-Loop](https://github.com/ethanfel/ComfyUI-MiniMaxH3-Contex-Loop) `204★ · 2026-08-14` — 可审核的长片工作流：分镜规划 + 逐段预览 + 重生成 + 检查点 + 自动拼接。
- [jlucasmcrell/ComfyUI-H3-Multishot](https://github.com/jlucasmcrell/ComfyUI-H3-Multishot) `70★ · 2026-08-14` — 一次生成多镜头。

### 拿视频模型编辑单张图

- ⭐ [tori29umai0123/ComfyUI-MiniMaxH3-SingleFrame](https://github.com/tori29umai0123/ComfyUI-MiniMaxH3-SingleFrame) `72★ · 2026-08-09` — 零专门训练就把 H3 变成图像编辑器：输入图钉在第 0 帧 → 直接生成单帧 AV latent → 解码为图像；另一模式钉住首尾两图取中间帧。含 Temporal RoPE Patch 与 Empty Single Frame Latent 节点。
- [Comfy-Org/ComfyUI#15416](https://github.com/Comfy-Org/ComfyUI/issues/15416) — 单帧 VAE 解码伪影的跟踪 issue——自己提单前先看这条。

### 其他

- [Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler](https://github.com/Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler) `192★ · 2026-08-03` — AV latent 放大。
- [matlowai/ComfyUI-MAINodes](https://github.com/matlowai/ComfyUI-MAINodes) `55★ · 2026-08-14` — Contact-Sheet 扩散（一次生成里出同一主体的多个视角）+ 用于推理期 de-roping 的 Motion Lab。

### 纯音频生成，不需要任何仓库

官方点名的三种玩法里，有一种压根没有仓库。做法：拿默认的图生视频工作流，把输入图断开，分辨率降到 32×32，再用 Get Video Components 单独取出对白、环境声和音效。接近实时，音质没有明显下降，产出还能回灌当音频参考。官方开源一周盘点里把这个技巧记在开发者 comfiestncoziest 名下；原帖应该在 Reddit，我们没能找到——知道出处的话欢迎告诉我们。

## Agent 制片

H3 出的是镜头，不是成片。这些项目补的是镜头之上的那层：分镜规划、连贯性、批量、剪辑与导出。

- ⭐ [chiphoton/MiniMax-H3-Codex-Drama](https://github.com/chiphoton/MiniMax-H3-Codex-Drama) `9★ · 2026-08-13` — 可安装的 Codex 插件，内置 9 项 Skills，经 ComfyUI MCP 调度本地 H3：角色与场景设定 → 分镜关键帧 → 按镜头选工作流 → FFmpeg 剪辑混音字幕导出质检。提示词、素材、候选镜头与选择结果全留档，中断可续、每次新尝试各留版本。
- ⭐ [huangserva/ComfyUI_MiniMaxH3_Director](https://github.com/huangserva/ComfyUI_MiniMaxH3_Director) `585★ · 2026-08-04` — 分段计划 + 条件编码 + 采样解码 + 导出整合进一个节点；PySceneDetect 自动切场景，上一段结尾动作与音频作为下一段上下文。
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) `424★ · 2026-08-14` — 多段导演，适配官方节点。
- [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) `190★ · 2026-08-10` — 时间轴故事板。
- [open-video-ai/open-video](https://github.com/open-video-ai/open-video) `81★ · 2026-08-07` — 「MiniMax H3 版的 Ollama」——架在 ComfyUI 之上的本地导演层。
- [yg496/CS-H3-Multimodal-Director](https://github.com/yg496/CS-H3-Multimodal-Director) `50★ · 2026-08-05` — 多模态导演套件。

## Agent Skills

可安装的 skill，让编码 agent（Claude Code、Codex、OpenCode 等）替你写提示词、驱动整条流水线。

- [benjiyaya/Minimax-H3-Prompt-AgentSkill](https://github.com/benjiyaya/Minimax-H3-Prompt-AgentSkill) `87★ · 2026-08-06` — 把素材 + 粗略想法转成规范 H3 提示词的 Agent Skill。
- [SlavaSexton/ComfyUI-Agent-Kit](https://github.com/SlavaSexton/ComfyUI-Agent-Kit) `74★ · 2026-08-10` — 一个 ComfyUI skill，Claude Code / Codex / Gemini CLI / Qwen Code 都能驱动。
- [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) `67★ · 2026-08-14` — 以可安装 skill 形式打包的创意 DNA 提示词案例。
- [unknowlei/minimax-h3-opencode-skills](https://github.com/unknowlei/minimax-h3-opencode-skills) `65★ · 2026-08-09` — OpenCode skill 套件：导演、路由、多镜头规划与提示词生成。

## 其他 ComfyUI 节点

归不进上面几类，但确实好用的节点。

- [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) `683★ · 2026-08-14` — 音频侧节点——多数 H3 工作流最没用起来的一块。
- [ethanfel/ComfyUI-MiniMax-H3-Guide](https://github.com/ethanfel/ComfyUI-MiniMax-H3-Guide) `169★ · 2026-08-11` — 把提示词规范化成 H3 吃得准的形状。
- [Carasibana/ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) `173★ · 2026-08-12` — 解决 H3 出片里小脸糊的问题：逐帧人脸跟踪、裁切、精修、贴回。
- [HM-RunningHub/ComfyUI_RH_MinMaxH3](https://github.com/HM-RunningHub/ComfyUI_RH_MinMaxH3) `114★ · 2026-08-05` — RunningHub 的 H3 节点包。
- [scottmudge/ComfyUI_MinimaxH3HybridLoader](https://github.com/scottmudge/ComfyUI_MinimaxH3HybridLoader) `96★ · 2026-08-11` — 混合加载器——把 fl2va 与 ref2va 两个模型的层/块混搭成一个。

## 提示词

H3 吃的提示词形状比较特定，这些工具帮你写对。

- [lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA](https://huggingface.co/lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA) `153♥ · 732↓ · 2026-08-07` — 改写提示词而不是改画面的 LoRA。
- [fal — H3 提示词指南](https://fal.ai/learn/devs/minimax-h3-prompting-guide) — 提示词指南，附 44 个视频示例。
- [1038lab/ComfyUI-MiniMax-H3-Promptor](https://github.com/1038lab/ComfyUI-MiniMax-H3-Promptor) `120★ · 2026-08-14` — 影视级提示词自动化。
- [T8mars/comfyui-minimax-h3-prompt-enhancer-T8](https://github.com/T8mars/comfyui-minimax-h3-prompt-enhancer-T8) `118★ · 2026-08-14` — 多模态提示词增强。
- [Adudeguyman/…-PromptBuilder](https://github.com/Adudeguyman/ComfyUI-Fantastic-MiniMaxH3-PromptBuilder) `90★ · 2026-08-14` — 提示词构建器节点。
- [duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer](https://github.com/duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer) `74★ · 2026-08-14` — 跑在 Gemma 4 GGUF 上的本地多模态提示词写手，不发 API 请求。
- [penposs/minimax-h3-video-prompt](https://github.com/penposs/minimax-h3-video-prompt) `51★ · 2026-08-04` — 从目标 + 多模态参考出发生成并复核提示词。

## 现成工作流

来自 Civitai 与 GitHub 的即插即用工作流，含那些真能跑起来的低显存配置。这块很热，但其他 H3 清单基本没收。

### GitHub 上的

- [Shrek3OnVH5/MiniMax-H3-NativeAudio-MusicVideo-Workflow](https://github.com/Shrek3OnVH5/MiniMax-H3-NativeAudio-MusicVideo-Workflow) `61★ · 2026-08-05` — 围绕 H3 原生音频搭的音乐视频工作流。

### Civitai 上的

- [H3 [LightX2V 6-8steps] collection](https://civitai.com/models/579280) *(Workflows)* `27.8k↓` — 下载量最高的 H3 工作流合集。
- [MiniMax H3 INT8/INT4 ConvRot](https://civitai.com/models/2830065) *(Checkpoint)* `16.8k↓` — 打包给 ComfyUI 的 ConvRot 检查点。
- [Lonecat's Simple Workflows](https://civitai.com/models/2600919) *(Workflows)* `13.7k↓` — 刻意做简的工作流。
- [MiniMax H3 lightx2v turbo accelerator](https://civitai.com/models/1063735) *(LORA)* `10.5k↓` — 以 LoRA 形式直接换入的 Turbo 加速。
- [MiniMax H3: EZ Turbo / RTX Upscale / LTX Refine](https://civitai.com/models/2831976) *(Workflows)* `9.2k↓` — Turbo 加超分与精修环节。
- [T2V / I2V / REF2V Advanced Filmmaking](https://civitai.com/models/2834514) *(Workflows)* `8.3k↓` — 一套影视流程覆盖三种输入模式。
- [MiniMax-H3 Multishot Seamless Chain](https://civitai.com/models/2833322) *(Workflows)* `4.6k↓` — 多镜头无缝串联生成。
- [Ultra Fastest Workflow (6GB VRAM / 16GB RAM)](https://civitai.com/models/2835250) *(Workflows)* `4k↓` — 真能跑起来的低配方案。
- [SageAttention four-mode workflow](https://civitai.com/models/2831550) *(ComfyWorkflows)* `3.7k↓` — SageAttention 四种模式并列对比。
- [4 STEPS TURBO AIO](https://civitai.com/models/2838258) *(Workflows)* `2.9k↓` — 4 步一体化配置。
- [INT4 ConvRot (12GB VRAM)](https://civitai.com/models/2830162) *(Checkpoint)* `2.4k↓` — 把 H3 塞进 12GB 显存。
- [SEEDVR2 upscaler + Ollama prompt helper](https://civitai.com/models/2836319) *(Workflows)* `2.4k↓` — 超分与本地提示词助手合在一张图里。
- [Claymation Transformation](https://civitai.com/models/1659949) *(LORA)* `1.4k↓` — 黏土动画风格。

## 教程与资讯

跟得上节奏的指南与资讯源。

### 英文

- [ComfyUI Wiki — H3](https://comfyui-wiki.com/en/tutorial/advanced/video/minimax/minimax-h3) — 中英双语教程 + 每日新闻，Turbo LoRA、Image VAE、AI-Toolkit 训练落地时都跟进报道过。
- [Oxen.ai — H3 完整指南](https://www.oxen.ai/blog/minimax-h3) — 长篇完整指南。
- [RunPod — 跑起来到底要什么配置](https://www.runpod.io/blog/minimax-h3-the-open-weight-omni-modal-video-model-and-what-it-takes-to-run-it) — 对硬件账单的老实核算。
- [Morphic — H3 规格页](https://morphic.com/resources/models/minimax-h3) — 规格速查。
- [Kingy.ai — ComfyUI 本地部署指南](https://kingy.ai/ai/ai-guides/minimax-h3-comfyui-local-guide/) — ComfyUI 本地部署走查。
- [ComfyUI Wiki — AI-Toolkit 加入 H3 训练](https://comfyui-wiki.com/en/news/2026-08-03-ai-toolkit-minimax-h3-training) — ai-toolkit 加入 H3 训练的报道。

### 中文

- [macin.top — 本地部署](https://macin.top/posts/12dcc77b/index.html) — 中文本地部署笔记。
- [jiazhuangai — LoRA + ComfyUI](https://jiazhuangai.com/articles/minimax-h3-loracomfyui4) — 中文 LoRA + ComfyUI 指南。

## 相关清单

同一片地上，做得有价值的其他清单。

- [wildminder/awesome-minimax-H3](https://github.com/wildminder/awesome-minimax-H3) `197★ · 2026-08-13` — 在权重、量化与节点清单上做得极细——需要文件级细节时该看它。
- [AtlasCloudAI/awesome-minimax-h3-prompts](https://github.com/AtlasCloudAI/awesome-minimax-h3-prompts) `15★ · 2026-08-13` — 本清单的姊妹仓：官方案例 H3 提示词，每条附成片预览，20 语言。

---

## MiniMax H3 是什么？

H3 是 MiniMax 的开放权重全模态视频模型。它不把文生视频、图生视频、参考条件和音频当成几个不同的模型，而是读同一份多模态上下文，把画面与立体声一起生成。整个生态之所以长成现在这样，根子就在这个设计上：下面最有意思的那些项目，多半是有人发现这一个模型已经能干一些没人专门训练过它的事——编辑单张图、单独生成音频、把一个镜头无限续下去。

## 收录标准

- **只收 SFW。** H3 的 LoRA 生态里成人向占了不小比例，这里一概不收；去审查组件（比如被剥掉限制的文本编码器）同样不收——哪怕某些加速工作本身做得不错，只要依赖它就一起排除。
- **热度门槛 + 一条豁免。** GitHub ≥ 50 星、Hugging Face ≥ 10 likes、Civitai ≥ 500 下载。门槛是为了挡住这个关键词下泛滥的 SEO 空壳。唯一豁免是官方点名：MiniMax 自己点过名的一律直收，不看热度——本清单最有意思的两条就只有个位数星。
- **每条链接都能打开。** 全清单已于 2026-08-14 用 GitHub / Hugging Face / Civitai 的 API 重新核验。已转私有、404、或无法程序化验证的条目一律剔除，不凭信任沿用。
- **是 H3，不是 MiniMax。** 见上面的收录范围。

## 清单怎么保持更新

条目数据在 [`data/ecosystem.json`](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/data/ecosystem.json)，两份 README 都由 `npm run generate` 生成。改 JSON，别改 Markdown。MiniMax 官方维护着一个持续更新的[社区精选页](https://hailuoai.com/h3-open#featured)，本清单会定期与它对齐。

## 参与贡献

发现遗漏？[提 issue](https://github.com/AtlasCloudAI/awesome-minimax-h3/issues/new/choose) 或直接发 PR。请附链接、它能做而这里其他项目做不到的事、以及当前星数/likes。先读 [CONTRIBUTING.md](https://github.com/AtlasCloudAI/awesome-minimax-h3/blob/main/CONTRIBUTING.md)——上面的标准是照字面执行的。

## 许可

[CC BY 4.0](LICENSE)。被收录项目各自的许可证不受影响。
