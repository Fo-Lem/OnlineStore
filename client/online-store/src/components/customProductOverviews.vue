<template lang="">
  <div class="bg-white">
    <div class=" max-w-7xl mx-auto pt-6 px-6">
      
      <div class=" flex flex-col gap-5 lg:flex-row">
        <div class="max-w-5xl">
          <div>
            <img :src="'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'"  class="h-full w-full object-cover rounded-lg object-center" />
          </div>
          <div class=" mt-6 grid max-w-7xl grid-cols-3 gap-x-6 ">
            <div class="rounded-lg ">
              <img :src="'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'"  class="h-full w-full object-cover rounded-lg object-center" />
            </div>
            <div class="rounded-lg ">
              <img :src="'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'"  class="h-full w-full object-cover rounded-lg object-center" />
            </div>
            <div class="rounded-lg ">
              <img  :src="'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'"  class="h-full w-full object-cover rounded-lg object-center" />
            </div>
          </div>
        </div>
        <!-- Options -->
        <div class=" min-w-[calc(24rem-20px)]">
          <h2 class="sr-only">Информация</h2>
          <h2 class="text-3xl tracking-tight text-gray-900">{{categorys[$route.params.categoryId].products[$route.params.productId].name}}</h2>
          
          <!-- {{ product.price }} -->
          <!-- Reviews -->
          <div class="mt-6">
            <h3 class="sr-only">Reviews</h3>

          </div>

          <form class="mt-10">
            <!-- Variants -->
            <div>
              <p class="text-sm font-medium text-gray-900">Варианты</p>
              <div  class="mt-4">
                <div class="flex flex-wrap gap-5 items-center ">
  
                  <router-link as="template" v-for="hero in categorys[$route.params.categoryId].products[$route.params.productId].heros" :key="hero.id" :v-html="hero" :value="hero" v-slot="{ active, checked }" :to="{ name: 'productOverviews', params: { productId: $route.params.productId, heroId: hero.id } }">
                    <div :class="[$route.params.heroId==hero.id ? 'ring-2' : '', 'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-lg p-0.5 focus:outline-none']">

                      <span aria-hidden="true" class=" rounded-lg px-4 py-2 border border-black border-opacity-10">{{ hero.name }}</span>
                    </div>
                  </router-link>
                </div>
              </div>
            </div>

            <!-- Sizes -->
            <div class="mt-10">
              <div class="flex items-center justify-between">
                <p class="text-sm font-medium text-gray-900">Характеристики</p>
                <a href="#" class="text-sm font-medium text-indigo-600 hover:text-indigo-500">Size guide</a>
              </div>
            <!-- Характеристики -->
              
            </div>
            <p class="text-3xl tracking-tight text-gray-900">Цена: {{categorys[$route.params.categoryId].products[$route.params.productId].price}}р</p>
            <button type="submit" class="mt-10 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Добавить в корзину</button>
          </form>
        </div>

      </div>

      <!-- Product info -->
      <div class="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16">
        <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
          <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">{{ $route.params.name }}</h1>
        </div>

        

        <div class="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6">
          <!-- Description and details -->
          <div>
            <h3 class="sr-only">Description</h3>

            <div class="space-y-6">
              <!-- <p class="text-base text-gray-900">{{ product.description }}</p> -->
            </div>
          </div>

          <div class="mt-10">
            <h3 class="text-sm font-medium text-gray-900">Highlights</h3>

            <div class="mt-4">
              <ul role="list" class="list-disc space-y-2 pl-4 text-sm">
                <!-- <li v-for="highlight in product.highlights" :key="highlight" class="text-gray-400"> -->
                  <!-- <span class="text-gray-600">{{ highlight }}</span> -->
                <!-- </li> -->
              </ul>
            </div>
          </div>

          <div class="mt-10">
            <h2 class="text-sm font-medium text-gray-900">Details</h2>

            <div class="mt-4 space-y-6">
              <!-- <p class="text-sm text-gray-600">{{ product.details }}</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { StarIcon } from '@heroicons/vue/20/solid'
import { RadioGroup, RadioGroupLabel, RadioGroupOption } from '@headlessui/vue'

export default {
  components: {
    StarIcon, RadioGroup, RadioGroupLabel, RadioGroupOption
  },
  name: "custom-cart",

  data() {
    return {
      selectedHero:'' 

    }
  },
  props: {

    //Хранит данные о товарах
    categorys: {
      require: true,
      type: Object
  }

}}
</script>
<style scoped>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
