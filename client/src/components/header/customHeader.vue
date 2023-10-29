<script lang="ts">
import type { PropType } from 'vue'
import { defineComponent } from 'vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import type { basket } from '../../controllers/basketController'

export default defineComponent(

  {
    name: 'CustomHeader',
    components: { Bars3Icon, XMarkIcon },
    props: {
      basket: {
        required: true,
        type: Object as PropType<basket>,
      },
    },
    data() {
      return {
        mobileMenuOpen: false,
      }
    },
    methods: {
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen
      },
      imgUrl() {
        return `${import.meta.env.VITE_BASE_URL}/imgs/logo.svg`
      },
    },

  })
</script>

<template>
  <header class=" mx-auto max-w-7xl px-6 lg:px-8">
    <nav
      class="flex justify-between"
      aria-label="Global"
    >
      <div class="flex gap-2">
        <router-link
          to="/catalog"
          class="flex items-center gap-2"
        >
          <img
            class="h-16 lg:h-20 w-auto"
            :src="imgUrl()"
            alt=""
          >
          <h1 class="text-3xl lg:text-5xl font-semibold tracking-wider leading-6 text-primary">
            WoodHouse
          </h1>
        </router-link>
      </div>

      <div class="flex items-center lg:hidden">
        <button
          type="button"
          @click="toggleMobileMenu"
        >
          <span class="sr-only">Open main menu</span>
          <Bars3Icon
            class="h-8 w-8 text-primary"
            aria-hidden="true"
          />
        </button>
      </div>
      <div class=" hidden text-lg lg:gap-x-12 lg:flex items-center">
        <router-link
          class="font-semibold leading-6 text-primary"
          to="/catalog"
        >
          Каталог
        </router-link>
        <router-link
          class="font-semibold leading-6 text-primary"
          to="/basket"
        >
          Корзина <span v-if="Object.keys(basket).length > 0" class="ml-2 bg-primary-light-1 text-primary-dark rounded-lg px-2 py-0.5">{{ Object.keys(basket).length }}</span>
        </router-link>
      </div>
      <dialog id="mobileMenu" :open="mobileMenuOpen" class="w-full bg-primary-light-2 z-50 backdrop-blur-lg shadow-sm pb-4 md:pb-6 px-6 bg-primary-light top-0 lg:hidden ">
        <div>
          <div class="flex justify-between items-center gap-2 lg:flex-1">
            <router-link
              to="/catalog"
              class="-m-1.5 p-1.5 flex items-center gap-2"
            >
              <img
                class="h-16 lg:h-20 w-auto"
                :src="imgUrl()"
                alt="Логотип"
              >
              <h1 class="text-3xl lg:text-5xl font-semibold tracking-wider leading-6 text-primary">
                WoodHouse
              </h1>
            </router-link>
            <button
              type="button"
              @click="toggleMobileMenu"
            >
              <span class="sr-only">Open main menu</span>
              <XMarkIcon
                class="h-8 w-8 text-primary"
                aria-hidden="true"
              />
            </button>
          </div>

          <div class="items-center text-lg flex gap-1 flex-col">
            <router-link
              class="font-semibold leading-6 p-2 text-primary"
              to="/catalog"
            >
              Каталог
            </router-link>
            <router-link
              class="font-semibold leading-6 p-2 text-primary"
              to="/basket"
            >
              Корзина
            </router-link>
          </div>
        </div>
        <hr class="border-primary border-t-2">
      </dialog>
    </nav>
  </header>
</template>

<style scoped>
.router-link-active{
  font-weight: bold;

}
</style>
