<template lang="">
  <header class="bg-white">
    <nav class="mx-auto flex max-w-7xl items-center justify-between px-6 lg:px-8" aria-label="Global">
      <div class="flex items-center gap-2 lg:flex-1">
        
        <router-link to="/catalog" class="-m-1.5 p-1.5">
          <span class="sr-only">WoodHouse</span>
          <img class="h-20 w-auto" src="../../assets/logo.svg" alt="" />
        </router-link>
        <h1 class="text-3xl font-semibold tracking-wider leading-6 text-gray-900">WoodHouse</h1>
      </div>

      <div class="flex lg:hidden">
        
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = !mobileMenuOpen">
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      <div class="items-center hidden lg:gap-x-12 lg:flex ">
        
        <router-link class="font-semibold leading-6 text-gray-900" to="/catalog">Каталог</router-link>
        <router-link class="font-semibold leading-6 text-gray-900" to="/cart">Корзина</router-link>
        <router-link class="font-semibold leading-6 text-gray-900" to="/about">О нас</router-link>

      </div>
    </nav>
    <Dialog as="div" class="lg:hidden" @close="mobileMenuOpen = !mobileMenuOpen" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-10" />
      <DialogPanel class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6  sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <router-link to="/catalog" class="-m-1.5 p-1.5">
            <span class="sr-only">WoodHaus</span>
            <img class="h-20 w-auto" src="../../assets/logo.svg" alt="" />
          </router-link>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = !mobileMenuOpen">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6">
              <router-link class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50" to="/catalog">Каталог</router-link>
              <router-link class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50" to="/cart">Карзина</router-link>
              <router-link class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50" to="/about">О нас</router-link>
              
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
</template>
<script>
import { Dialog, DialogPanel } from '@headlessui/vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'



export default {
  name: "custom-header",
  components: {
    Dialog, DialogPanel, Bars3Icon, XMarkIcon
  },
  data() {
    return {
      mobileMenuOpen: false,
    }

  }

}
</script>
<style scoped></style>
