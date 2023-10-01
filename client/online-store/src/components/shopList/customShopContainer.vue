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
    <CustomBreadcrumbs
      class="mb-5"
      :catalog="catalog"
    />
    <router-view
      :basket="basket"
      :catalog="catalog"
      @add-product-basket="addProductBasket"
    />
  </div>
</template>

<style scoped></style>
