import { $admin } from '../../../axiosInstance/instance'

export default class HeroController {
  async create(heroName: string) {
    await $admin
      .post('/hero', { heroName })
      .then((response) => {
        return response.status
      })
      .catch((error) => {
        return error
      })
  }

  async update(heroId: number, newHeroName: string) {
    await $admin
      .put('/hero', {
        id: heroId,
        name: newHeroName,

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

  async delete(heroId: number) {
    await $admin
      .delete('/hero', {
        data: {
          id: heroId,
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
