// astro.config.mjs
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://encoding-tools.vercel.app', // 替换为你的 Vercel 域名
  integrations: [sitemap()],
});