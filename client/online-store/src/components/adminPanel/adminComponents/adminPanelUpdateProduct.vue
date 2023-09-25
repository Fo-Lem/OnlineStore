<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import type { catalog, catalogCategories, catalogHeroes, catalogItem, catalogTypes } from '../../../controllers/productController'
import { Admin } from '../adminControllers/adminControllers'
import type { ElementSelected } from './adminPanelCreations.vue'

interface State {
  sizeName: {
    height: 'Высота'
    width: 'Ширина'
    depth: 'Глубина'
  }
  newProduct: newProduct
  curentProduct: catalogItem

}
interface newProduct {
  newName: string
  newCategory_id: number
  newProduct_type_id: number
  newHero_id: number
  newDescription: string
  newPrice: number
  size: {
    height: number
    width: number
    depth: number
  }
  photos: FileList[]

}
export default defineComponent({
  name: 'AdminPanelUpdateProduct',
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
  emits: ['updateData'],
  data(): State {
    return {
      sizeName: {
        height: 'Высота',
        width: 'Ширина',
        depth: 'Глубина',
      },
      curentProduct: {} as catalogItem,
      newProduct: {
        newName: '',
        newCategory_id: 0,
        newProduct_type_id: 0,
        newHero_id: 0,
        newDescription: '',
        newPrice: 0,
        size: {
          height: 0,
          width: 0,
          depth: 0,
        },
        photos: [],

      },
    }
  },
  beforeMount() {
    this.curentProduct = this.catalog.items[this.$route.params.itemId as unknown as number]
    this.newProduct.newCategory_id = this.curentProduct.category_id
    this.newProduct.newProduct_type_id = this.curentProduct.product_type_id
    this.newProduct.newHero_id = this.curentProduct.hero_id
    this.newProduct.newPrice = this.curentProduct.price
    this.newProduct.size = this.sizeParser(this.curentProduct.size)
    this.newProduct.newDescription = this.curentProduct.description
    this.newProduct.photos = []
    // console.log(this.curentProduct)
  },

  methods: {
    sizeParser(size: string): State['newProduct']['size'] {
      const arr = size.split('x')
      return {
        height: arr[0] as unknown as number,
        width: arr[1] as unknown as number,
        depth: arr[2] as unknown as number,
      }
    },

    getElementSelected(items: catalogTypes | catalogCategories | catalogHeroes) {
      const res = {} as ElementSelected
      for (const key in items)
        res[key as unknown as number] = items[key].name

      return res
    },
    updateSelectedCategory(select: number) {
      this.newProduct.newCategory_id = select
    },
    updateSelectedType(select: number) {
      this.newProduct.newProduct_type_id = select
    },
    async UpdateProduct() {
      // console.log(this.curentProduct)
      const obj = {
        id: this.curentProduct.id,
        id_1: this.curentProduct.id_1,
        name: this.newProduct.newName,
        category_id: this.newProduct.newCategory_id,
        product_type_id: this.newProduct.newProduct_type_id,
        hero_id: this.newProduct.newHero_id,
        description: this.newProduct.newDescription,
        size: `${this.newProduct.size.height}x${this.newProduct.size.width}x${this.newProduct.size.depth}`,
        price: this.newProduct.newPrice,
      }
      await Admin.productController.update(obj.id, obj.id_1, obj.name, obj.category_id, obj.product_type_id, obj.hero_id, obj.description, obj.size, obj.price)
      this.$emit('updateData')
      this.$router.push({ name: 'products' })
    },

  },
})
</script>

<template>
  <form
    class="py-5 flex flex-col gap-5"
    @submit.prevent="UpdateProduct"
  >
    <admin-input
      input-name="Название продукта"
      input-in="productName"
      placeholder="Меч длинный &laquoАлеша Попович&raquo"
      :value="newProduct.newName"
      @update-input="(value:string) => curentProduct.name = value"
    />

    <admin-select
      :key="curentProduct.name"
      :options="getElementSelected(catalog.categories)"
      select-in="Category"
      select-name="Категория"
      :curent-option="{ index: curentProduct.category_id, option: catalog.categories[curentProduct.category_id].name }"
      @change-option-category="(select:number) => updateSelectedCategory(select)"
    />

    <admin-select
      :key="newProduct.newCategory_id"
      :options="getElementSelected(catalog.categories[newProduct.newCategory_id].product_types)"
      :curent-option="{ index: curentProduct.product_type_id, option: catalog.categories[curentProduct.category_id].product_types[curentProduct.product_type_id].name }"
      select-in="Type"
      select-name="Тип"
      @change-option-type="(select:number) => updateSelectedType(select)"
    />

    <admin-select
      :key="curentProduct.hero_id"
      :options="getElementSelected(catalog.heroes)"
      select-in="Hero"
      select-name="Герой"
      :curent-option="{ index: curentProduct.hero_id, option: catalog.heroes[curentProduct.hero_id].name }"
      @change-option-hero="(select:number) => newProduct.newHero_id = select"
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

      <admin-input
        v-for="(item, index) in newProduct.size"
        :key="index"
        :input-name="sizeName[index]"
        :input-in="index"
        placeholder="300"
        :value="item"
        @update-input="(value: number) => newProduct.size[index] = value"
      />
    </div>

    <div class="flex flex-col gap-2">
      <label
        for="message"
        class="block text-md text-gray-900"
      >Описание</label>
      <textarea
        id="message"
        v-model="newProduct.newDescription"
        rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
        placeholder="Write your thoughts here..."
      />
    </div>
    <admin-input
      input-name="Цена"
      input-in="price"
      placeholder="3000"
      :value="String(curentProduct.price)"
      @update-input="(value:number) => newProduct.newPrice = value"
    />

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <router-link
        class="text-sm font-semibold leading-6 text-gray-900"
        :to="{ name: 'products' }"
      >
        Отменить
      </router-link>
      <button
        type="submit"
        class="rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Изменить
      </button>
    </div>
  </form>
</template>
