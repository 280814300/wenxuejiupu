#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""开卷八分钟 · 自动发布脚本
按日期顺序取「仍处于草稿、且 pubDate 在 2007-01」的文章，每批发布 N 篇：
- 将 draft: true -> draft: false
- 将 pubDate 改为脚本运行当天（发布当日，而非 2007 节目日期）
仅改 frontmatter 两行，正文/导航保持不变（导航仍用原始 2007 期序）。
用法: python3 publish_batch.py [--batch 5] [--date YYYY-MM-DD] [--dry-run]
"""
import os, re, sys, subprocess, glob, argparse
from datetime import date

OUT = "/Users/weixing/WorkBuddy/公司网站/wenxuejiupu/src/content/humanities"
TARGET_YEAR_MONTH = "2007-01"  # 只处理 2007-01 这批

def parse_frontmatter(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return None, txt, None
    fm = m.group(1)
    body = txt[m.end():]
    pub = re.search(r"(?m)^pubDate:\s*(.+)$", fm)
    dr = re.search(r"(?m)^draft:\s*(.+)$", fm)
    return fm, body, (pub.group(1).strip() if pub else None, dr.group(1).strip() if dr else None)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=5)
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(OUT, "kaijuan-youyi-*.md")))
    candidates = []
    for f in files:
        fm, body, meta = parse_frontmatter(f)
        if meta is None:
            continue
        pub, dr = meta
        if not pub or not pub.startswith(TARGET_YEAR_MONTH):
            continue
        if dr and dr.lower() == "false":
            continue  # 已发布，跳过
        candidates.append((pub, f))
    # 按原始 pubDate 升序（即 2007-01 期序）
    candidates.sort(key=lambda x: x[0])

    batch = candidates[:args.batch]
    if not batch:
        print(f"[publish_batch] 没有待发布的 2007-01 草稿文章了。")
        return

    print(f"[publish_batch] 目标日={args.date}  本批 {len(batch)} 篇:")
    changed = []
    modified = []
    for pub, f in batch:
        txt = open(f, encoding="utf-8").read()
        txt = re.sub(r"(?m)^pubDate:.*$", f"pubDate: {args.date}", txt, count=1)
        txt = re.sub(r"(?m)^draft:.*$", "draft: false", txt, count=1)
        if not args.dry_run:
            open(f, "w", encoding="utf-8").write(txt)
        changed.append((os.path.basename(f), pub))
        modified.append(f)
        print(f"  - {os.path.basename(f)}  (原 {pub} -> 发布 {args.date})")

    if args.dry_run:
        print("[publish_batch] DRY-RUN，未写入。")
        return

    # 本地提交（仅 add 本次改动的文章文件，绝不 git add -A，
    # 避免把未提交的主题/其它改动卷进提交并随部署 push 出去）
    try:
        repo = os.path.dirname(OUT) + "/../.."
        if modified:
            subprocess.run(["git", "-C", repo, "add", *modified],
                           check=True, capture_output=True)
        msg = f"chore: 自动发布开卷八分钟 2007-01 批次 {args.date} ({len(changed)} 篇)"
        subprocess.run(["git", "-C", repo, "commit", "-m", msg],
                       check=True, capture_output=True)
        print("[publish_batch] 已 git commit（仅文章）。")
    except Exception as e:
        print(f"[publish_batch] git 提交跳过/失败: {e}")

    print(f"[publish_batch] 完成。剩余 2007-01 草稿: {max(0, len(candidates)-len(batch))} 篇。")

if __name__ == "__main__":
    main()
