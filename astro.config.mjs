import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// https://wenxuejiupu.com — 纯静态输出，部署目标 Cloudflare Pages
// 强制要求：trailingSlash 'always' + build.format 'directory'
// 文章 URL 永久结构：/栏目/年份/slug/  例：/ai/2026/claude-china-guide-2026/
export default defineConfig({
  site: 'https://wenxuejiupu.com',
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  integrations: [
    tailwind(),
    sitemap(),
  ],
  // 纯静态，无 SSR / 无适配器
  output: 'static',
});
