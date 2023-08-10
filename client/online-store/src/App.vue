<script>
import customHeader from './components/header/customHeader.vue'
import customFooter from './components/footer/customFooter.vue'
import customErrorPage from './components/errorPage/customErrorPage.vue'
import {
  addProductBasket, correctBasket, deleteProductBasket, getDataBasket, updateCountProductBasket,
} from './controllers/basketController'
import { getCategorys, sortItems } from './controllers/productController'

export default {
  components: { CustomHeader: customHeader, CustomFooter: customFooter, CustomErrorPage: customErrorPage },
  data() {
    return {
      catalog: {},
      basket: {},
      isAdmin: false,
      searchInput: '',
      error: false,
      loading: false,
    }
  },
  beforeMount() {
    if (localStorage.basket !== undefined && localStorage.basket !== '')
      this.basket = getDataBasket()
      // console.log('basket')
      // console.log(this.basket)

    this.initCatalog()
  },
  methods: {
    addProductBasket(basket, curentProduct) {
      this.basket = addProductBasket(basket, curentProduct)
    },
    deleteProductBasket(curentProduct) {
      this.basket = deleteProductBasket(curentProduct)
    },
    updateCountProductBasket(newCount, id) {
      this.basket = updateCountProductBasket(newCount, id)
    },
    updateSearchInput(value) {
      this.searchInput = value
    },
    async initCatalog() {
      await getCategorys().then((response) => {
        this.catalog = sortItems(response.data)
        correctBasket(this.basket, this.catalog)
      })
        .catch((error) => {
          // console.log(error)
          this.error = error
        })
        .finally(() => {
          this.loading = true
          // console.log('catalog')
          // console.log(this.catalog)
        })
    },
  },

}
</script>

<template>
  <div>
    <div v-if="$router.currentRoute.value.path.split('/')[1] !== '_adminPanel'">
      <CustomHeader />
      <hr class="mx-auto max-w-7xl">
    </div>
    <CustomErrorPage
      v-if="error"
      :error="error"
    />
    <custom-loading-spiner v-if="!loading" />

    <router-view
      v-if="loading && !error"
      :basket="basket"
      :catalog="catalog"
      :search-input="searchInput"
      @update-search-input="updateSearchInput"
      @delete-product-basket="deleteProductBasket"
      @update-count-product-basket="(newCount, id) => { updateCountProductBasket(newCount, id) }"
      @add-product-basket="(curentProduct) => { addProductBasket(basket, curentProduct) }"
      @update-data="initCatalog"
    />

    <div v-if="$router.currentRoute.value.path.split('/')[1] !== '_adminPanel'">
      <hr class="mx-auto max-w-7xl">
      <CustomFooter />
    </div>
  </div>
</template>
