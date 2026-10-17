import { fileURLToPath } from 'node:url'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

const designDir = fileURLToPath(new URL('../josanai-design', import.meta.url))

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: { '@design': designDir },
  },
  server: {
    fs: { allow: ['.', designDir] },
    proxy: {
      '/api': process.env.NEWS_API_URL ?? 'http://localhost:8000',
    },
  },
})
