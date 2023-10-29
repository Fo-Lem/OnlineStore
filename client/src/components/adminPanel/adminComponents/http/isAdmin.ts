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
