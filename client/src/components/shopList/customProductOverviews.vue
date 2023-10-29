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
    deleteProductBasket(index: number) {
      return Number(index)
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
    deleteProductBasket() {
      let index = 0
      for (const key in this.basket) {
        if (this.basket[key].item[this.basket[key].version] === this.curentProduct.item[this.curentProduct.version]) {
          index = Number(key)
          break
        }
      }
      if (index) {
        this.$emit('deleteProductBasket', index)
        this.inBasket = productInBasket(this.curentProduct)
      }
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
          if (item.category_id === Number(this.$route.params.categoryId) && item.product_type_id === Number(this.$route.params.typeId))
            this.catalogItems.push(item)
        }
        this.variants = this.groupByHeroId(this.catalogItems)
      }

      for (const item in this.variants[newHeroId])
        this.curentProduct.item.push(this.variants[newHeroId][item].id)

      this.inBasket = productInBasket(this.curentProduct)
    },
  },
})
</script>

<template>
  <div>
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
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg  focus:outline-none"
            :class="[curentImage === 0 ? 'ring-2 ring-primary' : '']"
          >
            <img
              :src="`${imgUrl}0.jpg`"
              class="h-full w-full object-cover rounded-lg object-center"
              @click="curentImage = 0"
            >
          </div>
          <div
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg  focus:outline-none"
            :class="[curentImage === 1 ? 'ring-2 ring-primary' : '']"
          >
            <img
              :src="`${imgUrl}1.jpg`"
              class="h-full w-full object-cover rounded-lg object-center"
              @click="curentImage = 1"
            >
          </div>
          <div
            class="relative -m-0.5 flex  cursor-pointer items-center justify-center rounded-lg  focus:outline-none"
            :class="[curentImage === 2 ? 'ring-2 ring-primary' : '']"
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
        <h2 class="text-2xl md:text-3xl tracking-tight text-primary">
          {{ catalog.items[curentProduct.item[curentProduct.version]].name }}
        </h2>
        <hr class="border-primary">

        <div
          class=" flex gap-5 flex-col mt-5"
        >
          <!-- Варианты -->
          <div class="flex flex-col gap-5">
            <p class="text-xl font-medium text-primary">
              Герои
            </p>
            <div class="flex flex-wrap gap-2 ">
              <router-link
                v-for="hero in variants"
                :key="hero[0].id"
                as="template"
                :value="hero"
                :to="{ name: 'productOverviews', params: { typeId: $route.params.typeId, heroId: hero[0].hero_id } }"
                @click="heroId = hero[0].hero_id"
              >
                <div
                  class="flex cursor-pointer rounded-lg"
                  :class="[Number($route.params.heroId) === hero[0].hero_id ? 'ring-2 ring-primary' : '']"
                >
                  <span
                    class=" rounded-lg text-md px-3 py-2 border text-primary-dark border-primary-light-1"
                  >{{ catalog.heroes[hero[0].hero_id].name }}</span>
                </div>
              </router-link>
            </div>
          </div>
          <div v-if="curentProduct.item.length > 1" class="flex flex-col gap-5">
            <p class="text-xl font-medium text-primary">
              Вариации
            </p>

            <div class="flex flex-wrap gap-2 items-center ">
              <div
                v-for="(itemId, index) in curentProduct.item"
                :key="itemId"
                class="rounded-lg text-sm "
                :class="[curentProduct.version === index ? 'ring-2 ring-primary' : '']"
              >
                <button
                  class="rounded-lg text-sm px-4 py-2 border text-primary-dark border-primary-light-1"
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
              <h3 class="font-medium text-xl text-primary">
                Характеристики
              </h3>
            </div>

            <!-- Размер -->
            <div class="flex flex-col gap-5">
              <div class="flex items-center justify-between">
                <h3 class="font-medium text-xl text-primary">
                  Размер
                </h3>
              </div>

              <div class="flex flex-col">
                <p v-for="(size, index) in sizeConvertor(catalog.items[curentProduct.item[curentProduct.version]].size)" :key="index" class="text-primary-dark">
                  {{ size }}
                </p>
              </div>
            </div>
            <!-- Описание -->
            <div class="flex flex-col gap-5">
              <h3 class="font-medium text-xl text-primary">
                Описание
              </h3>
              <div>
                <p class="text-primary-dark">
                  {{ catalog.items[curentProduct.item[curentProduct.version]].description }}
                </p>
              </div>
            </div>
          </div>
          <p class="text-xl font-medium text-primary">
            Цена: {{ catalog.items[curentProduct.item[curentProduct.version]].price }} руб.
          </p>
          <div v-if="!inBasket">
            <button
              type="submit"
              class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-primary px-8 py-3 text-base font-medium text-primary-light-2 hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
              @click="addProductBasket"
            >
              Добавить в корзину
            </button>
          </div>
          <div v-if="inBasket">
            <button
              type="submit"
              class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-primary-light-1 px-8 py-3 text-base font-medium text-primary-dark hover:bg-primary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
              @click="deleteProductBasket()"
            >
              Удалить из корзины
            </button>
          </div>
        </div>
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
