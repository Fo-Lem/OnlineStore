<template lang="">
  <div class="bg-white mb-5">
    <div class=" max-w-7xl mx-auto pt-6 px-6">
      
      
      <div class=" flex flex-col gap-5 lg:flex-row">
        <!-- Галлерея -->
        <div class="max-w-5xl">
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
        <div class=" min-w-[calc(24rem-20px)]">
          <h2 class="sr-only">Информация</h2>
          <h2 class="text-3xl tracking-tight text-gray-900">{{categorys[$route.params.categoryId].products_type[$route.params.productId].heroes[$route.params.heroId].items[0].name}}</h2>
          

          <form @submit.prevent="addProductBasket" class="mt-10">
            <!-- Варианты -->
            <div>
              <p class="text-xl font-medium text-gray-900">Варианты</p>
              <div  class="mt-4">
                <div class="flex flex-wrap gap-5 items-center ">
  
                  <router-link as="template" @click="heroId=hero.id"  v-for="hero in categorys[$route.params.categoryId].products_type[$route.params.productId].heroes" :key="hero.id" :v-html="hero" :value="hero" v-slot="{ active, checked }" :to="{ name: 'productOverviews', params: { productId: $route.params.productId, heroId: hero.id } }">
                    <div :class="[$route.params.heroId==hero.id ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">

                      <span aria-hidden="true" class=" rounded-lg px-4 py-2 border border-black border-opacity-10">{{ hero.name }}</span>
                    </div>
                  </router-link>
                </div>
              </div>
            </div>

            <!-- Характеристики -->
            <div class="mt-5">
              <div class="">
                <p class="font-medium text-xl text-gray-900">Характеристики</p>
              </div>
              
              <!-- Размер -->
              <div class="mt-5">
                <div class="flex items-center justify-between">
                  <h3 class="font-medium text-xl text-gray-900">Размер</h3>
                </div>
                
                <div class="mt-4  ">
                  <p v-for="size in sizeConvertor(categorys[$route.params.categoryId].products_type[$route.params.productId].heroes[$route.params.heroId].items[0].size)">{{size}}</p>
                  
                </div>
              </div>
              <!-- Описание -->
              <div class="mt-5">
                <h3 class="font-medium text-xl text-gray-900">Описание</h3>
                <div class="mt-5">
                  <p>{{categorys[$route.params.categoryId].products_type[$route.params.productId].heroes[$route.params.heroId].items[0].discriptions}}</p>
                </div>
              </div>
            </div>
            <p class=" mt-5 text-xl tracking-tight text-gray-900">Цена: {{categorys[$route.params.categoryId].products_type[$route.params.productId].heroes[$route.params.heroId].items[0].price}} р</p>
            <div v-if="!inBasket">
                <button type="submit" class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Добавить в корзину</button>
            </div>
            <div class="mt-5 flex w-full justify-center rounded-md border border-transparent bg-gray-100" v-if="inBasket">
              <h1 class=" px-8 py-3 text-base text-gray-500 font-medium">Товар уже в корзине</h1>
            </div>
            </form>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { productInBasket } from "../../controllers/basketController";
export default {
  name: "custom-cart",
  emits: ['addProductBasket'],

  data() {
    return {
      inBasket: false,
      curentImage: 1,
      rebuilSize: '',
      curentProduct: {},
      heroId: '',

    }
  },
  props: {

    categorys: {
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
    updateCurentProduct(newHeroId) {
      this.curentProduct = {
        category: this.categorys[this.$route.params.categoryId].id,
        products_type: this.categorys[this.$route.params.categoryId].products_type[this.$route.params.productId].id,
        hero: this.categorys[this.$route.params.categoryId].products_type[this.$route.params.productId].heroes[newHeroId].id,
        count: 1
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
<style scoped>
</style>
