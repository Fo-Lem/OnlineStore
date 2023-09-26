import { createRouter, createWebHistory } from 'vue-router'
import customShopContainer from '../components/shopList/customShopContainer.vue'
import customProductList from '../components/shopList/customProductList.vue'
import customProductOverviews from '../components/shopList/customProductOverviews.vue'
import customAdminPanel from '../components/adminPanel/customAdminPanelWrapper.vue'
import customBasket from '../components/basketPage/customBasket.vue'
import customAbout from '../components/aboutPage/customAbout.vue'
import adminAnalytics from '../components/adminPanel/adminComponents/adminAnalytics.vue'
import adminPanelCreations from '../components/adminPanel/adminComponents/adminPanelCreations.vue'
import adminPanelUpdateProduct from '../components/adminPanel/adminComponents/adminPanelUpdateProduct.vue'
import adminProducts from '../components/adminPanel/adminComponents/adminProducts.vue'
import adminAuth from '../components/adminPanel/adminComponents/adminAuth.vue'
import { isAdmin } from '../components/adminPanel/adminComponents/http/isAdmin'
import { relogin } from '../components/adminPanel/adminComponents/http/relogin'

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
    path: '/basket',
    component: customBasket,
  },
  {
    path: '/about',
    component: customAbout,
  },
  {
    name: 'adminPanel',
    path: '/_adminPanel',
    redirect: '/_adminPanel/products',
    component: customAdminPanel,
    children: [
      { name: 'authorization', path: 'auth', component: adminAuth },
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
router.beforeEach(async (to, _from, next) => {
  if (to.name === 'adminPanel' || to.name === 'analutics' || to.name === 'products' || to.name === 'panelCreations' || to.name === 'panelUpdate') {
    if (await isAdmin()) {
      next()
    }
    else {
      if (await relogin())
        next()

      else
        next({ name: 'authorization' })
    }

    // next()
  }
  else { next() }

  console.error(to.name)
})
export { router }
