---
title: Ventoy 多系统启动盘
description: 一个开源工具，让你把多个系统镜像放进同一个 U 盘，启动时自由选择，免去反复烧录。
slug: ventoy-boot-usb
pubDate: 2026-04-18
tags: ["开源", "工具", "启动盘"]
repo: https://github.com/ventoy/Ventoy
license: GPL-3.0
platforms: ["Windows", "Linux", "macOS"]
author: 文学酒铺
draft: false
---

## 痛点

传统做法是"一个 U 盘一个镜像"，换系统就得重新烧录。Ventoy 改变了这一点。

## 怎么用

1. 用 Ventoy 把 U 盘初始化一次
2. 把 `.iso` 文件直接拷进 U 盘
3. 开机从 U 盘启动，在菜单里选择镜像

## 支持格式

ISO、WIM、IMG、VHDx 等主流镜像格式都能直接引导，无需逐个制作。
