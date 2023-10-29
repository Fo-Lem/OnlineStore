<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AdminSelect',
  props: {
    options: {
      required: true,
      type: Object,
    },
    selectIn: {
      required: true,
      type: String,
    },
    selectName: {
      required: true,
      type: String,
    },
    curentOption: {
      default: {},
    },
  },
  emits: {
    changeOptionCategory(select: number) {
      Number(select)

      return Boolean(select)
    },
    changeOptionType(select: number) {
      Number(select)

      return Boolean(select)
    },
    changeOptionHero(select: number) {
      Number(select)

      return Boolean(select)
    },
    changeOptionItem(select: number) {
      Number(select)

      return Boolean(select)
    },
    openAddPopup(): boolean {
      return true
    },
    openDeletePopup(): boolean {
      return true
    },
    openUpdatePopup(): boolean {
      return true
    },
  },

  methods: {
    changeOption(event: Event) {
      if (event.target instanceof HTMLSelectElement) {
        switch (this.selectIn) {
          case 'Category':
            this.$emit('changeOptionCategory', Number(event.target.value))
            break
          case 'Type':
            this.$emit('changeOptionType', Number(event.target.value))
            break
          case 'Hero':
            this.$emit('changeOptionHero', Number(event.target.value))
            break
          case 'Item':
            this.$emit('changeOptionItem', Number(event.target.value))
            break
        }
      }
    },
    nameParser(item: any) {
      if (item !== undefined) {
        if (item.name)
          return item.name

        return item
      }

      return 'Выберите из списка'
    },
  },

})
</script>

<template lang="">
  <div class="flex gap-2 flex-col ">
    <label
      :for="selectIn"
      class="block text-md text-gray-900"
    >{{ selectName }}</label>
    <div class="flex items-center gap-5">
      <select
        :id="selectIn"
        :name="selectIn"
        class="sm:max-w-md sm:leading-6 bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg flex w-full p-2 "
        @change="changeOption"
      >
        <option
          :key="curentOption.index"
          disabled
          default
          :value="curentOption.index"
          selected
        >
          {{ nameParser(curentOption.option) }}
        </option>
        <option
          v-for="(option, index) in options"
          :key="index"
          :value="index"
        >
          {{ nameParser(option) }}
        </option>
      </select>
      <div
        v-if="!$route.params.itemId"
        class="flex gap-2"
      >
        <svg
          v-if="selectName === 'Категория'"
          class="h-10 w-10 bg-gray-50 border border-gray-300 text-green-700 rounded-lg cursor-pointer hover:text-green-500"
          fill="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          @click="$emit('openAddPopup')"
        >
          <path
            clip-rule="evenodd"
            fill-rule="evenodd"
            d="M12 3.75a.75.75 0 01.75.75v6.75h6.75a.75.75 0 010 1.5h-6.75v6.75a.75.75 0 01-1.5 0v-6.75H4.5a.75.75 0 010-1.5h6.75V4.5a.75.75 0 01.75-.75z"
          />
        </svg>
        <svg
          v-if="selectName === 'Категория'"
          class="h-10 w-10 bg-gray-50 border border-gray-300 text-red-700 rounded-lg cursor-pointer hover:text-red-500"
          fill="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          @click="$emit('openDeletePopup')"
        >
          <path
            clip-rule="evenodd"
            fill-rule="evenodd"
            d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"
          />
        </svg>
        <svg
          v-if="selectName === 'Категория'"
          fill="none"
          stroke="currentColor"
          stroke-width="1.5"
          viewBox="0 0 24 24"
          class="h-10 w-10 bg-gray-50 border border-gray-300 text-yellow-700 rounded-lg cursor-pointer hover:text-yellow-500"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          @click="$emit('openUpdatePopup')"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
          />
        </svg>
      </div>
    </div>
  </div>
</template>
