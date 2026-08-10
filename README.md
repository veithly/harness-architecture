# Harness Architecture · Docs Site

> Public bilingual documentation site for Harness Architecture.
>
> Live site: <https://harness-architecture.pages.dev>
>
> **Harness 释义**：指 LLM 之外那一整套支撑——loop、上下文、工具、沙箱、verifier、memory、observability。本书横向拆 4 个真实 Harness，作为自己做 Agent 的参考蓝本。

## Positioning

This site is written for engineers building real agent runtimes. It compares Codex, Claude Code, OpenClaw, and Hermes at the harness layer: loop, context, tools, verification, sandboxing, memory, skills, background tasks, security, todo/task progress, and execution-state routing.

The public surface is intentionally bilingual:

- Chinese is the default reading path.
- English mirrors the same structure for international sharing.
- Every pattern chapter keeps source trails to concrete files and line ranges under the studied systems.

## 技术栈

- **Astro 6** + **Starlight 0.39** — 静态站点 + 文档骨架
- **MDX** — 章节内嵌 Astro 组件
- **Pagefind** — 全文搜索
- **Sharp** — 图片优化

## 开发

```bash
pnpm install
pnpm dev          # http://localhost:4321
```

## 校验与构建

| 命令 | 用途 |
|------|------|
| `pnpm check` | astro check（TypeScript + content schema） |
| `pnpm check:template` | 检查元数据、证据入口、标题与附录锚点 |
| `pnpm check:i18n` | 中英文章节 1:1 对齐 |
| `pnpm check:all` | 上面三件套 |
| `pnpm build` | SSG 输出到 `dist/` |
| `pnpm preview` | 本地预览 build 产物 |

## Deploy

This repository is designed for Cloudflare Pages as the public project site:

- Repository: `veithly/harness-architecture`
- Domain: `https://harness-architecture.pages.dev`
- Cloudflare Pages project: `harness-architecture`
- Manual deploy command: `pnpm deploy:cloudflare`

The GitHub workflow validates every push with:

```bash
pnpm install --frozen-lockfile
pnpm check:all
pnpm build
```

Publishing runs the same build and uploads `dist/` to Cloudflare Pages.

## 目录约定

```text
src/content/docs/             # 中文（默认 locale = root）
├── index.mdx                 # 首页
├── interview.mdx             # 220 道面试题索引
├── skill.mdx                 # 配套 build-your-own-agent skill
├── preview.mdx               # 组件预览（dev only）
├── patterns/                 # 22 章工程模块
└── systems/                  # 4 个系统画像
src/content/docs/en/          # 英文镜像（i18n parity 由 CI 校验）
src/content/i18n/             # UI 字符串翻译
src/components/               # 文章与站点 Astro 组件
src/styles/                   # tokens + handdrawn 主题
diagrams/                     # Excalidraw 源文件（入仓）
public/diagrams/              # 导出的 SVG/PNG（部署用）
scripts/                      # 模板与 i18n 校验脚本
```

## 编辑契约

Pattern 文章不再复制固定十段。每篇围绕一个工程冲突组织，保留可追溯源码，同时说明版本、证据类型、失败代价和结论边界。CI 检查：

- `author`、`last_verified`、`evidence` 元数据；
- 至少四个不重复的二级标题；
- 至少一个源码或外部证据入口；
- 中文结论不超过 280 字，英文不超过 600 字符；
- 练习和复盘题位于稳定的折叠附录。

完整规则见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 视觉与组件

- **组件预览**：dev 模式访问 [`/preview/`](http://localhost:4321/preview/)
- **字体**：`Excalifont` / `Virgil`（手绘）+ `Source Han Sans SC`（中文）
- **主题**：`src/styles/tokens.css` + `src/styles/handdrawn.css`

## 写新章节的最短路径

1. 写下文章只回答的一个工程问题和证据类型。
2. 从最能暴露取舍的源码行为、失败或约束开场。
3. 同步复写 `src/content/docs/en/patterns/<同名>.mdx`。
4. 跑 `pnpm check:all` 和 `pnpm build`。
5. PR 说明核验日期、source snapshot 和未验证边界。

---

Companion skill: <https://github.com/veithly/build-your-own-agent>
