<template lang="">
    <form class="py-5 flex flex-col gap-5">
              <div class="flex gap-2 flex-col">
                <label for="name" class="block text-md font-medium leading-6 text-gray-900">Название продукта</label>
                  <div class="flex rounded shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
                    <input type="text" name="name" id="name"  class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder='Меч длинный "Алеша Попович"' />
                  </div>
              </div>
              <div class="flex gap-2 flex-col">
                <label for="category" class="block text-md font-medium text-gray-900">Категория</label>
                <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg flex gap-5 w-full p-2.5 ">
                  <option disabled selected>Выберите категорию</option>
                  <option value="Мечи">Мечи</option>
                  <option value="Щиты">Щиты</option>
                </select>
              </div>
              <div class="flex gap-2 flex-col">
                <label for="category" class="block text-md font-medium text-gray-900">Тип</label>
                <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg flex gap-5 w-full p-2.5 ">
                  <option disabled selected>Выберите тип</option>
                  <option value="Мечи">Мечи</option>
                  <option value="Щиты">Щиты</option>
                </select>
              </div>
              
    
              <div class="flex flex-col gap-2">
                <div>
                  <h2 class=" text-md leading-6 font-medium">Размеры</h2>
                  <p class=" text-xs leading-6 text-gray-400">(Размеры в милиметрах)</p>
                </div>
                <div class="flex flex-col gap-2">
                    <label for="height" class="block text-sm  leading-6 text-gray-900">Высота:</label>
                  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
                    <input type="text" name="height" id="height"  class=" border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 sm:max-w-md" placeholder='400' />
                  </div>
                </div>
                <div class="flex flex-col gap-2">
                    <label for="width" class="block text-sm  leading-6 text-gray-900">Ширина:</label>
                  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
                    <input type="text" name="width" id="width"  class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6" placeholder='400' />
                  </div>
                </div>
                <div class="flex flex-col gap-2">
                    <label for="depth" class="block text-sm  leading-6 text-gray-900">Глубина:</label>
                  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 sm:max-w-md">
                    <input type="text" name="depth" id="depth"  class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6" placeholder='400' />
                  </div>
                </div>
                
              </div>

              <div class="flex flex-col gap-2">
                  <label for="message" class="block text-md font-medium text-gray-900">Описание</label>
                  <textarea id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Write your thoughts here..."></textarea>
              </div>
    
    
              <div class="">
                <label for="cover-photo" class="block text-md font-medium leading-6 text-gray-900">Фотографии</label>
                <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                  <div class="text-center">
                    <svg class="mx-auto h-12 w-12 text-gray-300" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                      <path clip-rule="evenodd" fill-rule="evenodd" d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z"></path>
                    </svg>
                    <div class="mt-4 flex text-sm leading-6 text-gray-600">
                      <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                        <span>Upload a file</span>
                        <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                      </label>
                      <p class="pl-1">or drag and drop</p>
                    </div>
                    <p class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 5MB</p>
                  </div>
                </div>
              </div>
     
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
</template>
<script>

export default {
  name: 'admin-add-products'
}
</script>