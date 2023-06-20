<template lang="">
  <div  class="bg-white mb-5">
    <div  class=" max-w-7xl mx-auto pt-3 px-6">
      
      
      <div v-if="$route.params.heroId>0&&catalog.items[curentProduct.item[curentProduct.version]]" class=" flex flex-col justify-between gap-5 lg:flex-row">
        <!-- Галлерея -->
        <div class="max-w-5xl ">
          <div>
            <img :src="`https://tailwindui.com/img/ecommerce-images/category-page-0${$route.params.heroId}-image-card-0${curentImage}.jpg`"  class="h-full w-full object-cover rounded-lg object-center" />
          </div>
          <div class=" mt-6 grid max-w-7xl grid-cols-3 gap-x-5 ">
            <div :class="[curentImage==1 ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">
              <img :src="`https://tailwindui.com/img/ecommerce-images/category-page-0${$route.params.heroId}-image-card-01.jpg`" @click="curentImage=1" class="h-full w-full object-cover rounded-lg object-center" />
            </div>
            <div :class="[curentImage==2 ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">
              <img :src="`https://tailwindui.com/img/ecommerce-images/category-page-0${$route.params.heroId}-image-card-02.jpg`" @click="curentImage=2"  class="h-full w-full object-cover rounded-lg object-center" />
            </div>
            <div :class="[curentImage==3 ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">
              <img  :src="`https://tailwindui.com/img/ecommerce-images/category-page-0${$route.params.heroId}-image-card-03.jpg`" @click="curentImage=3"  class="h-full w-full object-cover rounded-lg object-center" />
            </div>
          </div>
        </div>


        <!-- Информация -->
        <div class=" min-w-[calc(28rem-20px)]">
          <h2 class="sr-only">Информация</h2>
          <h2 class="text-3xl tracking-tight text-gray-900">{{catalog.items[curentProduct.item[curentProduct.version]].name}}</h2>
          <hr>

          <form @submit.prevent="addProductBasket" class=" flex gap-5 flex-col mt-5">
            <!-- Варианты -->
            <div>
              <p class="text-xl font-medium text-gray-900">Герои</p>
              <div  class="mt-4">
                <div class="flex flex-wrap gap-2 items-center ">
                  <router-link as="template" @click="heroId=hero[0].hero_id"  v-for="hero in variants" :key="hero[0].id" :v-html="hero" :value="hero" v-slot="{ active, checked }" :to="{ name: 'productOverviews', params: { productId: $route.params.productId, heroId: hero[0].hero_id } }">
                    <div :class="[$route.params.heroId==hero[0].hero_id ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">
                      <span aria-hidden="true" class=" rounded-lg text-sm px-2 py-2 border border-black border-opacity-10">{{ catalog.heroes[hero[0].hero_id].name }}</span>
                    </div>
                  </router-link>
                  
                </div>
              </div>
            </div>
            <div v-if="curentProduct.item.length>1">
              <p class="text-xl font-medium text-gray-900">Вариации</p>
              <div  class="mt-4">
                <div class="flex flex-wrap gap-2 items-center ">
                  <button @click="this.updateCurentProduct(this.$route.params.heroId,index)" 
                  :class="[curentProduct.version==index ? 'ring-2' : '', 'rounded-lg text-sm px-4 py-2 border border-black border-opacity-10']" 
                  v-for="(itemId, index) in curentProduct.item" 
                  :key="index"
                  type="button">
                    {{index+1}}
                  </button>
                  
                </div>
              </div>
            </div>
            
            <!-- Характеристики -->
            <div class="">
              <div class="">
                <p class="font-medium text-xl text-gray-900">Характеристики</p>
              </div>
              
              <!-- Размер -->
              <div class="mt-5">
                <div class="flex items-center justify-between">
                  <h3 class="font-medium text-xl text-gray-900">Размер</h3>
                </div>
                
                <div class="mt-4  ">
                  <p v-for="size in sizeConvertor(catalog.items[curentProduct.item[curentProduct.version]].size)">{{size}}</p>
                  
                </div>
              </div>
              <!-- Описание -->
              <div class="mt-5">
                <h3 class="font-medium text-xl text-gray-900">Описание</h3>
                <div class="mt-5">
                  <p>{{catalog.items[curentProduct.item[curentProduct.version]].description}}</p>
                </div>
              </div>
            </div>
            <p class=" mt-5 text-xl tracking-tight font-medium text-gray-900">Цена: {{catalog.items[curentProduct.item[curentProduct.version]].price}} р</p>
            <div v-if="!inBasket">
                <button type="submit" class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Добавить в корзину</button>
            </div>
            <div  class="mt-5 flex w-full justify-center rounded-md border border-transparent bg-gray-100" v-if="inBasket">
              <h1 class=" px-8 py-3 text-base text-gray-500 font-medium">Товар уже в корзине</h1>
            </div>
            </form>

        </div>
      </div>
      <div v-else class="py-3 text-base text-red-500 font-medium">
        <h1>Такого товара не существует</h1>
      </div>
    </div>
    
  </div>
  
</template>
<script>
import { productInBasket } from "../../controllers/basketController";
export default {
  name: "custom-product-overviews",
  emits: ['addProductBasket'],

  data() {
    return {
      inBasket: false,
      curentImage: 1,
      rebuilSize: '',
      curentProduct: {},
      heroId: '',
      variants: []

    }
  },
  props: {

    catalog: {
      require: true,
      type: Object
    },
    basket: {
      require: true,
      type: Object
    }


  },
  methods: {
    sizeConvertor(size) {
      return size.split('x').reduce(
        function (obj, currentSize, index) {
          var Arr = ['Ширинa: ', 'Высота: ', 'Глубина: '];
          obj[index] = `${Arr[index]} ${currentSize} мм`;
          return obj;
        }, {}
      )
    },
    addProductBasket() {
      this.$emit('addProductBasket', this.curentProduct)
      this.inBasket = productInBasket(this.basket, this.curentProduct)
    },
    groupBy(key) {
      return function group(array) {
        return array.reduce((acc, obj) => {
          const property = obj[key];
          acc[property] = acc[property] || [];
          acc[property].push(obj);
          return acc;
        }, {});
      };
    },
    updateCurentProduct(newHeroId, newVersion = 0) {
      this.curentProduct = {
        item: [],
        version: newVersion,
        count: 1
      }
      if (this.variants.length < 1) {
        for (const item in this.catalog.items) {
          const cItem = this.catalog.items[item]
          if (cItem.category_id == this.$route.params.categoryId && cItem.product_type_id == this.$route.params.productId) {
            this.variants.push(cItem)
          }
        }
        const groupByHeroId = this.groupBy("hero_id");
        this.variants = groupByHeroId(this.variants)

      }
      for (const item in this.variants[newHeroId]) {
        this.curentProduct.item.push(this.variants[newHeroId][item].id)
      }
      this.inBasket = productInBasket(this.basket, this.curentProduct)
    }
  },
  beforeMount() {
    this.updateCurentProduct(this.$route.params.heroId)
  },
  watch: {
    heroId(newHeroId) {
      this.updateCurentProduct(newHeroId)
    }

  }
}
</script>
<style scoped></style>
