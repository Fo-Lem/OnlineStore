import { $admin } from '../../../axiosInstance/instance';

export default class ImageController {
  async create(formData) {
    await $admin({
      method: 'post',
      url: '/image',
      data: formData,
      headers: { 'Content-Type': 'multipart/form-data', },
    })
      .then(response => {
        console.log(response.data);
        return response.data;
      })
      .catch(error => {
        console.log(error);
        return error;
      });

  }

  async delete(cover_path) {
    await $admin
      .delete('/image', {
        data: {
          full_path: cover_path,
        },
      })
      .then(response => {
        console.log(response.data);
        return response.data;
      })
      .catch(error => {
        console.log(error);
        return error;
      });

  }
}
