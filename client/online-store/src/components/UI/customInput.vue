<template lang="">
  
      <input @input="updateInput($event)" :value="item.count" name="count" id="count" class="h-8 w-8 border bg-white text-center text-xs outline-none" type="number"  min="1" />
  
</template>
<script>

export default {
  name: "custom-input",
  data() {
    return {
    }
  },
  props:{
    item:[Object]
          
    },
    methods:{
       updateInput(event){
        // передаем содержимое инпута
        this.$emit('updateInput',event.target.value)

       } 
    }

}
</script>
<style scoped></style>