<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import type { category } from '../../controllers/productController'

export default defineComponent({

  name: 'CustomList',

  props: {
    category: {
      required: true,
      type: Object as PropType<category>,
    },
  },

  methods: {
    imgUrl(): string {
      if (this.category.cover_path)
        return `${import.meta.env.VITE_BASE_URL}${this.category.cover_path.slice(2)}`
      return ''
    },
  },
})
</script>

<template>
  <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-xl xl:aspect-h-8 xl:aspect-w-7">
    <div class="">
      <img :src="imgUrl" class="h-full w-full object-cover rounded-lg object-center hover:opacity-75">
      <div class="flex justify-between py-2 items-center">
        <h3 v-if="category" class="text-gray-900">
          {{ category.name }}
        </h3>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
