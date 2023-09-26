<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { ElementSelected } from '../adminPanelCreations.vue'
import AdminSelect from '../../UI/adminSelect.vue'
import AdminInput from '../../UI/adminInput.vue'
import AdminDropZone from '../../UI/adminDropZone.vue'
import { Admin } from '../../adminControllers/adminControllers'

// import { Admin } from '../../adminControllers/adminControllers'
interface State {
  newItem: string
  selectedItem: number
  selectedCategory: number
  selected: { 1: 'Категорию'; 2: 'Тип'; 3: 'Героя' }
  photos: FileList[]
}
export default defineComponent({
  name: 'AdminAddPopup',
  components: { AdminSelect, AdminInput, AdminDropZone },
  props: {
    categories: {
      type: Object as PropType<ElementSelected>,
      required: true,
    },
  },
  emits: {
    closeAddPopup() {
      return true
    },
    updateData() {
      return true
    },
  },
  data(): State {
    return {
      newItem: '',
      selectedItem: 0,
      selectedCategory: 0,
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
      photos: [],
    }
  },
  methods: {
    updateSelectedItem(select: number) {
      this.selectedItem = select
    },
    updateSelectedCategory(select: number) {
      this.selectedCategory = select
    },
    uploadPhoto(photos: FileList[]) {
      this.photos = photos
    },
    async createItem() {
      const newItem = document.getElementById('newItem') as HTMLFormElement
      const formData = new FormData(newItem)
      const select = Number(formData.get('Item'))

      if (select === 1) {
        const fd = new FormData()
        fd.append('file', newItem.get('fileUpload'))
        fd.append('path', newItem.get('name'))
        fd.append('name', `${newItem.get('name')}.jpg`)
        await Admin.imageController.create(fd)
        const obj = {
          name: formData.get('name') as string,
          cover_img: `../imgs/${formData.get('name')}/${formData.get('name')}.jpg`,
        }
        await Admin.categoryController.create(obj.name, obj.cover_img)
      }
      if (select === 2) {
        const obj = {
          name: formData.get('name') as string,
          category_id: Number(formData.get('Category')),
        }
        await Admin.typeController.create(obj.category_id, obj.name)
      }
      if (select === 3) {
        const obj = {
          name: formData.get('name') as string,
        }
        await Admin.heroController.create(obj.name)
      }
      this.$emit('updateData')
      this.$emit('closeAddPopup')
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
            id="newItem"
            action="#"
            @submit.prevent="createItem"
          >
            <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
              <AdminSelect
                :options="selected"
                select-in="Item"
                select-name="Что создаем?"
                @change-option-item="(select) => updateSelectedItem(select)"
              />
              <AdminSelect
                v-if="selectedItem === 2"
                :options="categories"
                select-in="Category"
                select-name="Выберите категорию"
                @change-option-category="(select) => updateSelectedCategory(select)"
              />
              <AdminInput
                v-if="selectedItem"
                input-name="Название"
                :value="newItem"
                input-in="name"
                @update-input="(value) => newItem = value"
              />
              <AdminDropZone
                v-if="selectedItem === 1"
                :photos="photos"
                @upload-photo="uploadPhoto"
              />
            </div>
            <div class="bg-gray-50  flex flex-row-reverse">
              <button
                type="submit"
                class="inline-flex w-full justify-center rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 sm:ml-3 sm:w-auto"
              >
                Создать
              </button>
              <button
                type="button"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                @click="$emit('closeAddPopup')"
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
