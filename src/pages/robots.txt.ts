import type { APIRoute } from 'astro';
import { SITE } from '../consts';

export const GET: APIRoute = () => {
  const body = `User-agent: *\nAllow: /\nSitemap: https://${SITE.domain}/sitemap-index.xml\n`;
  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
