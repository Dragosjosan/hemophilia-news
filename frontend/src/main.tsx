import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import '@design/fonts.css'
import '@design/tokens.css'
import '@design/elements.css'
import './app/global.css'
import App from './app/App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
