import { toTypedSchema } from '@vee-validate/zod'
import * as zod from 'zod'

const houseRegex = /^[0-9]*\/?[0-9]*?[а-яА-Яa-zA-Z]?$/

export const isEmail = toTypedSchema(
  zod.string()
    .email({ message: 'Must be a valid email' }),
)
export const isText = toTypedSchema(
  zod.string()
    .min(2, { message: 'Must be at least 3 characters' })
    .max(15, { message: 'Must be less than 15' }),
)
export const isAdressHouse = toTypedSchema(

  zod.string()
    .regex(houseRegex, { message: 'Must be a valid house number' }),
)
export const isAdressStrit = toTypedSchema(
  zod.string()
    .min(3, { message: 'Must be at least 3 characters' }),
)
export const isAdressCity = toTypedSchema(
  zod.string()
    .min(3, { message: 'Must be at least 3 characters' }),
)
export const isNumberPhone = toTypedSchema(
  zod.string()
    .min(11, { message: 'Не корректный номер телефона (79876543210)' })
    .max(11, { message: 'Не корректный номер телефона (79876543210)' })
    .regex(/^[0-9]*$/, { message: 'Не корректный номер телефона (79876543210)' }),
)
