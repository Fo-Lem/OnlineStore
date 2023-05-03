import customShopComponent from "../components/customShopComponent.vue"
import customCategoryList from "../components/customCategoryList.vue"
import customTypeList from "../components/customTypeList.vue"
import customProductList from "../components/customProductList.vue"
import customProductOverviews from "../components/customProductOverviews.vue"
import customCart from '../components/customCart.vue';
import { createRouter } from "vue-router"
import { createWebHistory } from "vue-router"

const routes = [
  { path: '/', redirect: '/catalog' },

  {
    name: 'catalog',
    path: '/catalog',
    component: customShopComponent,
    children: [
      { name: 'categoryList',path: '', component: customCategoryList },
      { name: 'typeList',path: 'category=:categoryName', component: customTypeList },
      { name: 'productList',path: 'category=:categoryName/type=:typeName', component: customProductList },
      { name: 'productOverviews',path: 'category/:categoryName/type/:typeName/product/:productName/', component: customProductOverviews }

    ]
  },
  {
    path: '/cart',
    component: customCart
  },
  

]
const router= createRouter(
    {
        routes,
        history:createWebHistory(import.meta.env.BASE_URL)
    }
)
export default router