<template lang="">
    <div class="relative shadow-md sm:rounded-lg">
        <table class="w-full text-sm text-left text-gray-500 ">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 ">
                <tr>
                    <!-- <th scope="col" class="px-6 py-3">
                        <span class="sr-only">choice</span>
                    </th> -->
                    <th scope="col" class="px-6 py-3">
                        <div class="flex items-center">
                            Product name
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                        </div>
                    </th>
                    <th scope="col" class="px-6 py-3 ">
                        <div class="flex items-center">
                            category
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                    
                        </div>
                    </th>
                    <th scope="col" class="px-6 py-3 ">
                        <div class="flex items-center">
                            Hero
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                    
                        </div>
                    </th>
                    
                    <th scope="col" class="px-6 py-3">
                        <div class="flex items-center">
                            Discription
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                    
                        </div>
                    </th>
                    <th scope="col" class="px-6 py-3">
                        <div class="flex items-center">
                            Size
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                    
                        </div>
                    </th>
                    <th scope="col" class="px-6 py-3">
                        <div class="flex items-center">
                            Price
                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg></a>
                    
                        </div>
                    </th>
                    <th scope="col" class="px-6 py-3">
                        <span class="sr-only">Edit and Delete</span>
                    </th>
                </tr>
            </thead>
            <tbody >
                <tr class="bg-white border-b  hover:bg-gray-50 ">
                    <!-- <td class="px-4 py-4 w-5" >
                        <div class="flex items-center">
                            <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="checkbox-all-search" class="sr-only">checkbox</label>
                        </div>
                    </td> -->
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 gap-5 whitespace-nowrap ">
                        Apple MacBook Pro 17"
                    </th>
                    <td class="px-6 py-4">
                        Sheld
                    </td>
                    <td class="px-6 py-4">
                        Aluosha
                    </td>
                    <td class="px-6 py-4 relative w-96 ">
                        <p class="text-ellipsis  w-96 overflow-hidden whitespace-nowrap hover:p-4 hover:z-50  hover:block hover:bg-white hover:border-2 hover:rounded-md hover:whitespace-normal hover:absolute hover:top-0 hover:text-clip hover:overflow-visible">
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vel tempore praesentium dolores a illum. Fugit unde odio exercitationem totam, autem quod pariatur deleniti cum sit veritatis voluptatem minima similique perspiciatis.
                        </p>
                    </td>
                    <td class="px-6 py-4">
                        Laptop
                    </td>
                    <td class="px-6 py-4">
                        $2999
                    </td>
                    <td class="px-6 py-4 flex justify-end gap-5 text-right">
                        <a href="#" class="font-medium text-blue-600  hover:underline">Edit</a>
                        <a href="#" class="font-medium text-red-600  hover:underline">Delete</a>
                    </td>
                </tr>
                <tr class="bg-white border-b  hover:bg-gray-50 ">
                    <!-- <td class="px-4 py-4 w-5" >
                        <div class="flex items-center">
                            <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="checkbox-all-search" class="sr-only">checkbox</label>
                        </div>
                    </td> -->
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 gap-5 whitespace-nowrap ">
                        Apple MacBook Pro 17"
                    </th>
                    <td class="px-6 py-4">
                        Sheld
                    </td>
                    <td class="px-6 py-4">
                        Aluosha
                    </td>
                    <td class="px-6 py-4 relative w-96 ">
                        <p class="text-ellipsis  w-96 overflow-hidden whitespace-nowrap hover:p-4 hover:z-50  hover:block hover:bg-white hover:border-2 hover:rounded-md hover:whitespace-normal hover:absolute hover:top-0 hover:text-clip hover:overflow-visible">
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vel tempore praesentium dolores a illum. Fugit unde odio exercitationem totam, autem quod pariatur deleniti cum sit veritatis voluptatem minima similique perspiciatis.
                        </p>
                    </td>
                    <td class="px-6 py-4">
                        Laptop
                    </td>
                    <td class="px-6 py-4">
                        $2999
                    </td>
                    <td class="px-6 py-4 flex justify-end gap-5 text-right">
                        <a href="#" class="font-medium text-blue-600  hover:underline">Edit</a>
                        <a href="#" class="font-medium text-red-600  hover:underline">Delete</a>
                    </td>
                </tr>
                <tr class="bg-white border-b  hover:bg-gray-50 ">
                    <!-- <td class="px-4 py-4 w-5" >
                        <div class="flex items-center">
                            <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="checkbox-all-search" class="sr-only">checkbox</label>
                        </div>
                    </td> -->
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 gap-5 whitespace-nowrap ">
                        Apple MacBook Pro 17"
                    </th>
                    <td class="px-6 py-4">
                        Sheld
                    </td>
                    <td class="px-6 py-4">
                        Aluosha
                    </td>
                    <td class="px-6 py-4 relative w-96 ">
                        <p class="text-ellipsis  w-96 overflow-hidden whitespace-nowrap hover:p-4 hover:z-50  hover:block hover:bg-white hover:border-2 hover:rounded-md hover:whitespace-normal hover:absolute hover:top-0 hover:text-clip hover:overflow-visible">
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vel tempore praesentium dolores a illum. Fugit unde odio exercitationem totam, autem quod pariatur deleniti cum sit veritatis voluptatem minima similique perspiciatis.
                        </p>
                    </td>
                    <td class="px-6 py-4">
                        Laptop
                    </td>
                    <td class="px-6 py-4">
                        $2999
                    </td>
                    <td class="px-6 py-4 flex justify-end gap-5 text-right">
                        <a href="#" class="font-medium text-blue-600  hover:underline">Edit</a>
                        <a href="#" class="font-medium text-red-600  hover:underline">Delete</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
export default {
    name: 'admin-analytics'
}
</script>
<style scoped></style>