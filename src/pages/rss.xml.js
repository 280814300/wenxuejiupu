import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../consts';

export async function GET(context) {
  const columns = ['ai', 'tools', 'resources', 'humanities'];
  let items = [];
  for (const col of columns) {
    const entries = (await getCollection(col)).filter((e) => !e.data.draft);
    for (const e of entries) {
      items.push({
        title: e.data.title,
        description: e.data.description,
        pubDate: e.data.pubDate,
        link: `/${col}/${e.data.slug}/`,
      });
    }
  }
  items.sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime());

  return rss({
    title: SITE.title,
    description: SITE.description,
    site: context.site,
    items,
    customData: `<language>zh-cn</language>`,
  });
}
