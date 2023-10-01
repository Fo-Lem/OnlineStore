<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog } from '../../controllers/productController'

export default defineComponent({
  name: 'CustomBreadcrumbs',
  props: {
    catalog: {
      type: Object as PropType<catalog>,
      required: true,
    },
  },

})
</script>

<template>
  <div class="">
    <ol class="flex justify-center text-gray-700 lg:justify-start">
      <li class="pr-2">
        <router-link
          to="/catalog"
          :class="!$route.params.categoryId ? 'text-gray-500' : 'hover:underline'"
        >
          Главная
        </router-link>
      </li>
      <li class="text-gray-500 select-none">
        /
      </li>
      <li
        v-if="$route.params.categoryId"
        class="px-2"
      >
        <router-link
          :to="{ name: 'productList', params: { categoryId: $route.params.categoryId } }"
          :class="!$route.params.productId ? 'text-gray-500' : 'hover:underline'"
        >
          {{ catalog.categories[Number($route.params.categoryId)].name }}
        </router-link>
      </li>
      <li
        v-if="$route.params.productId"
        class="text-gray-500 select-none"
      >
        /
      </li>
      <li
        v-if="$route.params.categoryId && $route.params.productId"
        class="px-2 text-gray-500"
      >
        {{ catalog.categories[Number($route.params.categoryId)].product_types[Number($route.params.productId)].name }}
      </li>
    </ol>
  </div>
</template>

<style scoped>

</style>
