/**
 * Generates README.md (English) and i18n/README_zh.md (Simplified Chinese)
 * from data/ecosystem.json.
 *
 * Do not hand-edit the generated READMEs — run `npm run generate` instead.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const REPO = 'https://github.com/AtlasCloudAI/awesome-minimax-h3'

type Locale = 'en' | 'zh'

interface Item {
  kind: string
  /** Repository ids stay verbatim; descriptive names carry a per-locale form. */
  name: string | Record<Locale, string>
  url: string
  official?: boolean
  tag?: string
  trick?: string
  updated?: string
  metrics: { stars?: number; likes?: number; downloads?: number }
  civitaiType?: string
  note: Record<Locale, string>
}
interface Group { id: string; items: Item[] }
interface Section { id: string; groups: Group[] }
interface Data {
  meta: { snapshot: string; total: number; officialPicks: number; thresholds: Record<string, number> }
  sections: Section[]
}

const data: Data = JSON.parse(readFileSync(join(ROOT, 'data/ecosystem.json'), 'utf8'))

/* ---------------------------------------------------------------- copy --- */

const T = {
  title: { en: 'Awesome MiniMax H3', zh: 'Awesome MiniMax H3' },
  tagline: {
    en: 'Everything built on top of MiniMax H3 — the open-weight omni-modal video model that generates picture and native audio together. Weights, quantizations, LoRAs, ComfyUI nodes, workflows and the tricks people found. Every entry checked against a live API and dated.',
    zh: '围绕 MiniMax H3 长出来的一切——这是一个开放权重的全模态视频模型，画面与原生音频一起生成。权重、量化、LoRA、ComfyUI 节点、现成工作流，以及社区挖出来的各种玩法。每条都实测过、带日期。',
  },
  scopeTitle: { en: 'Scope: H3 only', zh: '收录范围：只收 H3' },
  scope: {
    en: 'MiniMax ships plenty besides H3 — the M-series LLMs, Music, an agent stack with more stars than H3 itself. None of it is here. If an entry cannot be pointed at H3, it does not belong on this list.',
    zh: 'MiniMax 的产品线不止 H3——M 系列 LLM、Music、星数比 H3 还高的 Agent 那条线，这里一概不收。一条目如果落不到 H3 上，就不属于这个清单。',
  },
  whatTitle: { en: 'What is MiniMax H3?', zh: 'MiniMax H3 是什么？' },
  what: {
    en: "H3 is MiniMax's open-weight omni-modal video model. Instead of treating text-to-video, image-to-video, reference conditioning and audio as separate models, it reads one multimodal context and generates picture and stereo audio jointly. That single design decision is why this ecosystem looks the way it does: the interesting projects below are mostly people discovering that one model already does things nobody trained it to do — editing a single image, generating audio on its own, continuing a shot indefinitely.",
    zh: 'H3 是 MiniMax 的开放权重全模态视频模型。它不把文生视频、图生视频、参考条件和音频当成几个不同的模型，而是读同一份多模态上下文，把画面与立体声一起生成。整个生态之所以长成现在这样，根子就在这个设计上：下面最有意思的那些项目，多半是有人发现这一个模型已经能干一些没人专门训练过它的事——编辑单张图、单独生成音频、把一个镜头无限续下去。',
  },
  legendTitle: { en: 'How to read an entry', zh: '条目怎么读' },
  legend: {
    en: `Every entry carries its popularity and the date it was last touched, both read from the live API on ${data.meta.snapshot}. \`⭐\` marks a community project that MiniMax named itself, in its release roundup or on its community picks page — so it is not applied inside the Official section, where everything is official by definition.`,
    zh: `每条都带热度与最后更新时间，均为 ${data.meta.snapshot} 从官方 API 实测读取。\`⭐\` 表示这个社区项目被 MiniMax 官方点过名（开源一周盘点或社区精选页）——所以「官方」那一节里不标，那节本来就整节都是官方的。`,
  },
  contents: { en: 'Contents', zh: '目录' },
  curationTitle: { en: 'What gets in', zh: '收录标准' },
  curation: {
    en: [
      `**SFW only.** A meaningful slice of the H3 LoRA scene is adult-oriented. None of it is here, and neither are uncensored components such as stripped text encoders — including otherwise-good speed work that depends on them.`,
      `**Popularity floor, with one exemption.** ${data.meta.thresholds.github}+ stars on GitHub, ${data.meta.thresholds.hf}+ likes on Hugging Face, ${data.meta.thresholds.civitai}+ downloads on Civitai. The floor keeps out the SEO shells that crowd this keyword. The single exemption is official recognition: anything MiniMax named itself goes in regardless — two of the best entries here have single-digit stars.`,
      `**Every link resolves.** The whole list was re-checked against the GitHub, Hugging Face and Civitai APIs on ${data.meta.snapshot}. Entries that had gone private, 404'd, or that could not be verified programmatically were dropped rather than carried over on trust.`,
      `**H3, not MiniMax.** See the scope note above.`,
    ],
    zh: [
      `**只收 SFW。** H3 的 LoRA 生态里成人向占了不小比例，这里一概不收；去审查组件（比如被剥掉限制的文本编码器）同样不收——哪怕某些加速工作本身做得不错，只要依赖它就一起排除。`,
      `**热度门槛 + 一条豁免。** GitHub ≥ ${data.meta.thresholds.github} 星、Hugging Face ≥ ${data.meta.thresholds.hf} likes、Civitai ≥ ${data.meta.thresholds.civitai} 下载。门槛是为了挡住这个关键词下泛滥的 SEO 空壳。唯一豁免是官方点名：MiniMax 自己点过名的一律直收，不看热度——本清单最有意思的两条就只有个位数星。`,
      `**每条链接都能打开。** 全清单已于 ${data.meta.snapshot} 用 GitHub / Hugging Face / Civitai 的 API 重新核验。已转私有、404、或无法程序化验证的条目一律剔除，不凭信任沿用。`,
      `**是 H3，不是 MiniMax。** 见上面的收录范围。`,
    ],
  },
  contribTitle: { en: 'Contributing', zh: '参与贡献' },
  contrib: {
    en: `Found something missing? [Open an issue](${REPO}/issues/new/choose) or send a PR. Include the link, what it does that nothing else here does, and its current star or like count. Read [CONTRIBUTING.md](${REPO}/blob/main/CONTRIBUTING.md) first — the bar above is applied literally.`,
    zh: `发现遗漏？[提 issue](${REPO}/issues/new/choose) 或直接发 PR。请附链接、它能做而这里其他项目做不到的事、以及当前星数/likes。先读 [CONTRIBUTING.md](${REPO}/blob/main/CONTRIBUTING.md)——上面的标准是照字面执行的。`,
  },
  maintTitle: { en: 'How this list stays current', zh: '清单怎么保持更新' },
  maint: {
    en: `Entries live in [\`data/ecosystem.json\`](${REPO}/blob/main/data/ecosystem.json); both READMEs are generated from it by \`npm run generate\`. Edit the JSON, not the Markdown. MiniMax keeps its own [community picks page](https://hailuoai.com/h3-open#featured) updated, and this list is periodically reconciled against it.`,
    zh: `条目数据在 [\`data/ecosystem.json\`](${REPO}/blob/main/data/ecosystem.json)，两份 README 都由 \`npm run generate\` 生成。改 JSON，别改 Markdown。MiniMax 官方维护着一个持续更新的[社区精选页](https://hailuoai.com/h3-open#featured)，本清单会定期与它对齐。`,
  },
  licenseTitle: { en: 'License', zh: '许可' },
  license: {
    en: '[CC BY 4.0](LICENSE). Linked projects keep their own licenses.',
    zh: '[CC BY 4.0](LICENSE)。被收录项目各自的许可证不受影响。',
  },
  audioTrickTitle: {
    en: 'Audio-only generation, no repository required',
    zh: '纯音频生成，不需要任何仓库',
  },
  audioTrick: {
    en: "One of the three tricks MiniMax highlighted has no repo at all. Take the default image-to-video workflow, disconnect the input image, and drop the resolution to 32×32. Pull dialogue, ambience and effects out separately with Get Video Components. It runs close to real time, audio quality does not noticeably suffer, and the result can be fed back in as an audio reference. Credited to developer comfiestncoziest in the official one-week roundup; the original write-up appears to be a Reddit post we have not been able to locate — a pointer would be welcome.",
    zh: '官方点名的三种玩法里，有一种压根没有仓库。做法：拿默认的图生视频工作流，把输入图断开，分辨率降到 32×32，再用 Get Video Components 单独取出对白、环境声和音效。接近实时，音质没有明显下降，产出还能回灌当音频参考。官方开源一周盘点里把这个技巧记在开发者 comfiestncoziest 名下；原帖应该在 Reddit，我们没能找到——知道出处的话欢迎告诉我们。',
  },
} as const

