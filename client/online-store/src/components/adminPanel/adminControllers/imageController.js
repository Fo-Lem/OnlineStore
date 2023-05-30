import axios from "axios";


export default class ImageController {
  async createImage(formData){
    await axios({
      method: 'post',
      url: 'http://176.99.12.84/admin/image',
      data: formData,
      headers: { "Content-Type": "multipart/form-data" },
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
  async updateImage(data) {
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
  async deleteImage(cover_path){
    await axios
      .delete('http://176.99.12.84/admin/image',{data: {
        full_path: cover_path
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