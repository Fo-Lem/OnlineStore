import axios from 'axios';

export const getCategorys = async () => {
    return await axios.get('http://176.99.12.84/api/catalog')
}
