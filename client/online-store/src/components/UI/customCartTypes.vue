<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import type { type } from '../../controllers/productController'

export default defineComponent({

  name: 'CustomList',

  props: {
    type: {
      required: true,
      type: Object as PropType<type>,
    },
  },

  methods: {
    imgUrl(): string {
      if (this.type.items) {
        const item = this.type.items[Object.keys(this.type.items)[0]]
        return `${import.meta.env.VITE_BASE_URL}${item.img_path}/${item.art}_0.jpg`
      }
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
        <h3 v-if="type.name" class="text-gray-900">
          {{ type.name }}
        </h3>
        <p
          v-if="type.items"
          class="text-gray-900"
        >
          Цена: {{ type.items[Object.keys(type.items)[0]].price }} р
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
