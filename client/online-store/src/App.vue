<template>
  <div>
    <custom-header></custom-header>

    <hr class="mx-auto max-w-7xl">

    <router-view></router-view>

    <hr class="mx-auto max-w-7xl">
    
    <custom-footer></custom-footer>
    

  </div>
</template>
<script >
import customHeader from "./components/customHeader.vue"
import customFooter from "./components/customFooter.vue"


export default {
  components: { customHeader,customFooter },

}
</script>
<style scoped></style>