<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import { ErrorMessage, Field, Form } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as zod from 'zod'
import { summarizePriceProductBasket } from '../../controllers/basketController'
import type { basket } from '../../controllers/basketController'
import type { catalog } from '../../controllers/productController'
import type { address, user } from '../../controllers/orderController'
import { checkout } from '../../controllers/orderController'

interface State {
  address: address
  user: user
  orderSchema: any
}

export default defineComponent({
  name: 'CustomCart',
  components: {
    Field, Form, ErrorMessage,
  },
  props: {
    basket: {
      required: true,
      type: Object as PropType<basket>,
    },
    catalog: {
      required: true,
      type: Object as PropType<catalog>,
    },

  },
  emits: {
    deleteProductBasket(index: number) {
      return Number(index)
    },
    updateCountProductBasket(count: number, index: number) {
      return Number(index) && Number(count)
    },
  },
  data(): State {
    return {
      address: {
        city: '',
        street: '',
        house: '',
      },
      user: {
        numberPhone: '',
        email: '',
        name: '',
        surname: '',
        patronymic: '',
      },
      orderSchema: toTypedSchema(
        zod.object({
          numberPhone: zod.string()
            .regex(/^[0-9]*$/, { message: 'Не корректный номер телефона (79876543210)' })
            .min(11, { message: 'Номер должен содержать 11 символов' })
            .max(11, { message: 'Номер должен содержать не более 11 символов' }),
          name: zod.string()
            .regex(/^[а-яА-Яa-zA-Z]*$/, { message: 'Должно содержать только буквы' })
            .min(2, { message: 'Должно содержать более 2 символов' })
            .max(15, { message: 'Должно содержать менее 15 символов' }),
          surname: zod.string()
            .regex(/^[а-яА-Яa-zA-Z]*$/, { message: 'Должно содержать только буквы' })
            .min(2, { message: 'Должно содержать более 2 символов' })
            .max(15, { message: 'Должно содержать менее 15 символов' }),
          patronymic: zod.string()
            .regex(/^[а-яА-Яa-zA-Z]*$/, { message: 'Должно содержать только буквы' })
            .min(2, { message: 'Должно содержать более 2 символов' })
            .max(15, { message: 'Должно содержать менее 15 символов' }),
          email: zod.string()
            .email({ message: 'Не корректный Email' }),
          city: zod.string()
            .min(3, { message: 'Должно содержать более 3 символов' }),
          street: zod.string()
            .min(3, { message: 'Должно содержать более 3 символов' }),
          house: zod.string()
            .regex(/^[0-9]*\/?\-?[0-9]*?[а-яА-Яa-zA-Z]?$/, { message: 'Не корректный номер дома' }),
        }),
      ),
    }
  },
  computed: {
    sumPrice() {
      if (this.basket)
        return summarizePriceProductBasket(this.catalog)
      return 0
    },
  },
  methods: {
    deleteProductBasket(index: number) {
      this.$emit('deleteProductBasket', index)
    },
    updateCount(count: number, index: number) {
      if (count < 1)
        count = 1
      if (count > 1000)
        count = 1000

      this.$emit('updateCountProductBasket', count, index)
    },

    imgUrl(id: number) {
      return `${import.meta.env.VITE_BASE_URL}${this.catalog.items[id].img_path}/${this.catalog.items[id].art}_0.jpg`
    },
    checkout() {
      checkout(this.catalog, this.basket, this.user, this.address)
    },

  },

})
</script>

