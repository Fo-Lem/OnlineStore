<script>
import { summarizePriceProductBasket } from '../../controllers/basketController';

export default {
  name: 'CustomCart',
  props: {
    basket: {
      require: true,
      type: Object,
    },
    catalog: {
      require: true,
      type: Object,
    },
  },
  emits: ['deleteProductBasket', 'updateCountProductBasket'],
  data() {
    return {
      sumPrice: 0,
    };
  },
  watch: {
    basket() {
      this.sumPrice = summarizePriceProductBasket(this.basket, this.catalog);
    },
  },
  beforeMount() {
    console.log(this.basket);
    this.sumPrice = summarizePriceProductBasket(this.basket, this.catalog);
  },
  methods: {
    deleteProductBasket(index) {
      this.$emit('deleteProductBasket', index);
    },
    updateCount(count, index) {
      if (count > 0) {
        this.$emit('updateCountProductBasket', count, index);
      }
    },
    imgUrl(id) {
      return `${ import.meta.env.VITE_BASE_URL }${ this.catalog.items[id].img_path }/${ this.catalog.items[id].art }_0.jpg`;
    },
  },

};
</script>

<template lang="">
  <div class="bg-white p-10">
    <div
      v-if="Object.keys(basket).length > 0"
      class="mx-auto max-w-7xl justify-center px-6 lg:flex lg:space-x-6 xl:px-0"
    >
      <div class="rounded-lg lg:w-2/3">
        <div
          v-for="(item, index) in basket"
          :key="index"
          class="justify-between mb-6 rounded-lg bg-white p-6 shadow-md sm:flex sm:justify-start"
        >
          <img
            :src="imgUrl(item.item[0])"
            alt="product-image"
            class="w-full rounded-lg sm:w-40"
          >
          <div class="sm:ml-4 sm:flex sm:w-full sm:justify-between">
            <div class="mt-5 sm:mt-0">
              <h2 class="text-lg font-bold text-gray-900">
                {{ catalog.items[item.item[item.version]].name }}
              </h2>
              <p class="mt-1 text-xs text-gray-700">
                36EU - 4US
              </p>
            </div>
            <div class="mt-4 flex justify-between sm:space-y-6 sm:mt-0 sm:block sm:space-x-6">
              <div class="flex items-center border-gray-100">
                <span
                  class="cursor-pointer rounded-l bg-gray-100 py-1 px-3.5 duration-100 hover:bg-blue-500 hover:text-blue-50"
                  @click="updateCount(Number(item.count) - 1, index)"
                > - </span>
                <custom-input
                  :id="index"
                  :item="item"
                  @updateInput="(newCount) => { updateCount(newCount, index) }"
                />
                <span
                  class="cursor-pointer rounded-r bg-gray-100 py-1 px-3 duration-100 hover:bg-blue-500 hover:text-blue-50"
                  @click="updateCount(Number(item.count) + 1, index)"
                > + </span>
              </div>
              <div class="flex items-center space-x-4">
                <p class="text-sm">
                  {{ catalog.items[item.item[item.version]].price * item.count }} Р
                </p>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 cursor-pointer duration-150 hover:text-red-500"
                  @click="deleteProductBasket(index)"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Sub total -->
      <div class="mt-6 h-full rounded-lg border bg-white p-6 shadow-md md:mt-0 lg:w-1/3">
        <div class="mb-2 flex justify-between">
          <p class="text-gray-700">
            Сумма заказа
          </p>
          <p class="text-gray-700">
            {{ sumPrice }}
          </p>
        </div>
        <div class="flex justify-between">
          <p class="text-gray-700">
            Доставка
          </p>
          <p class="text-gray-700">
            $4.99
          </p>
        </div>
        <hr class="my-4">
        <div class="flex justify-between">
          <p class="text-lg font-bold">
            Итого
          </p>
          <div class="">
            <p class="mb-1 text-lg font-bold">
              {{ sumPrice }}
            </p>
          </div>
        </div>
        <button class="mt-6 w-full rounded-md bg-blue-500 py-1.5 font-medium text-blue-50 hover:bg-blue-600">
          Check out
        </button>
      </div>
    </div>
    <div
      v-else
      class="mx-auto max-w-7xl justify-center px-6 lg:flex lg:space-x-6 xl:px-0"
    >
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
