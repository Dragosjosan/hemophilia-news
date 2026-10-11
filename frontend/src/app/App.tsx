import { RouterProvider } from 'react-router'
import { router } from '../routes/router.tsx'
import TopicsProvider from './TopicsProvider.tsx'

function App() {
  return (
    <TopicsProvider>
      <RouterProvider router={router} />
    </TopicsProvider>
  )
}

export default App
