<template lang="">
  <div>
    <div class="relative rounded-md shadow-sm">
      <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center self-center pl-2">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
        </svg>

      </div>
      <input type="text" name="price" id="price" class="block w-full rounded-md border-0 py-1.5 pl-10 pr-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Поиск" />
    </div>
  </div>
</template>
<script>

export default {
  name: "custom-search-input",
  data() {
    return {
    }
  },

}
</script>
<style scoped></style>