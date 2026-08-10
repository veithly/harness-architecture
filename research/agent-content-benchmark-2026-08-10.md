# Agent 内容竞品调研与改稿方案

> 调研日期：2026-08-10
> 对象：`harness-architecture` 中文内容、线上站点及国内外 Agent 内容样本
> 方法：ego-browser 实页检查、agent-reach 网页/GitHub 核验、仓库只读审计
> 状态：已据此完成 22 篇 pattern 的中英文批量改写；本地验证中，未提交、未推送、未部署

## 先说结论

站里并不缺材料。源码路径、实现细节和对照表都很多。卡住读者的是组织方式：**22 篇文章读起来像同一份压缩简报换了 22 次主题，很少像一个作者在追到底的工程问题。**

读者首先看到长结论、四家枚举、评分和术语解释，之后才碰到问题本身。文章几乎没有作者、时间、现场、失败过程、成本和可复现实验。结果是事实很多，人的判断过程却不可见；语气又长期保持确定、完整、全面，读起来就像模型一次性生成的知识库。

建议把定位从“四套系统横向比较百科”改成：

> **Agent 工程现场：每篇解决一个真实决策，给出实测、源码、代价、边界和复现材料。**

只换标题和卡片样式解决不了它。需要同时处理三层问题：

1. **发布层**：线上仍是旧版，本地已经做过的阅读体验改进没有上线。
2. **文章层**：解除“四家 + 十段 + 评分卡”的默认结构，每篇只服务一个问题。
3. **信任层**：补作者、日期、验证时间、版本、实验和更新记录，让判断有出处、有时效。

目前没有站内阅读完成率、回访、来源点击或用户访谈数据。因此，“AI 味导致没人看”还只是一个很有根据的判断，不是已经证明的因果关系。本文能确认页面和语料特征；流失原因还要靠埋点、A/B 和访谈验证。

## 研究范围与证据等级

本文把证据分成四类，避免把竞品宣传和自己的推断混在一起：

- **页面事实**：浏览器当前可见的标题、作者、日期、目录、代码、数字和链接。
- **仓库事实**：当前工作区中的 MDX、组件、校验脚本、固定 commit 和 Git 状态。
- **来源主张**：厂商或作者公开的数据，例如 Anthropic 的内部 eval、花叔落地页的案例数字；只代表来源方自述。
- **编辑推断**：基于上面证据提出的内容判断，需要后续数据验证。

样本包括：

- 国内：Datawhale `agent-tutorial`、花叔 Harness Engineering 橙皮书。
- 国外：Anthropic Engineering、OpenAI 官方文档/Cookbook、LangChain Blog、Simon Willison、Chip Huyen、Lilian Weng、Latent.Space/AINews。
- 本站：线上首页和 `02/10/20`，本地 HEAD 首页和 `01/02/10/20`，22 篇中文 pattern 源文件。

## 线上与本地不是同一个网站

| 项目 | 线上 `harness-architecture.pages.dev` | 本地工作树（基于 `b6fdae4`） |
| --- | --- | --- |
| 首页 | 仍有 `loop / graph / four systems`、`paper mode`、`frame 0000`、滚动计数等伪仪表盘 | 已换成更安静的 `field-notes` 结构 |
| `02 Agent Loop` 标题 | `§1 · TL;DR`、`§2 · 共有的最小循环加四家泳道图` | `循环先要扛住哪些事故`、`最小循环与四条执行泳道` |
| 摘要和附录 | 长摘要与所有练习直接展开 | 读前提示和附录已折叠 |
| Git 状态 | 对应较早的 `origin/main` | `main` 比 `origin/main` 超前 1 个提交，尚未部署 |

