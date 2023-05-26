<template lang="">
    <div class="flex flex-col gap-2">
        <label :for="inputIn" class="block text-md leading-6 text-gray-900">{{inputName}}</label>
      <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
        <input @input="updateInput" :placeholder='placeholder' type="text" :name="inputIn" :id="inputIn" :value="value" class="block flex-1 border-0 bg-transparent p-2.5 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6"  />
      </div>
    </div>
</template>
<script>
export default {
    name: 'admin-input',
    props: {
        value: {
            require: true,
            type: String
        },
        placeholder: {
            require: true,
            type: String
        },
        inputIn: {
            require: true,
            type: String
        },
        inputName: {
            require: true,
            type: String
        }
    },
    methods: {
        updateInput(event) {
            this.$emit(`updateInput`, event.target.value)
        }
    }

}
</script>