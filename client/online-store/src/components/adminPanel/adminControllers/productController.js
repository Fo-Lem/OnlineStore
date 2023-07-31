import { $admin } from "../../../axiosInstance/instance";


  export default class ProductController {
    async create (data){
      await $admin
        .post('/product',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async update(data) {
      await $admin
        .put('/product',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async delete(productId){
      await $admin
        .delete('/product',{data: {
          id: productId
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