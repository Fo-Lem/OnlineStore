<template lang="">
    <div class="relative  z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
      
        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:ml-64 sm:items-center sm:p-0">
            <div class="relative overflow-hidden rounded-lg bg-white text-left p-5 shadow-xl ">
              <form id="deleteItem" @submit.prevent="deleteItem" action="#">
              <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
                <admin-select 
                v-bind:options="selected"
                v-bind:selectIn="'Item'"
                v-bind:selectName="'Что удаляем?'"
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
              </div>
              <div class="bg-gray-50  flex flex-row-reverse">
                <button type="submit" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-reg-500 sm:ml-3 sm:w-auto">Удалить</button>
                <button @click="$emit('closeDeletePopup')" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Отмена</button>
              </div>
            </form>
            </div>
          </div>
        </div>
      </div>
      
</template>
<script>
export default {
  name: 'admin-delete-popup',

  emits: ['closeDeletePopup', 'updateData'],

  data() {
    return {
      selectedItem: '',
      selectedHero: '',
      selectedType: '',
      selectedCategory: '',
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' }
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
    },
    updateSelectedCategory(select) {
      this.selectedCategory = select
      this.selectedType = ''
    },
    updateSelectedType(select) {
      this.selectedType = select
    },
    updateSelectedHero(select) {
      this.selectedHero = select

    },
    uploadPhoto(photos) {
      this.photos = photos

    },
    async deleteItem() {
      if (this.selectedItem == 1) {
        await this.AdminController.imageController.deleteImage(this.catalog.categories[this.selectedCategory].cover_path)
        await this.AdminController.categoryController.deleteCategory(this.selectedCategory)
      }
      if (this.selectedItem == 2) {
        await this.AdminController.typeController.deleteType(this.selectedType)
      }
      if (this.selectedItem == 3) {
        await this.AdminController.heroController.deleteHero(this.selectedHero)
      }


      this.selectedItem = ''
      this.selectedCategory = ''
      this.selectedType = ''
      this.selectedHero = ''
      this.$emit('updateData')
      this.$emit('closeDeletePopup')
    }
  }

}
</script>