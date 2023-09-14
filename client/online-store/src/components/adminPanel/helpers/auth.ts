import { $user } from '../../../axiosInstance/instance.ts'

export async function login(email: string, password: string) {
  const { data } = await $user.post('admin/login', { email, password })
  localStorage.setItem('token', data.token)
}
