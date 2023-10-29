import { $admin } from '../../../axiosInstance/instance'

export default class TypeController {
  async create(categoryId: number, typeName: string) {
    await $admin
      .post('/product_type', {
        category_id: categoryId,
        name: typeName,
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

  async update(typeId: number, newTypeName: string) {
    await $admin
      .put('/product_type', {
        id: typeId,
        name: newTypeName,
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

  async delete(typeId: number) {
    await $admin
      .delete('/product_type', {
        data: {
          id: typeId,
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
