import { hashMd5 } from '../../helpers/hashMd5.ts'
import { $auth } from '../../../../axiosInstance/instance'

interface FetchLogin {
  token: string
  refresh_token: string
  msg: ErrorMessage

}
export type ErrorMessage = string

export async function login(login: string, password: string): Promise<boolean> {
  login = hashMd5(login)
  password = hashMd5(password)
  return await $auth.post<FetchLogin>('/login', { login, password }).then((res) => {
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
