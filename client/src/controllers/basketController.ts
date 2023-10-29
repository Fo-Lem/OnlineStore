import type { catalog } from './productController'

export interface basket {
  [key: number]: {
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
  return localStorage.basket ? JSON.parse(localStorage.basket) : {}
}

export function saveDataBasket(newBasket: basket): basket {
  localStorage.basket = JSON.stringify(newBasket)
  return newBasket
}

export function addProductBasket(newProduct: newProduct): basket {
  const basket = getDataBasket()
  let id = 1
  if (Object.keys(basket).length > 0)
    id = Number(Object.keys(basket)[Object.keys(basket).length - 1]) + 1

  basket[id] = newProduct
  return saveDataBasket(basket)
}

export function deleteProductBasket(id: number): basket {
  const basket = getDataBasket()
  delete basket[id]
  return saveDataBasket(basket)
}
export function correctBasket(catalog: catalog): basket {
  const basket = getDataBasket()
  for (const key in basket) {
    if (!catalog.items[basket[key].item[basket[key].version]])
      delete basket[key]
  }
  return saveDataBasket(basket)
}

export function updateCountProductBasket(newCount: number, id: number) {
  const basket = getDataBasket()
  basket[id].count = newCount
  return saveDataBasket(basket)
}
export function summarizePriceProductBasket(catalog: catalog): number {
  const basket = getDataBasket()
  let sum = 0
  if (Object.keys(basket).length > 0) {
    for (const key in basket) {
      const item = basket[key]
      sum += catalog.items[item.item[item.version]].price * item.count
    }
  }
  return sum
}
export function productInBasket(curentProduct: curentProduct): boolean {
  const basket = getDataBasket()

  if (Object.keys(basket).length > 0) {
    for (const key in basket) {
      if (basket[key].item[basket[key].version] === curentProduct.item[curentProduct.version])
        return true
    }
  }
  return false
}

export function clearBasket() {
  saveDataBasket({})
}
