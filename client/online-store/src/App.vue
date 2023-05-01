<template>
  <div>
    <custom-header></custom-header>
    <custom-breadcrumbs></custom-breadcrumbs>
  </div>
</template>
<script >
import customHeader  from "./components/customHeader.vue"
import customBreadcrumbs  from "./components/customBreadcrumbs.vue"
export default {
  components:{customHeader,customBreadcrumbs},

}
</script>
<style scoped>
  
</style>