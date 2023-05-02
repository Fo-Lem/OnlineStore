import customShopComponent from "../components/customShopComponent.vue"
import customCart from '../components/customCart.vue';
import { createRouter } from "vue-router"
import { createWebHistory } from "vue-router"

const routes = [
  { path: '/', redirect: '/home' },

  {
    path: '/home',
    component: customShopComponent
  },
  {
    path: '/cart',
    component: customCart
  }

]
const router= createRouter(
    {
        routes,
        history:createWebHistory(import.meta.env.BASE_URL)
    }
)
export default router