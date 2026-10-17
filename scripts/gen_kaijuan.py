#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""开卷八分钟批量生成器（续推管线）。
读取 scripts/kaijuan_pending.json，跳过已发布（磁盘已有同名 slug 文件）与无链接项，
按 5 篇/天节奏生成标准格式文章，注入真实夸克链接。

用法:
  python3 scripts/gen_kaijuan.py --start-date 2026-10-18 --count 5
  python3 scripts/gen_kaijuan.py --start-date 2026-10-18 --count 5 --dry-run
"""
import json, os, re, sys, argparse, datetime
from pypinyin import lazy_pinyin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PENDING = os.path.join(ROOT, "scripts", "kaijuan_pending.json")
HUMANITIES = os.path.join(ROOT, "src", "content", "humanities")
PER_DAY = 5

# 地区前缀 -> 中文标签
REGION = {
    "美": "美国", "英": "英国", "德": "德国", "法": "法国",
    "台": "台湾", "港": "香港", "日": "日本", "俄": "俄国",
    "英.出版社": "英国出版机构", "英.出版": "英国出版机构",
}
# 书名 -> 类型标签（用于 tags 第二维）
GENRE = {
    "光的故事": "科普", "永经堂": "人文", "新式历书": "人文",
    "中国方术考": "社科", "天学真原": "科学史",
}
# 书名 -> 「关于」段落（诚实、可考据，不杜撰情节）
SUBJECT_HINTS = {
    "光的故事": "《光的故事》是美国物理学家 Sidney Perkowitz 写给大众的科普书，从“光到底是什么”讲起，串起人类认识光、利用光的历史。",
    "永经堂": "《永经堂》关联香港著名的通胜（黄历）世家蔡伯励，这本书围绕传统历法、择日与民俗信仰展开，是了解香港民间时间观的一扇窗。",
    "新式历书": "《新式历书》是一本谈历法与时间的通书，由香港一众玄学研究者编撰，延续了民间对黄历、择日的实用需求。",
    "中国方术考": "《中国方术考》是李零系统梳理中国古代方术——包括占卜、天文、堪舆、厌胜等——的考据之作，把常被轻忽的“方术”放回学术视野。",
    "天学真原": "《天学真原》是江晓原关于中国传统“天学”（古代天文历法体系）的研究专著，揭示古人如何以星象理解宇宙与皇权。",
}

TITLE_OVERRIDE = {  # 特殊书名校正（与历史约定一致）
    "梁文道谈金庸武侠": "金庸武侠",
    "于丹《论语》心得": "论语心得",
    "No Smoking": "No Smoking",
}


def clean_title_author(title, author):
    t = title.replace("[", "").replace("]", "")
    # 作者保留 ] 以便 clean_author_region 解析 “地区]姓名” 分隔符
    a = (author or "").replace("[", "")
    # 书名里可能嵌了作者，如 "中国方术考.李零"
    if (not a) and "." in t:
        parts = t.split(".")
        cand = parts[-1].strip()
        if 0 < len(cand) <= 8 and len(parts) > 1:
            t = ".".join(parts[:-1]).strip()
            a = cand
    return t.strip(), a.strip()


def clean_author_region(a):
    """返回 (region_label, name)。region_label 可能为空。"""
    if not a:
        return "", ""
    m = re.match(r"^([\u4e00-\u9fff]+(?:\.[\u4e00-\u9fff]+)?)\](.*)$", a)
    if m:
        region = m.group(1)
        name = m.group(2).strip()
        label = REGION.get(region, region)
        return label, name
    return "", a.strip()


def slugify(title):
    if title in TITLE_OVERRIDE:
        base = TITLE_OVERRIDE[title]
    else:
        py = lazy_pinyin(title, style=0)  # 无声调
        base = "-".join([w for w in py if w])
    base = re.sub(r"[^a-z0-9\-]+", "-", base.lower()).strip("-")
    return base


def unique_slug(base):
    slug = base
    i = 2
    while os.path.exists(os.path.join(HUMANITIES, f"kaijuan-youyi-{slug}.md")):
        slug = f"{base}-{i}"
        i += 1
    return slug


def published_titles():
    """从已有 kaijuan 文章 frontmatter 提取已发布书名（去重依据，与 slug 拼写无关）。"""
    s = set()
    if not os.path.isdir(HUMANITIES):
        return s
    for fn in os.listdir(HUMANITIES):
        if not fn.startswith("kaijuan-youyi-") or not fn.endswith(".md"):
            continue
        try:
            txt = open(os.path.join(HUMANITIES, fn), encoding="utf-8").read(600)
        except Exception:
            continue
        m = re.search(r"title:\s*开卷八分钟｜《([^》]+)》", txt)
        if m:
            s.add(m.group(1).strip())
    return s


def build_md(item, pubdate, slug):
    title, raw_author = clean_title_author(item["title"], item.get("author", ""))
    region_label, name = clean_author_region(raw_author)
    if region_label and "出版机构" not in region_label:
        author_disp = f"{name}（{region_label}）"
    elif region_label:
        author_disp = f"{name}（{region_label}）"
    else:
        author_disp = name or "梁文道（讲述）"

    genre = GENRE.get(title, "人文")
    about = SUBJECT_HINTS.get(
        title,
        f"《{title}》是{author_disp}的作品。梁文道在《开卷八分钟》里用八分钟，带听众走近这本书，聊聊它为什么值得一读。",
    )
    url = item["url"]
    pub_str = pubdate.isoformat()

    md = f"""---
