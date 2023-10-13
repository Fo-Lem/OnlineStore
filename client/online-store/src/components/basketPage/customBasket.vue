<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import { summarizePriceProductBasket } from '../../controllers/basketController'
import type { basket } from '../../controllers/basketController'
import type { catalog } from '../../controllers/productController'

interface State {
  address: {
    city: string
    street: string
    house: string
  }
  user: {
    numberPhone: string
    email: string
  }
}
export default defineComponent({
  name: 'CustomCart',
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
      },
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
    updateCount(count: number | string, index: number) {
      if (typeof count === 'number') {
        if (count > 0)
          this.$emit('updateCountProductBasket', count, index)
      }
    },
    imgUrl(id: number) {
      return `${import.meta.env.VITE_BASE_URL}${this.catalog.items[id].img_path}/${this.catalog.items[id].art}_0.jpg`
    },

  },

})
</script>

<template>
  <div class="bg-white">
    <div v-if="Object.keys(basket).length > 0" class="mx-auto lg:flex lg:space-x-6">
      <div class="rounded-lg lg:w-2/3">
        <div
          v-for="(item, index) in basket" :key="index"
          class="justify-between relative gap-5 mb-6 rounded-lg bg-white p-6 border border-black border-opacity-10 md:flex md:justify-start"
        >
          <img :src="imgUrl(item.item[item.version])" alt="product-image" class="w-full rounded-lg md:w-40">
          <div class="gap-5 sm:flex sm:w-full sm:justify-between">
            <div class="mt-5 sm:mt-0">
              <h2 class="text-lg font-bold text-gray-900">
                {{ catalog.items[item.item[item.version]].name }}
              </h2>
              <p class="mt-1 text-xs text-gray-700">
                C{{ (catalog.items[item.item[item.version]].art).split('C')[1] }}
              </p>
            </div>
            <div class="flex flex-col justify-end gap-5 items-end">
              <div class="flex items-center border-gray-100">
                <span
                  class="cursor-pointer rounded-l bg-gray-100 py-1 px-3.5 text-2xl duration-100 hover:bg-blue-500 hover:text-blue-50"
                  @click="updateCount(Number(item.count) - 1, index)"
                > - </span>
                <input :id="String(index)" v-model="item.count" type="number" min="1" class="text-center w-16" @input="$emit('updateCountProductBasket', item.count, index)">
                <span
                  class="cursor-pointer rounded-r bg-gray-100 py-1 px-3 text-2xl duration-100 hover:bg-blue-500 hover:text-blue-50"
                  @click="updateCount(Number(item.count) + 1, index)"
                > + </span>
              </div>
              <div class="flex items-end gap-2 flex-col">
                <p class="text-base">
                  1 шт. {{ catalog.items[item.item[item.version]].price }} руб.
                </p>
              </div>
            </div>
          </div>
          <svg
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="h-8 w-8 absolute top-5 right-5 cursor-pointer duration-150 hover:text-red-500"
            @click="deleteProductBasket(index)"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </div>
      </div>
      <!-- Sub total -->
      <div class="mt-6 h-full rounded-lg border bg-white p-6 shadow-md md:mt-0 lg:w-1/3">
        <div class="mb-2 flex flex-col gap-5">
          <p v-for="(item, index) in basket" :key="index">
            {{ catalog.items[item.item[item.version]].name }}:
            {{ catalog.items[item.item[item.version]].price * item.count }} руб.
          </p>
          <p class="text-gray-700 font-bold">
            Сумма заказа: {{ sumPrice }} руб.
          </p>
        </div>

        <hr class="my-4">
        <div class="mb-2 flex flex-col gap-5 items-start justify-between">
          <p class="text-gray-700 font-bold">
            Адрес доставки
          </p>
          <div class=" flex flex-col w-full items-end gap-2">
            <div class="flex w-full gap-5 items-center">
              <label for="city">Город</label>
              <input id="city" v-model="address.city" placeholder="Москва" class="w-full border border-black border-opacity-10 p-3 rounded-lg" type="text">
            </div>
            <div class="flex gap-5 w-full items-center">
              <label for="street">Улица</label>
              <input id="street" v-model="address.street" placeholder="Пушкина" class=" w-full border border-black border-opacity-10 p-3 rounded-lg" type="text">
            </div>
            <div class="flex gap-5 w-full items-center">
              <label for="house">Дом</label>
              <input id="house" v-model="address.house" placeholder="6" class="w-full border border-black border-opacity-10 p-3 rounded-lg" type="text">
            </div>
          </div>
        </div>
        <hr class="my-4">
        <div class="mb-2 flex flex-col gap-5 items-start justify-between">
          <p class="text-gray-700 font-bold">
            Контактные данные
          </p>
          <div class=" flex flex-col w-full items-end gap-2">
            <div class="flex w-full gap-5 items-center">
              <label for="email">Email</label>
              <input id="email" v-model="user.email" placeholder="1234@example.com" class="w-full border border-black border-opacity-10 p-3 rounded-lg" type="email">
            </div>
            <div class="flex gap-5 w-full items-center">
              <label class=" whitespace-nowrap" for="namberPhone">Номер телефона</label>
              <input id="namberPhone" v-model="user.numberPhone" maxlength="11" placeholder="79123456789" class=" w-full border border-black border-opacity-10 p-3 rounded-lg" type="tel">
            </div>
          </div>
        </div>

        <button class="mt-6 w-full rounded-md bg-blue-500 py-1.5 font-medium text-blue-50 hover:bg-blue-600">
          Сделать заказ
        </button>
      </div>
    </div>
    <div v-else class="mx-auto max-w-7xl justify-center px-6 lg:flex lg:space-x-6 xl:px-0">
      <p>Карзина пуста</p>
    </div>
  </div>
</template>

<style scoped>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
