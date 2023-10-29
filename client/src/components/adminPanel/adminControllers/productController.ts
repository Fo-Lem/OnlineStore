import { $admin } from '../../../axiosInstance/instance'

export default class ProductController {
  async create(name: string, categoryId: number, productTypeId: number, heroId: number, description: string, art: string, imgPath: string, size: string, price: number) {
    await $admin
      .post('/product', {
        name,
        category_id: categoryId,
        product_type_id: productTypeId,
        hero_id: heroId,
        description,
        art,
        img_path: imgPath,
        size,
        price,
      })
      .then((response) => {
        // console.log(response.data)
        return response.data
      })
      .catch((error) => {
        // console.log(error)
        return error
      })
  }

  async update(productId: number, productId_1: number, newProductName: string, newCategoryId: number, newProductTypeId: number, newHeroId: number, newDescription: string, newSize: string, newPrice: number) {
    await $admin
      .put('/product', {
        id: productId,
        id_1: productId_1,
        name: newProductName,
        category_id: newCategoryId,
        product_type_id: newProductTypeId,
        hero_id: newHeroId,
        description: newDescription,
        size: newSize,
        price: newPrice,
      })
      .then((response) => {
        // console.log(response.data)
        return response.data
      })
      .catch((error) => {
        // console.log(error)
        return error
      })
  }

  async delete(productId: number) {
    await $admin
      .delete('/product', {
        data: {
          id: productId,
        },
      })
      .then((response) => {
        // console.log(response.data)
        return response.data
      })
      .catch((error) => {
        // console.log(error)
        return error
      })
  }
}
