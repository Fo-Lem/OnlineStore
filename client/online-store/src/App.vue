<template>
  <div>
    <custom-header></custom-header>

    <hr class="mx-auto max-w-7xl">

    <router-view></router-view>

    

  </div>
</template>
<script >
import customHeader from "./components/customHeader.vue"


export default {
  components: { customHeader },

}
</script>
<style scoped></style>