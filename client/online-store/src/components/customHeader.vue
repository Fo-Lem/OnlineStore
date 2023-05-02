<template lang="">
  <header class="bg-white">
    <nav class="mx-auto flex max-w-7xl items-center justify-between px-6 lg:px-8" aria-label="Global">
      <div class="flex lg:flex-1">
        <a href="#" class="-m-1.5 p-1.5">
          <span class="sr-only">WoodHaus</span>
          <img class="h-20 w-auto" src="../assets/6_kopia-01.svg" alt="" />
        </a>
      </div>

      <div class="flex lg:hidden">
        
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = true">
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      <div class="items-center hidden lg:gap-x-12 lg:flex ">
        <custom-search-input></custom-search-input>
        <a href="#" class="text-sm font-semibold leading-6 text-gray-900">О нас</a>
        <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Карзина</a>
      </div>
    </nav>
    <Dialog as="div" class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-10" />
      <DialogPanel class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6  sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <a href="#" class="-m-1.5 p-1.5">
            <span class="sr-only">WoodHaus</span>
            <img class="h-20 w-auto" src="../assets/6_kopia-01.svg" alt="" />
          </a>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6">
              <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">О нас</a>
              <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Карзина</a>
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
</template>
<script>
import {Dialog,DialogPanel} from '@headlessui/vue'
import {Bars3Icon,XMarkIcon} from '@heroicons/vue/24/outline'

import customSearchInput from "../UI/customSearchInput.vue";



export default {
  name: "custom-header",
  components: {
    Dialog,DialogPanel,Bars3Icon,XMarkIcon,customSearchInput},
  data() {
    return {
      mobileMenuOpen: false
    }
  },

}
</script>
<style scoped></style>
