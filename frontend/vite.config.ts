import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // news-api (FastAPI). In production nginx routes /api the same way.
    proxy: {
      '/api': process.env.NEWS_API_URL ?? 'http://localhost:8000',
    },
  },
})
