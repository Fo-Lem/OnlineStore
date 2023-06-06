<template lang="">
    <div class="flex gap-2 flex-col ">
        <label :for="selectIn" class="block text-md text-gray-900">{{selectName}}</label>
        <div class="flex items-center gap-5">
            <select :id="selectIn" :name="selectIn" @change="changeOption" class="sm:max-w-md sm:leading-6 bg-gray-50 border border-gray-300 text-gray-900 text-md rounded-lg flex w-full p-2 ">
                <option disabled default :value="curentOption.index" :key="curentOption.index" selected>{{nameParser(curentOption.option)}}</option>
                <option v-for="(option, index) in options" :key="index" :value="index">{{nameParser(option)}}</option>
            </select>
            <div v-if="!this.$route.params.itemId"  class="flex gap-2">
            <svg @click="$emit('openAddPopup')" v-if="selectName=='Категория'" class="h-10 w-10 bg-gray-50 border border-gray-300 text-green-700 rounded-lg cursor-pointer hover:text-green-500" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M12 3.75a.75.75 0 01.75.75v6.75h6.75a.75.75 0 010 1.5h-6.75v6.75a.75.75 0 01-1.5 0v-6.75H4.5a.75.75 0 010-1.5h6.75V4.5a.75.75 0 01.75-.75z"></path>
            </svg>
            <svg @click="$emit('openDeletePopup')" v-if="selectName=='Категория'" class="h-10 w-10 bg-gray-50 border border-gray-300 text-red-700 rounded-lg cursor-pointer hover:text-red-500" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"></path>
            </svg>
            <svg fill="none" @click="$emit('openUpdatePopup')" v-if="selectName=='Категория'" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" class="h-10 w-10 bg-gray-50 border border-gray-300 text-yellow-700 rounded-lg cursor-pointer hover:text-yellow-500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"></path>
              </svg>
            </div>
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
        },
        curentOption: {
            default: ''
        }
    },
    methods: {
        changeOption(option) {
            console.log(option.target.value)
            this.$emit(`changeOption${this.selectIn}`, option.target.value)
        },
        nameParser(item) {
            if (item != undefined) {
                if (item.name) {
                    return item.name
                }
                return item
            }

            return 'Выберите из списка'


        }
    }

}
</script>
