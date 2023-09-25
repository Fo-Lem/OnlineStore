<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import CustomSearchInput from '../../UI/customSearchInput.vue'
import type { catalog, catalogItem, catalogItems } from '../../../controllers/productController'
import { Admin } from '../adminControllers/adminControllers'

interface State {
  searchQuery: string
}
export default defineComponent({
  name: 'AdminAnalytics',
  components: { CustomSearchInput },
  props: {
    catalog: {
      type: Object as PropType<catalog>,
      required: true,
    },
    isAdminAuth: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['updateData'],
  data(): State {
    return {
      searchQuery: '',

    }
  },
  computed: {
    searchedItems(): catalogItems {
      const searchObj = {} as catalogItems
      for (const key in this.catalog.items) {
        const item = this.catalog.items[key]
        if (item.name.toLowerCase().includes(this.searchQuery.toLowerCase()))
          searchObj[key] = item
      }
      return searchObj
    },
  },
  methods: {
    deleteItem(product: catalogItem) {
      for (let i = 0; i < 3; i++)
        Admin.imageController.delete(`${product.img_path}/${product.art}_${i}.jpg`)

      Admin.productController.delete(product.id)

      this.$emit('updateData')
    },

  },
})
</script>

<template>
  <div class="relative flex flex-col gap-5 ">
    <CustomSearchInput @update-search-input="(value:string) => { searchQuery = value }" />
    <table class="w-full text-sm text-left text-gray-500 ">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 ">
        <tr>
          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Артикул
            </div>
          </th>
          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Название
            </div>
          </th>
          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Категория
            </div>
          </th>
          <th
            scope="col"
            class=" py-3  px-6"
          >
            <div class="flex items-center">
              Тип
            </div>
          </th>
          <th
            scope="col"
            class=" py-3 px-6 "
          >
            <div class="flex items-center">
              Герой
            </div>
          </th>

          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Описание
            </div>
          </th>
          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Размеры
            </div>
          </th>
          <th
            scope="col"
            class=" py-3 px-6"
          >
            <div class="flex items-center">
              Цена
            </div>
          </th>
          <th
            scope="col"
            class=" py-3"
          >
            <span class="sr-only">Edit and Delete</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(product, index) in searchedItems"
          :key="index"
          class="bg-white  hover:bg-gray-50 "
        >
          <td
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 gap-5 whitespace-nowrap "
          >
            C{{ product.art.split('C')[1] }}
          </td>
          <td
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 gap-5 whitespace-nowrap "
          >
            {{ product.name }}
          </td>
          <td class="px-6 py-4">
            {{ catalog.categories[product.category_id].name }}
          </td>
          <td class="px-6 py-4">
            {{ catalog.categories[product.category_id].product_types[product.product_type_id].name }}
          </td>
          <td class="px-6 py-4">
            {{ catalog.heroes[product.hero_id].name }}
          </td>
          <td class="py-4 relative max-w-sm w-96 ">
            <p class="text-ellipsis px-6 w-96 overflow-hidden whitespace-nowrap hover:px-6 hover:py-4 hover:z-50 hover:block hover:bg-gray-50 hover:rounded-md hover:whitespace-normal hover:absolute hover:top-3 hover:text-clip hover:overflow-visible">
              {{ product.description }}
            </p>
          </td>
          <td class="px-6 py-4">
            {{ product.size }}
          </td>
          <td class="px-6 py-4">
            {{ product.price }}р
          </td>
          <td class="px-6 py-4 flex flex-col gap-2">
            <router-link
              class="font-medium text-blue-700 text-center hover:underline"
              :to="{ name: 'panelUpdate', params: { itemId: product.id } }"
            >
              Изменить
            </router-link>
            <button
              class="font-medium text-red-700  hover:underline"
              @click="deleteItem(product)"
            >
              Удалить
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
