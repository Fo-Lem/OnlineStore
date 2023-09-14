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

  })
</script>

<template lang="">
  <header class="bg-white">
    <nav
      class="mx-auto flex max-w-7xl items-center justify-between px-6 lg:px-8"
      aria-label="Global"
    >
      <div class="flex items-center gap-2 lg:flex-1">
        <router-link
          to="/catalog"
          class="-m-1.5 p-1.5"
        >
          <span class="sr-only">WoodHouse</span>
          <img
            class="h-20 w-auto"
            src="../../assets/logo.svg"
            alt=""
          >
        </router-link>
        <h1 class="text-3xl font-semibold tracking-wider leading-6 text-gray-900">
          WoodHouse
        </h1>
      </div>

      <div class="flex lg:hidden">
        <button
          type="button"
          class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          <span class="sr-only">Open main menu</span>
          <Bars3Icon
            class="h-6 w-6"
            aria-hidden="true"
          />
        </button>
      </div>
      <div class="items-center hidden lg:gap-x-12 lg:flex ">
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
    </nav>
  </header>
</template>

<style scoped></style>
