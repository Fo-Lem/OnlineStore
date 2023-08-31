import { createRouter, createWebHistory } from 'vue-router'

import customShopContainer from '../components/shopList/customShopContainer.vue'
import customProductList from '../components/shopList/customProductList.vue'
import customProductOverviews from '../components/shopList/customProductOverviews.vue'
import customAdminPanel from '../components/adminPanel/customAdminPanel.vue'
import customBasket from '../components/basketPage/customBasket.vue'
import customAbout from '../components/aboutPage/customAbout.vue'
import adminAnalytics from '../components/adminPanel/adminComponents/adminAnalytics.vue'
import adminPanelCreations from '../components/adminPanel/adminComponents/adminPanelCreations.vue'
import adminPanelUpdateProduct from '../components/adminPanel/adminComponents/adminPanelUpdateProduct.vue'
import adminProducts from '../components/adminPanel/adminComponents/adminProducts.vue'

const routes = [
  { path: '/', redirect: '/catalog' },

  {
    name: 'catalog',
    path: '/catalog',
    component: customShopContainer,
    children: [
      {
        name: 'categoryList', path: '', component: customProductList, props: { type: 'categoryList' },
      },
      {
        name: 'productList', path: 'category_:categoryId', component: customProductList, props: { type: 'productList' },
      },
      { name: 'productOverviews', path: 'category_:categoryId/product_:productId/hero_:heroId', component: customProductOverviews },
    ],
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
    path: '/_adminPanel', redirect: '/_adminPanel/products',
  },
  {
    path: '/_adminPanel',
    component: customAdminPanel,
    children: [
      { name: 'analutics', path: 'analytics', component: adminAnalytics },
      { name: 'products', path: 'products', component: adminProducts },
      { name: 'panelCreations', path: 'admin-panel-creations', component: adminPanelCreations },
      { name: 'panelUpdate', path: 'admin-panel-update-product_:itemId', component: adminPanelUpdateProduct },
    ],
  },

]
const router = createRouter(
  {
    routes,
    history: createWebHistory(),
  },
)
export { router }
