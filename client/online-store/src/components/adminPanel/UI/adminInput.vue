<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AdminInput',
  props: {
    value: {
      require: true,
      type: String,
    },
    placeholder: {
      require: true,
      type: String,
    },
    inputIn: {
      require: true,
      type: String,
    },
    inputName: {
      require: true,
      type: String,
    },
  },
  emits: {
    updateInput(value: string) {
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

<template lang="">
  <div class="flex flex-col gap-2">
    <label
      :for="inputIn"
      class="block text-md leading-6 text-gray-900"
    >{{ inputName }}</label>
    <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
      <input
        :id="inputIn"
        :placeholder="placeholder"
        type="text"
        :name="inputIn"
        :value="value"
        class="block flex-1 border-0 bg-transparent p-2.5 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6"
        @input="updateInput"
      >
    </div>
  </div>
</template>
