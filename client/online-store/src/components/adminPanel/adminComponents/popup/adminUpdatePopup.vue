<script>
export default {
  name: 'AdminUpdatePopup',
  props: {
    categorys: {
      type: Object,
      require: true,
    },
    catalog: {
      type: Object,
      require: true,
    },
    adminController: {
      type: Object,
      require: true,
    },
  },
  emits: ['closeUpdatePopup', 'updateData'],
  data() {
    return {
      newValue: '',
      selectedItem: '',
      selectedHero: '',
      selectedType: '',
      selectedCategory: '',
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
      photos: [],
      uploadPhoto: '',
    }
  },
  methods: {
    updateSelectedItem(select) {
      this.selectedItem = select
      this.selectedCategory = ''
      this.selectedType = ''
      this.selectedHero = ''
      this.newValue = ''
    },
    updateSelectedCategory(select) {
      this.selectedCategory = select
      this.selectedType = ''
      this.newValue = ''
    },
    updateSelectedType(select) {
      this.selectedType = select
    },
    updateSelectedHero(select) {
      this.selectedHero = select
    },
    async updateItem() {
      if (this.selectedItem === 1) {
        if (this.photos.length > 0) {
          const formData = new FormData(updateItem)
          const fd = new FormData()
          fd.append('file', formData.get('fileUpload'))
          fd.append('path', formData.get('name'))
          fd.append('name', `${formData.get('name')}.jpg`)
          await this.AdminController.imageController.deleteImage(this.catalog.categories[this.selectedCategory].cover_path)
          await this.AdminController.imageController.createImage(fd)
          const cover_img = `../imgs/${formData.get('name')}/${formData.get('name')}.jpg`
          await this.AdminController.categoryController.updateCategory(this.selectedCategory, this.newValue, cover_img)
        }
        else {
          await this.AdminController.categoryController.updateCategory(this.selectedCategory, this.newValue)
        }
      }
      if (this.selectedItem === 2)
        await this.AdminController.typeController.updateType(this.selectedType, this.newValue)

      if (this.selectedItem === 3) {
        // console.log(this.selectedHero, this.newValue)
        await this.AdminController.heroController.updateHero(this.selectedHero, this.newValue)
      }
      this.$emit('updateData')
      this.$emit('closeUpdatePopup')
    },
  },

}
</script>

<template lang="">
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
              <admin-select
                :options="selected"
                select-in="Item"
                select-name="Что изменяем?"
                @change-option-iotem="(select) => updateSelectedItem(select)"
              />

              <admin-select
                v-if="selectedItem === 1 || selectedItem === 2"
                :key="selectedItem"
                :options="categorys"
                select-in="Category"
                select-name="Выберите категорию"
                @change-option-category="(select) => updateSelectedCategory(select)"
              />
              <admin-select
                v-if="selectedItem === 2 && selectedCategory"
                :key="selectedCategory"
                :options="catalog.categories[selectedCategory].product_types"
                select-in="Type"
                select-name="Выберите тип"
                @change-option-type="(select) => updateSelectedType(select)"
              />
              <admin-select
                v-if="selectedItem === 3"
                :key="selectedItem"
                :options="catalog.heroes"
                select-in="Hero"
                select-name="Выберите героя"
                @change-option-hero="(select) => updateSelectedHero(select)"
              />
              <admin-input
                v-if="selectedItem === 1 && selectedCategory || selectedItem === 3 && selectedHero || selectedItem === 2 && selectedType"
                input-name="Новое название"
                :value="newValue"
                input-in="name"
                @update-input="(value) => newValue = value"
              />
              <admin-drop-zone
                v-if="selectedItem === 1 && selectedCategory"
                :photos="photos"
                @upload-photo="uploadPhoto"
              />
            </div>
            <div class="bg-gray-50  flex flex-row-reverse">
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
