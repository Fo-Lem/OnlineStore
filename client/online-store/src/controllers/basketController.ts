import type { catalog } from './productController'

export interface basket {
  [key: string]: {
    item: number[]
    version: number
    count: number
  }
}

export interface newProduct {
  item: number[]
  version: number
  count: number
}

export interface curentProduct {
  item: number[]
  version: number
  count: number
}

export function getDataBasket(): basket {
  return JSON.parse(localStorage.basket)
}

export function saveDataBasket(basket: basket): basket {
  localStorage.basket = JSON.stringify(basket)
  return basket
}

export function addProductBasket(basket: basket, newProduct: newProduct): basket {
  let id = 1
  if (Object.keys(basket).length > 0)
    id = Number(Object.keys(basket)[Object.keys(basket).length - 1]) + 1

  basket[id] = newProduct
  saveDataBasket(basket)
  return basket
}

export function deleteProductBasket(id: number): basket {
  const basket = getDataBasket()
  delete basket[id]
  saveDataBasket(basket)
  return basket
}
export function correctBasket(basket: basket, catalog: catalog): basket {
  for (const [key, obj] of Object.entries(basket)) {
    if (!catalog.items[obj.item[obj.version]])
      delete basket[key]
  }

  saveDataBasket(basket)
  return basket
}

export function updateCountProductBasket(newCount: number, id: number) {
  const basket = getDataBasket()
  basket[id].count = newCount
  saveDataBasket(basket)
  return basket
}
export function summarizePriceProductBasket(basket: basket, catalog: catalog): number {
  let sum = 0
  if (Object.keys(basket).length > 0) {
    for (const key in basket) {
      const item = basket[key]
      sum += catalog.items[item.item[item.version]].price * item.count
    }
  }
  return sum
}
export function productInBasket(basket: basket, curentProduct: curentProduct): boolean {
  if (Object.keys(basket).length > 0) {
    let flagIs = true
    for (const key in basket) {
      if (JSON.stringify(basket[key].item) !== JSON.stringify(curentProduct.item)) {
        flagIs = false
        break
      }
      if (JSON.stringify(basket[key].version) !== JSON.stringify(curentProduct.version)) {
        flagIs = false
        break
      }
    }
    return flagIs
  }
  return false
}
