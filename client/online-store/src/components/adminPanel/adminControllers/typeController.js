import { $admin } from "../../../axiosInstance/instance";


  export default class TypeController {
    async create(data){
      await $admin
        .post('/product_type',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async update(typeId,newValue) {
      await $admin
        .put('/product_type',{
          id: typeId,
          name:newValue
        })
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async delete(typeId){
      await $admin
        .delete('/product_type',{data: {
          id: typeId
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