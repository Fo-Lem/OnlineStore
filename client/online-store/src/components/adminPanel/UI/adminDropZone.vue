<template>
    <div v-bind="getRootProps()" class="">
        <label for="cover-photo" class="block text-md font-medium leading-6 text-gray-900">Фотографии</label>
        <div  id="droppable" class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
          <div class="text-center">
            <svg  class="mx-auto h-12 w-12 text-gray-300" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <path clip-rule="evenodd" fill-rule="evenodd" d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z"></path>
            </svg>
            <div class="mt-4 flex text-sm leading-6 text-gray-600">
              <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                <span >Upload a file</span>
                <input v-bind="getInputProps()" id="file-upload" name="file-upload" type="file" class="sr-only" />
              </label>
              <p class="pl-1">or drag and drop</p>
            </div>
            <p  class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 5MB</p>
          </div>
        </div>
      </div>



  </template>
  
  <script>
  import { useDropzone } from "vue3-dropzone";
  import axios from "axios";
  
  export default {
    name: "admin-drop-zone",
    setup() {
      const url = "{your_url}"; // Your url on the server side
      const saveFiles = (files) => {
        const formData = new FormData(); // pass data as a form
        for (var x = 0; x < files.length; x++) {
          // append files as array to the form, feel free to change the array name
          formData.append("images[]", files[x]);
        }
        console.log(formData)
  
        // post the formData to your backend where storage is processed. In the backend, you will need to loop through the array and save each file through the loop.
  
        axios
          .post(url, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            console.info(response.data);
          })
          .catch((err) => {
            console.error(err);
          });
      };
  
      function onDrop(acceptFiles, rejectReasons) {
        saveFiles(acceptFiles); // saveFiles as callback
        console.log(rejectReasons);
      }
  
      const { getRootProps, getInputProps, ...rest } = useDropzone({ onDrop });
  
      return {
        getRootProps,
        getInputProps,
        ...rest,
      };
    },
  };
  </script>