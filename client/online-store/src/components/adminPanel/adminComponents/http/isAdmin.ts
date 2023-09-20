// import axios from 'axios'

import { $admin } from '../../../../axiosInstance/instance'

export async function isAdmin(): Promise<boolean> {
  return await $admin.get('/test').then((res) => {
    if (res.status === 200)
      return true
    return false
  }).catch((error: Error): boolean => {
    console.error(error)
    return false
  })
}
// export async function isAdmin(): Promise<boolean> {
//   return await axios.get('https://woodhouse-yar.ru/admin/test',
//     { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } }).then((res) => {
//     if (res.status === 200)
//       return true
//     return false
//   }).catch((error: Error): boolean => {
//     console.error(error)
//     return false
//   })
// }
