import './AsyncState.css'

export function LoadingState({ label = 'Loading' }: { label?: string }) {
  return (
    <div className="async-state" role="status">
      <span className="spinner" aria-hidden="true" />
      <span className="text-muted">{label}…</span>
    </div>
  )
}

export function ErrorState({ title, error }: { title: string; error: Error }) {
  return (
    <div className="alert alert-danger" role="alert">
      <span className="alert-icon" aria-hidden="true">
        !
      </span>
      <div className="alert-content">
        <h3 className="alert-title">{title}</h3>
        <p>{error.message}</p>
      </div>
    </div>
  )
}

export function EmptyState({ title, copy }: { title: string; copy?: string }) {
  return (
    <div className="empty-state">
      <h3 className="empty-state-title">{title}</h3>
      {copy && <p className="empty-state-copy">{copy}</p>}
    </div>
  )
}
