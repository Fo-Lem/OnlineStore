<template lang="">
    <div class="flex gap-2 flex-col ">
        <label :for="selectIn" class="block text-md text-gray-900">{{selectName}}</label>
        <div class="flex items-center gap-5">
            <select :id="selectIn" :name="selectIn" @:change="changeOption" class="sm:max-w-md sm:leading-6 bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg flex w-full p-2 ">
                <option disabled default value="" selected>Выберите из списка</option>
                <option v-for="(option, index) in options" :key="index" :value="index">{{nameParser(option)}}</option>
            </select>
            <svg @click="$emit('openAddPopup')" v-if="selectName=='Категория'" class="h-10 w-10 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg cursor-pointer hover:text-green-500" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M12 3.75a.75.75 0 01.75.75v6.75h6.75a.75.75 0 010 1.5h-6.75v6.75a.75.75 0 01-1.5 0v-6.75H4.5a.75.75 0 010-1.5h6.75V4.5a.75.75 0 01.75-.75z"></path>
            </svg>
            <svg @click="$emit('openDeletePopup')" v-if="selectName=='Категория'" class="h-10 w-10 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg cursor-pointer hover:text-red-500" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"></path>
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
        },
        nameParser(item){
            if(item.name){
                return item.name
            }
            return item
        }
    }

}
</script>
