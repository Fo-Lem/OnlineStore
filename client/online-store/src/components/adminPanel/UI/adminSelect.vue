<template lang="">
    <div class="flex gap-2 flex-col ">
        <label :for="selectIn" class="block text-md text-gray-900">{{selectName}}</label>
        <div class="flex items-center gap-5">
            <select :id="selectIn" :name="selectIn" @:change="changeOption" class="sm:max-w-md sm:leading-6 bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg flex w-full p-2 ">
                <option disabled default value="" selected>Выберите из списка</option>
                <option v-for="(option, index) in options" :key="index" :value="index">{{option}}</option>
            </select>
            <svg @click="$emit('openPopup')" v-if="selectName=='Категория'" class="h-10 w-10 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg cursor-pointer hover:bg-gray-200" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M12 5.25a.75.75 0 01.75.75v5.25H18a.75.75 0 010 1.5h-5.25V18a.75.75 0 01-1.5 0v-5.25H6a.75.75 0 010-1.5h5.25V6a.75.75 0 01.75-.75z"></path>
            </svg>
        </div>
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
            console.log(option.target.value)
            this.$emit(`changeOption${this.selectIn}`, option.target.value)
        }
    }

}
</script>
