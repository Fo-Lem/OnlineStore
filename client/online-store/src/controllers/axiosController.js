export const getCategorys = async () => {
    await axios
      .get('http://176.99.12.84/api/catalog')
      .then(response => {
        console.log(response.data)
        return response.data;
      })
      .catch(error => {
        console.log(error)
        return error;
      })
    
}