// astro.config.mjs
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://encoding-tools.vercel.app', // ← 必须是你实际的 Vercel 域名
  integrations: [sitemap()],
}); 