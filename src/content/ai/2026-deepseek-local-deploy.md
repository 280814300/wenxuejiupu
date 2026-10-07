---
title: DeepSeek 本地部署实操
description: 在普通电脑上用 Ollama 跑通 DeepSeek 蒸馏模型，覆盖安装、量化选择与常见报错。
slug: deepseek-local-deploy-2026
pubDate: 2026-04-02
tags: ["AI", "DeepSeek", "本地部署"]
level: 进阶
software: DeepSeek
author: 文学酒铺
draft: false
---

## 为什么本地跑

云端 API 方便，但本地模型胜在**隐私可控、零调用成本、可离线**。DeepSeek 的蒸馏版对硬件相当友好。

## 安装 Ollama

Ollama 把模型管理简化为一条命令：

1. 从官网下载安装 Ollama
2. 命令行执行 `ollama run deepseek-r1:7b`

## 量化怎么选

- 7B 级别：4-bit 即可，8GB 内存可跑
- 14B 级别：建议 16GB 内存
- 32B 以上：需要独立显卡

## 常见报错

> 显存不足时，优先降量化，而非换模型。

遇到 `CUDA out of memory`，把量化降到 q4 再试，通常就能跑起来。
