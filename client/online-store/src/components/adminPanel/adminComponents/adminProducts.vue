<script>
import CustomSearchInput from '../../UI/customSearchInput.vue'

export default {
  name: 'AdminAnalytics',
  components: { CustomSearchInput },
  props: {
    catalog: {
      type: Object,
      required: true,
    },
    isAdminAuth: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['updateData'],
  data() {
    return {
      searchQuery: '',
    }
  },
  computed: {
    searchedItems() {
      const searchObj = {}
      for (const [key, obj] of Object.entries(this.catalog.items)) {
        if (obj.name.toLowerCase().includes(this.searchQuery.toLowerCase()))
          searchObj[key] = obj
      }
      return searchObj
    },
  },
  methods: {
    deleteItem(product) {
      for (let i = 0; i < 3; i++)
        this.Admin.imageController.delete(`${product.img_path}/${product.art}_${i}.jpg`)

      this.Admin.productController.delete(product.id)

      this.$emit('updateData')
    },

  },
}
</script>

<template lang="">
  <div class="relative flex flex-col gap-5 ">
    <CustomSearchInput @update-search-input="(value) => { searchQuery = value }" />
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
