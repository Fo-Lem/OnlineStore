<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog, catalogItem, catalogItems } from '../../controllers/productController'

import type { basket, curentProduct } from '../../controllers/basketController'
import { productInBasket } from '../../controllers/basketController'

interface State {
  inBasket: boolean
  curentImage: number
  rebuilSize: string
  curentProduct: curentProduct
  heroId: number
  variants: Variants
  catalogItems: catalogItem[]

}
interface Variants {
  [key: number]: catalogItem[]
}
export default defineComponent({
  name: 'CustomProductOverviews',
  props: {

    catalog: {
      required: true,
      type: Object as PropType<catalog>,
    },
    basket: {
      required: true,
      type: Object as PropType<basket>,
    },

  },
  emits: {
    addProductBasket(curentProduct: curentProduct) {
      return curentProduct
    },
  },

  data(): State {
    return {
      inBasket: false,
      curentImage: 0,
      rebuilSize: '',
      curentProduct: {
        item: [],
        version: 0,
        count: 1,
      },
      heroId: 0,
      variants: [],
      catalogItems: [],

    }
  },
  computed: {
    imgUrl() {
      return `${import.meta.env.VITE_BASE_URL}${this.catalog.items[this.curentProduct.item[this.curentProduct.version]].img_path}/${this.catalog.items[this.curentProduct.item[this.curentProduct.version]].art}_`
    },

  },
  watch: {
    heroId(newHeroId) {
      this.updateCurentProduct(newHeroId)
    },

  },
  beforeMount() {
    this.updateCurentProduct(this.$route.params.heroId as unknown as number)
  },
  methods: {
    sizeConvertor(size: string): string[] {
      return size.split('x').reduce(
        (arr: string[], currentSize: string, index: number) => {
          const Arr = [
            'Ширинa: ', 'Высота: ', 'Глубина: ',
          ]
          arr[index] = `${Arr[index]} ${currentSize} мм`
          return arr
        }, [],
      )
    },
    addProductBasket() {
      this.$emit('addProductBasket', this.curentProduct)
      this.inBasket = productInBasket(this.curentProduct)
    },

    groupByHeroId(catalogItems: catalogItems): Variants {
      const obj = {} as Variants
      for (const index in catalogItems) {
        const item = catalogItems[index]
        obj[item.hero_id] = obj[item.hero_id] || []
        obj[item.hero_id].push(item)
      }
      return obj
    },

    updateCurentProduct(newHeroId: number, newVersion = 0) {
      this.curentProduct = {
        item: [],
        version: newVersion,
        count: 1,
      }
      if (Object.keys(this.catalogItems).length === 0) {
        for (const itemId in this.catalog.items) {
          const item = this.catalog.items[itemId]
          if (item.category_id === Number(this.$route.params.categoryId) && item.product_type_id === Number(this.$route.params.productId))
            this.catalogItems.push(item)
        }
        this.variants = this.groupByHeroId(this.catalog.items)
      }

      for (const item in this.variants[newHeroId])
        this.curentProduct.item.push(this.variants[newHeroId][item].id)

      this.inBasket = productInBasket(this.curentProduct)
    },
  },
})
</script>

