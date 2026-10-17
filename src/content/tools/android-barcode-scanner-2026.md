---
title: 条码扫描 离线扫码 商品条码 二维码识别 本地隐私 零售仓储盘点 免费安卓
description: 条码扫描是一款完全离线、零联网的安卓条码识别工具，支持商品条码与二维码（EAN-13/Code128/QR 等），识别结果仅存本机、绝不外传，适合零售、仓储、盘点等场景，免费开源。
slug: android-barcode-scanner-2026
pubDate: 2026-10-17
tags: ["开源", "Android", "效率工具", "条码扫描"]
repo: https://github.com/280814300/barcode-scanner
license: MIT
platforms: ["Android"]
summary: 条码扫描：完全离线、零联网的安卓条码识别工具，支持商品条码与二维码，数据本地存储、隐私安全，零售仓储盘点好帮手，免费开源。
author: 文学酒铺
draft: false
---

## 写在前面

你有没有过这种时候：店里来批新货要盘点，或者仓库收货要对条码，拿起手机想扫一下，结果要么弹出广告、要么还要联网登录、要么数据悄悄传到了某个云？

**条码扫描** 干的事很简单：打开相机，对着条码扫，结果就乖乖列在本地列表里，想复制就复制、想导出 CSV 就导出，全程不连网、不上传。一句话——**一个只活在手机里的条码本**。

## 它是什么

**条码扫描** 是一款 **Android 应用**，用原生 Kotlin 基于 `zxing-android-embedded`（ZXing 引擎）写成。它**完全离线运行**，安装即用，不用联网下载任何模型，也不申请任何网络权限——安装包里除了摄像头权限，什么都没有。

> 包名 `com.maoge.barcodescanner`，最低支持 Android 6.0（API 23），v1.0 已发布。

## 核心功能：能帮你做什么

- **单码实时识别**：相机预览连续自动解码，扫到即入列表；支持常见一维 / 二维码——EAN-13、EAN-8、Code128、Code39、UPC、QR 等。
- **本地列表自动保存**：识别结果写入本机 `barcodes.json`，带格式与时间，下次打开直接加载历史。
- **一键复制**：每条都有「复制」按钮，点一下进剪贴板。
- **批量导出**：顶部菜单「导出 CSV / 导出 JSON」，走系统分享发到微信 / 邮件（CSV 带 BOM，Excel 打开中文不乱码）。
- **辅助操作**：闪光灯开关、手动录入（没摄像头或不方便扫时手填）、关键字筛选、单条删除、清空（带确认）。

## 适合谁 / 使用场景

- 小店老板 / 店员做**零售盘点、收货对账**，一扫就记录，不用纸笔；
- 仓管做**入库核验**，批量导出 CSV 直接进表格；
- 在意**隐私**的人——数据只在本机，断网也能用，绝对不外传；
- 需要把条码和 Excel / 微信流转对接的轻量场景。

> 小提醒：v1.0 是**单码**版本，一次识别一个码。如果你常遇到一物多码（69 码 / SN / IMEI 紧挨着）需要同框批量识别，可以等后续多码版本；当前版本聚焦"稳、准、简单"。

## 开源地址与许可证

- GitHub 仓库：github.com/280814300/barcode-scanner
- 下载：GitHub Releases 提供 `app-release.apk`（自签名，可直接安装 / 覆盖升级）
- 许可证：MIT（仅供学习与交流）
- 平台：Android 6.0（API 23）及以上

## 一句话总结

如果你想要一个**不联网、不上传、扫完就在本地**的条码工具，条码扫描把"简单"做到了位——装好就能扫，数据全留在这台手机上。

## 下载指引

<div class="card" style="border:2px solid #0ea5e9;background:#f0f9ff;text-align:center;padding:1.15rem;margin:1.25rem 0;">
<strong style="font-size:1.05rem;">点击下载指引 →</strong><br/>
<a href="https://pan.quark.cn/s/ea9e43db123d" style="display:inline-block;margin-top:.6rem;padding:.55rem 1.3rem;background:#0ea5e9;color:#fff;border-radius:8px;text-decoration:none;font-weight:600;">本文已存夸克网盘 · 点此下载 / 转存</a>
</div>
