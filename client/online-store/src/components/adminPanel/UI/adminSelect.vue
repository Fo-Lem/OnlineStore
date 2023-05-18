<template lang="">
    <div class="flex gap-2 flex-col ">
        <label :for="selectIn" class="block text-md text-gray-900">{{selectName}}</label>
        <select :id="selectIn" @:change="changeOption" class="sm:max-w-md sm:text-sm sm:leading-6 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg flex w-full p-2.5 ">
          <option disabled default value="" selected>Выберите из списка</option>
          <option v-for="(option, index) in options" :key="index" :value="index">{{option}}</option>
        </select>
      </div>
</template>
<script>
export default {
    name: 'admin-select',
    props: {
        options: {
            require: true,
            type: Object
        },
        selectIn: {
            require: true,
            type: String
        },
        selectName: {
            require: true,
            type: String
        }
    },
    methods: {
        changeOption(option) {
            this.$emit(`changeOption${this.selectIn}`, option.target.value)
        }
    }

}
</script>