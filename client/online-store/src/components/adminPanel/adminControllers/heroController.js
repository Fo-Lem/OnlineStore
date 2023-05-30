import axios from "axios";

  export default class HeroController {
    async createHero(data){
      await axios
        .post('http://176.99.12.84/admin/hero',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async updateHero(data) {
      await axios
        .put('http://176.99.12.84/admin/hero',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async deleteHero(heroId){
      await axios
        .delete('http://176.99.12.84/admin/hero',{data: {
          id: heroId
        }})
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
  }