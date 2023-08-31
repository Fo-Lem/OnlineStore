import { $user } from '../axiosInstance/instance.ts'

export interface catalogItems {
  [key: string]: {
    art: string
    id: number
    id_1: number
    category_id: number
    product_type_id: number
    hero_id: number
    img_path: string
    name: string
    size: string
    price: number
    description: string
  }
}
export interface catalogHeroes {
  [key: string]: {
    id: number
    name: string
  }
}
export interface type {

  id: number
  name: string
  items: catalogItems

}
export interface catalogTypes {
  [key: string]: type
}
export interface category {
  id: number
  name: number
  cover_path: string
  product_types: catalogTypes

}
export interface catalogCategories {
  [key: string]: category
}
export interface catalog {
  categories: catalogCategories
  heroes: catalogHeroes
  items: catalogItems
}

export async function getCategorys(): Promise<catalog> {
  return await $user.get<catalog>('/catalog')
    .then((res) => {
      return sortItems(res.data)
    })
    .catch((error) => {
      // console.log(error)
      return error
    })
}

export function sortItems(catalog: catalog) {
  for (const [key, item] of Object.entries(catalog.items)) {
    if (!catalog.categories[item.category_id].product_types[item.product_type_id].items)
      catalog.categories[item.category_id].product_types[item.product_type_id].items = {}

    catalog.categories[item.category_id].product_types[item.product_type_id].items = {
      [key]: item,
    }
  }
  return catalog
}
