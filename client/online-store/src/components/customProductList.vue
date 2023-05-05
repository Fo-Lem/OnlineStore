<template lang="">
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 py-4 flex flex-col items-center gap-6 sm:px-6 sm:py-6 lg:max-w-7xl lg:px-8">
      <div v-if="type=='categoryList'" class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
        <router-link  v-for="category in categorys" :key="category.id" :to="{ name: 'productList', params: { categoryId: category.id } }"  class="group">
          <custom-list v-bind:list="category"></custom-list>
        </router-link>
      </div>

      <div v-if="type=='productList'" class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
        <router-link v-for="product in categorys[$route.params.categoryId].products" :key="product.id" :to="{ name: 'productOverviews', params: { productId: product.id,heroId: product.id } }"  class="group">
          <custom-list v-bind:list="product"></custom-list>
        </router-link>
      </div>

      
    </div>
  </div>
</template>
<script>
import customList from "../UI/customList.vue";
export default {
  components:{customList},
  
  name: "custom-product-list",

  props: {
    //Определяет текущий компонент для отрисовки
    type: {
      require: true,
      type: String
    },
    //Хранит данные о товарах
    categorys: {
      require: true,
      type: Object
  }
  },
  data() {
    return {
    }
  },

}
</script>
<style scoped></style>