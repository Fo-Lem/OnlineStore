<template>
  <div class="flex gap-2 flex-col ">
    <p class="text-md leading-6 text-gray-900 ">Фотографии</p>
    <div :class="[isDrag ? 'bg-gray-200/60' : '', 'justify-center rounded-lg border border-dashed border-gray-900/25']">
      <div id="droppable" class="relative block text-md leading-6 m-5 text-gray-900">
        <div v-if="!Object.keys(photos).length > 0" class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg aria-hidden="true" class="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor"
            viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
          </svg>
          <p class="mb-2 text-sm text-gray-500 "><span class="font-semibold">Click to upload</span> or drag and drop</p>
          <p class="text-xs text-gray-500 ">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
        </div>
        <input @change="uploadPhoto" @dragenter="isDrag = true" @dragleave="isDrag = false" id="fileUpload" name="fileUpload"
          multiple type="file" class="absolute cursor-pointer top-0 bottom-0 right-0 left-0 opacity-0" />
        <div v-if="Object.keys(photos).length > 0" class="flex justify-center gap-5">
          <div v-for="(photo, index) in photos" :key="index">
            <div class="relative cursor-default">
              <img class="max-h-48 rounded-md" :src="getSrc(photo)" :alt="`фотография${index}`">
              <p class="text-sm text-center">{{ photo.name }}</p>
              <svg fill="white" @click.stop.prevent="removePhoto(index)"
                class="absolute h-7 cursor-pointer top-1 bg-gray-500/50 rounded-md right-1" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd"
                  d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z">
                </path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>

export default {
  name: "admin-drop-zone",
  data() {
    return {
      isDrag: false
    }
  },
  props: {
        photos: {
            require: true,
            type: Array
        }
    },
  methods: {
    uploadPhoto(currentTarget) {
      if (currentTarget.target.files) {
        this.$emit('uploadPhoto',[...this.photos, ...Array.from(currentTarget.target.files)])
      }
      if (fileUpload.value) {
        fileUpload.value = '';
      }
      this.isDrag = false;
    },
    getSrc(photo) {
      return URL.createObjectURL(photo)
    },
    removePhoto(index) {
      this.$emit('uploadPhoto',this.photos.filter((p, i) => i !== index))
    }

  }

};
</script>