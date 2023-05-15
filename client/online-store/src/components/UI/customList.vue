<template>
  <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-xl xl:aspect-h-8 xl:aspect-w-7">
    <div class="">
      <img
        :src="list.imageSrc ? list.imageSrc : `https://tailwindui.com/img/ecommerce-images/category-page-0${$route.params.categoryId}-image-card-01.jpg`"
        :alt="list.imageAlt" class="h-full w-full object-cover rounded-lg object-center hover:opacity-75" />
      <div class="flex justify-between py-2 items-center">
        <h3 v-if="list.name" class="text-gray-900">{{ list.name }}</h3>
        <p v-if="list.heroes" class="text-gray-900"> Цена: {{ list.heroes[1].items[0].price }} р</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'custom-list',

  props: {
    list: {
      require: true
    }
  }
}
</script>
<style scoped></style>