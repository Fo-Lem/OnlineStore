<script>
export default {
  name: 'CustomInput',
  props: {
    item: [Object],

  },
  emits: ['updateInput'],
  data() {
    return {}
  },
  methods: {
    updateInput(event) {
      // передаем содержимое инпута
      this.$emit('updateInput', event.target.value)
    },
  },

}
</script>

<template lang="">
  <input
    id="count"
    :value="item.count"
    name="count"
    class="h-8 w-8 border bg-white text-center text-xs outline-none"
    type="number"
    min="1"
    @input="updateInput($event)"
  >
</template>

<style scoped></style>
