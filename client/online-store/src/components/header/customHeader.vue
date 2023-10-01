<script lang="ts">
import { defineComponent } from 'vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'

export default defineComponent(

  {
    name: 'CustomHeader',
    components: { Bars3Icon, XMarkIcon },
    data() {
      return {
        mobileMenuOpen: false,
      }
    },
    methods: {
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen
      },
    },

  })
</script>

<template>
  <header class="bg-white mx-auto max-w-7xl px-6 lg:px-8">
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
            src="../../assets/logo.svg"
            alt=""
          >
          <h1 class="text-3xl lg:text-5xl font-semibold tracking-wider leading-6 text-gray-900">
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
            class="h-8 w-8"
            aria-hidden="true"
          />
        </button>
      </div>
      <div class=" hidden lg:gap-x-12 lg:flex items-center">
        <router-link
          class="font-semibold leading-6 text-gray-900"
          to="/catalog"
        >
          Каталог
        </router-link>
        <router-link
          class="font-semibold leading-6 text-gray-900"
          to="/basket"
        >
          Корзина
        </router-link>
        <router-link
          class="font-semibold leading-6 text-gray-900"
          to="/about"
        >
          О нас
        </router-link>
      </div>
      <dialog id="mobileMenu" :open="mobileMenuOpen" class="w-full z-50 backdrop-blur-lg shadow-sm pb-4 md:pb-6 px-6 bg-white top-0 lg:hidden ">
        <div>
          <div class="flex justify-between items-center gap-2 lg:flex-1">
            <router-link
              to="/catalog"
              class="-m-1.5 p-1.5 flex items-center gap-2"
            >
              <img
                class="h-16 lg:h-20 w-auto"
                src="../../assets/logo.svg"
                alt="Логотип"
              >
              <h1 class="text-3xl lg:text-5xl font-semibold tracking-wider leading-6 text-gray-900">
                WoodHouse
              </h1>
            </router-link>
            <button
              type="button"
              @click="toggleMobileMenu"
            >
              <span class="sr-only">Open main menu</span>
              <XMarkIcon
                class="h-8 w-8"
                aria-hidden="true"
              />
            </button>
          </div>

          <div class="items-center flex gap-1 flex-col">
            <router-link
              class="font-semibold leading-6 p-2 text-gray-900"
              to="/catalog"
            >
              Каталог
            </router-link>
            <router-link
              class="font-semibold leading-6 p-2 text-gray-900"
              to="/basket"
            >
              Корзина
            </router-link>
            <router-link
              class="font-semibold leading-6 p-2 text-gray-900"
              to="/about"
            >
              О нас
            </router-link>
          </div>
        </div>
      </dialog>
    </nav>
    <hr class="mx-auto max-w-7xl">
  </header>
</template>

<style scoped></style>
