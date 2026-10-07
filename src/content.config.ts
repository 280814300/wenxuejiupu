import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// ───────────────────────────────────────────────────────────
// 文学酒铺 · Content Collections 严格 Schema
// 三个栏目：ai（AI应用落地）/ tools（软件分享）/ resources（资源合集）
// slug 强制：小写英文 + 短横线（由正则保证，写入即校验）
// ───────────────────────────────────────────────────────────

// 全站通用 slug 规则：小写字母数字，段间单短横线，首尾无横线
const slugRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

// 共享基础字段（各栏目在 base 之上 merge 自己的专属字段）
const base = z.object({
  // 标题：2~120 字
  title: z
    .string()
    .min(2, '标题至少 2 个字')
    .max(120, '标题不超过 120 字'),

  // 摘要：用于 meta description 与卡片，10~200 字
  description: z
    .string()
    .min(10, '摘要至少 10 个字')
    .max(200, '摘要不超过 200 字'),

  // 永久 URL slug：小写英文 + 短横线，由正则强校验
  slug: z
    .string()
    .regex(slugRegex, 'slug 必须为小写英文 + 短横线，例：claude-china-guide-2026'),

  // 发布日期（frontmatter 写 YYYY-MM-DD 字符串，自动转 Date）
  pubDate: z.coerce.date(),

  // 更新日期（可选）
  updatedDate: z.coerce.date().optional(),

  // 标签
  tags: z.array(z.string()).default([]),

  // 作者（默认站名）
  author: z.string().default('文学酒铺'),

  // 封面图（可选，本地路径或绝对 URL）
  cover: z.string().optional(),

  // 草稿开关：true 则不发布
  draft: z.boolean().default(false),
});

// ai —— AI 应用落地教学
const ai = base.merge(
  z.object({
    // 难度分级
    level: z.enum(['入门', '进阶', '精通']).default('入门'),
    // 相关软件名（可选）
    software: z.string().optional(),
  })
);

// tools —— 软件分享（开源工具 + 工具清单 合并）
// repo / license 仅开源工具需要，清单类无此字段，故设为可选；
// summary 为清单类摘要，工具类可忽略，亦设为可选。
const tools = base.merge(
  z.object({
    // 仓库 / 官网地址（开源工具填写；清单类可省略）
    repo: z
      .string()
      .url('请填写合法 URL，如 https://github.com/...')
      .optional(),
    // 开源协议 / 许可说明
    license: z.string().optional(),
    // 支持平台
    platforms: z
      .array(z.enum(['Windows', 'macOS', 'Linux', 'Android', 'iOS', 'Web']))
      .default([]),
    // 清单类摘要（可选）
    summary: z.string().max(300).optional(),
  })
);

// resources —— 资源合集（原网盘资源）
const resources = base.merge(
  z.object({
    // 资源名称
    resource: z.string().min(1, '请填写资源名称'),
    // 网盘链接（必须合法 URL）
    panUrl: z.string().url('请填写合法网盘 URL'),
    // 提取码（可选）
    extractCode: z.string().max(20).optional(),
    // 体积（可选，如 "48GB"）
    size: z.string().max(30).optional(),
  })
);

// humanities —— 人文记录（自由写作，仅需基础字段）
const humanities = base;

export const collections = {
  ai: defineCollection({
    loader: glob({ pattern: '**/*.md', base: './src/content/ai' }),
    schema: ai,
  }),
  tools: defineCollection({
    loader: glob({ pattern: '**/*.md', base: './src/content/tools' }),
    schema: tools,
  }),
  resources: defineCollection({
    loader: glob({ pattern: '**/*.md', base: './src/content/resources' }),
    schema: resources,
  }),
  humanities: defineCollection({
    loader: glob({ pattern: '**/*.md', base: './src/content/humanities' }),
    schema: humanities,
  }),
};
