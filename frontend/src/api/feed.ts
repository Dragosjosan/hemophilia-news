import { getJson } from './client.ts'
import type { FeedFilters, FeedPage, Topic } from './types.ts'

export function fetchFeedPage(
  filters: FeedFilters,
  cursor: string | null,
  signal?: AbortSignal,
): Promise<FeedPage> {
  return getJson<FeedPage>('/items', { ...filters, cursor }, signal)
}

export function fetchTopics(signal?: AbortSignal): Promise<Topic[]> {
  return getJson<Topic[]>('/topics', {}, signal)
}
