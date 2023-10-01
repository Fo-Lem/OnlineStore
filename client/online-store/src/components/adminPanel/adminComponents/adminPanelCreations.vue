<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog, catalogCategories, catalogHeroes, catalogTypes } from '../../../controllers/productController'
import { Admin } from '../adminControllers/adminControllers'
import AdminInput from '../UI/adminInput.vue'
import AdminSelect from '../UI/adminSelect.vue'
import AdminDropZone from '../UI/adminDropZone.vue'
import AdminAddPopup from './popup/adminAddPopup.vue'
import AdminDeletePopup from './popup/adminDeletePopup.vue'
import AdminUpdatePopup from './popup/adminUpdatePopup.vue'

interface State {
  openAddPopup: boolean
  openDeletePopup: boolean
  openUpdatePopup: boolean
  size: {
    height: string
    width: string
    depth: string
  }
  newProduct: {
    productName: string
    selected: {
      category: number
      type: number
      hero: number
    }
    size: {
      height: number
      width: number
      depth: number
    }
    description: string
    price: number
    photos: File[]
  }

}
export interface ElementSelected {
  [key: number]: string
}

export default defineComponent({
  name: 'AdminPanelCreations',
  components: { AdminAddPopup, AdminDeletePopup, AdminUpdatePopup, AdminInput, AdminSelect, AdminDropZone },
  props: {
    catalog: {
      type: Object as PropType<catalog>,
      required: true,
    },
    isAdminAuth: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['updateData', 'isAdminAuth'],
  data(): State {
    return {
      openAddPopup: false,
      openDeletePopup: false,
      openUpdatePopup: false,
      size: {
        height: 'Высота',
        width: 'Ширина',
        depth: 'Глубина',
      },
      newProduct: {
        productName: '',
        selected: {
          category: 0,
          type: 0,
          hero: 0,
        },
        size: {
          height: 0,
          width: 0,
          depth: 0,
        },
        description: '',
        price: 0,
        photos: [],
      },
    }
  },

  methods: {

    getElementSelected(items: catalogTypes | catalogCategories | catalogHeroes) {
      const res: ElementSelected = {}
      for (const key in items)
        res[key] = items[key].name

      return res
    },
    updateSelectedCategory(select: number) {
      this.newProduct.selected.category = select
      this.newProduct.selected.type = 0
      this.newProduct.selected.hero = 0
    },
    updateSelectedType(select: number) {
      this.newProduct.selected.type = select
      this.newProduct.selected.hero = 0
    },
    uploadPhoto(photos: File[]) {
      this.newProduct.photos = photos
    },
    async AddProduct() {
      // console.log(this.newProduct)
      let count = 0
      for (const item in this.catalog.items) {
        const cItem = this.catalog.items[item]
        if (cItem.category_id === this.newProduct.selected.category && cItem.product_type_id === this.newProduct.selected.type && cItem.hero_id === this.newProduct.selected.hero)
          count++
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
        price: this.newProduct.price,
      }
      this.newProduct.photos.forEach(async (photo, index) => {
        const fd = new FormData()
        fd.append('file', photo)
        fd.append('path', `items/${this.catalog.categories[obj.category_id].name}`)
        fd.append('name', `${`${obj.art}_${index}`}.jpg`)
        await Admin.imageController.create(fd)
      })
      await Admin.productController.create(obj.name, obj.category_id, obj.product_type_id, obj.hero_id, obj.description, obj.art, obj.img_path, obj.size, obj.price)
      this.$emit('updateData')
      this.remoteNewProduct()
    },
    remoteNewProduct() {
      this.newProduct = {
        productName: '',
        selected: {
          category: 0,
          type: 0,
          hero: 0,
        },
        size: {
          height: 0,
          width: 0,
          depth: 0,
        },
        description: '',
        price: 0,
        photos: [],
      }
    },

  },
})
</script>

<template>
  <AdminAddPopup
    v-if="openAddPopup"
    :categories="getElementSelected(catalog.categories)"
    @update-data="$emit('updateData')"
    @close-add-popup="openAddPopup = false"
  />
  <AdminDeletePopup
    v-if="openDeletePopup"
    :catalog="catalog"
    :categories="getElementSelected(catalog.categories)"
    @update-data="$emit('updateData')"
    @close-delete-popup="openDeletePopup = false"
  />
  <AdminUpdatePopup
    v-if="openUpdatePopup"
    :catalog="catalog"
    :categories="getElementSelected(catalog.categories)"
    @update-data="$emit('updateData')"
    @close-update-popup="openUpdatePopup = false"
  />

  <form
    class="flex flex-col gap-5"
    @submit.prevent="AddProduct"
  >
    <AdminInput
      input-name="Название продукта"
      input-in="productName"
      placeholder="Меч длинный &laquoАлеша Попович&raquo"
      :value="newProduct.productName"
      @update-input="(value: string) => newProduct.productName = value"
    />

    <AdminSelect
      :key="newProduct.productName"
      :options="getElementSelected(catalog.categories)"
      select-in="Category"
      select-name="Категория"
      @change-option-category="updateSelectedCategory"
      @open-add-popup="openAddPopup = true"
      @open-delete-popup="openDeletePopup = true"
      @open-update-popup="openUpdatePopup = true"
    />

    <AdminSelect
      v-if="newProduct.selected.category"
      :key="newProduct.selected.category"
      :options="getElementSelected(catalog.categories[newProduct.selected.category].product_types)"
      select-in="Type"
      select-name="Тип"
      @change-option-type="updateSelectedType"
    />
    <AdminSelect
      v-if="newProduct.selected.type"
      :key="newProduct.selected.type"
      :options="getElementSelected(catalog.heroes)"
      select-in="Hero"
      select-name="Герой"
      @change-option-hero="(select: number) => newProduct.selected.hero = select"
    />

    <div class="flex flex-col gap-2">
      <div>
        <h2 class=" text-md leading-6">
          Размеры
        </h2>
        <p class=" text-xs leading-6 text-gray-400">
          (Размеры в милиметрах)
        </p>
      </div>

      <AdminInput
        v-for="(_item, index) in newProduct.size"
        :key="index"
        :input-name="size[index]"
        :input-in="index"
        placeholder="300"
        :value="newProduct.size[index]"
        @update-input="(value) => { newProduct.size[index] = (value as unknown) as number }"
      />
    </div>

    <div class="flex flex-col gap-2">
      <label
        for="message"
        class="block text-md text-gray-900"
      >Описание</label>
      <textarea
        id="message"
        v-model="newProduct.description"
        rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
        placeholder="Write your thoughts here..."
      />
    </div>
    <AdminInput
      input-name="Цена"
      input-in="price"
      placeholder="3000"
      :value="newProduct.price"
      @update-input="(value) => { newProduct.price = (value as unknown) as number }"
    />

    <AdminDropZone
      :photos="newProduct.photos"
      @upload-photo="uploadPhoto"
    />

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <button
        type="button"
        class="text-sm font-semibold leading-6 text-gray-900"
        @click="remoteNewProduct"
      >
        Сбросить
      </button>
      <button
        type="submit"
        class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Добавить
      </button>
    </div>
  </form>
</template>
