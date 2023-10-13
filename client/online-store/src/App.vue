<script lang="ts">
import { defineComponent } from 'vue'

import CustomHeader from './components/header/customHeader.vue'
import CustomFooter from './components/footer/customFooter.vue'

import CustomErrorPage from './components/errorPage/customErrorPage.vue'
import { addProductBasket, correctBasket, deleteProductBasket, getDataBasket, updateCountProductBasket } from './controllers/basketController'
import { getCategorys } from './controllers/productController'

import type { catalog } from './controllers/productController'
import type { basket, curentProduct } from './controllers/basketController'
import CustomLoadingSpiner from './components/UI/customLoadingSpiner.vue'

interface State {
  catalog: catalog
  basket: basket
  isAdmin: boolean
  searchInput: string
  error: Error
  loading: boolean
}

export default defineComponent({
  components: { CustomHeader, CustomFooter, CustomErrorPage, CustomLoadingSpiner },
  data(): State {
    return {
      catalog: {
        categories: {},
        heroes: {},
        items: {},
      },
      basket: {},
      isAdmin: false,
      searchInput: '',
      error: {
        name: '',
        message: '',
      },
      loading: false,
    }
  },
  beforeMount() {
    if (localStorage.basket !== undefined && localStorage.basket !== '')
      this.basket = getDataBasket()

    this.initCatalog()
  },
  methods: {
    addProductBasket(curentProduct: curentProduct) {
      this.basket = addProductBasket(curentProduct)
    },
    deleteProductBasket(id: number) {
      this.basket = deleteProductBasket(id)
    },
    updateCountProductBasket(newCount: number, id: number) {
      this.basket = updateCountProductBasket(newCount, id)
    },
    updateSearchInput(value: string) {
      this.searchInput = value
    },
    async initCatalog() {
      await getCategorys().then((data) => {
        this.catalog = data
        correctBasket(this.catalog)
      })
        .catch((error) => {
          // console.log(error)
          this.error = error
        })
        .finally(() => {
          this.loading = true
          // console.log(this.catalog)
        })
    },
  },

})
</script>

<template>
  <CustomHeader v-if="$router.currentRoute.value.path.split('/')[1] !== '_adminPanel' && loading && !error.name" />
  <main class=" max-w-7xl py-3 md:py-5 lg:py-8 px-5 lg:px-8 m-auto min-h-[calc(100vh-80px)]">
    <CustomErrorPage v-if="error.name" :error="error" />
    <CustomLoadingSpiner v-if="!loading" />

    <router-view
      v-if="loading && !error.name" :basket="basket" :catalog="catalog" :search-input="searchInput"
      @update-search-input="updateSearchInput" @delete-product-basket="deleteProductBasket"
      @update-count-product-basket="(newCount: number, id: number) => { updateCountProductBasket(newCount, id) }"
      @add-product-basket="(curentProduct: curentProduct) => { addProductBasket(curentProduct) }"
      @update-data="initCatalog"
    />
  </main>

  <CustomFooter v-if="$router.currentRoute.value.path.split('/')[1] !== '_adminPanel' && loading && !error.name" />
</template>
