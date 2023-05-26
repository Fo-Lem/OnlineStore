<template lang="">
    <div class="relative  z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
      
        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:ml-64 sm:items-center sm:p-0">
            <div class="relative overflow-hidden rounded-lg bg-white text-left p-5 shadow-xl ">
              <form id="createItem" @submit.prevent="createItem" action="#">
              <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
                <admin-select 
                v-bind:options="selected"
                v-bind:selectIn="'Item'"
                v-bind:selectName="'Что создаем?'"
                @changeOptionItem="(select)=>updateSelectedItem(select)"
                ></admin-select>
                <admin-select
                v-if="selectedItem==2" 
                v-bind:options="categorys"
                v-bind:selectIn="'Category'"
                v-bind:selectName="'Выберите категорию'"
                @changeOptionCategory="(select)=>updateSelectedCategory(select)"
                ></admin-select>
                <admin-input v-if="selectedItem"
                v-bind:inputName="'Название'"
                v-bind:value="newItem"
                v-bind:inputIn="'name'"
                @updateInput="(value)=>newItem=value"
                ></admin-input>
                <admin-drop-zone v-if="selectedItem==1" v-bind:photos="photos" @uploadPhoto="uploadPhoto"></admin-drop-zone> 
              </div>
              <div class="bg-gray-50  flex flex-row-reverse">
                <button type="submit" class="inline-flex w-full justify-center rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 sm:ml-3 sm:w-auto">Создать</button>
                <button @click="$emit('closePopup')" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Отмена</button>
              </div>
            </form>
            </div>
          </div>
        </div>
      </div>
      
</template>
<script>
export default {
  name: 'admin-popup',
  data() {
    return {
      newItem: '',
      selectedItem: '',
      selectedCategory:'',
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя' },
      photos: []
    }
  },
  props: {
    categorys: {
      type: Object,
      require: true
    }
  },
  methods: {
    updateSelectedItem(select) {
      this.selectedItem = select
    },
    updateSelectedCategory(select) {
      this.selectedCategory = select
    },
    uploadPhoto(photos) {
      this.photos = photos

    },
    createItem(){
      let formData = new FormData(createItem)
      let select = formData.get('Item')
      if(select == 1){
        console.log(
        formData.get('Item'),
        formData.get('name'),
        formData.get('fileUpload')
      
      )}
      if(select == 2){
        console.log(
        formData.get('Item'),
        formData.get('Category'),
        formData.get('name'),
      
      )}
      if(select == 3){
        console.log(
        formData.get('Item'),
        formData.get('name')
      
      )
      }
      
      
      
       this.$emit('closePopup')
    }
  },
  emits: ['closePopup']

}
</script>