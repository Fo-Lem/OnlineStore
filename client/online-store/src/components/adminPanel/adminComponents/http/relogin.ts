import { $auth } from '../../../../axiosInstance/instance'
import type { ErrorMessage } from './login.ts'

interface FetchRelogin {
  token: string
  refresh_token: string
  msg: ErrorMessage

}

export async function login(): Promise<boolean | ErrorMessage > {
  const refresh_token = localStorage.getItem('refresh_token')
  return await $auth.post<FetchRelogin>('/relogin', { refresh_token }).then((res) => {
    if (res.status === 213)
      return res.data.msg
    localStorage.setItem('token', res.data.token)
    localStorage.setItem('refresh_token', res.data.refresh_token)
    return true
  }).catch((error: Error): ErrorMessage => {
    console.error(error)
    return error.message
  })
}
