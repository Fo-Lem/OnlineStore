<template lang="">
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 pt-3 pb-6 flex flex-col items-center gap-6 sm:px-6  lg:max-w-7xl lg:px-8">
      <div v-if="type=='categoryList'" class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
        <router-link  v-for="category in catalog['categories']" :key="category.id" :to="{ name: 'productList', params: { categoryId: category.id } }">
          <custom-list v-if="Object.keys(category.product_types).length>0" v-bind:list="category"></custom-list>
        </router-link>
      </div>

      <div v-if="type=='productList'" class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
        <router-link v-for="type in catalog['categories'][$route.params.categoryId].product_types" v-bind:basket="basket" :key="type.id" :to="{ name: 'productOverviews', params: { productId: type.id,heroId: searchFirstHero($route.params.categoryId,type.id) } }">
          <custom-list v-bind:list="type"></custom-list>
        </router-link>
      </div>

      
    </div>
  </div>
</template>
<script>
export default {

  name: "custom-product-list",

  props: {
    //Определяет текущий компонент для отрисовки
    type: {
      require: true,
      type: String
    },
    //Хранит данные о товарах
    catalog: {
      require: true,
      type: Object
    },
    basket: {
      require: true,
      type: Object
    }
  },
  data() {
    return {
    }
  },
  methods: {
    searchFirstHero(categoryId, typeId) {
      for (const cKey in this.catalog.items) {
        var firstHeroId
        if (this.catalog.items[cKey].product_type_id == typeId && this.catalog.items[cKey].category_id == categoryId) {
          if (!firstHeroId) {
            firstHeroId = this.catalog.items[cKey].hero_id
          } else {
            if (firstHeroId > this.catalog.items[cKey].hero_id) {
              firstHeroId = this.catalog.items[cKey].hero_id
            }
          }
        }
      }
      if (!firstHeroId) {
        return 0
          }
            return firstHeroId
          
      
    }
  }

}
</script>
<style scoped></style>