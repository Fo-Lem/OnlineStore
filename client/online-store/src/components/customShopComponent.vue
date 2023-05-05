<template lang="">
  <div>
    <div class="mx-auto max-w-7xl p-6 flex flex-col-reverse justify-between lg:px-8 md:flex-row ">
      <custom-breadcrumbs v-bind:categorys="categorys" class="mt-2 md:mt-0"></custom-breadcrumbs>
      <custom-search-input class="md:w-1/2" v-bind:shopComponentSearchInput="shopComponentSearchInput" v-model="shopComponentSearchInput"></custom-search-input></div>
    <router-view v-bind:categorys="categorys"></router-view>
  </div>
</template>
<script>
import customSearchInput from "../UI/customSearchInput.vue";
import customBreadcrumbs from "../UI/customBreadcrumbs.vue"

export default {
  components: { customSearchInput, customBreadcrumbs },

  name: "custom-shop-component",
  props: {
    type: {
      require: true
    }
  },

  data() {
    return {
      shopComponentSearchInput: '',
      roadHistory: [],
      categorys: {}

    }
  },

  beforeMount() {
    this.categorys = {
      1: {
        id: 1,
        name: 'Щиты',
        products: {
          1: {
            id: 1,
            name: 'Щит круглый',
            price: 4500,
            discriptions:'',
            size: { heught: 300, width: 200, depth: 150 },
            heros: {
              1: {id: 1, name: 'Илья'},
              2: {id: 2, name: 'Добрыня'},
              3: {id: 3, name: 'Алеша'},
              4: {id: 4, name: 'Иван'},
              5: {id: 5, name: 'Георгий'}
            },
            imageSrc: `https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg`
          }
        }
      }
    }

  }
}
</script>
<style scoped></style>