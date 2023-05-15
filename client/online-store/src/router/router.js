import customShopContainer from "../components/shopList/customShopContainer.vue"
import customProductList from "../components/shopList/customProductList.vue"
import customProductOverviews from "../components/shopList/customProductOverviews.vue"
import customAdminPanel from "../components/adminPanel/customAdminPanel.vue"
import customBasket from '../components/basketPage/customBasket.vue';
import customAbout from '../components/aboutPage/customAbout.vue';
import adminAnalytics from '../components/adminPanel/adminComponents/adminAnalytics.vue';
import adminAddProductsForm from '../components/adminPanel/adminComponents/adminAddProductsForm.vue';
import adminProducts from '../components/adminPanel/adminComponents/adminProducts.vue';
import adminAdmins from '../components/adminPanel/adminComponents/adminAdmins.vue';
import { createRouter } from "vue-router"
import { createWebHistory } from "vue-router"

const routes = [
  { path: '/', redirect: '/catalog', },

  {
    name: 'catalog',
    path: '/catalog',
    component: customShopContainer,
    children: [
      { name: 'categoryList',path: '', component: customProductList,props: { type: 'categoryList' }},
      { name: 'productList',path: 'category_:categoryId', component: customProductList,props: { type: 'productList'} },
      { name: 'productOverviews',path: 'category_:categoryId/product_:productId/hero_:heroId', component: customProductOverviews }
    ]
  },
  {
    path: '/cart',
    component: customBasket,
  },
  {
    path: '/about',
    component: customAbout,
  },
  {
     path: '/admin', redirect: '/admin/analytics', 
  },
  {
    path: '/admin',
    component: customAdminPanel,
    children: [
      { name: 'analutics',path: 'analytics', component: adminAnalytics },
      { name: 'products',path: 'products', component: adminProducts },
      { name: 'addProductsForm',path: 'add-products-form', component: adminAddProductsForm },
      { name: 'admins',path: 'admins', component: adminAdmins }
    ]
  }
  

]
const router= createRouter(
    {
        routes,
        history:createWebHistory(import.meta.env.BASE_URL)
    }
)
export default router