<template lang="">
    <form class="py-5 flex flex-col gap-5">
              <div class="flex gap-2 flex-col">
                <label for="name" class="block text-md font-medium leading-6 text-gray-900">Название продукта</label>
                  <div class="flex rounded shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
                    <input type="text" name="name" id="name"  class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder='Меч длинный "Алеша Попович"' />
                  </div>
              </div>
              
              <admin-select 
              v-bind:options="getElementSelected(categorys)"
              v-bind:selectIn="'Category'"
              v-bind:selectName="'Категория'"
              @changeOptionCategory="(select)=>updateSelectedCategory(select)"
              >
              </admin-select>

              <admin-select 
              
              v-if="selected['category']"
              :key="selected['category']"
              v-bind:options="getElementSelected(categorys[selected['category']].product_types)"
              v-bind:selectIn="'Type'"
              v-bind:selectName="'Тип'"
              @changeOptionType="(select)=>updateSelectedType(select)"
              >
              </admin-select>
              <admin-select 
              
              v-if="selected['type']"
              :key="selected['type']"
              v-bind:options="getElementSelected(categorys[selected['category']].product_types[selected['type']].heroes)"
              v-bind:selectIn="'Hero'"
              v-bind:selectName="'Герой'"
              @changeOptionHero="(select)=>selected['hero']=select"
              >
              </admin-select>
              
    
              <div class="flex flex-col gap-2">
                <div>
                  <h2 class=" text-md leading-6 font-medium">Размеры</h2>
                  <p class=" text-xs leading-6 text-gray-400">(Размеры в милиметрах)</p>
                </div>
                
                <admin-input v-for="(item, index) in size" :key="index"
                v-bind:inputName="size[index].name"
                v-bind:inputIn="index"
                v-bind:value="size[index].size"
                @updatedepth="(value)=>size[index].size=value">
                </admin-input>
                
              </div>

              <div class="flex flex-col gap-2">
                  <label for="message" class="block text-md font-medium text-gray-900">Описание</label>
                  <textarea id="message" v-model="discription" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Write your thoughts here..."></textarea>
              </div>
    
    
         <admin-drop-zone></admin-drop-zone>     
     
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
</template>
<script>

export default {
  name: 'admin-add-products',
  data() {
    return {
      productName:'',
      selected: {
        category: '',
        type: '',
        hero: ''
      },
      size: { 
        height: {name:'Высота',size:''}, 
        widht: {name:'Ширина',size:''}, 
        depth: {name:'Глубина',size:''} 
      },
      discription:'',
      images:[]
    }
  },
  props: {
    categorys: {
      type: Object,
      require: true
    }
  },

  methods: {

    getElementSelected(items) {
      const res = {}
      for (var key in items) {
        res[key] = items[key].name
      }
      //console.log(this.selected['category'], this.selected['type'], this.selected['hero'])
      return res
    },
    updateSelectedCategory(select) {
      this.selected['category'] = select
      this.selected['type'] = ''
      this.selected['hero'] = ''
    },
    updateSelectedType(select) {
      this.selected['type'] = select
      this.selected['hero'] = ''
    }


  }
}
</script>