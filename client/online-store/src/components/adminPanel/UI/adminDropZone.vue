<template>
  <div class="flex gap-2 flex-col ">
    <p class="text-md leading-6 text-gray-900 ">Фотографии</p>
    <div :class="[isDrag ? 'bg-gray-200/60' : '', 'justify-center rounded-lg border border-dashed border-gray-900/25']">
        <div id="droppable" class="relative block text-md leading-6 m-5 text-gray-900">
          <span v-if="!Object.keys(photos).length>0" class="block text-center p-12">Загрузите файлы</span>
          <input @change="uploadPhoto" @dragenter="isDrag=true" @dragleave="isDrag=false" id="fileUpload" name="fileUpload" multiple type="file" class="absolute cursor-pointer  top-0 bottom-0 right-0 left-0 opacity-0" />
          <div v-if="Object.keys(photos).length>0" class="flex justify-center p-5 ">
            <div v-for="(photo, index) in photos" :key="index">
              <div class="relative cursor-default">
              <img class="max-h-52 rounded-md" :src="getSrc(photo)" :alt="`фотография${index}`">
              <p class="text-sm text-center">{{photo.name}}</p>
              <svg fill="white" @click.stop.prevent="removePhoto(index)" class="absolute h-7 cursor-pointer top-1 bg-gray-500/50 rounded-md right-1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"></path>
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
      photos: [],
      isDrag:false
    }
  },
  methods: {
    uploadPhoto(currentTarget) {
      if (currentTarget.target.files) {
        this.photos = [...this.photos, ...Array.from(currentTarget.target.files)]
        console.log(this.photos)
      }
      if (fileUpload.value) {
        fileUpload.value = '';
      }
      this.isDrag = false;
    },
    getSrc(photo) {
      return URL.createObjectURL(photo)
    },
    removePhoto(index){
      this.photos=this.photos.filter((p,i)=>i!==index)
    }

  }

};
</script>