const SECTIONS: Record<string, { title: Record<Locale, string>; intro: Record<Locale, string> }> = {
  official: {
    title: { en: 'Official', zh: '官方' },
    intro: { en: 'Start here. Weights, docs and the endpoints, straight from MiniMax.', zh: '从这里开始。权重、文档与接口，全部来自 MiniMax 官方。' },
  },
  run: {
    title: { en: 'Run it', zh: '跑起来' },
    intro: { en: 'Getting H3 to produce a first clip, on whatever hardware you actually have.', zh: '在你手头这台机器上，让 H3 出第一条片子。' },
  },
  fit: {
    title: { en: 'Fit it on your GPU', zh: '塞进你的显卡' },
    intro: { en: 'The full model is 123.6GB. These are the projects that got it down to something a desktop can hold.', zh: '完整模型 123.6GB。这一节是把它压到台式机装得下的那些项目。' },
  },
  fast: {
    title: { en: 'Make it fast', zh: '提速' },
    intro: { en: 'Two separate levers: fewer sampling steps (Turbo LoRAs) and cheaper steps (caching, attention kernels). They compose.', zh: '两条互不冲突的路子：减少采样步数（Turbo LoRA）和让每步更便宜（缓存、注意力 kernel）。两者可以叠加。' },
  },
  lora: {
    title: { en: 'LoRAs and training', zh: 'LoRA 与训练' },
    intro: { en: 'Teaching H3 a look it does not have — and the paths to training your own.', zh: '教会 H3 它本来没有的调性——以及自己动手训练的几条路。' },
  },
  tricks: {
    title: { en: 'Unusual tricks', zh: '冷门玩法' },
    intro: { en: "The most interesting corner of this ecosystem: things H3 turned out to do that it was never trained to do. MiniMax's own release roundup led with these rather than with benchmarks.", zh: '整个生态最有意思的一角：H3 被发现能干一些它从没被训练去干的事。MiniMax 官方的开源一周盘点，开篇讲的正是这些而不是跑分。' },
  },
  film: {
    title: { en: 'Direct a film', zh: 'Agent 制片' },
    intro: { en: 'H3 makes shots, not films. These projects add what sits above a shot: planning, continuity, batching, edit and export.', zh: 'H3 出的是镜头，不是成片。这些项目补的是镜头之上的那层：分镜规划、连贯性、批量、剪辑与导出。' },
  },
  skills: {
    title: { en: 'Agent skills', zh: 'Agent Skills' },
    intro: { en: 'Installable skills that let a coding agent — Claude Code, Codex, OpenCode and friends — do the prompting and drive the pipeline for you.', zh: '可安装的 skill，让编码 agent（Claude Code、Codex、OpenCode 等）替你写提示词、驱动整条流水线。' },
  },
  nodes: {
    title: { en: 'Other ComfyUI nodes', zh: '其他 ComfyUI 节点' },
    intro: { en: 'Useful nodes that do not fit the categories above.', zh: '归不进上面几类，但确实好用的节点。' },
  },
  prompting: {
    title: { en: 'Prompting', zh: '提示词' },
    intro: { en: 'H3 responds to a fairly specific prompt shape. These help you hit it.', zh: 'H3 吃的提示词形状比较特定，这些工具帮你写对。' },
  },
  workflows: {
    title: { en: 'Ready-made workflows', zh: '现成工作流' },
    intro: { en: 'Drop-in graphs from Civitai and GitHub — including the low-VRAM configurations that actually run. Popular, and largely absent from other H3 lists.', zh: '来自 Civitai 与 GitHub 的即插即用工作流，含那些真能跑起来的低显存配置。这块很热，但其他 H3 清单基本没收。' },
  },
  learn: {
    title: { en: 'Learn', zh: '教程与资讯' },
    intro: { en: 'Guides and news sources that keep up.', zh: '跟得上节奏的指南与资讯源。' },
  },
  related: {
    title: { en: 'Related lists', zh: '相关清单' },
    intro: { en: 'Other people covering the same ground, usefully.', zh: '同一片地上，做得有价值的其他清单。' },
  },
}

