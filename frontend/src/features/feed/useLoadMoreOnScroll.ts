import { useEffect, useRef } from 'react'

/** Calls `onVisible` when the returned sentinel element scrolls near the viewport. */
export function useLoadMoreOnScroll<T extends Element>(onVisible: () => void, enabled: boolean) {
  const sentinel = useRef<T | null>(null)

  useEffect(() => {
    const node = sentinel.current
    if (!node || !enabled) return
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries.some((entry) => entry.isIntersecting)) onVisible()
      },
      { rootMargin: '400px 0px' },
    )
    observer.observe(node)
    return () => observer.disconnect()
  }, [onVisible, enabled])

  return sentinel
}
