<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog } from '../../controllers/productController'
import type { basket, curentProduct } from '../../controllers/basketController'
import CustomBreadcrumbs from '../UI/customBreadcrumbs.vue'

export default defineComponent({

  name: 'CustomShopContainer',
  components: {
    CustomBreadcrumbs,
  },
  props: {
    catalog: {
      required: true,
      type: Object as PropType<catalog>,
    },
    searchInput: [String, Number],
    basket: {
      required: true,
      type: Object as PropType<basket>,
    },
  },
  emits: ['addProductBasket', 'updateSearchInput'],
  methods: {
    addProductBasket(curentProduct: curentProduct) {
      this.$emit('addProductBasket', curentProduct)
    },

  },
})
</script>

<template>
  <div>
    <div class="mx-auto max-w-7xl p-3 flex flex-col-reverse items-center justify-between lg:px-8 md:flex-row ">
      <CustomBreadcrumbs
        :catalog="catalog"
        class="mt-2 md:mt-0"
      />
      <!-- <custom-search-input @update-search-input="(value)=>{this.$emit('updateSearchInput',value)}" v-bind:searchInput="searchInput" v-if="!$route.params.heroId" class="md:w-1/2" ></custom-search-input> -->
    </div>
    <router-view
      :basket="basket"
      :catalog="catalog"
      @add-product-basket="addProductBasket"
    />
  </div>
</template>

<style scoped></style>
