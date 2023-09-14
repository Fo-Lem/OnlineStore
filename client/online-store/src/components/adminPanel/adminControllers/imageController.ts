import { $admin } from '../../../axiosInstance/instance'

export default class ImageController {
  /**
 * Создать изображениe по указанному пути.
 *
 * @param formData - Форма для загрузки изображения содержит в себе:
 * - path - полный путь к изображению.
 * - name - название изображения.
 * - file - файл изображения.
 * @returns The response data or an error if the request failed.
 */
  async create(formData: FormData) {
    await $admin({
      method: 'post',
      url: '/image',
      data: formData,
      headers: { 'Content-Type': 'multipart/form-data' },
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

  /**
 * Удалить изображение по указанному пути.
 *
 * @param {string} cover_path - Путь к изображению, которое нужно удалить.
 * @returns {Promise} - Промис, который разрешается с данными ответа или отклоняется с ошибкой.
 */
  async delete(cover_path: string) {
    await $admin
      .delete('/image', {
        data: {
          full_path: cover_path,
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
