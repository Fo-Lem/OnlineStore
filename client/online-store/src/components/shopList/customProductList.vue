<script>
export default {

  name: 'CustomProductList',

  props: {
    // Определяет текущий компонент для отрисовки
    type: {
      require: true,
      type: String,
    },
    // Хранит данные о товарах
    catalog: {
      require: true,
      type: Object,
    },
    basket: {
      require: true,
      type: Object,
    },
  },
  data() {
    return {}
  },
  methods: {
    searchFirstHero(categoryId, typeId) {
      for (const cKey in this.catalog.items) {
        let firstHeroId
        if (this.catalog.items[cKey].product_type_id === typeId && this.catalog.items[cKey].category_id === categoryId) {
          if (firstHeroId) {
            if (firstHeroId > this.catalog.items[cKey].hero_id)
              firstHeroId = this.catalog.items[cKey].hero_id
          }
          else {
            firstHeroId = this.catalog.items[cKey].hero_id
          }
        }
      }
      if (!firstHeroId)
        return 0

      return firstHeroId
    },
  },

}
</script>

<template lang="">
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
          <custom-list
            v-if="Object.keys(category.product_types).length > 1 && category.name !== 'Без категории'"
            :list="category"
          />
        </router-link>
      </div>

      <div
        v-if="type === 'productList'"
        class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8"
      >
        <router-link
          v-for="typ in catalog.categories[$route.params.categoryId].product_types"
          :key="typ.id"
          :basket="basket"
          :to="{ name: 'productOverviews', params: { productId: typ.id, heroId: searchFirstHero($route.params.categoryId, typ.id) } }"
        >
          <custom-list
            v-if="typ.name !== '-' && typ.items "
            :list="typ"
          />
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
