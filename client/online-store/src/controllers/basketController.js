export const getDataBasket = () => JSON.parse(localStorage.basket)

export function saveDataBasket(basket) {
  localStorage.basket = JSON.stringify(basket)
}

export function addProductBasket(basket, newProduct) {
  let id = 1
  if (Object.keys(basket).length > 0)
    id = Number(Object.keys(basket)[Object.keys(basket).length - 1]) + 1

  basket[id] = newProduct
  saveDataBasket(basket)
  return basket
}

export function deleteProductBasket(id) {
  const basket = getDataBasket()
  delete basket[id]
  saveDataBasket(basket)
  return basket
}
export function correctBasket(basket, catalog) {
  for (const [key, obj] of Object.entries(basket)) {
    if (!catalog.items[obj.item[obj.version]])
      delete basket[key]
  }

  saveDataBasket(basket)
  return basket
}

export function updateCountProductBasket(newCount, id) {
  const basket = getDataBasket()
  basket[id].count = newCount
  saveDataBasket(basket)
  return basket
}
export function summarizePriceProductBasket(basket, catalog) {
  let sum = 0
  if (Object.keys(basket).length > 0) {
    for (const basketKey in basket) {
      const item = basket[basketKey]
      sum += catalog.items[item.item[item.version]].price * item.count
    }
  }
  return sum
}
export function productInBasket(basket, curentProduct) {
  if (Object.keys(basket).length > 0) {
    let flagIs = true
    for (const basketKey in basket) {
      let flag = true
      for (const name of Object.keys(basket[basketKey])) {
        if (JSON.stringify(basket[basketKey][name]) !== JSON.stringify(curentProduct[name]) && name !== 'count') {
          flag = false
          break
        }
      }
      if (flag === true) {
        flagIs = true
        break
      }
      else {
        (
          flagIs = false
        )
      }
    }
    return flagIs
  }
}
