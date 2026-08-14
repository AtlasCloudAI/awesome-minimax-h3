# Contributing

Suggestions are welcome. The bar below is applied literally, so please check against it before opening anything — it saves us both a round trip.

## What belongs here

**H3, and only H3.** MiniMax publishes plenty of other things — the M-series LLMs, Music, an agent stack that has more stars than H3 itself. None of it belongs on this list. If you cannot point your entry at H3, it is out of scope, however good it is.

**SFW only.** Adult-oriented models, LoRAs and workflows are not accepted. Neither are uncensored components such as stripped text encoders, and neither is work that depends on them — including speed work that would otherwise qualify.

**Popularity floor.** 50+ stars on GitHub, 10+ likes on Hugging Face, 500+ downloads on Civitai. This keyword attracts a lot of empty SEO repositories and the floor is what keeps them out.

**One exemption to the floor:** projects MiniMax named itself, in its release roundup or on its [community picks page](https://hailuoai.com/h3-open#featured), are accepted regardless of stars. Say so in your suggestion and link the mention.

**It has to work.** Every link on this list resolves as of the snapshot date in the README. Dead, private and unverifiable links are removed rather than carried on trust.

## How to suggest an entry

[Open an issue](https://github.com/AtlasCloudAI/awesome-minimax-h3/issues/new/choose) with the link, its current star or like count, and — most importantly — what it does that nothing already on the list does. "Another H3 node pack" is not a reason; "the only one that fixes small faces" is.

## Sending a PR

Entries live in [`data/ecosystem.json`](data/ecosystem.json). Both READMEs are generated from it.

```bash
npm install
# edit data/ecosystem.json
npm run generate
```

Do not hand-edit `README.md` or `i18n/README_zh.md` — the generator overwrites them. Entries need both an `en` and a `zh` note; if you cannot write the Chinese one, write the English one and say so in the PR, and we will fill it in.

Popularity numbers and dates are snapshots, not live values. Leave them as they are in your PR; they are refreshed in bulk against the GitHub, Hugging Face and Civitai APIs.

---

## 中文说明

同样的四条标准：**只收 H3**（MiniMax 的 M 系列 LLM、Music、Agent 那条线一概不收）；**只收 SFW**（成人向与去审查组件，以及依赖它们的项目，都不收）；**热度门槛**（GitHub ≥ 50 星 / HF ≥ 10 likes / Civitai ≥ 500 下载，唯一豁免是官方点名过的项目）；**链接必须能打开**。

提交时请说明：链接、当前热度、以及**它能做而清单里其他项目做不到的事**——这一条最重要。

改数据请改 [`data/ecosystem.json`](data/ecosystem.json) 后跑 `npm run generate`，**不要手改两份 README**（会被覆盖）。条目需要中英两份 note；写不了中文的话写英文并在 PR 里说一声，我们来补。
