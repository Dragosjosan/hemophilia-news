import { useCallback, useEffect, useRef, useState } from 'react'
import { fetchFeedPage } from '../../api/feed.ts'
import type { FeedFilters, FeedItem } from '../../api/types.ts'

type FeedState = {
  items: FeedItem[]
  nextCursor: string | null
  status: 'loading' | 'idle' | 'error'
  error: Error | null
}

const INITIAL: FeedState = { items: [], nextCursor: null, status: 'loading', error: null }

export function useFeed({ topic, tag }: FeedFilters) {
  const [state, setState] = useState<FeedState>(INITIAL)
  const request = useRef<AbortController | null>(null)

  const filterKey = `${topic ?? ''}|${tag ?? ''}`
  const [loadedKey, setLoadedKey] = useState(filterKey)
  if (loadedKey !== filterKey) {
    setLoadedKey(filterKey)
    setState(INITIAL)
  }

  const fetchPage = useCallback(
    (cursor: string | null) => {
      request.current?.abort()
      const controller = new AbortController()
      request.current = controller

      fetchFeedPage({ topic, tag }, cursor, controller.signal)
        .then((page) =>
          setState((prev) => ({
            items: cursor === null ? page.items : [...prev.items, ...page.items],
            nextCursor: page.next_cursor,
            status: 'idle',
            error: null,
          })),
        )
        .catch((error: Error) => {
          if (!controller.signal.aborted) setState((prev) => ({ ...prev, status: 'error', error }))
        })
    },
    [topic, tag],
  )

  useEffect(() => {
    fetchPage(null)
    return () => request.current?.abort()
  }, [fetchPage])

  const { status, nextCursor } = state
  const loadMore = useCallback(() => {
    if (status === 'loading' || !nextCursor) return
    setState((prev) => ({ ...prev, status: 'loading', error: null }))
    fetchPage(nextCursor)
  }, [status, nextCursor, fetchPage])

  return { ...state, hasMore: nextCursor !== null, loadMore }
}
