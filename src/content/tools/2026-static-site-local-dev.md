---
title: 用 WorkBuddy 从零搭建静态网站（三）：本地跑起来看效果
description: 以 WorkBuddy 生成的 Astro 项目为例，手把手装 Node.js 与 VS Code，预览、改一句话热更新、写文并构建。每一步带命令与验证。
slug: static-site-local-dev-2026
pubDate: 2026-10-08
tags: ["教程", "静态网站", "Astro", "本地调试", "WorkBuddy"]
summary: WorkBuddy 生成项目后，你装环境、npm run dev 看效果、npm run build 出成品。
author: 文学酒铺
draft: false
---

## 目标

本篇结束，你能在**自己电脑**上看到 WorkBuddy 帮你搭的网站，并且改一句话、刷新就变。

> 别怕"命令"。命令就是"对电脑下指令"。下面每个命令都给全，你**复制、粘贴、回车**就行。

## 第 1 步：装 Node.js（网站的"发电机"）

Node.js 是后面所有工具的运行环境。没有它，命令跑不起来。

1. 打开浏览器，访问 `https://nodejs.org`。
2. 首页会推荐一个**长线版（LTS）**，点大大的下载按钮。
3. 下载完双击安装包，一路点"下一步 / Next"，全默认即可。
4. 验证装好没：打开"终端"（Mac 叫终端 Terminal；Windows 叫"命令提示符"或 PowerShell），粘贴这行回车：

   ```bash
   node -v
   ```

5. 如果屏幕显示类似 `v18.17.1` 或更大的数字，✅ 成功。报错就重启电脑再试一次。

> 小知识：`node -v` 的 `-v` 是"看版本号"。能显示版本 = 装好了。

## 第 2 步：装 VS Code（写字的"笔记本"）

1. 访问 `https://code.visualstudio.com`，下载并安装（同样一路下一步）。
2. 打开它。以后我们的文章就在这里写。

## 第 3 步：让项目跑起来（WorkBuddy 已经帮你建好了）

WorkBuddy 生成站点时，底层用的就是下面这条官方命令。你可以直接打开它给你的文件夹，也可以自己跑一遍体会：

```bash
npm create astro@latest
```

按提示选：**Empty**（空模板）→ 装依赖选 Yes → 初始化 Git 选 No（后面第 4 篇再讲）。

拿到项目文件夹后，进入并装依赖、启动预览：

```bash
cd 项目文件夹
npm install
npm run dev
```

终端会出现一行 `http://localhost:4321`。**按住 Ctrl 点击它**（或复制到浏览器打开）。
→ 你看到网站首页，✅ 网站在本地跑起来了！（文学酒铺就是这样一个 Astro 项目，只是内容更多。）

## 第 4 步：改一句话，看"热更新"

"热更新"= 你改了内容，网页自动变，不用重启。

1. 在 VS Code 里打开项目文件夹。
2. 找到 `src/pages/index.astro`（这是首页，WorkBuddy 生成的），双击打开。
3. 找里面某段文字，随便改几个字，按 `Ctrl/Cmd + S` 保存。
4. 回到浏览器，网页**已经变了**。✅ 这就是本地调试。

## 第 5 步：写你的第一篇文章

真正的内容放在 `src/content` 里（文学酒铺的文章就在这里面分栏目存放）。我们用的"内容站"方式：

1. 在 `src/content` 下新建文件夹（叫 `posts`），在里面新建文件 `hello.md`。
2. 打开 `hello.md`，写入：

   ```markdown
   ---
   title: 我的第一篇文章
   description: 这是用 Astro 写的第一篇。
   slug: hello
   pubDate: 2026-10-08
   tags: ["随笔"]
   author: 我
   draft: false
   ---

   ## 你好，世界

   这是我自己的网站写的第一句话！
   ```

3. 保存。你的文章就进内容库了（具体怎么在页面上显示，取决于模板，本系列聚焦"能发"这条主线）。

## 第 6 步：构建出"成品"（重要）

"预览"是给你自己看的；"构建"才生成真正能放到网上的文件。

1. 回到终端，按 `Ctrl + C` 停掉预览。
2. 运行：

   ```bash
   npm run build
   ```

3. 看到 `✓ Completed` 字样，✅ 成功。生成的网页都在 `dist` 文件夹里——那就是要放到网上的东西。

## 常见坑（先存着，遇到对着查）

| 现象 | 多半原因 | 办法 |
|------|----------|------|
| `node -v` 报错"找不到命令" | Node 没装好/没重启 | 重装后重启电脑 |
| 浏览器打不开 localhost | 预览没启动 | 确认终端显示 `localhost:4321` 再点 |
| 端口被占 | 之前没关 | 关掉终端重开再 `npm run dev` |
| 构建报错一堆红字 | 文章格式写错 | 看它说哪个文件哪一行，照改（也可把报错发给 WorkBuddy） |

## 本篇小结

你现在已经能在自己电脑上：**打开项目 → 预览 → 写文章 → 构建出成品**。

下一篇，把这些成果存到 **GitHub**（网上的代码保险箱），这样换电脑也不丢，还能一键发布。

> 记住三个命令，后面天天用：`npm run dev`（本地看）、`npm run build`（出成品）、`Ctrl+C`（停掉）。

---

## 本系列文章

> 《用 WorkBuddy 从零搭建静态网站》系列（共 5 篇），建议按顺序阅读：

- [（一）从文学酒铺说起](/tools/static-site-why-2026/)
- [（二）选框架：WorkBuddy 怎么帮你定 Astro](/tools/static-site-framework-2026/)
- [（三）本地跑起来看效果](/tools/static-site-local-dev-2026/)
- [（四）推到 GitHub](/tools/static-site-github-2026/)
- [（五）连 Cloudflare 上线](/tools/static-site-cloudflare-2026/)

> 你正在读：**（三）本地跑起来看效果** ← 本文
