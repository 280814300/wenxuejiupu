---
title: 开源 Android 工具推荐（二）：短信转发器 SmsForwarder，备用机短信自动转发
description: 短信转发器 SmsForwarder（pppscn/SmsForwarder）是一款开源 Android 应用，监听短信、来电与 App 通知，按规则转发到钉钉、企业微信、飞书、邮箱、Telegram 等，是备用机神器。
slug: android-smsforwarder-2026
pubDate: 2026-10-14
tags: ["开源", "Android", "效率工具", "App推荐", "短信转发"]
repo: https://github.com/pppscn/SmsForwarder
license: BSD
platforms: ["Android"]
summary: 监控短信/来电/App 通知并按规则转发到钉钉/企业微信/飞书/邮箱/Telegram 等的开源 Android 工具，备用机必备，BSD 协议。
author: 文学酒铺
draft: false
---

## 写在前面

很多人手里有一台"备用机"：插着副卡，专门收验证码、收银行短信。问题是——你总不能天天盯着它看。

**短信转发器 SmsForwarder** 干的事很简单：备用机收到短信 / 来电 / App 通知，立刻按你定的规则，转发到你的主力机（或任意渠道）。一台旧手机，瞬间变成"永不漏消息"的短信中枢。

## 它是什么

SmsForwarder 是一款 **开源 Android 应用**，监控手机的短信、来电和 App 通知，并根据指定规则转发到其它地方。它不是只能转发短信——准确说，是"消息中转站"。

## 核心功能：能帮你做什么

- **多通道转发**：钉钉群机器人、钉钉企业内机器人、企业微信群机器人、企业微信应用消息、飞书群机器人、邮箱、Bark、Webhook、Telegram 机器人、Server 酱、PushPlus、手机短信……覆盖面很广。
- **监听范围全**：短信、来电、App 通知，三类都能触发转发。
- **规则过滤**：支持正则匹配，只转发你关心的（比如只转"验证码"，过滤垃圾短信）。
- **双向远程控制**：不只是"收"，还能主动控制——远程发短信、查短信、查通话记录、查通讯录、查电量等（V3.0 新增的服务端 / 客户端能力）。
- **自动任务 & 快捷指令**：把重复操作自动化（v3.3 新增）。

## 适合谁 / 使用场景

- 双卡 / 多卡用户，副卡放备用机，验证码实时推到主力机；
- 做小生意、需要把店铺手机短信汇总到工作群的人；
- 想给家里老人机装一个，关键时刻能远程查状态的子女。

> 隐私声明（来自项目官方）：SmsForwarder **不收集任何隐私数据**，仅在做版本统计 / 检查更新时发送版本号；代码与 APK 仅供测试和学习研究。

## 开源地址与许可证

- 仓库：[github.com/pppscn/SmsForwarder](https://github.com/pppscn/SmsForwarder)
- 下载：GitHub Releases 为首发地址，另有 Gitee 国内镜像与网盘下载
- 许可证：**BSD**
- 平台：Android 4.4 ~ 13（v3.x）

## 一句话总结

一台吃灰的旧 Android 手机 + SmsForwarder，等于白捡一个"永远在线、自动转发"的短信秘书——而且完全开源免费。

