<template lang="">
    <div class="">
        <ol class="flex justify-center text-gray-700 lg:justify-start">
          <li class="pr-2"><a href="#" class="hover:underline">Главная</a></li>
          <li class="text-gray-500 select-none">/</li>
          <li v-if="$route.params.categoryId" class="px-2"><a href="#" class="hover:underline">{{categorys[$route.params.categoryId].name}}</a></li>
          <li v-if="$route.params.typeId" class="text-gray-500 select-none">/</li>
          <li v-if="$route.params.categoryId&&$route.params.typeId" class="px-2 text-gray-500">{{categorys[$route.params.categoryId].types[$route.params.typeId].name}}</li>
        </ol>
      </div>
</template>
<script>
export default {
    name:"custom-breadcrumbs",
    props: {
      categorys: {
      type:Object,
      require: true
    }
  }
    
}
</script>
<style scoped>
    
</style>