const GROUPS: Record<string, Record<Locale, string>> = {
  'official-model': { en: 'Model and weights', zh: '模型与权重' },
  'official-docs': { en: 'Documentation, API and community', zh: '文档、API 与社区' },
  'run-comfyui': { en: 'In ComfyUI', zh: '在 ComfyUI 里' },
  'run-frameworks': { en: 'Serving frameworks', zh: '推理框架' },
  'run-local': { en: 'Local and cross-platform', zh: '本地与跨平台' },
  'run-hardware': { en: 'Hardware-specific', zh: '特定硬件' },
  'run-online': { en: 'Try it online', zh: '在线试玩' },
  'fit-builds': { en: 'Packaged builds', zh: '打包版' },
  'fit-quant': { en: 'Quantizations', zh: '量化' },
  'fit-components': { en: 'Split-out components', zh: '分离组件' },
  'fast-turbo': { en: 'Turbo LoRAs — 20 steps down to 4–8', zh: 'Turbo LoRA——20 步降到 4–8 步' },
  'fast-cache': { en: 'Caching and attention', zh: '缓存与注意力' },
  'lora-style': { en: 'Style and capability LoRAs', zh: '风格 / 能力 LoRA' },
  'lora-train': { en: 'Train your own', zh: '自己练一个' },
  'tricks-long-video': { en: 'Continue a shot indefinitely', zh: '把镜头无限续下去' },
  'tricks-image-edit': { en: 'Use a video model to edit one image', zh: '拿视频模型编辑单张图' },
  'tricks-misc': { en: 'Other', zh: '其他' },
  'workflows-gh': { en: 'On GitHub', zh: 'GitHub 上的' },
  'workflows-all': { en: 'On Civitai', zh: 'Civitai 上的' },
  'learn-en': { en: 'English', zh: '英文' },
  'learn-zh': { en: 'Chinese', zh: '中文' },
}

