<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import type { catalogType } from '../../controllers/productController'

export default defineComponent({

  name: 'CustomCartTypes',

  props: {
    type: {
      required: true,
      type: Object as PropType<catalogType>,
    },
  },

  methods: {
    imgUrl(): string {
      if (this.type.items) {
        const item = this.type.items[Number(Object.keys(this.type.items)[0])]
        return `${import.meta.env.VITE_BASE_URL}${item.img_path}/${item.art}_0.jpg`
      }
      return ''
    },
  },
})
</script>

<template>
  <div class="border-2 border-primary rounded-xl p-5 betterhover:hover:scale-105 transition">
    <img :src="imgUrl()" class="h-full w-full object-cover rounded-lg object-center ">
    <div class="flex justify-between pt-2 items-center">
      <h3 class="text-primary text-lg">
        {{ type.name }}
      </h3>
      <!-- <p
        v-if="type.items"
        class="text-primary text-md"
      >
        от {{ type.items[Number(Object.keys(type.items)[0])].price }} руб.
      </p> -->
    </div>
  </div>
</template>

<style scoped></style>
