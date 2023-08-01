<template>
  <admin-add-popup v-if="openAddPopup" @updateData="$emit('updateData')" @closeAddPopup="openAddPopup = !openAddPopup"
    v-bind:AdminController="AdminController" v-bind:categorys="getElementSelected(catalog.categories)"></admin-add-popup>
  <admin-delete-popup v-if="openDeletePopup" @updateData="$emit('updateData')"
    @closeDeletePopup="openDeletePopup = !openDeletePopup" v-bind:AdminController="AdminController"
    v-bind:catalog="catalog" v-bind:categorys="getElementSelected(catalog.categories)"></admin-delete-popup>
  <admin-update-popup v-if="openUpdatePopup" @updateData="$emit('updateData')"
    @closeUpdatePopup="openUpdatePopup = !openUpdatePopup" v-bind:catalog="catalog"
    v-bind:categorys="getElementSelected(catalog.categories)"
    v-bind:AdminController="AdminController"></admin-update-popup>

  <form @submit.prevent="AddProduct" class="flex flex-col gap-5">
    <admin-input v-bind:inputName="'Название продукта'" v-bind:inputIn="'productName'"
      v-bind:placeholder="`Меч длинный &laquoАлеша Попович&raquo`" v-bind:value="newProduct.productName"
      @updateInput="(value) => newProduct.productName = value">
    </admin-input>

    <admin-select :key="newProduct.productName" v-bind:options="getElementSelected(catalog.categories)"
      v-bind:selectIn="'Category'" v-bind:selectName="'Категория'"
      @changeOptionCategory="(select) => updateSelectedCategory(select)" @openAddPopup="openAddPopup = true"
      @openDeletePopup="openDeletePopup = true" @openUpdatePopup="openUpdatePopup = true">
    </admin-select>

    <admin-select v-if="newProduct.selected['category']" :key="newProduct.selected['category']"
      v-bind:options="getElementSelected(catalog.categories[newProduct.selected['category']].product_types)"
      v-bind:selectIn="'Type'" v-bind:selectName="'Тип'" @changeOptionType="(select) => updateSelectedType(select)">
    </admin-select>
    <admin-select v-if="newProduct.selected['type']" :key="newProduct.selected['type']"
      v-bind:options="getElementSelected(catalog.heroes)" v-bind:selectIn="'Hero'" v-bind:selectName="'Герой'"
      @changeOptionHero="(select) => newProduct.selected['hero'] = select">
    </admin-select>

    <div class="flex flex-col gap-2">
      <div>
        <h2 class=" text-md leading-6">Размеры</h2>
        <p class=" text-xs leading-6 text-gray-400">(Размеры в милиметрах)</p>
      </div>

      <admin-input v-for="(item, index) in newProduct.size" :key="index" v-bind:inputName="size[index]"
        v-bind:inputIn="index" v-bind:placeholder="'300'" v-bind:value="newProduct.size[index]"
        @updateInput="(value) => newProduct.size[index] = value">
      </admin-input>

    </div>

    <div class="flex flex-col gap-2">
      <label for="message" class="block text-md text-gray-900">Описание</label>
      <textarea id="message" v-model="newProduct.description" rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
        placeholder="Write your thoughts here..."></textarea>
    </div>
    <admin-input v-bind:inputName="'Цена'" v-bind:inputIn="'price'" v-bind:placeholder="`3000`"
      v-bind:value="newProduct.price" @updateInput="(value) => newProduct.price = value">
    </admin-input>

    <admin-drop-zone v-bind:photos="newProduct.photos" @uploadPhoto="uploadPhoto"></admin-drop-zone>

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <button type="button" @click="remoteNewProduct"
        class="text-sm font-semibold leading-6 text-gray-900">Сбросить</button>
      <button type="submit"
        class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Добавить</button>
    </div>
  </form>
</template>
<script>
import adminAddPopup from './popup/adminAddPopup.vue'
import adminDeletePopup from './popup/adminDeletePopup.vue'
import adminUpdatePopup from './popup/adminUpdatePopup.vue'
export default {
  components: { adminAddPopup, adminDeletePopup, adminUpdatePopup },
  name: 'admin-panel-creations',
  emits: ['updateData'],
  data() {
    return {
      openAddPopup: false,
      openDeletePopup: false,
      openUpdatePopup: false,
      size: {
        height: 'Высота',
        width: 'Ширина',
        depth: 'Глубина'
      },
      newProduct: {
        productName: '',
        selected: {
          category: '',
          type: '',
          hero: ''
        },
        size: {
          height: '',
          width: '',
          depth: ''
        },
        description: '',
        price: '',
        photos: []
      }
    }
  },
  props: {
    catalog: {
      type: Object,
      require: true
    },
    Admin: {
      type: Object,
      require: true
    }
  },

  methods: {

    getElementSelected(items) {
      console.log()
      console.log(items)
      const res = {}
      for (var key in items) {
        res[key] = items[key].name
      }
      return res
    },
    updateSelectedCategory(select) {
      this.newProduct.selected['category'] = select
      this.newProduct.selected['type'] = ''
      this.newProduct.selected['hero'] = ''
    },
    updateSelectedType(select) {
      this.newProduct.selected['type'] = select
      this.newProduct.selected['hero'] = ''
    },
    uploadPhoto(photos) {
      this.newProduct.photos = photos

    },
    async AddProduct() {
      console.log(this.newProduct)
      let count = 0
      for (const item in this.catalog.items) {
        const cItem = this.catalog.items[item]
        if (cItem.category_id == this.newProduct.selected.category && cItem.product_type_id == this.newProduct.selected.type && cItem.hero_id == this.newProduct.selected.hero) {
          count++
        }
      }
      const obj = {
        name: this.newProduct.productName,
        category_id: this.newProduct.selected.category,
        product_type_id: this.newProduct.selected.type,
        hero_id: this.newProduct.selected.hero,
        description: this.newProduct.description,
        art: `D${Date.now()}C${this.newProduct.selected.category}T${this.newProduct.selected.type}H${this.newProduct.selected.hero}V${count + 1}`,
        img_path: `/imgs/items/${this.catalog.categories[this.newProduct.selected.category].name}`,
        size: `${this.newProduct.size.height}x${this.newProduct.size.width}x${this.newProduct.size.depth}`,
        price: this.newProduct.price
      }
      this.newProduct.photos.forEach(async (photo, index) => {
        let fd = new FormData()
        fd.append('file', photo)
        fd.append('path', `items/${this.catalog.categories[obj.category_id].name}`)
        fd.append('name', `${obj.art + '_' + index}.jpg`)
        await this.Admin.imageController.create(fd)
      });
      await this.Admin.productController.create(obj)
      this.$emit('updateData')
      this.remoteNewProduct()
    },
    remoteNewProduct() {
      this.newProduct = {
        productName: '',
        selected: {
          category: '',
          type: '',
          hero: ''
        },
        size: {
          height: '',
          width: '',
          depth: ''
        },
        description: '',
        price: '',
        photos: []
      }
    }


  }
}
</script>