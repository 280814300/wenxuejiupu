---
title: 开源 Android 工具推荐（四）：MusicFree，插件化无广告免费音乐播放器
description: MusicFree（maotoumao/MusicFree）是一款插件化、定制化、无广告的免费开源音乐播放器，支持 Android 与 Harmony OS，本身不集成音源，所有功能靠插件，数据本地存储。
slug: android-musicfree-2026
pubDate: 2026-10-16
tags: ["开源", "Android", "效率工具", "App推荐", "音乐播放器"]
repo: https://github.com/maotoumao/MusicFree
license: AGPL-3.0
platforms: ["Android"]
summary: 插件化、无广告、免费的 Android/Harmony OS 音乐播放器，本身不集成音源，所有搜索/播放靠插件，数据本地存储，AGPL-3.0 开源。
author: 文学酒铺
draft: false
---

## 写在前面

市面上的音乐 App，要么广告多，要么会员墙高，要么"云村""绿钻"各守一摊。想在一个地方听个痛快，反而很难。

**MusicFree** 的思路很"极客"也很干净：它**自己不内置任何音源**，只做一个播放器外壳，所有搜索、播放、歌单、歌词都靠**插件**实现。你要听什么，装对应的插件就行。无广告、免费、开源。

## 它是什么

MusicFree 是一款 **插件化、定制化、无广告的免费音乐播放器**，目前支持 **Android 和 Harmony OS**（另有独立的桌面版 MusicFreeDesktop）。

它的核心哲学：**软件只是播放器，音源由插件提供**。只要有对应的插件，你在网上能搜到的音源，就能在这里搜、放、收藏。

## 核心功能：能帮你做什么

- **插件化架构**：搜索、播放、查看专辑 / 作者、导入歌单、获取歌词……全靠插件。没有插件，它就只是个空壳播放器。
- **无广告 / 免费**：基于 AGPL 协议开源，作者明确承诺保持免费。
- **定制化**：浅色 / 深色模式、自定义背景，界面随你调。
- **隐私优先**：所有数据都存在本地，不收集任何个人信息。
- **歌词关联**：可以把两首歌的歌词关联起来（如 A→B→C），关联后都显示同一份歌词。
- **多端**：Android、Harmony OS，外加桌面版，听歌不挑设备。

## 适合谁 / 使用场景

- 受够了会员墙和开屏广告、想要"一个播放器听遍全网"的人；
- 愿意自己装插件、动手配置音源源的玩家；
- 在意隐私、不想被 App 收集听歌习惯的人。

> 几个官方提醒（节选自项目说明）：
> - 应用商店里出现的"收费版 / 破解版"都是假的，**遇到收费版请直接举报**；
> - 软件不提倡也不提供任何破解行为，请合法合规使用，产生的版权数据请及时删除；
> - 第三方插件请自行鉴别安全性，别装来路不明的东西。

## 开源地址与许可证

- 仓库：[github.com/maotoumao/MusicFree](https://github.com/maotoumao/MusicFree)
- 桌面版：[github.com/maotoumao/MusicFreeDesktop](https://github.com/maotoumao/MusicFreeDesktop)
- 许可证：**AGPL-3.0**
- 平台：Android、Harmony OS（另有桌面版）

## 一句话总结

如果你想要一个"不内置音源、但什么都能听、还无广告"的播放器，MusicFree 把选择权交回了你自己——装什么插件，听什么世界。

