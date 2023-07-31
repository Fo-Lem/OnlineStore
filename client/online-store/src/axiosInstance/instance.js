import axios from 'axios';

const $user = axios.create({
    baseURL:import.meta.env.VITE_API_URL
})

const $admin = axios.create({
    baseURL:import.meta.env.VITE_ADMIN_URL
})
// const authInterceptor = config => {
//     config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
//     return config
// }

// $admin.interceptors.request.use(authInterceptor)
export{
    $admin,$user
}