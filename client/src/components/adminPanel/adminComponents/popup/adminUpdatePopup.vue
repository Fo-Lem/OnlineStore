<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

import type { ElementSelected } from '../adminPanelCreations.vue'
import type { catalog } from '../../../../controllers/productController'
import { Admin } from '../../adminControllers/adminControllers'
import AdminSelect from '../../UI/adminSelect.vue'
import AdminInput from '../../UI/adminInput.vue'
import AdminDropZone from '../../UI/adminDropZone.vue'

interface State {
  newValue: string
  selectedItem: number
  selectedHero: number
  selectedType: number
  selectedCategory: number
  selected: { [key: number]: string }
  photos: File[]
}
export default defineComponent({
  name: 'AdminUpdatePopup',
  components: { AdminSelect, AdminInput, AdminDropZone },
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
  emits: ['closeUpdatePopup', 'updateData'],
  data(): State {
    return {
      newValue: '',
      selectedItem: 0,
      selectedHero: 0,
      selectedType: 0,
      selectedCategory: 0,
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
      photos: [],
    }
  },
  methods: {
    updateSelectedItem(select: number) {
      this.selectedItem = select
      this.selectedCategory = 0
      this.selectedType = 0
      this.selectedHero = 0
      this.newValue = ''
    },
    updateSelectedCategory(select: number) {
      this.selectedCategory = select
      this.selectedType = 0
      this.newValue = ''
    },
    updateSelectedType(select: number) {
      this.selectedType = select
    },
    updateSelectedHero(select: number) {
      this.selectedHero = select
    },
    async updateItem() {
      if (this.selectedItem === 1) {
        if (this.photos.length > 0) {
          const updateItem = document.getElementById('updateItem') as HTMLFormElement
          const formData = new FormData(updateItem)
          const fd = new FormData()
          fd.append('file', formData.get('fileUpload') as FileList[0])
          fd.append('path', formData.get('name') as string)
          fd.append('name', `${formData.get('name')}.jpg`)
          await Admin.imageController.delete(this.catalog.categories[this.selectedCategory].cover_path)
          await Admin.imageController.create(fd)
          const cover_img = `../imgs/${formData.get('name')}/${formData.get('name')}.jpg`
          await Admin.categoryController.update(this.selectedCategory, this.newValue, cover_img)
        }
        else {
          await Admin.categoryController.update(this.selectedCategory, this.newValue)
        }
      }
      if (this.selectedItem === 2)
        await Admin.typeController.update(this.selectedType, this.newValue)
      if (this.selectedItem === 3)
        await Admin.heroController.update(this.selectedHero, this.newValue)
      this.$emit('updateData')
      this.$emit('closeUpdatePopup')
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
            id="updateItem"
            action="#"
            @submit.prevent="updateItem"
          >
            <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
              <AdminSelect
                :options="selected"
                select-in="Item"
                select-name="Что изменяем?"
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
              <AdminInput
                v-if="selectedItem === 1 && selectedCategory || selectedItem === 3 && selectedHero || selectedItem === 2 && selectedType"
                input-name="Новое название"
                :value="newValue"
                input-in="name"
                @update-input="(value) => newValue = value"
              />
              <AdminDropZone
                v-if="selectedItem === 1 && selectedCategory"
                :photos="photos"
                @upload-photo="(uploadPhoto) => photos = uploadPhoto"
              />
            </div>
            <div class=" flex flex-row-reverse">
              <button
                type="submit"
                class="inline-flex w-full justify-center rounded-md bg-yellow-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-yellow-500 sm:ml-3 sm:w-auto"
              >
                Изменить
              </button>
              <button
                type="button"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                @click="$emit('closeUpdatePopup')"
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