title: 开卷八分钟｜《{title}》：梁文道八分钟讲透一本书 · 音频播客听书
description: {author_disp}的《{title}》——梁文道在《开卷八分钟》里用八分钟讲透的一本书。本篇把音频核心内容写成图文，方便通勤、睡前用耳朵重读经典。｜梁文道《开卷八分钟》音频听书
slug: kaijuan-youyi-{slug}
pubDate: {pub_str}
tags: ["开卷八分钟", "{genre}", "读书"]
author: 文学酒铺
draft: false
---

> 本文整理自**梁文道《开卷八分钟》**音频听书专栏，本期书单为 **{author_disp}《{title}》**。梁文道在《开卷八分钟》里用八分钟讲透一本书，本篇把音频核心内容写成图文，方便你通勤、睡前用耳朵重读经典，也可一键转存夸克网盘音频随时听。

## 📖 书籍信息

| 项目 | 内容 |
| --- | --- |
| 书名 | {title} |
| 作者 | {author_disp} |
| 出版年 | 陆续补充 |
| 页数 | 陆续补充 |
| ISBN | 陆续补充 |

**常见搜索词（电商 / 豆瓣）**：{title}、{name or title}、{genre}、正版、经典
**在线试听**：本期音频已上线，见下方「试听与转存」转存夸克网盘随时听。

关于《{title}》

{about}

梁文道为什么推荐《{title}》

梁文道做《开卷八分钟》，本就不是要替读者读完一本书，而是把一本书“翻开放在桌面上”：哪些地方值得停留，哪些说法值得商榷，他都用自己的阅读经验带出来。读《{title}》这期，他同样延续这种“引路”的姿态——不替你下结论，只帮你把门推开。

《{title}》适合谁阅读

对这本书主题感兴趣的普通读者；想用碎片时间重拾阅读习惯的人；喜欢听梁文道“讲书”式导览的听众。

<div class="excerpt-box">
  <div class="excerpt-box__head">📜 内容亮点</div>
  <div class="excerpt-item">
    <p class="excerpt-text">梁文道用八分钟带读《{title}》，把厚书读薄，给出可落地的阅读入口。</p>
  </div>
  <div class="excerpt-item">
    <p class="excerpt-text">从音频到图文，通勤、睡前都能用耳朵或眼睛重读经典。</p>
  </div>
  <div class="excerpt-item">
    <p class="excerpt-text">一键转存夸克网盘音频，随时随地听梁文道讲书。</p>
  </div>
</div>

## 📥 试听与转存

本集完整音频已分享至夸克网盘，点下方链接即可**一键试听 / 转存**到你的夸克网盘，随时随地听梁文道讲书。

- 夸克网盘（本集音频）：[《{title}》 · 一键试听 / 转存]({url})

## ❓ 常见问题（FAQ）

<div class="faq-item">
  <div class="faq-q">Q1：《{title}》主要讲什么？</div>
  <div class="faq-a">{about}</div>
</div>
<div class="faq-item">
  <div class="faq-q">Q2：梁文道为什么推荐《{title}》？</div>
  <div class="faq-a">梁文道做《开卷八分钟》是“引路”而非“替读”：把书翻开放在桌面上，指出值得停留与商榷之处，帮你把门推开。</div>
</div>
<div class="faq-item">
  <div class="faq-q">Q3：《{title}》适合谁阅读？</div>
  <div class="faq-a">对本书主题感兴趣的普通读者；想用碎片时间重拾阅读习惯的人；喜欢听梁文道“讲书”式导览的听众。</div>
</div>
<div class="faq-item">
  <div class="faq-q">Q4：《{title}》是什么类型的书？</div>
  <div class="faq-a">《{title}》属于「{genre}」类读物，可在文学酒铺按题材检索同类讲书。</div>
</div>
"""
    return md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start-date", required=True, help="首日发布日期 YYYY-MM-DD")
    ap.add_argument("--count", type=int, default=PER_DAY)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.load(open(PENDING))
    have = [x for x in data if x.get("has_link") and x.get("url")]
    done = published_titles()  # 已发布书名集合
    # 已发布检测：按书名去重（与 slug 拼写无关）
    todo = []
    for x in have:
        t, _ = clean_title_author(x["title"], x.get("author", ""))
        if t in done:
            continue  # 已发布，跳过
        base = slugify(t)
        slug = unique_slug(base)
        todo.append((x, slug))

    start = datetime.date.fromisoformat(args.start_date)
    out = []
    for i, (item, slug) in enumerate(todo[: args.count]):
        pub = start + datetime.timedelta(days=i // PER_DAY)
        md = build_md(item, pub, slug)
        out.append((slug, pub, item, md))

    for slug, pub, item, md in out:
        if args.dry_run:
            print(f"[dry] {pub}  kaijuan-youyi-{slug}.md  ({item['title']})")
        else:
            path = os.path.join(HUMANITIES, f"kaijuan-youyi-{slug}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"[ok] {pub}  kaijuan-youyi-{slug}.md  ({item['title']})")

    print(f"\n拟生成 {len(out)} 篇；剩余待生成（去重后）{len(todo) - len(out)} 篇。")


if __name__ == "__main__":
    main()
