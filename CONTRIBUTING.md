# 写作贡献指南

## 文章契约

Pattern 文章不使用固定十段模板。每篇只回答一个工程问题，标题和顺序服从这个问题。CI 检查最小编辑质量，不检查组件数量。

开稿前先写清五件事：

1. 读者正在做什么决定？
2. 哪个失败、约束或源码行为让这个决定变得困难？
3. 本文使用源码分析、实验、官方文档还是混合证据？
4. 结论在哪些版本和场景下成立？
5. 读完后，读者能采取什么具体动作？

推荐顺序是“问题 → 材料或实验 → 观察 → 失败与代价 → 条件化判断 → 复现与来源”。可以删减，也可以换序。不要为了凑齐四套系统而加入没有产生决策差异的案例。

## 元数据

每篇 pattern 的 frontmatter 必须包含作者、核验日期和证据类型：

```yaml
title: 02 · Agent Loop
description: 进程中断后，怎样恢复工具副作用、验证状态和下一步执行
author: Rick
last_verified: "2026-08-10"
evidence: source-analysis
```

`evidence` 可选值：`source-analysis`、`experiment`、`official-docs`、`mixed`。没有真实运行轨迹时，不要写 `experiment`。

## 开头与正文

- 第一屏先出现问题、约束或已观察到的源码行为，不从 Agent 定义和行业趋势写起。
- `<Verdict>` 可用但不强制。中文最多 280 字，英文最多 600 字符。
- 普通段落尽量不超过 240 字符；一个段落只推进一个判断。
- “唯一、完整、真正、生产级、标准做法”必须有范围和来源，否则删除。
- 合成例子写明“假设场景”或“测试向量”，不要包装成线上事故。
- 数字评分必须公开 rubric、样本和算法。没有 rubric 时改成条件化决策表或文字判断。

## 组件按需使用

| 组件 | 适用情况 |
| --- | --- |
| `<Verdict>` | 能用两三句话给出有边界的结论 |
| `<Diagram>` / `<AgentLoopSVG>` | 图能减少正文解释，而不是装饰 |
| `<CompareTable>` | 至少两个实现产生了明确决策差异 |
| `<TradeOff>` | 两条可解释的取舍轴确实存在 |
| `<BuildRecipe>` | 有可执行步骤和已知失败模式 |
| `<SourceBlock>` / `<SourceTrail>` | 展示引用材料和 pinned source 路线 |

import 路径继续使用 `@components/*`。删除组件后同步清理 import。

## 视觉规则

- 所有架构图都用 **Excalidraw** 画。源文件放 `docs-site/diagrams/NN-*.excalidraw`，导出 SVG 到 `docs-site/public/diagrams/NN-*.svg`。
- 不允许在 MDX 里手写大型 SVG（除非用 `<AgentLoopSVG>` 这类复用组件）。
- 颜色编码遵循 `src/styles/tokens.css`：
  - 🟢 共同点（绿）
  - 🟠 差异点（橙）
  - 🟣 点评（紫）
  - 🔴 风险（红）
  - 🔵 源码（蓝）

## i18n 流程

1. 先用中文完成问题、证据和判断。
2. 跑 `pnpm check:template` 检查元数据、证据入口、标题与附录锚点。
3. 在 `src/content/docs/en/<相同路径>` 复写英文，保留判断，不逐句直译。
4. 跑 `pnpm check:i18n` 确认中英文件 1:1 对齐。
5. 英文未完成时允许 stub（顶部一行 `🚧 WIP — see Chinese version` + 中文链接）。

## 引用规范

- 所有评价类断言必须挂引用：`REF/...` 路径或官方文档外链。
- 厂商 benchmark 和案例数字标为来源方主张，不外推成行业规律。
- 源码文章保留 pinned commit；更新 `src/lib/repoLinks.ts` 后重新核验受影响的判断。
- 闭源系统（Claude Code）章节顶部必须出现：
  > 以下基于公开文档 + sourcemap 解包做行为推断，非源码逐行。

## 附录

练习和复盘题放在一个带 `id="interview-drill"` 的折叠附录里。源码目录、完整对照表和次要实现也可以下沉到折叠区域，主线不要因此断开。

## 提交前 checklist

```bash
pnpm check:all   # = astro check + template check + i18n parity check
pnpm build       # 确认能 SSG 通过
pnpm preview     # 本地预览
```
