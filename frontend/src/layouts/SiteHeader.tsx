import { Link, useSearchParams } from 'react-router'
import { useTopics } from '../app/topicsContext.ts'
import { feedUrl, paths } from '../routes/paths.ts'
import './SiteHeader.css'

function SiteHeader() {
  const topicsState = useTopics()
  const [searchParams] = useSearchParams()
  const activeTopic = searchParams.get('topic')

  return (
    <header className="site-header">
      <div className="container site-header-inner">
        <Link to={paths.home} className="site-brand">
          News
        </Link>
        {topicsState.status === 'ready' && (
          <nav className="site-nav" aria-label="Topics">
            {topicsState.topics.map((topic) => (
              <Link
                key={topic.slug}
                to={feedUrl({ topic: topic.slug })}
                className="site-nav-link"
                aria-current={activeTopic === topic.slug ? 'page' : undefined}
              >
                {topic.name}
              </Link>
            ))}
          </nav>
        )}
      </div>
    </header>
  )
}

export default SiteHeader
