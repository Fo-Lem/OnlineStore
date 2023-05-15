

export const getDataBasket = () => {
    return JSON.parse(localStorage.basket)
}

export const saveDataBasket = (basket) => {
    localStorage.basket = JSON.stringify(basket)
}

export const addProductBasket = (basket, newProduct) => {
    let id = 1
    if (Object.keys(basket).length > 0) {
        id = Number(Object.keys(basket)[Object.keys(basket).length - 1]) + 1
    }
    basket[id] = newProduct
    saveDataBasket(basket)
    return basket
}

export const deleteProductBasket = (id) => {
    let basket = getDataBasket()
    delete basket[id]
    saveDataBasket(basket)
    return basket
}

export const updateCountProductBasket = (newCount, id) => {
    let basket = getDataBasket()
    basket[id].count = newCount
    saveDataBasket(basket)
    return basket
}
export const summarizePriceProductBasket = (basket, categorys) => {
    let sum = 0
    if (Object.keys(basket).length > 0) {
        for (let basketKey in basket) {
            const item = basket[basketKey]
            sum += categorys[item.category].products_type[item.products_type].heroes[item.hero].items[0].price * item.count
        }
    }
    return sum
}


