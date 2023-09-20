import { $admin } from '../../../axiosInstance/instance'
import type { ErrorMessage } from '../adminComponents/http/login'

interface CategoryCreate {
  id: number
  name: string
  cover_img: string
  categories_to_types_id: number
}
interface CategoryUpdate {
  name: string
  cover_path: string
  err: string
}

export default class CategoruController {
  async create(categoryName: string, coverImg: string): Promise<boolean | ErrorMessage> {
    return await $admin
      .post<CategoryCreate>('/category', {
        name: categoryName,
        cover_img: coverImg,
      })
      .then((res) => {
        if (res.status === 201)
          return true
        return false
      })
      .catch((error: Error) => {
        return error.message
      })
  }

  async update(categoryId: number, newCategoryName: string, newCoverImg?: string): Promise<boolean | ErrorMessage> {
    return await $admin
      .put<CategoryUpdate>('/category', {
        id: categoryId,
        name: newCategoryName,
        cover_img: newCoverImg,
      })
      .then((res) => {
        if (res.status === 213)
          return res.data.err
        return true
      })
      .catch((error: Error) => {
        return error.message
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
      .catch((error: Error) => {
        // console.log(error)
        return error
      })
  }
}