<template>
  <div class="">
    <div v-if="Object.keys(basket).length > 0" class="mx-auto lg:flex lg:space-x-6">
      <div class="rounded-lg lg:w-2/3">
        <div
          v-for="(item, index) in basket" :key="index"
          class="justify-between relative gap-5 mb-6 rounded-lg p-6 border border-primary flex flex-col md:flex-row md:justify-start"
        >
          <img :src="imgUrl(item.item[item.version])" alt="product-image" class="w-full rounded-lg md:w-40">
          <div class="gap-5 flex flex-col md:flex-col sm:w-full sm:justify-between">
            <div class="">
              <h2 class="text-lg font-bold md:mr-10 text-primary-dark">
                {{ catalog.items[item.item[item.version]].name }}
              </h2>
              <p class="mt-1 text-sm text-primary">
                C{{ (catalog.items[item.item[item.version]].art).split('C')[1] }}
              </p>
            </div>
            <div class="flex flex-row justify-items-start gap-5 items-end">
              <div class="flex items-center">
                <span
                  class="cursor-pointer rounded-l text-primary-dark bg-primary-light-1 py-1 px-3.5 text-3xl duration-100 hover:bg-primary "
                  @click="updateCount(Number(item.count) - 1, index)"
                > - </span>
                <input
                  :id="String(index)" v-model="item.count" name="count" type="number" min="1" maxlength="5"
                  class="text-center text-lg w-16 bg-primary-light-2 focus:outline-none"
                  @input="updateCount(item.count, index)"
                >
                <span
                  class="cursor-pointer  rounded-r text-primary-dark bg-primary-light-1 py-1 px-3 text-3xl duration-100 hover:bg-primary "
                  @click="updateCount(Number(item.count) + 1, index)"
                > + </span>
              </div>
              <p class="text-lg font-bold text-primary-dark">
                {{ catalog.items[item.item[item.version]].price }} руб.
              </p>
            </div>
          </div>

          <svg
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="h-8 w-8 absolute top-5 right-5 cursor-pointer duration-150 text-primary hover:text-primary-dark"
            @click="deleteProductBasket(index)"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </div>
      </div>
      <!-- Sub total -->
      <div class="mt-6 h-full rounded-lg border border-primary p-6 shadow-md md:mt-0 lg:w-1/3">
        <div class="mb-2 flex flex-col gap-5">
          <p class="text-primary-dark text-lg font-bold">
            Ваш заказ
          </p>
          <p v-for="(item, index) in basket" :key="index" class="text-primary-dark">
            {{ catalog.items[item.item[item.version]].name }}:
            {{ item.count }} шт.
            {{ catalog.items[item.item[item.version]].price * item.count }} руб.
          </p>
          <p class="text-primary-dark font-bold">
            Сумма заказа: {{ sumPrice }} руб.
          </p>
        </div>

        <hr class="my-4 border-primary">
        <Form :validation-schema="orderSchema" @submit="checkout">
          <div class="mb-2 flex flex-col gap-5 items-start justify-between">
            <p class="text-primary-dark font-bold">
              Адрес доставки
            </p>
            <div class=" flex flex-col w-full items-end gap-3">
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="city">Город</label>
                <Field
                  id="city" v-model="address.city" name="city" required placeholder="Москва"
                  class="w-full bg-primary-light-2   border border-primary-dark placeholder:text-primary-light-1 text-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="city" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="street">Улица</label>
                <Field
                  id="street" v-model="address.street" name="street" required placeholder="Пушкина"
                  class=" w-full bg-primary-light-2 border placeholder:text-primary-light-1 border-primary-dark text-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="street" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="house">Дом</label>
                <Field
                  id="house" v-model="address.house" name="house" required placeholder="6"
                  class="w-full bg-primary-light-2 border placeholder:text-primary-light-1 border-primary-dark text-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="house" />
              </div>
            </div>
          </div>
          <hr class="my-4 border-primary">
          <div class="mb-2 flex flex-col gap-5 items-start justify-between">
            <p class="text-primary-dark font-bold">
              Контакты
            </p>
            <div class=" flex flex-col w-full items-end gap-3">
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="surname">Фамилия</label>
                <Field
                  id="surname" v-model="user.surname" name="surname" required placeholder="Иванов"
                  class="w-full bg-primary-light-2 border border-primary-dark placeholder:text-primary-light-1 text-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="surname" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="name">Имя</label>
                <Field
                  id="name" v-model="user.name" name="name" required placeholder="Артем"
                  class="w-full text-primary-dark bg-primary-light-2 border placeholder:text-primary-light-1 border-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="name" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="patronymic">Отчество</label>
                <Field
                  id="patronymic" v-model="user.patronymic" name="patronymic" required placeholder="Дмитриевич"
                  class="w-full text-primary-dark bg-primary-light-2 border placeholder:text-primary-light-1 border-primary-dark p-3 rounded-lg" type="text"
                />
                <ErrorMessage class="text-red-500" name="patronymic" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="email">Email</label>
                <Field
                  id="email" v-model="user.email" name="email" required placeholder="1234@example.com"
                  class="w-full text-primary-dark p-3 bg-primary-light-2 placeholder:text-primary-light-1 border border-primary-dark rounded-lg" type="email"
                />
                <ErrorMessage class="text-red-500" name="email" />
              </div>
              <div class="flex flex-col w-full gap-1">
                <label class="text-primary-dark" for="numberPhone">Номер телефона</label>
                <Field
                  id="numberPhone" v-model="user.numberPhone" name="numberPhone" required maxlength="11"
                  placeholder="79123456789" class="bg-primary-light-2 border placeholder:text-primary-light-1 border-primary-dark w-full text-primary-dark  p-3 rounded-lg"
                  type="tel"
                />
                <ErrorMessage class="text-red-500" name="numberPhone" />
              </div>
            </div>
          </div>

          <button type="submit" class="mt-3 text-lg w-full rounded-md bg-primary-light-1 py-3 font-medium text-primary-dark hover:bg-primary">
            Оформить заказ
          </button>
        </Form>
      </div>
    </div>
    <div v-else class="mx-auto max-w-7xl justify-center px-6 lg:flex lg:space-x-6 xl:px-0">
      <p class="text-lg text-primary-dark">
        Корзина пуста
      </p>
    </div>
  </div>
</template>

<style scoped>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
}
input[type=number] {
    -moz-appearance:textfield;
}
</style>
