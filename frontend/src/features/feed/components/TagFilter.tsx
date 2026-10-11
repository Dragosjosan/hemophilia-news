import { useTopics } from '../../../app/topicsContext.ts'
import TagChip from '../../../components/TagChip/TagChip.tsx'
import { feedUrl } from '../../../routes/paths.ts'
import './TagFilter.css'

type TagFilterProps = {
  topic?: string
  tag?: string
}

/** Tag chips for the current topic (or every topic), taken from the API's tag list. */
function TagFilter({ topic, tag }: TagFilterProps) {
  const topicsState = useTopics()
  if (topicsState.status !== 'ready') return null

  const scope = topic ? topicsState.topics.filter((t) => t.slug === topic) : topicsState.topics
  const tags = [...new Set(scope.flatMap((t) => t.tags))].sort()
  if (tags.length === 0) return null

  return (
    <nav className="tag-filter" aria-label="Filter by tag">
      <TagChip label="all" to={feedUrl({ topic })} active={!tag} />
      {tags.map((name) => (
        <TagChip key={name} label={name} to={feedUrl({ topic, tag: name })} active={tag === name} />
      ))}
    </nav>
  )
}

export default TagFilter
