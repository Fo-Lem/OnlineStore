import axios from "axios";


  export default class TypeController {
    async createType(data){
      await axios
        .post('http://176.99.12.84/admin/product_type',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async updateType(typeId,newValue) {
      await axios
        .put('http://176.99.12.84/admin/product_type',{
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
    async deleteType(typeId){
      await axios
        .delete('http://176.99.12.84/admin/product_type',{data: {
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