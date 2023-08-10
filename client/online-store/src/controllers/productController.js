import axios from 'axios'

export const getCategorys = async () => await axios.get(`${import.meta.env.VITE_API_URL}/catalog`)

export function sortItems(catalog) {
  for (const [key, item] of Object.entries(catalog.items)) {
    if (!catalog.categories[item.category_id].product_types[item.product_type_id].items)
      catalog.categories[item.category_id].product_types[item.product_type_id].items = {}

    catalog.categories[item.category_id].product_types[item.product_type_id].items = {
      [key]: item,
    }
  }
  return catalog
}
