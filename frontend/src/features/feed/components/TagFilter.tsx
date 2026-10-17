import { Link } from 'react-router'
import { feedUrl } from '../../../routes/paths.ts'
import './TagFilter.css'

type TagFilterProps = {
  topic?: string
  tag?: string
}

function TagFilter({ topic, tag }: TagFilterProps) {
  if (!tag) return null

  return (
    <div className="tag-filter">
      <span>tagged #{tag}</span>
      <Link to={feedUrl({ topic })} className="tag-filter-clear">
        clear
      </Link>
    </div>
  )
}

export default TagFilter
