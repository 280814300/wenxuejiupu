---
title: 用 WorkBuddy 从零搭建静态网站（四）：把成果存到 GitHub
description: 以文学酒铺为例，用网盘比喻讲清 Git/GitHub，手把手注册、用 GitHub Desktop 把 WorkBuddy 生成的站点推上去，零命令行也能做。
slug: static-site-github-2026
pubDate: 2026-10-08
tags: ["教程", "静态网站", "GitHub", "部署", "WorkBuddy"]
summary: 把 GitHub 当"代码网盘"，把 WorkBuddy 写的站点存上去。
author: 文学酒铺
draft: false
---

## 回顾

上篇你把 WorkBuddy 生成的项目在本地跑起来了，能预览、能写文章、能构建。但文件只在**你这台电脑**上——换电脑就没了，也没法发布。

这篇解决：**把 WorkBuddy 帮你写好的站点，存到网上一个保险箱**，叫 GitHub。

## 一、Git 和 GitHub 是什么（先懂比喻）

- **Git** = 一个"记录每次改动"的小工具，像作文的"修订记录"。
- **GitHub** = 把 Git 记录存在**网上**的地方，相当于**代码的网盘**。

为什么要存上去？三个好处：

1. **不丢**：电脑坏了，网上的还在。
2. **能发布**：下一篇 Cloudflare 直接从 GitHub 取代码上线。
3. **有历史**：改错了能退回上一版。

## 二、注册 GitHub（2 分钟）

1. 浏览器打开 `https://github.com`。
2. 点右上角 **Sign up**（注册）。
3. 填邮箱 → 设密码 → 取个用户名（英文，比如 `xiaoming`）→ 验证邮箱。
4. 注册完登录。✅

## 三、装 GitHub Desktop（不用记命令的"网盘客户端"）

GitHub 网站能传文件，但用**桌面客户端**最省事，像把文件夹拖进网盘。

1. 打开 `https://desktop.github.com`，下载安装。
2. 打开后用刚注册的 GitHub 账号登录。

## 四、在 GitHub 上建一个"仓库"

"仓库"（repository）= 一个项目的文件夹。

1. 网页右上角点 **+** → **New repository**。
2. 仓库名填 `my-site`（和本地文件夹同名最好）。
3. 选 **Public**（公开，免费；私有的有些功能要钱）。
4. **不要**勾 "Add a README"（我们本地已有内容）。
5. 点 **Create repository**。✅ 网上保险箱建好了。

## 五、把本地网站推上去（点几下就行）

1. 打开 **GitHub Desktop**。
2. 菜单 **File → Add Local Repository**，选你本机的 `my-site` 文件夹（就是 WorkBuddy 生成、你跑起来的那个）。
3. 它会提示"发布到 GitHub"，点 **Publish repository**。
4. 确认仓库名 `my-site`、保持 **Public**，点 **Publish**。
5. 等进度条走完。✅ 搞定！

> 不想用客户端？命令行也行（在 `my-site` 目录里）：

```bash
git init
git add .
git commit -m "我的第一个网站"
git branch -M main
git remote add origin https://github.com/你的用户名/my-site.git
git push -u origin main
```

## 六、验证真的上去了

1. 浏览器打开 `https://github.com/你的用户名/my-site`。
2. 能看到 `src`、`package.json`、`dist` 等文件，✅ 成功。
3. 以后每改一次，在 GitHub Desktop 里写句说明（比如"加了新文章"），点 **Commit to main** → **Push origin**，就同步上去了。

## 本篇小结

WorkBuddy 帮你写好的网站代码，现在**安全地躺在 GitHub 上**，换电脑、重装都不怕，而且——

下一篇，让 **Cloudflare** 从这个仓库里取代码，自动变成全世界能访问的真网站。你只要改文章、点推送，网站就自己更新。

> 口诀：**本地改 → Desktop 提交推送 → 网上更新**。记住这三步，后面全自动。

---

## 本系列文章

> 《用 WorkBuddy 从零搭建静态网站》系列（共 5 篇），建议按顺序阅读：

- [（一）从文学酒铺说起](/tools/static-site-why-2026/)
- [（二）选框架：WorkBuddy 怎么帮你定 Astro](/tools/static-site-framework-2026/)
- [（三）本地跑起来看效果](/tools/static-site-local-dev-2026/)
- [（四）推到 GitHub](/tools/static-site-github-2026/)
- [（五）连 Cloudflare 上线](/tools/static-site-cloudflare-2026/)

> 你正在读：**（四）推到 GitHub** ← 本文
