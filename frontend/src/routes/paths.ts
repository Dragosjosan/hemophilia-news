import type { FeedFilters } from '../api/types.ts'

// Single source of truth for URLs; use these in route config and links.
export const paths = {
  home: '/',
} as const

/** The feed is one page; topic and tag filters live in the query string. */
export function feedUrl({ topic, tag }: FeedFilters = {}): string {
  const params = new URLSearchParams()
  if (topic) params.set('topic', topic)
  if (tag) params.set('tag', tag)
  const qs = params.toString()
  return qs ? `${paths.home}?${qs}` : paths.home
}
