<template>
  <div>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != 'adminPanel'">
      <custom-header></custom-header>
      <hr class="mx-auto max-w-7xl">
    </div>
    <custom-error-page v-if="error" v-bind:error="error"></custom-error-page>
    <custom-loading-spiner v-if="!loading"></custom-loading-spiner>

    <router-view v-if="loading" v-bind:basket="basket" v-bind:catalog="catalog" v-bind:searchInput="searchInput"
      @update-search-input="updateSearchInput" @delete-product-basket="deleteProductBasket"
      @update-count-product-basket="(newCount, id) => { updateCountProductBasket(newCount, id) }"
      @add-product-basket="(curentProduct) => { addProductBasket(basket, curentProduct) }">
    </router-view>

    <div v-if="$router.currentRoute.value.path.split('/')[1] != 'adminPanel'">
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

    async getCategorys() {
      await axios
        .get('http://176.99.12.84/api/catalog')
        .then(response => {
          this.catalog = response.data;
        })
        .catch(error => {
          console.log(error)
          //this.error = error;
        })
        .finally(() => {
          this.loading = true;
          console.log(this.catalog)
        });

    }
  },
  beforeMount() {

    if (localStorage.basket != undefined && localStorage.basket != "") {
      console.log(localStorage.basket)
      this.basket = JSON.parse(localStorage.basket)
      console.log(this.basket)
    }
    this.catalog = {
      categories: {
        1: {
          id: 1,
          name: "Щит",
          cover_path: null,
          product_types: {
            1: {
              id: 1,
              name: "Миндаль"
            },
            2: {
              id: 2,
              name: "Круглый"
            }
          }
        },
        2: {
          id: 2,
          name: "Меч",
          cover_path: null,
          product_types: {
            3: {
              id: 3,
              name: "Художественный"
            },
            4: {
              id: 4,
              name: "Обыкновенный"
            }
          }
        },
        3: {
          id: 3,
          name: "Топор",
          cover_path: null,
          product_types: {
            3: {
              id: 3,
              name: "Художественный"
            },
            4: {
              id: 4,
              name: "Обыкновенный"
            }
          }
        },
        4: {
          id: 4,
          name: "Шашка",
          cover_path: null,
          product_types: {
            3: {
              id: 3,
              name: "Художественный"
            },
            4: {
              id: 4,
              name: "Обыкновенный"
            }
          }
        },
        5: {
          id: 5,
          name: "Катана",
          cover_path: null,
          product_types: {
            
          }
        }
      },
      heroes: {
        1: {
          id: 1,
          name: "Добрыня Никитич"
        },
        2: {
          id: 2,
          name: "Алеша Попович"
        },
        3: {
          id: 3,
          name: "Илья Муромец"
        },
        4: {
          id: 4,
          name: "Александр Невский"
        },
        5: {
          id: 5,
          name: "Иван Сусанин"
        }
      },
      items: {
        1: {
          id: 1,
          name: "ЩИТ МИНДАЛЬ \"ПЕРУН\"",
          hero_id: 1,
          product_type_id: 1,
          category_id: 1,
          description: "Вес 150",
          img_path: "/imgs/test",
          size: "650x480",
          price: 400.0
        },
        2: {
          id: 2,
          name: "Меч Илья Муромец",
          hero_id: 3,
          product_type_id: 4,
          category_id: 2,
          description: "Вес 200г. \\n Габариты 600х80х20",
          img_path: "imgs/test",
          size: "600x80x20",
          price: 150.0
        },
        3: {
          id: 3,
          name: "Меч Илья Муромец 2",
          hero_id: 3,
          product_type_id: 4,
          category_id: 2,
          description: "Вес 200г. \\n Габариты 600х80х20",
          img_path: "imgs/test",
          size: "600x80x20",
          price: 150.0
        },
        4: {
          id: 4,
          name: "Меч Александр Невский",
          hero_id: 4,
          product_type_id: 4,
          category_id: 2,
          description: "Вес 200г. \\n Габариты 600х80х20",
          img_path: "imgs/test",
          size: "600x80x20",
          price: 150.0
        },
        5: {
          id: 5,
          name: "Меч Алеша Попович",
          hero_id: 2,
          product_type_id: 4,
          category_id: 2,
          description: "Вес 200г. \\n Габариты 600х80х20",
          img_path: "imgs/test",
          size: "600x80x20",
          price: 150.0
        }
      }
    }
    //this.getCategorys()
    this.loading = true;
  }


}



</script>
<style scoped></style>