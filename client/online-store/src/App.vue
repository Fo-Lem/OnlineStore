<template>
  <div>
    <custom-header></custom-header>
    
    <hr class="mx-auto max-w-7xl">

    <div class="mx-auto max-w-7xl p-6 flex flex-col-reverse justify-between lg:px-8 md:flex-row ">
      <custom-breadcrumbs class="mt-2 md:mt-0"></custom-breadcrumbs>
      <custom-search-input class="lg:hidden"></custom-search-input>
    </div>

    <custom-product-list></custom-product-list>
  </div>
</template>
<script >
import customHeader from "./components/customHeader.vue"
import customBreadcrumbs from "./components/customBreadcrumbs.vue"
import CustomProductList from "./components/customProductList.vue";
import customSearchInput from "./UI/customSearchInput.vue";


export default {
  components: { customHeader, customBreadcrumbs, CustomProductList, customSearchInput },

}
</script>
<style scoped></style>