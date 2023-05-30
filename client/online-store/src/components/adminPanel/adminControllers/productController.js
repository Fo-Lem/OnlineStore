import axios from "axios";


  export default class ProductController {
    async createProduct (data){
      await axios
        .post('http://176.99.12.84/admin/product',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async updateProduct(data) {
      await axios
        .put('http://176.99.12.84/admin/product',data)
        .then(response => {
          console.log(response.data)
          return response.data;
        })
        .catch(error => {
          console.log(error)
          return error;
        })
      
    }
    async deleteProduct(productId){
      await axios
        .delete('http://176.99.12.84/admin/product',{data: {
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