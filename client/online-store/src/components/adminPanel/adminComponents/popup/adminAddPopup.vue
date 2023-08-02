<script>
export default {
  name: 'AdminAddPopup',
  props: {
    categorys: {
      type: Object,
      require: true,
    },
    AdminController: {
      type: Object,
      require: true,
    },
  },
  emits: ['closeAddPopup', 'updateData'],
  data() {
    return {
      newItem: '',
      selectedItem: '',
      selectedCategory: '',
      selected: { 1: 'Категорию', 2: 'Тип', 3: 'Героя', },
      photos: [],
    };
  },
  methods: {
    updateSelectedItem(select) {
      this.selectedItem = select;
    },
    updateSelectedCategory(select) {
      this.selectedCategory = select;
    },
    uploadPhoto(photos) {
      this.photos = photos;

    },
    async createItem() {
      let formData = new FormData(createItem);
      let select = formData.get('Item');
      if (select == 1) {
        let fd = new FormData();
        fd.append('file', formData.get('fileUpload'));
        fd.append('path', formData.get('name'));
        fd.append('name', `${ formData.get('name') }.jpg`);
        await this.AdminController.imageController.createImage(fd);
        const obj = {
          name: formData.get('name'),
          cover_img: `../imgs/${ formData.get('name') }/${ formData.get('name') }.jpg`,
        };
        this.AdminController.categoryController.createCategory(obj);

      }
      if (select == 2) {
        const obj = {
          name: formData.get('name'),
          category_id: `${ formData.get('Category') }`,
        };
        await this.AdminController.typeController.createType(obj);
      }
      if (select == 3) {
        const obj = {
          name: formData.get('name'),
        };
        await this.AdminController.heroController.createHero(obj);
      }

      this.$emit('updateData');
      this.$emit('closeAddPopup');
    },
  },

};
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
            id="createItem"
            action="#"
            @submit.prevent="createItem"
          >
            <div class="bg-white flex flex-col w-74 sm:w-96 gap-5 mb-5">
              <admin-select
                :options="selected"
                select-in="Item"
                select-name="Что создаем?"
                @changeOptionItem="(select) => updateSelectedItem(select)"
              />
              <admin-select
                v-if="selectedItem == 2"
                :options="categorys"
                select-in="Category"
                select-name="Выберите категорию"
                @changeOptionCategory="(select) => updateSelectedCategory(select)"
              />
              <admin-input
                v-if="selectedItem"
                input-name="Название"
                :value="newItem"
                input-in="name"
                @updateInput="(value) => newItem = value"
              />
              <admin-drop-zone
                v-if="selectedItem == 1"
                :photos="photos"
                @uploadPhoto="uploadPhoto"
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
