import { fileURLToPath } from 'node:url'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// josanai-design is a submodule at the repo root, outside the frontend package.
const designDir = fileURLToPath(new URL('../josanai-design', import.meta.url))

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: { '@design': designDir },
  },
  server: {
    fs: { allow: ['.', designDir] },
    // news-api (FastAPI). In production nginx routes /api the same way.
    proxy: {
      '/api': process.env.NEWS_API_URL ?? 'http://localhost:8000',
    },
  },
})
