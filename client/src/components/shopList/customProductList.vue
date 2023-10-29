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
  methods: {
    searchFirstHero(categoryId: number, typeId: number) {
      let firstHeroId
      for (const itemId in this.catalog.categories[categoryId].product_types[typeId].items) {
        const itemHeroId = this.catalog.categories[categoryId].product_types[typeId].items[itemId].hero_id
        if (firstHeroId) {
          if (firstHeroId > itemHeroId)
            firstHeroId = itemHeroId
        }
        else { firstHeroId = itemHeroId }
      }

      if (!firstHeroId)
        return 0

      return firstHeroId
    },
  },

})
</script>

<template>
  <div>
    <div
      v-if="type === 'categoryList'"
      class="grid grid-cols-1 gap-x-5 gap-y-10 md:grid-cols-2 md:gap-x-6 lg:grid-cols-3 lg:gap-x-7 xl:gap-x-8"
    >
      <div
        v-for="category in catalog.categories"
        :key="category.id"
        :class="Object.keys(category.product_types).length > 1 && category.name !== 'Без категории' ? '' : 'hidden'"
      >
        <router-link
          :to="{ name: 'productList', params: { categoryId: category.id } }"
        >
          <CustomCartCategories
            :category="category"
          />
        </router-link>
      </div>
    </div>

    <div
      v-if="type === 'productList'"
      class="grid grid-cols-1 gap-x-5 gap-y-10 md:grid-cols-2 md:gap-x-6 lg:grid-cols-3 lg:gap-x-7 xl:gap-x-8"
    >
      <div
        v-for="typ in catalog.categories[Number($route.params.categoryId)].product_types"
        :key="typ.id"
        :class="typ.items && typ.name !== '-' ? '' : 'hidden'"
      >
        <router-link
          :basket="basket"
          :to="{ name: 'productOverviews', params: { typeId: typ.id, heroId: searchFirstHero(Number($route.params.categoryId), typ.id) } }"
        >
          <CustomCartTypes
            :type="typ"
          />
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
