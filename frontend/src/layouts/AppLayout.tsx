import { Outlet } from 'react-router'
import SiteHeader from './SiteHeader.tsx'
import './AppLayout.css'

function AppLayout() {
  return (
    <>
      <SiteHeader />
      <main className="app-main container section">
        <Outlet />
      </main>
    </>
  )
}

export default AppLayout
