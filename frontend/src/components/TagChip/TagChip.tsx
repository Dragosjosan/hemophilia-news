import { Link, type To } from 'react-router'
import './TagChip.css'

type TagChipProps = {
  label: string
  to: To
  active?: boolean
}

function TagChip({ label, to, active = false }: TagChipProps) {
  return (
    <Link to={to} className="tag-chip" aria-current={active ? 'true' : undefined}>
      {label}
    </Link>
  )
}

export default TagChip
