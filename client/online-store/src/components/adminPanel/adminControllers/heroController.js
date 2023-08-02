import { $admin } from '../../../axiosInstance/instance';

export default class HeroController {
  async create(data) {
    await $admin
      .post('/hero', data)
      .then(response => {
        console.log(response.data);
        return response.data;
      })
      .catch(error => {
        console.log(error);
      });

  }

  async update(heroId, newValue) {
    await $admin
      .put('/hero', {
        id: heroId,
        name: newValue,

      })
      .then(response => {
        console.log(response.data);
        return response.data;
      })
      .catch(error => {
        console.log(error);
      });

  }

  async delete(heroId) {
    await $admin
      .delete('/hero', {
        data: {
          id: heroId,
        },
      })
      .then(response => {
        console.log(response.data);
        return response.data;
      })
      .catch(error => {
        console.log(error);
      });

  }
}
