import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';

const columns = ['ai', 'tools', 'resources', 'humanities'] as const;
const columnName: Record<string, string> = {
  ai: 'AI 应用',
  tools: '软件分享',
  resources: '资源合集',
  humanities: '人文记录',
};

// 构建期生成全站已发布文章的轻量索引（静态托管友好，零运行时依赖）
export const GET: APIRoute = async () => {
  const items: Record<string, any>[] = [];
  for (const col of columns) {
    const entries = (await getCollection(col)).filter((e) => !e.data.draft);
    for (const e of entries) {
      items.push({
        title: e.data.title,
        description: e.data.description,
        tags: e.data.tags,
        column: col,
        columnName: columnName[col],
        slug: e.data.slug,
        url: `/${col}/${e.data.slug}/`,
        pubDate: e.data.pubDate.toISOString().slice(0, 10),
      });
    }
  }
  items.sort((a, b) => b.pubDate.localeCompare(a.pubDate));
  return new Response(JSON.stringify(items), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
