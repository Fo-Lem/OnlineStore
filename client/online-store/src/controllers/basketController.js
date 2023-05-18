

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
            sum += categorys[item.category].product_types[item.product_type].heroes[item.hero].price * item.count
        }
    }
    return sum
}
export const productInBasket = (basket,curentProduct)=>{
    if (Object.keys(basket).length > 0) {
        let flagIs = true
        for (let basketKey in basket) {
            let flag = true
            for (let name of Object.keys(basket[basketKey])) {
                if (basket[basketKey][name] != curentProduct[name]) {
                    if (name != "count") {
                        flag = false
                        break
                    }
                }
            };
            if (flag === true) {
                flagIs = true
                break
            } else (
                flagIs = false
            )
        }
        return flagIs
    }
}


