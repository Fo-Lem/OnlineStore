<template>
  <div>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != '_adminPanel'">
      <custom-header></custom-header>
      <hr class="mx-auto max-w-7xl">
    </div>
    <custom-error-page v-if="error" v-bind:error="error"></custom-error-page>
    <custom-loading-spiner v-if="!loading"></custom-loading-spiner>

    <router-view v-if="loading && !error" v-bind:basket="basket" v-bind:catalog="catalog" v-bind:searchInput="searchInput"
      @update-search-input="updateSearchInput" 
      @delete-product-basket="deleteProductBasket"
      @update-count-product-basket="(newCount, id) => { updateCountProductBasket(newCount, id) }"
      @add-product-basket="(curentProduct) => { addProductBasket(basket, curentProduct) }"
      @updateData="initCatalog">
    </router-view>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != '_adminPanel'">
      <hr class="mx-auto max-w-7xl">
      <custom-footer></custom-footer>
    </div>

  </div>
</template>
<script >
import customHeader from "./components/header/customHeader.vue"
import customFooter from "./components/footer/customFooter.vue"
import customErrorPage from './components/errorPage/customErrorPage.vue'
import { addProductBasket, deleteProductBasket, updateCountProductBasket, getDataBasket,correctBasket } from "./controllers/basketController";
import { getCategorys, sortItems } from "./controllers/productController";

//lol
export default {
  components: { customHeader, customFooter, customErrorPage },
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
      await getCategorys().then(response => {
        this.catalog=sortItems(response.data)
        correctBasket(this.basket,this.catalog)
      })
        .catch(error => {
          console.log(error)
          this.error = error;
        })
        .finally(() => {
          this.loading = true;
          console.log('catalog')
          console.log(this.catalog)
        });
    }
  },
  beforeMount() {

    if (localStorage.basket != undefined && localStorage.basket != "") {
      this.basket = getDataBasket()
      console.log('basket')
      console.log(this.basket)
    }
    this.initCatalog()
  }


}



</script>