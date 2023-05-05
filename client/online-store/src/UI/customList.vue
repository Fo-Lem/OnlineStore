<template>
    <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-lg bg-gray-200 xl:aspect-h-8 xl:aspect-w-7">
        <img :src="'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'" :alt="list.imageAlt" class="h-full w-full object-cover object-center group-hover:opacity-75" />
      </div>
      
      <h3 v-if="list.name" class="mt-4 text-sm text-gray-700">{{ list.name }}</h3>
      <p v-if="list.price" class="mt-4 text-sm text-gray-700">{{ list.price }}</p>
</template>
<script>
export default {
  name:'custom-list',

    props: {
    list: {
      require: true
    }
  }
}
</script>
<style scoped>
    
</style>