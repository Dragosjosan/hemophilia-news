// Interim types mirroring DESIGN.md ("The Contract", "Feed Ranking").
// Replace with the generated schema.d.ts once `make gen-types` exists.

export type Topic = {
  slug: string
  name: string
  tags: string[]
  remaining_today: number
}

export type FeedItem = {
  id: number
  title: string
  url: string
  domain: string
  topic: string
  tags: string[]
  score: number
  comment_count: number
  /** Username for human posts; null for agent posts (Product Rule: no "by" line). */
  submitted_by: string | null
  created_at: string
}

export type FeedPage = {
  items: FeedItem[]
  next_cursor: string | null
}

export type FeedFilters = {
  topic?: string
  tag?: string
}
