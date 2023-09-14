import { $admin } from '../../../axiosInstance/instance'

export function isAdmin() {
  return $admin.post('admin/auth', {}).then(() => {
    return true
  }).catch(() => {
    return false
  })
}
