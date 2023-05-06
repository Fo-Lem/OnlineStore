import customShopComponent from "../components/customShopComponent.vue"
import customProductList from "../components/customProductList.vue"
import customProductOverviews from "../components/customProductOverviews.vue"
import customCart from '../components/customCart.vue';
import customAbout from '../components/customAbout.vue';
import { createRouter } from "vue-router"
import { createWebHistory } from "vue-router"

const routes = [
  { path: '/', redirect: '/catalog', },

  {
    name: 'catalog',
    path: '/catalog',
    component: customShopComponent,
    props: { type:"catalog" },
    children: [
      { name: 'categoryList',path: '',props: { type:"categoryList" }, component: customProductList },
      { name: 'productList',path: 'category_:categoryId',props: { type:"productList" }, component: customProductList },
      { name: 'productOverviews',path: 'category_:categoryId/product_:productId/hero_:heroId',props: { type:"productOverviews" }, component: customProductOverviews }
    ]
  },
  {
    path: '/cart',
    component: customCart,
  },
  ,
  {
    path: '/about',
    component: customAbout,
  }
  

]
const router= createRouter(
    {
        routes,
        history:createWebHistory(import.meta.env.BASE_URL)
    }
)
export default router