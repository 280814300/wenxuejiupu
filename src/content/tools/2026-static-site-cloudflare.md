---
title: 用 WorkBuddy 从零搭建静态网站（五）：连 Cloudflare 自动上线
description: 以文学酒铺（wenxuejiupu.com）真实上线为例，讲清 Cloudflare Pages 如何把 GitHub 项目变全世界可访问的网站，并说明改文章自动更新。
slug: static-site-cloudflare-2026
pubDate: 2026-10-08
tags: ["教程", "静态网站", "Cloudflare", "部署", "WorkBuddy"]
summary: 把 GitHub 仓库交给 Cloudflare，约60秒变真网站；文学酒铺就是这样上线的。
author: 文学酒铺
draft: false
---

## 回顾

前四篇我们：想清楚要什么 → WorkBuddy 选 Astro 并生成 → 本机跑起来 → 存进 GitHub。
现在只差最后一步：**让全世界输入网址就能看到。**

这一篇用 **Cloudflare Pages**（免费）完成——文学酒铺（wenxuejiupu.com）就是这样公开上线的。

## 一、Cloudflare Pages 是什么（比喻）

把它想成一家**免费的"网站工厂"**：

- 你给它 GitHub 仓库的"图纸"；
- 它自动按图纸造出网页；
- 造好放在它家的服务器上，给一个网址；
- 你改了图纸（推一次 GitHub），它**自动重新造**，不用你动手。

而且——**免费**、速度快、还顺手送你 HTTPS（地址栏小锁，更安全）。

## 二、注册 Cloudflare（1 分钟）

1. 浏览器打开 `https://www.cloudflare.com`，点 **Sign up**。
2. 用邮箱注册登录。✅

## 三、连 GitHub，授权（一次性）

1. 登录后左上角选 **Workers & Pages**（产品或工作区）。
2. 点 **Create** → **Pages** → **Connect to Git**。
3. 点 **GitHub**，按提示**授权**（允许 Cloudflare 读取你的仓库）。
4. 授权后，列表里会出现你的 `my-site` 仓库。

## 四、新建项目，填三样（关键）

1. 选中 `my-site` 仓库，点 **Begin setup**。
2. 构建设置这样填：

   | 项目 | 填什么 | 说明 |
   |------|--------|------|
   | Framework preset | 选 **Astro**（没有就留空） | 让它用对命令 |
   | Build command | `npm run build` | 造网页的命令 |
   | Build output directory | `dist` | 成品放哪（Astro 默认就是 dist） |

3. 其它默认，点 **Save and Deploy**（保存并部署）。
4. 等进度条走完（通常 **约 60 秒**）。✅

## 五、拿到你的网址

部署完，页面会显示一个地址，类似：

```
https://my-site.pages.dev
```

**按住 Ctrl 点击它**（或复制到浏览器）。→ 你看到自己的网站，✅ **全世界上线了！**

把这个网址发给朋友，他们立刻能看。文学酒铺先经 WorkBuddy 做了预览发布，再正式连 Cloudflare，最终绑定了 wenxuejiupu.com 这个自己的域名——你照上面四步推上去，约 60 秒就能访问。

## 六、以后改文章，怎么自动更新

这是最爽的部分——**你只管写，工厂自己造**：

1. 在本机用 VS Code 改文章 / 加文章（见第三篇）。
2. 打开 **GitHub Desktop**，写句说明，点 **Commit to main** → **Push origin**。
3. 回到 Cloudflare，会看到一次**新的部署**自动开始；约 60 秒后，刷新网址就是新内容。

> 整套闭环一句话：**本地写 → 推 GitHub → Cloudflare 自动上线**。你再也不用碰服务器。

## 七、想用自己的域名（可选，不急）

如果你买了域名（比如 `xiaoming.com`），在 Cloudflare 项目里点 **Custom domains** → 填域名 → 按提示去域名商把 DNS 指过来即可。没有域名，`.pages.dev` 这个免费地址也完全能用；像文学酒铺那样绑定 wenxuejiupu.com 只是多了一步。

## 全系列通关小结

| 篇 | 你学会了（用 WorkBuddy） |
|----|----------|
| 一 | 网站=房子、域名=地址、服务器=地；整体思路 |
| 二 | 把需求告诉 WorkBuddy，它帮你定 Astro |
| 三 | 打开 WorkBuddy 生成的项目，本地预览/写文/构建 |
| 四 | 存进 GitHub 当保险箱 |
| 五 | 连 Cloudflare，全世界能访问，且自动更新 |

从零到上线，你走完了全程——而且主力是 WorkBuddy，你只管下指令、看效果。接下来，去写你的第一篇文章吧，**这个世界，值得看到你写的东西。**

> 卡住别慌：把报错那行字原样复制给 WorkBuddy，比说"坏了"有用一百倍。

---

## 本系列文章

> 《用 WorkBuddy 从零搭建静态网站》系列（共 5 篇），建议按顺序阅读：

- [（一）从文学酒铺说起](/tools/static-site-why-2026/)
- [（二）选框架：WorkBuddy 怎么帮你定 Astro](/tools/static-site-framework-2026/)
- [（三）本地跑起来看效果](/tools/static-site-local-dev-2026/)
- [（四）推到 GitHub](/tools/static-site-github-2026/)
- [（五）连 Cloudflare 上线](/tools/static-site-cloudflare-2026/)

> 你正在读：**（五）连 Cloudflare 上线** ← 本文
