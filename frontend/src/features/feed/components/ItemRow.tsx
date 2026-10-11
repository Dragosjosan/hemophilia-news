import type { FeedItem } from '../../../api/types.ts'
import TagChip from '../../../components/TagChip/TagChip.tsx'
import { pluralize, timeAgo } from '../../../lib/format.ts'
import { feedUrl } from '../../../routes/paths.ts'
import './ItemRow.css'

type ItemRowProps = {
  item: FeedItem
  rank: number
}

function ItemRow({ item, rank }: ItemRowProps) {
  return (
    <li className="item-row">
      <span className="item-rank">{rank}.</span>

      {/* Voting is wired up in a later step. */}
      <div className="item-votes">
        <button type="button" className="item-vote" aria-label={`Upvote ${item.title}`} disabled>
          ▲
        </button>
        <button type="button" className="item-vote" aria-label={`Downvote ${item.title}`} disabled>
          ▼
        </button>
      </div>

      <div className="item-body">
        <div className="item-headline">
          <a className="item-title" href={item.url} rel="noopener noreferrer">
            {item.title}
          </a>
          <span className="item-domain">({item.domain})</span>
        </div>

        <div className="item-meta">
          <span>{pluralize(item.score, 'point')}</span>
          {item.submitted_by && <span>by {item.submitted_by}</span>}
          <time dateTime={item.created_at} title={new Date(item.created_at).toLocaleString()}>
            {timeAgo(item.created_at)}
          </time>
          <span>{pluralize(item.comment_count, 'comment')}</span>
          {item.tags.map((tag) => (
            <TagChip key={tag} label={tag} to={feedUrl({ topic: item.topic, tag })} />
          ))}
        </div>
      </div>
    </li>
  )
}

export default ItemRow
