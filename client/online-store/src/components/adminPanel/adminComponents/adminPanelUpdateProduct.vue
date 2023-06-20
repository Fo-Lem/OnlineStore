<template>
  <form @submit.prevent="UpdateProduct" class="py-5 flex flex-col gap-5">
    <admin-input v-bind:inputName="'Название продукта'" v-bind:inputIn="'productName'"
      v-bind:placeholder="`Меч длинный &laquoАлеша Попович&raquo`" v-bind:value="curentProduct.name"
      @updateInput="(value) => curentProduct.name = value">
    </admin-input>

    <admin-select :key="curentProduct.name" v-bind:options="getElementSelected(catalog.categories)"
      v-bind:selectIn="'Category'" v-bind:selectName="'Категория'"
      v-bind:curentOption="{index:curentProduct.category_id,option:catalog.categories[curentProduct.category_id].name}"
      @changeOptionCategory="(select) => updateSelectedCategory(select)" 
      @openAddPopup="openAddPopup = true"
      @openDeletePopup="openDeletePopup = true" 
      @openUpdatePopup="openUpdatePopup = true"
      >
    </admin-select>

    <admin-select :key="curentProduct.newCategory_id"
      v-bind:options="getElementSelected(catalog.categories[curentProduct.newCategory_id].product_types)"
      v-bind:curentOption="{index:curentProduct.product_type_id,option:catalog.categories[curentProduct.category_id].product_types[curentProduct.product_type_id].name}"
      v-bind:selectIn="'Type'" v-bind:selectName="'Тип'" @changeOptionType="(select) => updateSelectedType(select)">
    </admin-select>

    <admin-select :key="curentProduct.hero_id"
      v-bind:options="getElementSelected(catalog.heroes)" v-bind:selectIn="'Hero'" v-bind:selectName="'Герой'"
      v-bind:curentOption="{index:curentProduct.hero_id,option:catalog.heroes[curentProduct.hero_id].name}"
      @changeOptionHero="(select) => curentProduct.newHero_id = select">
    </admin-select>


    <div class="flex flex-col gap-2">
      <div>
        <h2 class=" text-md leading-6">Размеры</h2>
        <p class=" text-xs leading-6 text-gray-400">(Размеры в милиметрах)</p>
      </div>

      <admin-input v-for="(item, index) in curentProduct.size" :key="index" v-bind:inputName="size[index]"
        v-bind:inputIn="index" v-bind:placeholder="'300'" v-bind:value="item"
        @updateInput="(value) => curentProduct.size[index] = value">
      </admin-input>

    </div>

    <div class="flex flex-col gap-2">
      <label for="message" class="block text-md text-gray-900">Описание</label>
      <textarea id="message" v-model="curentProduct.newDescription" rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
        placeholder="Write your thoughts here..."></textarea>
    </div>
    <admin-input v-bind:inputName="'Цена'" v-bind:inputIn="'price'" v-bind:placeholder="`3000`"
      v-bind:value="String(curentProduct.price)" @updateInput="(value) => curentProduct.newPrice = value">
    </admin-input>

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <router-link class="text-sm font-semibold leading-6 text-gray-900" :to="{ name: 'products' }">
        Отменить
      </router-link>
      <button type="submit"
        class="rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Изменить</button>
    </div>
  </form>
</template>
<script>
export default {
  name: 'admin-panel-update-product',
  data() {
    return {
      size: {
        height: 'Высота',
        width: 'Ширина',
        depth: 'Глубина'
      },
      curentProduct: {}
    }
  },
  props: {
    catalog: {
      type: Object,
      require: true
    },
    AdminController: {
      type: Object,
      require: true
    }
  },
  emits: ['updateData'],

  methods: {
    sizeParser(size){
      const arr= size.split('x')
      this.curentProduct.size={height: arr[0],
        width: arr[1],
        depth: arr[2]}
    },
      
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
      this.curentProduct.newCategory_id = select
    },
    updateSelectedType(select) {
      this.curentProduct.newProduct_type_id = select
    },
    async UpdateProduct() {
      console.log(this.curentProduct)
      const obj = {
        id: this.curentProduct.id,
        id_1: this.curentProduct.id_1,
        name: this.curentProduct.name,
        category_id: this.curentProduct.newCategory_id,
        product_type_id: this.curentProduct.newProduct_type_id,
        hero_id: this.curentProduct.newHero_id,
        description: this.curentProduct.newDescription,
        size: `${this.curentProduct.size.height}x${this.curentProduct.size.width}x${this.curentProduct.size.depth}`,
        price: this.curentProduct.newPrice
      }
      await this.AdminController.productController.updateProduct(obj)
      this.$emit('updateData')
      this.$router.push({ name: 'products'})
    },



  },
  beforeMount() {
    Object.assign(this.curentProduct,this.catalog.items[this.$route.params.itemId])
    this.curentProduct.newCategory_id=this.curentProduct.category_id
    this.curentProduct.newProduct_type_id=this.curentProduct.product_type_id
    this.curentProduct.newHero_id=this.curentProduct.hero_id
    this.curentProduct.newPrice=this.curentProduct.price
    this.sizeParser(this.curentProduct.size)
    this.curentProduct.newDescription=this.curentProduct.description
    this.curentProduct.photos=[]
    console.log(this.curentProduct)
  }
}
</script>