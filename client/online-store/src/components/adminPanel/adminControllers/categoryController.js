import axios from "axios";
export default class CategoruController {
  async createCategory(data){
    await axios
      .post('http://176.99.12.84/admin/category',data)
      .then(response => {
        console.log(response.data)
        return response.data;
      })
      .catch(error => {
        console.log(error)
        return error;
      })
    
  }
  async updateCategory(categoryId,newValue,cover_path) {
    if(cover_path){
      await axios
      .put('http://176.99.12.84/admin/category',{
        id: categoryId,
        name:newValue,
        cover_img:cover_path
      })
      .then(response => {
        console.log(response.data)
        return response.data;
      })
      .catch(error => {
        console.log(error)
        return error;
      })
    }else{
      await axios
      .put('http://176.99.12.84/admin/category',{
        id: categoryId,
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
    
    
  }
  async deleteCategory(categoryId){
    await axios
      .delete('http://176.99.12.84/admin/category',{data: {
        id: categoryId
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


  