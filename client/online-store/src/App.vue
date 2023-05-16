<template>
  <div>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != 'admin'">
      <custom-header></custom-header>
      <hr class="mx-auto max-w-7xl">
    </div>
    <custom-error-page v-if="error" v-bind:error="error"></custom-error-page>
    <custom-loading-spiner v-if="!loading"></custom-loading-spiner>

    <router-view v-if="loading" v-bind:basket="basket" v-bind:categorys="categorys" v-bind:searchInput="searchInput"
      @update-search-input="updateSearchInput" @delete-product-basket="deleteProductBasket"
      @update-count-product-basket="(newCount, id) => { updateCountProductBasket(newCount, id) }"
      @add-product-basket="(curentProduct) => { addProductBasket(basket, curentProduct) }">
    </router-view>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != 'admin'">
      <hr class="mx-auto max-w-7xl">
      <custom-footer></custom-footer>
    </div>

  </div>
</template>
<script >
import customHeader from "./components/header/customHeader.vue"
import customFooter from "./components/footer/customFooter.vue"
import customErrorPage from './components/errorPage/customErrorPage.vue'
import axios from 'axios';
import { addProductBasket, deleteProductBasket, updateCountProductBasket } from "./controllers/basketController";


export default {
  components: { customHeader, customFooter, customErrorPage },
  data() {
    return {
      categorys: {},
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

    async getCategorys() {
      await axios
        .get('http://176.99.12.84/api/catalog/',
          {
            headers: {
              'Access-Control-Allow-Origin': '*'
            }
          })
        .then(response => {
          console.log(response.data)
          this.categorys = response.data;
        })
        .catch(error => {
          console.log(error)
          //this.error = error;
        })
        .finally(() => {
          this.loading = true;
        });

    }
  },
  beforeMount() {

    if (localStorage.basket != undefined && localStorage.basket != "") {
      console.log(localStorage.basket)
      this.basket = JSON.parse(localStorage.basket)
      console.log(this.basket)
    }
    this.categorys = {
      1: {
        id: 1,
        name: 'Щиты',
        imageSrc: `https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg`,
        products_type: {
          1: {
            id: 1,
            name: 'Щит круглый',
            heroes: {
              1: {
                id: 1,
                name: 'Илья',
                items: [{
                  id: 1,
                  name: 'Щит миндаль \"Илья Муромец\"',
                  price: 4000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              },
              2: {
                id: 2,
                name: 'Добрыня',
                items: [{
                  id: 1,
                  name: 'Щит миндаль \"Добрыня Никитич\"',
                  price: 4000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              },
              3: {
                id: 3,
                name: 'Алеша',
                items: [{
                  id: 1,
                  name: 'Щит миндаль \"Алеша Попович\"',
                  price: 4000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              }
            }
          }
        }
      },
      2: {
        id: 2,
        name: 'Мечи',
        imageSrc: `https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-02.jpg`,
        products_type: {
          1: {
            id: 1,
            name: 'Меч длинный',
            heroes: {
              1: {
                id: 1,
                name: 'Илья',
                items: [{
                  id: 1,
                  name: 'Меч длинный \"Илья Муромец\"',
                  price: 3000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              },
              2: {
                id: 2,
                name: 'Добрыня',
                items: [{
                  id: 1,
                  name: 'Меч длинный \"Добрыня Никитич\"',
                  price: 3000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              },
              3: {
                id: 3,
                name: 'Алеша',
                items: [{
                  id: 1,
                  name: 'Меч длинный \"Алеша Попович\"',
                  price: 3000,
                  discriptions: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et nisi quae reprehenderit eveniet quo numquam minus dolore? Vitae aspernatur, illo exercitationem neque earum atque culpa possimus facilis rem perspiciatis molestiae.',
                  size: '650x480x200',
                }]
              }
            }
          }
        }
      }
    }
    this.getCategorys()


  }


}
</script>
<style scoped></style>