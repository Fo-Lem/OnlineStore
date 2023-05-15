<template lang="">
  <div v-if="loading===true">
    <div class="mx-auto ">
      <button @click="mobileMenuOpen = !mobileMenuOpen" data-drawer-target="default-sidebar" data-drawer-toggle="default-sidebar" aria-controls="default-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ml-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
        <span class="sr-only">Open sidebar</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
        </svg>
     </button>

     <Dialog as="div" class="sm:hidden" @close="mobileMenuOpen = !mobileMenuOpen" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-10" />
      <DialogPanel class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
          <ul class="space-y-2 font-medium">
             <li class="flex gap-5 justify-between">
                <router-link :to="{ name: 'analutics'}" class="flex items-center w-full p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                  <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path clip-rule="evenodd" fill-rule="evenodd" d="M12.577 4.878a.75.75 0 01.919-.53l4.78 1.281a.75.75 0 01.531.919l-1.281 4.78a.75.75 0 01-1.449-.387l.81-3.022a19.407 19.407 0 00-5.594 5.203.75.75 0 01-1.139.093L7 10.06l-4.72 4.72a.75.75 0 01-1.06-1.061l5.25-5.25a.75.75 0 011.06 0l3.074 3.073a20.923 20.923 0 015.545-4.931l-3.042-.815a.75.75 0 01-.53-.919z"></path>
                  </svg>
                    <span class="ml-3">Analytics</span>
                   
                </router-link>
                <button @click="mobileMenuOpen = !mobileMenuOpen" data-drawer-target="default-sidebar" data-drawer-toggle="default-sidebar" aria-controls="default-sidebar" type="button" class="inline-flex items-center p-2 h-fit text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                  <span class="sr-only">Open sidebar</span>
                  <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                     <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
                  </svg>
               </button>
             </li>
             <li>
                <router-link :to="{ name: 'products'}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                 <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd"></path></svg>
                 <span class="flex-1 ml-3 whitespace-nowrap">Products</span>
                   </router-link>
             </li>
             <li>
                <router-link :to="{ name: 'addProductsForm'}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                   <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"></path><path d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"></path></svg>
                   <span class="flex-1 ml-3 whitespace-nowrap">Add Products</span></router-link>
             </li>
             <li>
                <router-link :to="{ name: 'admins'}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                   <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
                   <span class="flex-1 ml-3 whitespace-nowrap">Admins</span>
                </router-link>
             </li>
          </ul>
       </div>
      </DialogPanel>
    </Dialog>
    
     <aside  id="default-sidebar" class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
        <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
           <ul class="space-y-2 font-medium">
              <li>
                 <router-link @click="curentPage='Аналитика'" :to="{ name: 'analutics'}"  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                  <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path clip-rule="evenodd" fill-rule="evenodd" d="M12.577 4.878a.75.75 0 01.919-.53l4.78 1.281a.75.75 0 01.531.919l-1.281 4.78a.75.75 0 01-1.449-.387l.81-3.022a19.407 19.407 0 00-5.594 5.203.75.75 0 01-1.139.093L7 10.06l-4.72 4.72a.75.75 0 01-1.06-1.061l5.25-5.25a.75.75 0 011.06 0l3.074 3.073a20.923 20.923 0 015.545-4.931l-3.042-.815a.75.75 0 01-.53-.919z"></path>
                  </svg>
                    <span class="ml-3">Analytics</span>
                 </router-link>
              </li>
              <li>
                 <router-link @click="curentPage='Продукты'" :to="{ name: 'products'}"  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                  <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd"></path></svg>
                  <span class="flex-1 ml-3 whitespace-nowrap">Products</span>
                    </router-link>
              </li>
              <li>
                 <router-link @click="curentPage='Добавление продукта'" :to="{ name: 'addProductsForm'}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                    <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"></path><path d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"></path></svg>
                    <span class="flex-1 ml-3 whitespace-nowrap">Add Products</span></router-link>
              </li>
              <li>
                 <router-link @click="curentPage='Админы'" :to="{ name: 'admins'}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                    <svg aria-hidden="true" class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
                    <span class="flex-1 ml-3 whitespace-nowrap">Admins</span>
                 </router-link>
              </li>
           </ul>
        </div>
     </aside>
     
     <div class="p-4 sm:ml-64">
      <admin-header></admin-header>
      <router-view></router-view>
     </div>
    </div> 
  </div>
</template>
<script>
import axios from 'axios';
import adminHeader from './adminComponents/adminHeader.vue';
export default {
   components:{adminHeader},
   name: "custom-admin-panel",

   data() {
      return {
         loading: false,
         mobileMenuOpen: false,
         curentPage:'Аналитика',
         categorys:{}
         

      }
   },
   
  methods: {
    async getCategorys() {
      await axios
        .get('http://localhost:555/api/catalog/')
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
