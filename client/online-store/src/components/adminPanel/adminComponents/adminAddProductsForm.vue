<template lang="">
    <form @submit.prevent="AddProduct" class="py-5 flex flex-col gap-5">
      <admin-input 
      v-bind:inputName="'Название продукта'"
      v-bind:inputIn="'productName'"
      v-bind:placeholder="`Меч длинный &laquoАлеша Попович&raquo`"
      v-bind:value="newProduct.productName"
      @updateInput="(value)=>newProduct.productName=value">
      </admin-input>
              <admin-select 
              :key="newProduct.productName"
              v-bind:options="getElementSelected(catalog.categories)"
              v-bind:selectIn="'Category'"
              v-bind:selectName="'Категория'"
              @changeOptionCategory="(select)=>updateSelectedCategory(select)"
              >
              </admin-select>
              
              <admin-select 
              
              v-if="newProduct.selected['category']"
              :key="newProduct.selected['category']"
              v-bind:options="getElementSelected(catalog.categories[newProduct.selected['category']].product_types)"
              v-bind:selectIn="'Type'"
              v-bind:selectName="'Тип'"
              @changeOptionType="(select)=>updateSelectedType(select)"
              >
              </admin-select>
              <admin-select 
              
              v-if="newProduct.selected['type']"
              :key="newProduct.selected['type']"
              v-bind:options="getElementSelected(catalog.heroes)"
              v-bind:selectIn="'Hero'"
              v-bind:selectName="'Герой'"
              @changeOptionHero="(select)=>newProduct.selected['hero']=select"
              >
              </admin-select>
              
    
              <div class="flex flex-col gap-2">
                <div>
                  <h2 class=" text-md leading-6">Размеры</h2>
                  <p class=" text-xs leading-6 text-gray-400">(Размеры в милиметрах)</p>
                </div>
                
                <admin-input v-for="(item, index) in newProduct.size" :key="index"
                v-bind:inputName="size[index]"
                v-bind:inputIn="index"
                v-bind:placeholder="'300'"
                v-bind:value="newProduct.size[index]"
                @updateInput="(value)=>newProduct.size[index]=value">
                </admin-input>
                
              </div>
              

              <div class="flex flex-col gap-2">
                  <label for="message" class="block text-md text-gray-900">Описание</label>
                  <textarea id="message" v-model="newProduct.discription" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Write your thoughts here..."></textarea>
              </div>
              <admin-input 
              v-bind:inputName="'Цена'"
              v-bind:inputIn="'price'"
              v-bind:placeholder="`3000`"
              v-bind:value="newProduct.price"
              @updateInput="(value)=>newProduct.price=value">
              </admin-input>
    
         <admin-drop-zone v-bind:photos="newProduct.photos" @uploadPhoto="uploadPhoto"></admin-drop-zone>     
     
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" @click="remoteNewProduct" class="text-sm font-semibold leading-6 text-gray-900">Сбросить</button>
          <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Добавить</button>
        </div>
      </form>
</template>
<script>

export default {
  name: 'admin-add-products',
  data() {
    return {
      size: {
          height: 'Высота',
          width: 'Ширина',
          depth: 'Глубина'
        },
      newProduct: {
        productName: '',
        selected: {
          category:'',
          type: '',
          hero: ''
        },
        size: {
          height: '' ,
          width: '' ,
          depth: '' 
        },
        discription: '',
        price: '',
        photos: []
      }
    }
  },
  props: {
    catalog: {
      type: Object,
      require: true
    }
  },

  methods: {

    getElementSelected(items) {
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
    AddProduct() {
      console.log(this.newProduct)
    },
    remoteNewProduct() {
      this.newProduct = {
        productName: '',
        selected: {
          category:'',
          type: '',
          hero: ''
        },
        size: {
          height: '' ,
          width: '' ,
          depth: '' 
        },
        discription: '',
        price: '',
        photos: []
      }
    }


  }
}
</script>