/* ----------------------------------------------------------- rendering --- */

const compact = (n: number): string =>
  n >= 1_000_000 ? `${(n / 1_000_000).toFixed(1).replace(/\.0$/, '')}M`
  : n >= 1_000 ? `${(n / 1_000).toFixed(1).replace(/\.0$/, '')}k`
  : `${n}`

function badge(it: Item, locale: Locale): string {
  const bits: string[] = []
  const { stars, likes, downloads } = it.metrics
  if (stars != null) bits.push(`${compact(stars)}★`)
  if (likes != null) bits.push(`${compact(likes)}♥`)
  if (downloads != null) bits.push(`${compact(downloads)}↓`)
  if (it.updated) bits.push(it.updated)
  if (!bits.length) return ''
  return ` \`${bits.join(' · ')}\``
}

function renderItem(it: Item, locale: Locale, markOfficial = true): string {
  const name = typeof it.name === 'string' ? it.name : it.name[locale]
  const star = it.official && markOfficial ? '⭐ ' : ''
  const label = it.tag ?? (it.kind === 'civitai' ? it.civitaiType : undefined)
  const type = label ? ` *(${label})*` : ''
  return `- ${star}[${name}](${it.url})${type}${badge(it, locale)} — ${it.note[locale]}`
}

// Mirrors GitHub's heading-anchor rules: lowercase, drop punctuation, spaces to
// hyphens — but keep non-Latin letters, or every anchor in the Chinese README
// would collapse to an empty string.
function anchor(s: string): string {
  return s.toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, '').trim().replace(/\s+/g, '-')
}

