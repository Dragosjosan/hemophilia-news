import type { FeedItem } from '../../../api/types.ts'
import ItemRow from './ItemRow.tsx'
import './ItemList.css'

function ItemList({ items }: { items: FeedItem[] }) {
  return (
    <ol className="item-list">
      {items.map((item, index) => (
        <ItemRow key={item.id} item={item} rank={index + 1} />
      ))}
    </ol>
  )
}

export default ItemList