线上旧版可以直接在 [02 Agent Loop](https://harness-architecture.pages.dev/patterns/02-agent-loop/) 看到编号模板。本地改动见 [`02-agent-loop.mdx`](../src/content/docs/patterns/02-agent-loop.mdx)。

因此，用户现在批评的实际对象主要还是旧版。上一轮本地改动修复了视觉噪音、标题和信息披露，但没有根治文章底层的统一生成感。不要把“本地已经好一点”和“线上已经解决”混为一谈。

## 本站为什么有明显 AI 味

### 1. 二十二篇文章拥有同一副骨架

仓库审计显示，22 篇中文 pattern 全部包含 `Verdict`、`ScoreCard`、`SourceTrail`、读前提示、四系统小节、“我的判断”和附录。21/22 出现“从……开始”，20/22 出现“沿着……读源码”。

这不是单篇文风问题，而是生产制度问题。更直接的证据是：在改稿前的仓库快照里，[`scripts/check-chapter-template.mjs`](../scripts/check-chapter-template.mjs) 第 3-6 行已经明确说“不要再次把 22 篇文章压成同一张表格”，但当时的 [`CONTRIBUTING.md`](../CONTRIBUTING.md) 和 [`README.md`](../README.md) 仍要求固定十段和固定组件。编辑规则互相冲突，下一次写作很容易重新滑回旧模板。

看完两篇，第三篇的节奏已经能猜出来。不同主题又都被迫出现比较、评分和练习，批量填充感由此产生。

### 2. 答案在问题之前，且一次塞完

[`01-overview.mdx`](../src/content/docs/patterns/01-overview.mdx) 第 19 行的 `Verdict` 约 741 个汉字；[`10-subagents.mdx`](../src/content/docs/patterns/10-subagents.mdx) 的开头 `Verdict` 约 2,255 个汉字。摘要先把灾难清单、四套实现、字段、工具和建议全部说完，后面再重复为提示、图、表和正文。

读者还没进入问题，答案已经压完了。这样的开头更像给机器准备上下文，很难制造继续读的理由。

### 3. 四家对比从研究手段变成了写作目的

中文语料中“四家”出现约 254 次。即便一个问题只需要两个案例，也会把 Codex、Claude Code、OpenClaw、Hermes 全部拉进来，造成大量“系统 A 做什么，系统 B 做什么”的平行枚举。

读者可能记住产品名和字段，却未必能回答“我该做什么决策”。比较应该由冲突触发，不该成为每章的入场券。

### 4. 语气比证据更确定

粗略词频中，“唯一”出现约 68 次，“真正”57 次，“我的判断”固定出现 22 次。`01` 里有“加起来就是完整认知”，`20` 里有“标准做法”“根本原则”“必须”等没有适用条件的判断。

让我觉得最像 AI 的地方就在这里：作者似乎永远知道完整答案，却不说它基于哪个版本、任务和约束。事实未必错，置信度却从头到尾一样高。

### 5. 括号解释过密，像术语压缩器

开头常把英文、中文解释、协议字段和结论塞进同一句。术语第一次出现时解释是好事，但每个名词都在正文中就地展开，会让主句失去动作。

每句话都像定义，人说话的呼吸没了。术语可以进侧栏、词汇表或首次定义，叙事主线只保留当下需要的意思。

### 6. 有“完整”，没有现场

`10 Subagents` 的浏览器抽样约 16,516 字、66 个段落、22 个折叠块、26 个代码块；`20 Security` 约 14,475 字。材料很多，但示例主要是合成场景，评分卡没有公开 rubric，缺少真实输入、运行轨迹、失败输出、耗时、token、成本和改稿过程。

信息显然来自大量资料，作者亲自撞上了什么问题、怎么排除错误答案，却看不见。

### 7. 页面没有人，也没有时间边界

22 篇 pattern 的 frontmatter 都没有 `author`、`published` 或 `last_verified`。Starlight 只开启了 [`astro.config.mjs`](../astro.config.mjs) 第 167 行的 `lastUpdated: true`。源码链接内部已经固定到 [`repoLinks.ts`](../src/lib/repoLinks.ts) 第 23-45 行的 commit，但文章页没有显式告诉读者“基于哪个快照”。

没人知道谁在承担这些判断，也不知道 2026 年读到的究竟是 2024 年的 Agent，还是当前版本。

### 8. 深度与更新速度混在一条内容线上

22 篇都按“永久教程”写，站内没有短更新、实验日志、版本变更和勘误时间线。Agent 领域变化很快，只有重型长文会导致两种结果：热点来不及写，旧文又看不出哪里已经过时。

网站看起来很大，却没有正在生长的时间线。

## 国内样本：差异不在文笔，而在读者动作

### Datawhale：把文章做成能跟着完成的学习任务

[Datawhale Agent 教程](https://github.com/datawhalechina/agent-tutorial) 开头先说用途：“通过实践引导学习者加深对 Agent 的理解”，并明确服务于《动手学 Agent 开发》学习活动。三章路径是概念、日程助手实践、应用展望。

代表正文 [`1.1 Agent 原理`](https://github.com/datawhalechina/agent-tutorial/blob/main/docs/%E7%AC%AC%E4%B8%80%E7%AB%A0%EF%BC%9AAgent%E7%AE%80%E4%BB%8B/1.1%20Agent%E5%8E%9F%E7%90%86.md) 不先给宏大定义，而是从“买相机”任务解释 Agent 与聊天的差别，随后让读者配置天气助手、调用天气和画图工具，观察任务拆分。 [`2.2 日程规划小助手`](https://github.com/datawhalechina/agent-tutorial/blob/main/docs/%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9AAgent%E5%AE%9E%E8%B7%B5/2.2%20%E6%97%A5%E7%A8%8B%E8%A7%84%E5%88%92%E5%B0%8F%E5%8A%A9%E6%89%8B.md) 则把实现、测试、部署和结果串成一条任务链。

可借鉴的是“每隔几分钟有一个读者可验证的产物”，不是它的旧技术栈。截至本次核验，GitHub 页面/API 显示约 417 stars、43 forks、42 commits，最新 push 是 2024-03-19。它适合作为教学结构样本，不应作为 2026 年 Agent 新鲜度样本。

### 花叔：先让读者在一个转变里看见自己

[Harness Engineering 橙皮书](https://www.huasheng.ai/orange-books/harness/) 的首屏不是定义，而是“从『和 AI 聊天』到『给 AI 造缰绳』”。页面显示作者、页数、出版状态，并用“7 个深度案例 + 从空白项目搭建 Harness + 一个核心问题”承诺读者收益。

目录从概念和历史，走到五个组件、真实案例、从零搭建、约束/记忆/编排和经验工程。标题会直接使用冲突和结果，例如“每次犯错加一条规则”“每周 1300 个 PR”。

可借鉴的是：个人声音、动作化标题、明确读者承诺和目录的叙事顺序。不能直接照搬的是页面数字：这是落地页主张，页面没有给出完整正文、复现实验、版本和日期，“每周 1300 个 PR”等必须回到原始案例核验后才能成为本站证据。

## 国外样本：高信任文章怎样讲 Agent

| 来源 | 它怎样开场 | 它拿什么证明 | 本站应借鉴什么 |
| --- | --- | --- | --- |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)（2024-12-19） | 先给反直觉结论：成功实现往往是简单、可组合的模式 | 客户经验、workflow 图、适用场景和外部 cookbook | 先讲什么时候不要用 Agent，再讲模式 |
| [Anthropic: Multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system)（2025-06-13） | 从开放式研究无法预先硬编码路径的产品问题进入 | 内部 eval、90.2% 提升主张、4x/15x token 代价、trace 和失败案例 | 把收益、代价、不适用场景写在同一页；数字注明“内部 eval” |
| [Anthropic: Long-running harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)（2025-11-26） | 用“工程师轮班却没有前一班记忆”解释跨 context 问题 | progress 文件、git、200+ feature checklist、JSON pass/fail、quickstart | 把抽象 loop 变成可恢复的具体交接协议 |
| [Anthropic: Agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)（2026-01-09） | 先说明多轮、工具和状态既是价值也是评估难点 | deterministic、LLM rubric、state、tool、transcript、latency 多层 eval | 不只看最终文本，还看轨迹、状态和代价 |
| [OpenAI: New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)（2025-03-11） | 先承认从模型能力到生产 Agent 的协调和可见性难题 | Responses API、工具、SDK 的最小 JS/Python 路径 | 首屏给问题和最小可运行代码，再引导深读 |
| [OpenAI Agents 指南](https://developers.openai.com/api/docs/guides/agents) | 一句定义后按任务分流 | Quickstart、handoff、guardrail、state、MCP、tracing/evals 的路径 | 文档页做“下一步选择器”，不要假装是观点长文 |
| [LangChain Blog](https://www.langchain.com/blog) | 一篇只承担一个观点或一个生产案例 | 栏目、作者、日期、阅读时间、trace、benchmark 和版本决策 | 拆出 Agent Architecture、Observability & Evals、Case Studies 三条线 |
| [Simon Willison: ai-agents](https://simonwillison.net/tags/ai-agents/) | 短判断、个人语气、明确日期，持续修正自己的定义 | 真实命令、原始链接、成本、后续更新、RSS/tag 时间线 | 不必每次写大全；短实验和勘误本身就是价值 |
| [Chip Huyen: Agents](https://huyenchip.com/2025/01/07/agents.html)（2025-01-07） | 从经典定义进入，但立即声明理论仍在演化 | 工具、规划、失败模式、效率与评估的具体例子 | 给范围声明和失败模型，不把演化中的概念写成定论 |
| [Lilian Weng: Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/)（2026-07-04） | 先建立历史和术语，再提出 harness 层的重要性 | 论文、GitHub、benchmark appendix、BibTeX | 研究综述保留完整引文，并区分证据和预测 |
| [Latent.Space: 2026 AI Engineering trends](https://www.latent.space/p/aiewf26trends)（2026-07-15） | 用“building with agents → systems around agents”概括会议趋势 | keynote、原文、引语和跨文链接 | 趋势文要有一个 thesis，并把观察挂回原始材料 |

这些来源并不都“更会写”。我看到的共性很具体：

1. 先出现一个具体问题或反直觉结论，再出现术语。
2. 作者让读者看到证据是怎么来的，包括失败、成本、trace、代码和版本。
3. 一篇文章只承担一种阅读任务：观点、教程、实验、案例或新闻，不混成大全。
4. 更新机制可见：作者、日期、阅读时间、RSS、tag、勘误和后续文章把内容连成时间线。

## 新的内容定位

### 核心承诺

我建议给新文章设一道硬门槛：读者离开时，至少拿到下面一项。

- 一个能复现的实验；
- 一个可直接用于架构决策的判断；
- 一条带版本和 commit 的源码路线；
- 一个真实生产案例的失败与代价；
- 一个本周发生、且会改变工程选择的新信号。

如果一篇文章只能让读者“知道 Agent 很复杂、四家做法不同”，就不应该发布。

### 四种内容，不再所有文章都写成长教程

| 内容类型 | 典型长度 | 核心证据 | 发布节奏 |
| --- | ---: | --- | --- |
| 实验记录 | 1,500-3,000 字 | 输入、环境、轨迹、结果、失败、成本 | 每周 1 篇 |
| 源码拆解 | 3,000-6,000 字 | pinned commit、关键调用链、最小验证 | 每两周 1 篇 |
| 生产案例 | 2,000-4,000 字 | 原始工程文章、访谈或公开 trace，明确自述边界 | 每两周 1 篇 |
| Agent Radar | 500-1,200 字 | 本周官方变更、benchmark、incident、release | 每周固定一期 |

原来的 22 章可以保留为“参考手册”，但不再承担整个站点的更新和分发。

## 新的文章结构

不要再换一套固定十段。根据主题删减，但保留下面的证据顺序：

1. **场景**：一次失败、一个任务、一条 trace 或一个反直觉数字。
2. **问题**：本文只回答什么，不回答什么。
3. **假设**：作者准备验证哪一个判断。
4. **实验/材料**：模型、版本、commit、输入、权限、机器、运行次数。
5. **观察**：先贴结果和原始证据，再解释。
6. **失败与代价**：哪次不工作、token/延迟/人工成本多少。
7. **判断**：在什么条件下选择哪种方案，置信度如何。
8. **复现与更新**：代码、日志、来源、`last_verified`、变更记录。

### 建议的页面元数据

```yaml
author: Rick
published: 2026-08-18
last_verified: 2026-08-18
evidence: experiment
systems:
  codex: f27cf9db0974d344d78e7e0b47e7c812776b1395
  openclaw: f6d0712f508b1f926ad6fc42f7d07b1a60e62730
models:
  - name: example-model
    version: exact-version-used
status: current
```

页面上应直接展示这些字段。只写在源码里不够。

### 句子层面的编辑规则

- 一段只推进一个动作或判断；术语解释不要嵌套三层括号。
- “唯一、完整、真正、必然、标准做法、生产级”出现时，必须补范围或删除。
- “我的判断”不能替代证据。先写“我观察到什么”，再写“因此在什么条件下我会选什么”。
- 不用“随着 AI 快速发展”“在当今时代”“赋能”“全面解析”开场。
- 不把四个系统写齐当作完整。没有产生决策差异的系统直接不写。
- 评分卡必须公开 rubric、样本和计算方法；否则改成有条件的文字判断。
- 合成场景明确写“假设场景”；真实事故给输入、输出和验证日期。
- 文章先给主线，源码清单、完整表格和复盘题放附录。

## 怎样跟进 Agent 的当下潮流

### 先盯“工程选择发生变化”的信号

优先级从高到低：

1. 官方 API、SDK、模型、权限和计费变更。
2. 可复现 benchmark、公开 trace、事故复盘和生产案例。
3. 主流开源 Agent 的 release、关键 commit 和 issue。
4. 一线作者的实测和工作流变化。
5. 会议趋势和二手观点；只用来发现线索，不直接当结论。

### 每周工作流

1. 周一收集 Anthropic Engineering、OpenAI docs/cookbook/changelog、LangChain blog/changelog、核心 GitHub release，以及 Simon/Lilian/Chip/Latent.Space 的 RSS/tag。
2. 只保留会改变架构决策的信号：接口变了、成本变了、失败模型变了、权限边界变了、评估方法变了。
3. 为最重要的一条信号跑一个最小复现实验；不能复现就写成“来源主张”，不要伪装成本站结论。
4. 周中发布一篇短 Radar，记录“发生了什么、为什么重要、现在要不要改”。
5. 只有当信号连续两周成立或影响足够大，再升级成长文；旧文增加 update note 和回链。

### 接下来 90 天最值得写的六条线

| 主题 | 为什么是现在 | 可写标题 |
| --- | --- | --- |
| Long-running harness | 关注点从单轮 prompt 转向跨 context 的状态、交接和恢复 | `Agent 跑到第 37 轮断电，重启后该从哪里接着做？` |
| Context reset vs compaction | 长任务不是简单“塞更多上下文”，reset、摘要和外部状态各有代价 | `压缩不是免费的：同一条 trajectory 被总结三次后还剩什么？` |
| Managed / deep agents | 产品从库和 demo 走向托管运行时，调度、隔离、审计变成核心 | `Deep Agent 到底替你托管了什么？` |
| Trajectory / state eval | 只评最终答案无法发现越权、绕政策和错误工具路径 | `答案对了，Agent 也可能不合格` |
| Containment and permissions | 浏览器、shell、MCP、远程 Agent 扩大了爆炸半径 | `Agent 忘记确认之后，哪一层还能拦住它？` |
| Production SRE/CX/voice | 真实案例开始公开 HITL、RBAC、误报和回归测试 | `生产 Agent 不是更自治，而是更会把危险动作交还给人` |

## 先重写三篇旗舰文章

### 02 Agent Loop：从“循环结构”改成“中断后怎样继续”

- **核心问题**：Agent 在第 37 轮进程被杀，哪些状态必须落盘，才能不重复危险动作？
- **实验**：同一任务、同一模型，强制在固定步骤杀进程，比较从零重跑、只保存消息、保存事件 + verifier 状态三种恢复方式。
- **结果指标**：重复工具调用数、恢复耗时、额外 token、是否重复副作用、最终测试状态。
- **只比较必要案例**：Codex rollout、Anthropic long-running harness 的 progress/git 交接、OpenClaw runId/event；Hermes 只有在跨会话 memory 真正影响恢复时再加入。
- **删除/下沉**：五组四家对照移入源码附录；ScoreCard 改成有条件的选型表。

### 10 Subagents：从“八种灾难”改成“为什么开八个 Agent 可能更慢”

- **核心问题**：任务可并行度多高时，多 Agent 才能覆盖协调和 token 成本？
- **实验**：同一组任务以 1/2/4/8 个 Agent 运行，记录 wall time、token、重复工作、冲突、合并人工时长。
- **必须写出的反例**：高度共享上下文、强顺序依赖、需要同一工作树写入时，多 Agent 可能更差。
- **来源边界**：Anthropic 90.2% 与 4x/15x 是其内部研究系统结果，不能写成通用规律。

### 20 Security：从“安全栈大全”改成“忘记确认后的爆炸半径”

- **核心问题**：模型已经决定执行危险动作时，prompt、tool policy、sandbox、OS 权限、审计各能拦住什么？
- **实验**：固定一组攻击输入，逐层关闭防线，记录哪一层拦截、误报、漏报和失败模式。
- **证据要求**：真实命令放在隔离环境；每个结论标注 threat model 和平台。
- **删除/下沉**：没有 rubric 的 10/9/7 评分；合成攻击字符串必须明确标“测试向量”，不是线上 incident。

## `02 Agent Loop` 改写样稿

下面是一段写作方向样稿，不是可直接发布的实验报告。方括号内容必须在真实运行后替换；没有轨迹和结果之前，不能把它包装成本站实测。

### 标题

**Agent 跑到第 37 轮断电，重启后该从哪里接着做？**

### 副标题

我们不再从 `while True` 讲 Agent Loop，而是从一次强制中断开始：消息、工具结果、文件改动和 verifier 状态，究竟哪些必须留下？

### 开头示范

大多数 Agent Loop 的文章先画一张 Observe、Plan、Act、Verify 的圆环。那张图没有错，但它避开了真正麻烦的一刻：Agent 已经改了六个文件、跑完一半测试，进程突然没了。

重新启动后有三个选择。第一种是从头再跑，最简单，也最可能重复发消息、重复创建资源、把已经正确的 patch 改坏。第二种只恢复聊天记录，看起来有记忆，却不知道哪些工具已经产生了副作用。第三种把每一步动作和验证结果写成可重放的事件，再从最后一个可靠检查点继续。

本文只回答一个问题：**怎样判断一个 loop 真的“可恢复”？** 我们会在同一个仓库任务中，于第 `[待实测步骤]` 步强制终止进程，然后比较三种恢复策略。判断标准不是模型说“我记得”，而是五个可测量结果：有没有重复副作用、恢复花了多久、多烧了多少 token、verifier 状态是否一致、最终测试是否通过。

### 实验卡

| 项目 | 值 |
| --- | --- |
| 任务 | `[待填：固定 repo 和任务描述]` |
| 模型/API | `[待填：精确版本]` |
| Harness | `[待填：版本或 commit]` |
| 中断点 | 工具调用完成后、结果写回前；verifier 运行中；context reset 后，各 1 次 |
| 对照组 | 从零重跑；只恢复消息；事件日志 + checkpoint + verifier 状态 |
| 重复次数 | 每组至少 5 次 |
| 原始材料 | `run.jsonl`、stdout/stderr、git diff、测试报告、token/延迟统计 |

### 先给判断，再给范围

一个 loop 能不能恢复，不取决于它保存了多少聊天记录，而取决于它能不能回答四个问题：

1. 上一个已确认完成的动作是什么？
2. 哪些工具调用已经产生不可逆副作用？
3. verifier 当时验证到了哪里？
4. 重新执行下一步会不会重复扣款、发消息或覆盖文件？

如果系统只能恢复 messages，它恢复的是模型的阅读材料，不是任务状态。对于纯读操作，这可能够用；对于会写文件、调用外部 API 或触发付款的 Agent，不够。

### 最小事件模型

```json
{"seq": 37, "type": "tool_started", "tool": "apply_patch", "idempotency_key": "run-9-step-37"}
{"seq": 38, "type": "tool_finished", "exit_code": 0, "artifact": "git:abc123"}
{"seq": 39, "type": "verifier_finished", "check": "targeted_tests", "passed": true}
{"seq": 40, "type": "checkpoint", "resume_from": 41}
```

这里最重要的字段不是模型写了什么，而是 `seq`、副作用标识、验证结果和 checkpoint。正式文章应展示一次真实中断前后的事件片段，并解释恢复器如何处理“工具已经执行，但 `tool_finished` 还没写盘”的灰色状态。

### 三个实现只在恢复问题上比较

- [Anthropic 的 long-running harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 用 progress 文件、git 和 feature checklist 把交接显式化。它解决的是跨 context 的“下一班工程师从哪里接手”。
- 本站研究的 Codex 路线把操作和事件写入 rollout，适合解释可回放时间线；正式发布时必须显示所依据的 pinned commit 和真实事件样本。
- OpenClaw 的 runId 和 lifecycle/tool/assistant 事件适合解释“运行是可观察资源”，但事件可订阅不自动等于副作用可恢复，仍要检查幂等和 checkpoint。

这里不需要为了“四家齐全”硬加第四个系统。只有当另一套实现提供不同的恢复语义时，比较才有意义。

### 文章必须展示的失败

最值得写的不是成功恢复，而是两类尴尬结果：

- 工具成功、日志未落盘，恢复器以为没执行，于是重复副作用。
- 消息和文件恢复了，verifier 的中间状态没恢复，系统把已通过的检查重新跑一遍，成本和延迟突然上升。

正式结论应写成条件句，例如：

> 在只有本地、幂等读操作的任务里，消息 + 文件快照可能已经足够。只要 loop 能触发外部副作用，就需要事件级持久化、幂等键和独立 verifier checkpoint。`[待实测数据]` 会说明这三项各自减少了什么风险，也会记录它们增加的写盘和实现成本。

### 结尾不是“最佳实践”，而是一张行动清单

读者看完应该能立即检查自己的 loop：

- 每个写操作有没有 idempotency key？
- 进程在工具成功与结果落盘之间退出时，恢复器如何判定？
- checkpoint 是否包含 verifier 状态，而不只是 messages？
- 恢复测试是否真的用 `kill -9`、网络断开和 context reset 跑过？
- 页面是否提供原始 trajectory 和版本信息？

这比再复述一次“Agent 是感知、规划、行动、反思的循环”更有用。

## 90 天执行顺序

### P0：先解除编辑制度冲突

- 统一 `CONTRIBUTING.md`、`README.md` 和实际校验脚本：不再要求固定十段和固定组件。
- 定义作者、发布日期、`last_verified`、版本、证据类型和更新记录的页面展示。
- 先决定是否部署当前本地提交；部署是独立决策，不能在内容研究中顺手发生。

### P1：用三篇旗舰文章验证新方法

- 重写 `02/10/20`，每篇先完成真实实验和原始材料。
- 旧版与新版做对照：首屏继续率、50%/90% 滚动深度、源码点击、代码复制、回访。
- 找 5-8 位目标读者做任务式访谈：读完后能否说出“何时选什么”，而不是只问“好不好看”。

### P2：建立活的内容线

- 每周一篇 Agent Radar，记录新接口、benchmark、事故和生产案例。
- 每两周一篇实验或源码拆解。
- 旧文顶部显示状态：`current`、`needs recheck`、`archived`。
- 每月根据数据决定下一批重写，不一次性翻修 22 篇。

## 成功标准

不要用字数或篇数衡量这次改造。建议记录：

- 进入正文后 30 秒仍在阅读的比例；
- 50% 和 90% 滚动深度；
- 源码、实验材料和“下一步”链接点击；
- 代码复制或 demo 启动；
- 7/30 天回访；
- 文章更新后旧读者再次进入的比例；
- 读者能否复述文章的条件化结论。

只有这些数据改善，才能说“AI 味下降后更多人愿意看”。

## 主要来源

### 国内

- [Datawhale Agent Tutorial](https://github.com/datawhalechina/agent-tutorial)
- [Datawhale 1.1 Agent 原理](https://github.com/datawhalechina/agent-tutorial/blob/main/docs/%E7%AC%AC%E4%B8%80%E7%AB%A0%EF%BC%9AAgent%E7%AE%80%E4%BB%8B/1.1%20Agent%E5%8E%9F%E7%90%86.md)
- [Datawhale 2.2 日程规划小助手](https://github.com/datawhalechina/agent-tutorial/blob/main/docs/%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9AAgent%E5%AE%9E%E8%B7%B5/2.2%20%E6%97%A5%E7%A8%8B%E8%A7%84%E5%88%92%E5%B0%8F%E5%8A%A9%E6%89%8B.md)
- [花叔 Harness Engineering 橙皮书](https://www.huasheng.ai/orange-books/harness/)

### 国外

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI: New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
- [OpenAI: Agents guide](https://developers.openai.com/api/docs/guides/agents)
- [OpenAI Cookbook: Evaluating Agents with Langfuse](https://developers.openai.com/cookbook/examples/agents_sdk/evaluate_agents)
- [LangChain: The rise of context engineering](https://www.langchain.com/blog/the-rise-of-context-engineering)
- [LangChain: Context Engineering](https://www.langchain.com/blog/context-engineering-for-agents)
- [LangChain: How We Benchmark Deep Agents](https://www.langchain.com/blog/how-we-benchmark-deep-agents)
- [LangChain: Autonomous SRE Agent for Kubernetes](https://www.langchain.com/blog/how-we-build-an-autonomous-sre-agent-for-kubernetes-deployments)
- [Simon Willison: ai-agents tag](https://simonwillison.net/tags/ai-agents/)
- [Simon Willison: How I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
- [Chip Huyen: Agents](https://huyenchip.com/2025/01/07/agents.html)
- [Chip Huyen: Common pitfalls when building generative AI applications](https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html)
- [Lilian Weng: Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/)
- [Latent.Space: 5 Trends That Defined AI Engineering at World's Fair 2026](https://www.latent.space/p/aiewf26trends)
- [Latent.Space: Ontologies Are So Back](https://www.latent.space/p/ontologies-agentic-systems)
- [Latent.Space: Unpacking ChatGPT Work](https://www.latent.space/p/unpacking-chatgpt-work)

## 调研限制

- Datawhale 教程最后活跃时间较早，部分 ModelScope/AgentFabric 操作可能已经变化。
- 花叔页面是书籍落地页，不是完整可复现实验；数字按作者主张处理。
- Anthropic、OpenAI、LangChain 的案例带有产品和生态立场，内部 eval 不外推为行业标准。
- Simon、Chip、Lilian 和 Latent.Space 代表一线作者/编辑判断，不等于统计共识。
- 本文没有访问站点分析后台，也没有实际访谈现有读者；关于留存的判断仍需验证。
