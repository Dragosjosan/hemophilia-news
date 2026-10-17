import { createContext, useContext } from 'react'
import type { Topic } from '../api/types.ts'

export type TopicsState =
  | { status: 'loading' }
  | { status: 'error'; error: Error }
  | { status: 'ready'; topics: Topic[] }

export const TopicsContext = createContext<TopicsState>({ status: 'loading' })

export function useTopics(): TopicsState {
  return useContext(TopicsContext)
}
