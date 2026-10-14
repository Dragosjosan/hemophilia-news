import { Outlet } from 'react-router'
import SiteFooter from './SiteFooter.tsx'
import SiteHeader from './SiteHeader.tsx'
import './AppLayout.css'

function AppLayout() {
  return (
    <div className="app-shell">
      <SiteHeader />
      <main className="app-main">
        <Outlet />
      </main>
      <SiteFooter />
    </div>
  )
}

export default AppLayout
