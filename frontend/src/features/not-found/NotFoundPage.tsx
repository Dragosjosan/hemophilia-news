import { Link } from 'react-router'
import { paths } from '../../routes/paths.ts'

function NotFoundPage() {
  return (
    <div className="empty-state">
      <h1 className="empty-state-title">Page not found.</h1>
      <p className="empty-state-copy">The page you are looking for does not exist.</p>
      <div className="empty-state-actions">
        <Link to={paths.home} className="btn">
          Back to home
        </Link>
      </div>
    </div>
  )
}

export default NotFoundPage
