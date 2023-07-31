<template>
  <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-xl xl:aspect-h-8 xl:aspect-w-7">
    <div class="">
      <img :src="imgUrl" class="h-full w-full object-cover rounded-lg object-center hover:opacity-75" />
      <div class="flex justify-between py-2 items-center">
        <h3 v-if="list.name" class="text-gray-900">{{ list.name }}</h3>
        <p v-if="list.items" class="text-gray-900"> Цена: {{ list.items[Object.keys(this.list.items)[0]].price }} р</p>
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
  },

  computed: {
    imgUrl() {
      if (this.list.cover_path) {
        return `${import.meta.env.VITE_BASE_URL}${this.list.cover_path.slice(2)}`
      }
      if (this.list.items) {
        let item = this.list.items[Object.keys(this.list.items)[0]]
        return `${import.meta.env.VITE_BASE_URL}${item.img_path}/${item.art}_0.jpg`
      }
      
    }

  }
}
</script>
<style scoped></style>