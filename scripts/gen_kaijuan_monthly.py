#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""开卷八分钟月度阅读总结推文生成器。
按月汇总某年度已发布讲书文章，生成 kaijuan-monthly-<year>-<mm>.md。
数据源：humanities 已发布文章（draft:false）+ kaijuan_pending.json 的节目日期。
不在 pending 里的文章归入 1 月（2007-01 批次来自更早 CSV，无日期记录）。

用法: python3 scripts/gen_kaijuan_monthly.py --year 2007 --start-date 2026-12-03
"""
import json, os, re, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PENDING = os.path.join(ROOT, "scripts", "kaijuan_pending.json")
HUMANITIES = os.path.join(ROOT, "src", "content", "humanities")

# 月度音频打包链接（毛哥 2026-11-21 提供，2007 年 01~12 月文件夹）
MONTH_LINKS = {
    "01": "70b26bad3ac0", "02": "a52d8ebae418", "03": "5a9cec9f589c",
    "04": "36c7ed55b88e", "05": "0d51018a2faf", "06": "ce8aa9600974",
    "07": "9029222ccb46", "08": "996144c52ad4", "09": "92ba3ddad688",
    "10": "30317e80614a", "11": "70469845a616", "12": "51a0e5188bb9",
}

def norm_paren(t):
    return t.replace("（", "(").replace("）", ")")

def published_articles():
    """返回 [(book_title, slug, author_disp)]，仅 draft:false 的讲书文章。"""
    out = []
    for fn in sorted(os.listdir(HUMANITIES)):
        if not fn.startswith("kaijuan-youyi-") or not fn.endswith(".md"):
            continue
        txt = open(os.path.join(HUMANITIES, fn), encoding="utf-8").read(3000)
        if "draft: false" not in txt:
            continue
        m = re.search(r"title: 开卷八分钟｜《([^》]+)》", txt)
        if not m:
            continue
        title = m.group(1).strip()
        a = re.search(r"^\| 作者 \| (.+?) \|$", txt, re.M)
        author = a.group(1).strip() if a else ""
        out.append((title, fn[:-3], author))
    return out

def month_map_from_pending():
    """书名(归一) -> 节目月份 'MM'。"""
    data = json.load(open(PENDING))
    mp = {}
    for x in data:
        if not (x.get("has_link") and x.get("url")):
            continue
        t, _ = clean_title_author(x["title"], x.get("author", ""))
        mp[norm_paren(t)] = x["date"][2:4]
    return mp

def clean_title_author(title, author):
    t = title.replace("[", "").replace("]", "")
    a = (author or "").replace("[", "")
    if (not a) and "." in t:
        parts = t.split(".")
        cand = parts[-1].strip()
        if 0 < len(cand) <= 12 and len(parts) > 1:
            if cand not in ("杂志",):
                a = cand
            t = ".".join(parts[:-1]).strip()
    return t.strip(), a.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", default="2007")
    ap.add_argument("--start-date", required=True, help="首篇发布日期 YYYY-MM-DD")
    args = ap.parse_args()

    arts = published_articles()
    mmap = month_map_from_pending()
    buckets = {f"{i:02d}": [] for i in range(1, 13)}
    for title, slug, author in arts:
        mm = mmap.get(norm_paren(title))
        if mm is None:
            mm = "01"  # 无日期记录的归 1 月（2007-01 批次）
        buckets[mm].append((title, slug, author))

    start = datetime.date.fromisoformat(args.start_date)
    written = 0
    for idx, mm in enumerate(sorted(buckets)):
        items = buckets[mm]
        if not items:
            continue
        pub = start + datetime.timedelta(days=idx)
        link_id = MONTH_LINKS.get(mm, "")
        rows = "\n".join(
            f"| 《{t}》 | {a or '梁文道（讲述）'} | [图文讲书](/humanities/{s}/) |"
            for t, s, a in items
        )
        md = f"""---
title: 开卷八分钟｜{args.year} 年 {int(mm)} 月书单全记录：{len(items)} 期节目 · 本月书目一览
description: 梁文道《开卷八分钟》{args.year} 年 {int(mm)} 月全月书单——{len(items)} 期节目、{len(items)} 篇图文讲书全收录，附当月音频夸克网盘打包链接，一次转存整月节目。｜梁文道《开卷八分钟》音频听书
slug: kaijuan-yuedu-{args.year}-{mm}
pubDate: {pub.isoformat()}
tags: ["开卷八分钟", "月度书单", "读书"]
author: 文学酒铺
draft: false
---

> 本文是**梁文道《开卷八分钟》{args.year} 年 {int(mm)} 月月度书单**。当月 {len(items)} 期节目全部整理为图文讲书，每篇附当集夸克网盘音频链接；文末可一键转存**整月音频打包**。

## 📚 {args.year} 年 {int(mm)} 月书目目录（{len(items)} 期）

| 书名 | 作者 | 图文讲书 |
| --- | --- | --- |
{rows}

## 📦 本月音频一键打包

- 夸克网盘（{args.year} 年 {int(mm)} 月全集）：[《开卷八分钟》{args.year}-{mm} 音频打包 · 一键转存](https://pan.quark.cn/s/{link_id})

## ❓ 常见问题（FAQ）

<div class="faq-item">
  <div class="faq-q">Q1：{args.year} 年 {int(mm)} 月《开卷八分钟》一共多少期？</div>
  <div class="faq-a">共 {len(items)} 期，本文目录已全部收录，每期对应一篇图文讲书与当集音频链接。</div>
</div>
<div class="faq-item">
  <div class="faq-q">Q2：可以一次下载 {args.year} 年 {int(mm)} 月全部音频吗？</div>
  <div class="faq-a">可以，点上方「本月音频一键打包」链接即可把 {args.year}-{mm} 全月节目转存到你的夸克网盘。</div>
</div>
<div class="faq-item">
  <div class="faq-q">Q3：想看 {args.year} 年其他月份的书单怎么办？</div>
  <div class="faq-a">每个月份都有一篇月度书单推文，年度总览见《开卷八分钟》{args.year} 年度全收录；可在 humanities 栏目按「月度书单」标签检索。</div>
</div>
"""
        path = os.path.join(HUMANITIES, f"kaijuan-monthly-{args.year}-{mm}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"[ok] {pub} kaijuan-monthly-{args.year}-{mm}.md  ({len(items)} 期)")
        written += 1
    print(f"\n共生成 {written} 篇月度推文。")

if __name__ == "__main__":
    main()
