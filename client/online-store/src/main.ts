import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { router } from './router/router'
import componentsAdmin from './components/adminPanel/UI/index'

const app = createApp(App)

for (const component of componentsAdmin)
  app.component(component.name, component)

app
  .use(router)
  .mount('#app')
