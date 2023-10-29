import { $user } from '../axiosInstance/instance'
import type { basket } from './basketController'
import { clearBasket, summarizePriceProductBasket } from './basketController'
import type { catalog } from './productController'

export interface order {
  [key: number]: object
}

export interface address {
  city: string
  street: string
  house: string
}
export interface user {
  numberPhone: string
  email: string
  name: string
  surname: string
  patronymic: string
}

export async function sendOrder(order: order) {
  return await $user.post('/mail', order).then((res) => {
    return res.status === 204
  }).catch((error) => {
    console.error(error)
    return false
  })
}

export async function checkout(catalog: catalog, basket: basket, user: user, address: address) {
  const order = {
    fio: `${user.surname} ${user.name} ${user.patronymic}`,
    email: user.email,
    phone: user.numberPhone,
    delivery_address: `${address.city} ${address.street} ${address.house}`,
    order_price: summarizePriceProductBasket(catalog),
    order: orderAssembly(catalog, basket),

  }
  if (await sendOrder(order)) {
    clearBasket()
    alert('Заказ оформлен')
  }
}

function orderAssembly(catalog: catalog, basket: basket) {
  const order: order = {}
  for (const key of Object.keys(basket)) {
    order[Number(key) - 1] = {
      article: `C${(catalog.items[basket[Number(key)].item[basket[Number(key)].version]].art).split('C')[1]}`,
      name: catalog.items[basket[Number(key)].item[basket[Number(key)].version]].name,
      price: catalog.items[basket[Number(key)].item[basket[Number(key)].version]].price,
      img_path: catalog.items[basket[Number(key)].item[basket[Number(key)].version]].img_path,
      count: basket[Number(key)].count,
    }
  }
  return order
}
