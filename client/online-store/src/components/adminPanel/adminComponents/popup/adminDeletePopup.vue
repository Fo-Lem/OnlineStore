<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog } from '../../../../controllers/productController'
import { Admin } from '../../adminControllers/adminControllers'
import type { ElementSelected } from '../adminPanelCreations.vue'
import AdminSelect from '../../UI/adminSelect.vue'

interface State {
  selectedItem: number
  selectedHero: number
  selectedType: number
  selectedCategory: number
  selected: { [key: number]: string }
}
export default defineComponent({
  name: 'AdminDeletePopup',
  components: { AdminSelect },
  props: {
    categories: {
      type: Object as PropType<ElementSelected>,
      required: true,
    },
    catalog: {
      type: Object as PropType<catalog>,
      required: true,
    },
  },
  emits: ['closeDeletePopup', 'updateData'],
  data(): State {
    return {
      selectedItem: 0,
      selectedHero: 0,
      selectedType: 0,
      selectedCategory: 0,
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
    }
  },
  methods: {
    updateSelectedItem(select: number) {
      this.selectedItem = select
      this.selectedCategory = 0
      this.selectedType = 0
      this.selectedHero = 0
    },
    updateSelectedCategory(select: number) {
      this.selectedCategory = select
      this.selectedType = 0
    },
    updateSelectedType(select: number) {
      this.selectedType = select
    },
    updateSelectedHero(select: number) {
      this.selectedHero = select
    },
    async deleteItem() {
      if (this.selectedItem === 1) {
        await Admin.imageController.delete(this.catalog.categories[this.selectedCategory].cover_path)
        await Admin.categoryController.delete(this.selectedCategory)
      }
      if (this.selectedItem === 2)
        await Admin.typeController.delete(this.selectedType)
      if (this.selectedItem === 3)
        await Admin.heroController.delete(this.selectedHero)
      this.selectedItem = 0
      this.selectedCategory = 0
      this.selectedType = 0
      this.selectedHero = 0
      this.$emit('updateData')
      this.$emit('closeDeletePopup')
    },
  },
})
</script>

<template>
  <div
    class="relative  z-10"
    aria-labelledby="modal-title"
    role="dialog"
    aria-modal="true"
  >
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />

    <div class="fixed inset-0 z-10 overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:ml-64 sm:items-center sm:p-0">
        <div class="relative overflow-hidden rounded-lg bg-white text-left p-5 shadow-xl ">
          <form
            id="deleteItem"
            action="#"
            @submit.prevent="deleteItem"
          >
            <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
              <AdminSelect
                :options="selected"
                select-in="Item"
                select-name="Что удаляем?"
                @change-option-item="(select) => updateSelectedItem(select)"
              />
              <AdminSelect
                v-if="selectedItem === 1 || selectedItem === 2"
                :key="selectedItem"
                :options="categories"
                select-in="Category"
                select-name="Выберите категорию"
                @change-option-category="(select) => updateSelectedCategory(select)"
              />
              <AdminSelect
                v-if="selectedItem === 2 && selectedCategory"
                :key="selectedCategory"
                :options="catalog.categories[selectedCategory].product_types"
                select-in="Type"
                select-name="Выберите тип"
                @change-option-type="(select) => updateSelectedType(select)"
              />
              <AdminSelect
                v-if="selectedItem === 3"
                :key="selectedItem"
                :options="catalog.heroes"
                select-in="Hero"
                select-name="Выберите героя"
                @change-option-hero="(select) => updateSelectedHero(select)"
              />
            </div>
            <div class="bg-gray-50  flex flex-row-reverse">
              <button
                type="submit"
                class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-reg-500 sm:ml-3 sm:w-auto"
              >
                Удалить
              </button>
              <button
                type="button"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                @click="$emit('closeDeletePopup')"
              >
                Отмена
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
