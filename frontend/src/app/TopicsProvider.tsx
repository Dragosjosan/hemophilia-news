import { useEffect, useState, type ReactNode } from 'react'
import { fetchTopics } from '../api/feed.ts'
import { TopicsContext, type TopicsState } from './topicsContext.ts'

function TopicsProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<TopicsState>({ status: 'loading' })

  useEffect(() => {
    const controller = new AbortController()
    fetchTopics(controller.signal)
      .then((topics) => setState({ status: 'ready', topics }))
      .catch((error: Error) => {
        if (!controller.signal.aborted) setState({ status: 'error', error })
      })
    return () => controller.abort()
  }, [])

  return <TopicsContext value={state}>{children}</TopicsContext>
}

export default TopicsProvider
