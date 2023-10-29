<script lang="ts">
import { ErrorMessage, Field } from 'vee-validate'
import type { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AdminDropZone',
  components: {
    Field, ErrorMessage,
  },
  props: {
    photos: {
      required: true,
      type: Array as PropType<File[]>,
    },
  },
  emits: {

    uploadPhoto(photos: File[]) {
      return photos.length > 0
    },
  },
  data() {
    return {
      isDrag: false,
    }
  },
  methods: {
    uploadPhoto(currentTarget: Event) {
      if (currentTarget.target instanceof HTMLInputElement && currentTarget.target.files)
        this.$emit('uploadPhoto', [...this.photos, ...currentTarget.target.files] as File[])

      this.isDrag = false
    },
    getSrc(photo: File) {
      return URL.createObjectURL(photo)
    },
    removePhoto(index: number) {
      this.$emit('uploadPhoto', this.photos.filter((_p, i) => {
        return i !== index
      }))
    },

  },

})
</script>

<template>
  <div class="flex gap-2 flex-col ">
    <p class="text-md leading-6 text-gray-900 ">
      Фотографии
    </p>

    <ErrorMessage class="text-red-500 text-sm" name="fileUpload" />
    <div
      class="justify-center rounded-lg border border-dashed border-gray-900/25"
      :class="[isDrag ? 'bg-gray-200/60' : '']"
    >
      <div
        id="droppable"
        class="relative block text-md leading-6 m-5 text-gray-900"
      >
        <div
          v-if="photos.length === 0"
          class="flex flex-col items-center justify-center pt-5 pb-6"
        >
          <svg
            aria-hidden="true"
            class="w-10 h-10 mb-3 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
          </svg>
          <p class="mb-2 text-sm text-gray-500 ">
            <span class="font-semibold">Нажмите, чтобы добавить</span> или перетащите
          </p>
          <p class="text-xs text-gray-500 ">
            Только JPG 1000x1000px (3 изображения)
          </p>
        </div>
        <Field
          id="fileUpload"
          name="fileUpload"
          multiple
          required
          max="3"
          type="file"
          class="absolute cursor-pointer top-0 bottom-0 right-0 left-0 opacity-0"
          accept="image/jpg, image/jpeg"
          @change="uploadPhoto"
          @dragenter="isDrag = true"
          @dragleave="isDrag = false"
        />
        <div
          v-if="photos.length > 0"
          class="flex justify-center gap-5"
        >
          <div
            v-for="(photo, index) in photos"
            :key="index"
          >
            <div class="relative cursor-default">
              <img
                class="max-h-48 rounded-md"
                :src="getSrc(photo)"
                :alt="`фотография${index + 1}`"
              >
              <p class="text-sm text-center">
                {{ photo.name }}
              </p>
              <svg
                fill="white"
                class="absolute h-7 cursor-pointer top-1 bg-gray-500/50 rounded-md right-1"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
                @click="removePhoto(index)"
              >
                <path
                  clip-rule="evenodd"
                  fill-rule="evenodd"
                  d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
