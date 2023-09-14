import { $admin } from '../../../axiosInstance/instance'

export default class CategoruController {
  async create(categoryName: string, coverImg: string) {
    await $admin
      .post('/category', {
        name: categoryName,
        cover_img: coverImg,
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

  async update(categoryId: number, newCategoryName: string, newCoverImg?: string) {
    await $admin
      .put('/category', {
        id: categoryId,
        name: newCategoryName,
        cover_img: newCoverImg,
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

  async delete(categoryId: number) {
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
