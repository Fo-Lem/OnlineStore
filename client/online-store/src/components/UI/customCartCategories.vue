<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import type { catalogCategory } from '../../controllers/productController'

export default defineComponent({

  name: 'CustomCartCategories',

  props: {
    category: {
      required: true,
      type: Object as PropType<catalogCategory>,
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
  <div class=" border-2 border-primary rounded-xl p-5 hover:scale-105 transition flex flex-col gap-2">
    <img :src="imgUrl()" class="h-full w-full object-cover rounded-lg object-center">
    <div class="flex justify-between items-center">
      <h3 v-if="category" class="text-primary w-full text-lg">
        {{ category.name }}
      </h3>
    </div>
  </div>
</template>

<style scoped></style>