<template>
  <div class="bg-white">
    <div
      v-if="$route.params.heroId !== '0' && catalog.items[curentProduct.item[curentProduct.version]]"
      class=" flex  flex-col justify-between gap-5 lg:flex-row"
    >
      <div class="flex flex-col gap-3 md:gap-5 flex-1">
        <div>
          <img
            :src="`${imgUrl}${curentImage}.jpg`"
            class=" w-full object-cover rounded-lg object-center"
          >
        </div>
        <div class="grid grid-cols-3 gap-3 md:gap-5 ">
          <div
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none"
            :class="[curentImage === 0 ? 'ring-2' : '']"
          >
            <img
              :src="`${imgUrl}0.jpg`"
              class="h-full w-full object-cover rounded-lg object-center"
              @click="curentImage = 0"
            >
          </div>
          <div
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none"
            :class="[curentImage === 1 ? 'ring-2' : '']"
          >
            <img
              :src="`${imgUrl}1.jpg`"
              class="h-full w-full object-cover rounded-lg object-center"
              @click="curentImage = 1"
            >
          </div>
          <div
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none"
            :class="[curentImage === 2 ? 'ring-2' : '']"
          >
            <img
              :src="`${imgUrl}2.jpg`"
              class="h-full w-full object-cover rounded-lg object-center"
              @click="curentImage = 2"
            >
          </div>
        </div>
      </div>

      <!-- Информация -->
      <div class="flex-1 ">
        <h2 class="text-3xl tracking-tight text-gray-900">
          {{ catalog.items[curentProduct.item[curentProduct.version]].name }}
        </h2>
        <hr>

        <form
          class=" flex gap-5 flex-col mt-5"
          @submit.prevent="addProductBasket"
        >
          <!-- Варианты -->
          <div class="flex flex-col gap-5">
            <p class="text-xl font-medium text-gray-900">
              Герои
            </p>
            <div class="flex flex-wrap gap-2 ">
              <router-link
                v-for="hero in variants"
                :key="hero[0].id"
                as="template"
                :value="hero"
                :to="{ name: 'productOverviews', params: { productId: $route.params.productId, heroId: hero[0].hero_id } }"
                @click="heroId = hero[0].hero_id"
              >
                <div
                  class="flex cursor-pointer rounded-lg p-0.5"
                  :class="[Number($route.params.heroId) === hero[0].hero_id ? 'ring-2' : '']"
                >
                  <span
                    class=" rounded-lg text-md px-3 py-2 border border-black border-opacity-10"
                  >{{ catalog.heroes[hero[0].hero_id].name }}</span>
                </div>
              </router-link>
            </div>
          </div>
          <div v-if="curentProduct.item.length > 1" class="flex flex-col gap-5">
            <p class="text-xl font-medium text-gray-900">
              Вариации
            </p>

            <div class="flex flex-wrap gap-2 items-center ">
              <div
                v-for="(itemId, index) in curentProduct.item"
                :key="itemId"
                class="rounded-lg text-sm p-0.5"
                :class="[curentProduct.version === index ? 'ring-2' : '']"
              >
                <button
                  class="rounded-lg text-sm px-4 py-2 border border-black border-opacity-10"
                  type="button"
                  @click="updateCurentProduct(Number($route.params.heroId), index)"
                >
                  {{ index + 1 }}
                </button>
              </div>
            </div>
          </div>

          <!-- Характеристики -->
          <div class="flex flex-col gap-5">
            <div class="">
              <h3 class="font-medium text-xl text-gray-900">
                Характеристики
              </h3>
            </div>

            <!-- Размер -->
            <div class="flex flex-col gap-5">
              <div class="flex items-center justify-between">
                <h3 class="font-medium text-xl text-gray-900">
                  Размер
                </h3>
              </div>

              <div class="flex flex-col">
                <p v-for="(size, index) in sizeConvertor(catalog.items[curentProduct.item[curentProduct.version]].size)" :key="index">
                  {{ size }}
                </p>
              </div>
            </div>
            <!-- Описание -->
            <div class="flex flex-col gap-5">
              <h3 class="font-medium text-xl text-gray-900">
                Описание
              </h3>
              <div>
                <p>{{ catalog.items[curentProduct.item[curentProduct.version]].description }}</p>
              </div>
            </div>
          </div>
          <p class="text-xl font-medium text-gray-900">
            Цена: {{ catalog.items[curentProduct.item[curentProduct.version]].price }} р
          </p>
          <div v-if="!inBasket">
            <button
              type="submit"
              class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              Добавить в корзину
            </button>
          </div>
          <div
            v-else
            class="mt-5 flex w-full justify-center rounded-md border border-transparent bg-gray-100"
          >
            <h1 class=" px-8 py-3 text-base text-gray-500 font-medium">
              Товар уже в корзине
            </h1>
          </div>
        </form>
      </div>
    </div>
    <div
      v-else
      class="py-3 text-base text-red-500 font-medium"
    >
      <h1>Такого товара не существует</h1>
    </div>
  </div>
</template>

<style scoped></style>
