import { $admin } from '../../../axiosInstance/instance'

export default class CategoruController {
  async create(data) {
    await $admin
      .post('/category', data)
      .then((response) => {
        // console.log(response.data)
        return response.data
      })
      .catch((error) => {
        // console.log(error)
        return error
      })
  }

  async update(categoryId, newValue, cover_path) {
    await (cover_path
      ? $admin
        .put('/category', {
          id: categoryId,
          name: newValue,
          cover_img: cover_path,
        })
        .then((response) => {
          // console.log(response.data)
          return response.data
        })
        .catch((error) => {
          // console.log(error)
          return error
        })
      : $admin
        .put('/category', {
          id: categoryId,
          name: newValue,

        })
        .then((response) => {
          // console.log(response.data)
          return response.data
        })
        .catch((error) => {
          // console.log(error)
          return error
        }))
  }

  async delete(categoryId) {
    await $admin
      .delete('/category', {
        data: {
          id: categoryId,
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
