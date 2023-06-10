<template lang="">
    <div class="relative  z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
      
        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:ml-64 sm:items-center sm:p-0">
            <div class="relative overflow-hidden rounded-lg bg-white text-left p-5 shadow-xl ">
              <form id="updateItem" @submit.prevent="updateItem" action="#">
              <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
                <admin-select 
                v-bind:options="selected"
                v-bind:selectIn="'Item'"
                v-bind:selectName="'Что изменяем?'"
                @changeOptionItem="(select)=>updateSelectedItem(select)"
                ></admin-select>
                
                <admin-select
                :key="selectedItem"
                v-if="selectedItem==1||selectedItem==2" 
                v-bind:options="categorys"
                v-bind:selectIn="'Category'"
                v-bind:selectName="'Выберите категорию'"
                @changeOptionCategory="(select)=>updateSelectedCategory(select)"
                ></admin-select>
                <admin-select
                :key="selectedCategory"
                v-if="selectedItem==2&&selectedCategory" 
                v-bind:options="catalog.categories[selectedCategory].product_types"
                v-bind:selectIn="'Type'"
                v-bind:selectName="'Выберите тип'"
                @changeOptionType="(select)=>updateSelectedType(select)"
                ></admin-select>
                <admin-select
                :key="selectedItem"
                v-if="selectedItem==3" 
                v-bind:options="catalog.heroes"
                v-bind:selectIn="'Hero'"
                v-bind:selectName="'Выберите героя'"
                @changeOptionHero="(select)=>updateSelectedHero(select)"
                ></admin-select>
                <admin-input v-if="selectedItem==1&&selectedCategory||selectedItem==3&&selectedHero ||selectedItem==2&&selectedType"
                v-bind:inputName="'Новое название'"
                v-bind:value="newValue"
                v-bind:inputIn="'name'"
                @updateInput="(value)=>newValue=value"
                ></admin-input>
                <admin-drop-zone v-if="selectedItem==1&&selectedCategory" v-bind:photos="photos" @uploadPhoto="uploadPhoto"></admin-drop-zone> 
              </div>
              <div class="bg-gray-50  flex flex-row-reverse">
                <button type="submit" class="inline-flex w-full justify-center rounded-md bg-yellow-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-yellow-500 sm:ml-3 sm:w-auto">Изменить</button>
                <button @click="$emit('closeUpdatePopup')" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Отмена</button>
              </div>
            </form>
            </div>
          </div>
        </div>
      </div>
      
</template>
<script>
export default {
  name: 'admin-update-popup',
  data() {
    return {
      newValue: '',
      selectedItem: '',
      selectedHero: '',
      selectedType: '',
      selectedCategory: '',
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
      photos: [],
      uploadPhoto: ''
    }
  },
  props: {
    categorys: {
      type: Object,
      require: true
    },
    catalog: {
      type: Object,
      require: true
    },
    AdminController: {
      type: Object,
      require: true
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

      if (this.selectedItem == 1) {
        if (this.photos.length > 0) {
          let formData = new FormData(updateItem)
          let fd = new FormData()
          fd.append('file', formData.get('fileUpload'))
          fd.append('path', formData.get('name'))
          fd.append('name', `${formData.get('name')}.jpg`)
          await this.AdminController.imageController.deleteImage(this.catalog.categories[this.selectedCategory].cover_path)
          await this.AdminController.imageController.createImage(fd)
          const cover_img = `../imgs/${formData.get('name')}/${formData.get('name')}.jpg`
          await this.AdminController.categoryController.updateCategory(this.selectedCategory, this.newValue, cover_img)
        } else {
          await this.AdminController.categoryController.updateCategory(this.selectedCategory, this.newValue)
        }
      }
      if (this.selectedItem == 2) {
        await this.AdminController.typeController.updateType(this.selectedType, this.newValue)
      }
      if (this.selectedItem == 3) {
        console.log(this.selectedHero, this.newValue)
        await this.AdminController.heroController.updateHero(this.selectedHero, this.newValue)
      }
      this.$emit('updateData')
      this.$emit('closeUpdatePopup')
      
    }
  },
  emits: ['closeUpdatePopup','updateData']

}
</script>