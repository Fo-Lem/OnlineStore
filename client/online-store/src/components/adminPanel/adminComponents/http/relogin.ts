import { $auth } from '../../../../axiosInstance/instance'
import type { ErrorMessage } from './login.ts'

interface FetchRelogin {
  token: string
  refresh_token: string
  msg: ErrorMessage

}

export async function relogin(): Promise<boolean> {
  const refresh_token = localStorage.getItem('refresh_token')
  return await $auth.post<FetchRelogin>('/relogin', { refresh_token }).then((res) => {
    if (res.status === 213) {
      console.error(res.data.msg)
      return false
    }
    localStorage.setItem('token', res.data.token)
    localStorage.setItem('refresh_token', res.data.refresh_token)
    return true
  }).catch((error: Error): boolean => {
    console.error(error)
    return false
  })
}
