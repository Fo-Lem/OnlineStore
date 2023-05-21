<template lang="">
  <div>
    <div class="mx-auto max-w-7xl p-3 flex flex-col-reverse items-center justify-between lg:px-8 md:flex-row ">
      <custom-breadcrumbs v-bind:catalog="catalog" class="mt-2 md:mt-0"></custom-breadcrumbs>
      <custom-search-input @update-search-input="(value)=>{this.$emit('updateSearchInput',value)}" v-bind:searchInput="searchInput" v-if="!$route.params.heroId" class="md:w-1/2" ></custom-search-input>
    </div> 
    <router-view @add-product-basket="(curentProduct) => {this.$emit('addProductBasket',curentProduct)}" v-bind:basket="basket"  v-bind:catalog="catalog"></router-view>
  </div>

</template>
<script>


export default {

  name: "custom-shop-container",
  emits: ['addProductBasket','updateSearchInput'],
  props: {
    //Хранит данные о товарах
    catalog: {
      require: true,
      type: Object
    },
    searchInput:[String,Number],
    basket: {
      require: true,
      type: Object
    }
  }
}
</script>
<style scoped></style>