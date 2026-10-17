#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解析夸克「分享结果导出」CSV -> scripts/kaijuan_pending.json
提取每集: date(YYMMDD) / title / author / url / status
跳过非剧集文件(AlbumArtSmall.jpg / Folder.jpg 等) 与共享失败的集。
"""
import csv, re, json, sys, os

CSVS = [
    "/Users/weixing/Downloads/分享结果导出-1792249713062.csv",
    "/Users/weixing/Downloads/分享结果导出-1792249732396.csv",
    "/Users/weixing/Downloads/分享结果导出-1792249747106.csv",
    "/Users/weixing/Downloads/分享结果导出-1792249760339.csv",
]
OUT = os.path.join(os.path.dirname(__file__), "kaijuan_pending.json")

def parse_name(name: str):
    """070201.[图解人体使用手册].[英.出版社]De Agostini.mp3 -> (date, title, author)"""
    if not name.lower().endswith(".mp3"):
        return None
    body = name[:-4]
    m = re.match(r"^(\d{6})\.(.*)$", body)
    if not m:
        return None
    date = m.group(1)
    rest = m.group(2)
    if ".[" in rest:
        title_raw, author = rest.split(".[", 1)
        title = title_raw.lstrip("[")
    else:
        title = rest.lstrip("[")
        author = ""
    # 清洗书名/作者里可能的残余方括号噪声
    title = title.strip()
    author = author.strip()
    return date, title, author

def parse_addr(addr: str):
    if not addr:
        return ""
    m = re.search(r"链接：(https?://[^\s\"]+)", addr)
    return m.group(1) if m else ""

rows = []
seen = set()
for path in CSVS:
    if not os.path.exists(path):
        print(f"[warn] 缺失: {path}")
        continue
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            status = (r.get("创建分享状态") or "").strip()
            name = (r.get("分享名") or "").strip()
            parsed = parse_name(name)
            if not parsed:
                # 非剧集文件（封面图等），跳过
                continue
            date, title, author = parsed
            url = parse_addr(r.get("分享地址") or "")
            key = (date, title)
            if key in seen:
                continue
            seen.add(key)
            rows.append({
                "date": date,
                "title": title,
                "author": author,
                "url": url,
                "status": status,
                "has_link": bool(url),
            })

# 按日期升序
rows.sort(key=lambda x: x["date"])
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

ok = [r for r in rows if r["status"] == "成功"]
fail = [r for r in rows if r["status"] != "成功"]
linked = [r for r in ok if r["has_link"]]
print(f"总集数: {len(rows)} | 成功: {len(ok)} | 失败: {len(fail)} | 成功且有链接: {len(linked)}")
print(f"日期跨度: {rows[0]['date']} ~ {rows[-1]['date']}")
from collections import Counter
c = Counter(r["date"][:4] + "-" + r["date"][4:6] for r in ok)
for k in sorted(c):
    print(f"  {k}: {c[k]} 期")
print(f"写出: {OUT}")
