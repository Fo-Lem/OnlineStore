<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog } from '../../controllers/productController'
import type { basket } from '../../controllers/basketController'
import CustomCartCategories from '../UI/customCartCategories.vue'
import CustomCartTypes from '../UI/customCartTypes.vue'

export default defineComponent({

  name: 'CustomProductList',
  components: { CustomCartCategories, CustomCartTypes },
  props: {
    // Определяет текущий компонент для отрисовки
    type: {
      required: true,
      type: String,
    },
    // Хранит данные о товарах
    catalog: {
      required: true,
      type: Object as PropType<catalog>,
    },
    basket: {
      required: true,
      type: Object as PropType<basket>,
    },
  },
  data() {
    return {}
  },
  methods: {
    searchFirstHero(categoryId: string, typeId: string) {
      let firstHeroId
      for (const itemId in this.catalog.categories[categoryId].product_types[typeId].items) {
        const itemHeroId = this.catalog.categories[categoryId].product_types[typeId].items[itemId].hero_id
        if (firstHeroId) {
          if (firstHeroId > itemHeroId)
            firstHeroId = itemHeroId
        }
        else {
          firstHeroId = itemHeroId
        }
      }

      if (!firstHeroId)
        return 0

      return firstHeroId
    },
  },

})
</script>

<template>
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 pt-3 pb-6 flex flex-col items-center gap-6 sm:px-6  lg:max-w-7xl lg:px-8">
      <div
        v-if="type === 'categoryList'"
        class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8"
      >
        <router-link
          v-for="category in catalog.categories"
          :key="category.id"
          :to="{ name: 'productList', params: { categoryId: category.id } }"
        >
          <CustomCartCategories
            v-if="Object.keys(category.product_types).length > 1 && category.name !== 'Без категории'"
            :category="category"
          />
        </router-link>
      </div>

      <div
        v-if="type === 'productList'"
        class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8"
      >
        <router-link
          v-for="typ in catalog.categories[$route.params.categoryId as string].product_types"
          :key="typ.id"
          :basket="basket"
          :to="{ name: 'productOverviews', params: { productId: typ.id, heroId: searchFirstHero($route.params.categoryId as string, typ.id) } }"
        >
          <CustomCartTypes
            v-if="typ.name !== '-' && typ.items "
            :type="typ"
          />
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
