# 文学酒铺 · 静态网站

> 个人品牌笔名。
> 定位：开源软件分享 · AI 软件落地教学 · 网盘资源工具内容

- 域名：`wenxuejiupu.com`
- Slogan：爱国、进步、民主、科学，科技与人文的浪漫主义
- 技术栈：Astro 5 + TypeScript(strict) + Content Collections(zod) + Tailwind(暗黑跟随系统)
- 输出：纯静态，部署目标 **Cloudflare Pages**
- 性能红线：默认零 JS、零外部字体阻塞，Lighthouse 四项 ≥ 95

---

## 一、URL 结构（永久固定，任何代码不得偏离）

```
文章：  /{栏目}/{发布年份}/{slug}/
示例：  /ai/2026/claude-china-guide-2026/
栏目：  /ai/  /tools/  /resources/  /humanities/
年份：  /ai/2026/  /ai/2025/
关于：  /about/
订阅：  /rss.xml     站点地图：/sitemap-index.xml     robots：/robots.txt
```

- 全站 URL 以 `/` 结尾（`trailingSlash: 'always'` + `build.format: 'directory'`）
- `slug` 强制小写英文 + 短横线，由 `src/content.config.ts` 的 zod 正则保证

四个栏目（content collections）：

| 栏目 | 目录 | 内容 |
|------|------|------|
| ai | `src/content/ai` | AI 应用落地教学（含 level / software 字段） |
| tools | `src/content/tools` | 软件分享 / 自托管 / 效率清单（含 repo / license / platforms / summary 字段） |
| resources | `src/content/resources` | 资源合集 · 网盘（含 resource / panUrl / extractCode / size 字段） |
| humanities | `src/content/humanities` | 人文记录（仅基础字段） |

---

## 二、本地开发

```bash
npm install      # 安装依赖
npm run dev      # 本地预览 http://localhost:4321
npm run check    # Astro + TypeScript 严格类型检查
npm run build    # 产出 dist/ 静态文件
npm run preview  # 本地预览构建结果
```

> Node 要求 ≥ 18.17.1。构建无 SSR、无适配器，纯静态。

---

## 三、目录结构

```
wenxuejiupu/
├─ astro.config.mjs        # 站点/集成/trailingSlash/format 配置
├─ tailwind.config.mjs     # darkMode: 'media' 跟随系统
├─ tsconfig.json           # extends astro/tsconfigs/strict
├─ src/
│  ├─ content.config.ts    # 四个 content collection 的 zod Schema（核心质检关）
│  ├─ consts.ts            # 站名/Slogan/栏目/导航 集中常量
│  ├─ styles/global.css    # Tailwind + 中文排版 + 暗黑覆盖
│  ├─ layouts/
│  │  └─ BaseLayout.astro  # SEO/OG/JSON-LD/系统字体栈/暗黑
│  ├─ components/
│  │  ├─ Header.astro  Footer.astro  PostCard.astro   # 全部零 JS
│  ├─ content/             # 文章数据（frontmatter 受 Schema 强校验）
│  │  ├─ ai/  tools/  resources/  humanities/
│  └─ pages/
│     ├─ index.astro                   # 首页
│     ├─ [column]/index.astro           # 栏目页
│     ├─ [column]/[year]/index.astro    # 年份归档
│     ├─ [column]/[year]/[slug].astro   # 文章详情
│     ├─ about/index.astro
│     ├─ rss.xml.js                     # RSS（@astrojs/rss）
│     ├─ robots.txt.ts
│     └─ 404.astro
├─ public/favicon.svg
└─ README.md
```

---

## 四、内容创作规范

在对应栏目目录新建 `xxx.md`，frontmatter 必须包含 Schema 要求的字段。**保存时 zod 会立即校验**，不合规直接报错，阻断构建。

### 通用必填字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string(2–120) | 标题 |
| `description` | string(10–200) | 摘要，用于 meta 与卡片 |
| `slug` | string(正则) | 小写英文+短横线，决定 URL |
| `pubDate` | date(YYYY-MM-DD) | 发布日期，决定年份段 |
| `tags` | string[] | 标签（默认空） |
| `author` | string | 默认"文学酒铺" |
| `draft` | boolean | true 则不发布 |

### 各栏目专属字段

- **ai**：`level: 入门|进阶|精通`（默认入门）、`software?: string`
- **tools**：`repo: url`、`license: string`、`platforms: (Windows|macOS|Linux|Android|iOS|Web)[]`
- **list**：`summary?: string`（清单正文写在 body）
- **pan**：`resource: string`、`panUrl: url`、`extractCode?: string`、`size?: string`

### 示例（ai）

```markdown
---
title: Claude 国内可用指南 2026
description: 2026 年国内用户如何稳定、合规地使用 Claude 系列 AI 工具。
slug: claude-china-guide-2026
pubDate: 2026-01-20
tags: ["AI", "Claude", "教程"]
level: 入门
software: Claude
author: 文学酒铺
draft: false
---

## 正文从这里开始（标准 Markdown）
```

> 正文用标准 Markdown 书写，自动渲染为 `.prose` 中文排版样式。

---

## 五、部署到 Cloudflare Pages

### 方式 A：连接 Git 仓库（推荐）

1. 登录 Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** → 连接 Git 仓库。
2. 构建配置：
   - **Framework preset**：无 / 选 Astro（若列出）
   - **Build command**：`npm run build`
   - **Build output directory**：`dist`
3. 保存并部署。此后每次 push 自动构建。
4. 在 **Custom domains** 绑定 `wenxuejiupu.com`（需先在域名商处把 DNS 指向 Cloudflare）。

### 方式 B：Wrangler 命令行

```bash
npm install -g wrangler
npm run build
wrangler pages deploy dist --project-name=wenxuejiupu
```

### 注意事项

- 本项目**纯静态**，无需 Functions、无需 SSR 适配器。
- `@astrojs/sitemap` 会自动生成 `/sitemap-index.xml`，`/robots.txt` 已指向它。
- 改站名/Slogan/栏目描述，集中改 `src/consts.ts` 一处即可。
- 换域名时同步改 `astro.config.mjs` 的 `site` 与 `src/consts.ts` 的 `domain`。

---

## 六、SEO 与性能要点

- 每页输出 `title` / `description` / `canonical` / Open Graph / Twitter Card。
- 文章页注入 `BlogPosting` 结构化数据（JSON-LD，非执行脚本，不计 JS）。
- 全站默认零 JavaScript：导航、卡片、目录均为纯 HTML/CSS。
- 字体走系统字体栈，无外部字体请求，无渲染阻塞。
- 暗黑模式由 `prefers-color-scheme` 自动切换，无需 JS、无闪烁。
- 图片/资源均响应式，移动端优先。

---

## 七、许可证

站点代码 MIT。文章内容版权归作者所有，转载请注明出处。
