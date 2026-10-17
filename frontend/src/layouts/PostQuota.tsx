import type { Topic } from '../api/types.ts'
import './PostQuota.css'

const DAILY_CAP = 5

function PostQuota({ topics }: { topics: Topic[] }) {
  if (topics.length === 0) return null

  return (
    <span className="post-quota" title={`Posts today per topic · ${DAILY_CAP} max`}>
      <span className="post-quota-label">posts today</span>
      {topics.map((topic) => {
        const used = Math.min(DAILY_CAP, Math.max(0, DAILY_CAP - topic.remaining_today))
        return (
          <span key={topic.slug} className="post-quota-topic">
            <span>{topic.slug}</span>
            <span className="post-quota-slots" aria-hidden="true">
              {Array.from({ length: DAILY_CAP }, (_, i) => (
                <span key={i} className="post-quota-slot" data-used={i < used} />
              ))}
            </span>
            <span className="post-quota-count">
              {used}/{DAILY_CAP}
            </span>
          </span>
        )
      })}
    </span>
  )
}

export default PostQuota