function render(locale: Locale): string {
  const L = (k: keyof typeof T) => (T[k] as Record<Locale, string>)[locale]
  const out: string[] = []
  const other = locale === 'en' ? 'zh' : 'en'
  const dot = locale === 'en' ? '.' : '。'
  const otherLink = locale === 'en'
    ? '[简体中文](i18n/README_zh.md)'
    : '[English](../README.md)'

  out.push(`# ${T.title[locale]}`)
  out.push('')
  // shields.io treats "-" as its field separator, so dates need doubled hyphens
  const snapBadge = data.meta.snapshot.replace(/-/g, '--')
  out.push(`[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Entries](https://img.shields.io/badge/entries-${data.meta.total}-blue.svg)](${REPO}) [![Verified](https://img.shields.io/badge/links%20verified-${snapBadge}-brightgreen.svg)](${REPO})`)
  out.push('')
  out.push(`> ${T.tagline[locale]}`)
  out.push('')
  out.push(otherLink)
  out.push('')
  out.push(`**${T.scopeTitle[locale]}${dot}** ${T.scope[locale]}`)
  out.push('')

  // contents
  out.push(`## ${T.contents[locale]}`)
  out.push('')
  for (const s of data.sections) {
    const meta = SECTIONS[s.id]
    out.push(`- [${meta.title[locale]}](#${anchor(meta.title[locale]) || s.id})`)
  }
  out.push(`- [${T.whatTitle[locale]}](#${anchor(T.whatTitle[locale]) || 'what'})`)
  out.push(`- [${T.curationTitle[locale]}](#${anchor(T.curationTitle[locale]) || 'curation'})`)
  out.push('')
  out.push(`**${T.legendTitle[locale]}${dot}** ${T.legend[locale]}`)
  out.push('')
  out.push('---')
  out.push('')

  for (const s of data.sections) {
    const meta = SECTIONS[s.id]
    // The Official section is official end to end; starring every line there
    // would drain the mark of the meaning it carries elsewhere.
    const mark = s.id !== 'official'
    out.push(`## ${meta.title[locale]}`)
    out.push('')
    out.push(meta.intro[locale])
    out.push('')

    if (s.id === 'tricks') {
      const order = ['long-video', 'image-edit', 'misc']
      const items = s.groups.flatMap((g) => g.items)
      for (const t of order) {
        const sub = items.filter((i) => i.trick === t)
        if (!sub.length) continue
        out.push(`### ${GROUPS[`tricks-${t}`][locale]}`)
        out.push('')
        sub.forEach((i) => out.push(renderItem(i, locale, mark)))
        out.push('')
      }
      out.push(`### ${T.audioTrickTitle[locale]}`)
      out.push('')
      out.push(T.audioTrick[locale])
      out.push('')
      continue
    }

    const named = s.groups.filter((g) => GROUPS[g.id])
    if (named.length > 1) {
      for (const g of named) {
        out.push(`### ${GROUPS[g.id][locale]}`)
        out.push('')
        g.items.forEach((i) => out.push(renderItem(i, locale, mark)))
        out.push('')
      }
    } else {
      s.groups.flatMap((g) => g.items).forEach((i) => out.push(renderItem(i, locale, mark)))
      out.push('')
    }
  }

  out.push('---')
  out.push('')
  out.push(`## ${T.whatTitle[locale]}`)
  out.push('')
  out.push(T.what[locale])
  out.push('')
  out.push(`## ${T.curationTitle[locale]}`)
  out.push('')
  T.curation[locale].forEach((line) => out.push(`- ${line}`))
  out.push('')
  out.push(`## ${T.maintTitle[locale]}`)
  out.push('')
  out.push(T.maint[locale])
  out.push('')
  out.push(`## ${T.contribTitle[locale]}`)
  out.push('')
  out.push(T.contrib[locale])
  out.push('')
  out.push(`## ${T.licenseTitle[locale]}`)
  out.push('')
  out.push(T.license[locale])
  out.push('')

  return out.join('\n')
}

writeFileSync(join(ROOT, 'README.md'), render('en'))
mkdirSync(join(ROOT, 'i18n'), { recursive: true })
writeFileSync(join(ROOT, 'i18n/README_zh.md'), render('zh'))
console.log(`generated README.md and i18n/README_zh.md — ${data.meta.total} entries, ${data.meta.officialPicks} official picks`)
