<script>
export default {

  name: 'CustomShopContainer',
  props: {
    // Хранит данные о товарах
    catalog: {
      require: true,
      type: Object,
    },
    searchInput: [String, Number],
    basket: {
      require: true,
      type: Object,
    },
  },
  emits: ['addProductBasket', 'updateSearchInput'],
}
</script>

<template lang="">
  <div>
    <div class="mx-auto max-w-7xl p-3 flex flex-col-reverse items-center justify-between lg:px-8 md:flex-row ">
      <custom-breadcrumbs
        :catalog="catalog"
        class="mt-2 md:mt-0"
      />
      <!-- <custom-search-input @update-search-input="(value)=>{this.$emit('updateSearchInput',value)}" v-bind:searchInput="searchInput" v-if="!$route.params.heroId" class="md:w-1/2" ></custom-search-input> -->
    </div>
    <router-view
      :basket="basket"
      :catalog="catalog"
      @add-product-basket="(curentProduct) => { $emit('addProductBasket', curentProduct) }"
    />
  </div>
</template>

<style scoped></style>
