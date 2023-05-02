<template lang="">
  <div>
    <div class="mx-auto max-w-7xl p-6 flex flex-col-reverse justify-between lg:px-8 md:flex-row ">
      <custom-breadcrumbs class="mt-2 md:mt-0"></custom-breadcrumbs>
      <custom-search-input class="lg:hidden"></custom-search-input>
    </div>
    <custom-product-list></custom-product-list>
  </div>
</template>
<script>
import customSearchInput from "../UI/customSearchInput.vue";
import customBreadcrumbs from "./customBreadcrumbs.vue"
import customProductList from "./customProductList.vue";
export default {
  components:{customSearchInput,customBreadcrumbs,customProductList},
  
  name: "custom-shop-component",
  data() {
    return {
      
    }
  },

}
</script>
<style scoped></style>