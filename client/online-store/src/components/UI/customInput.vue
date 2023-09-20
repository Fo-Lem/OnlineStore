<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { curentProduct } from '../../controllers/basketController'

export default defineComponent({
  name: 'CustomInput',
  props: {
    item: {
      type: Object as PropType<curentProduct>,
      required: true,
    },

  },
  emits: {
    updateInput(value: string | number) {
      return value
    },
  },
  methods: {
    updateInput(event: Event) {
      if (event.target instanceof HTMLInputElement)
        this.$emit('updateInput', event.target.value)
    },
  },

})
</script>

<template>
  <input
    id="count" :value="item.count" name="count" class="h-8 w-8 border bg-white text-center text-xs outline-none"
    type="number" min="1" @input="updateInput($event)"
  >
</template>

<style scoped></style>
