import { URL, fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue(
    // {
    //   template: {
    //     compilerOptions: {
    //       isCustomElement: (tag) => {
    //         return tag.startsWith('admin-')
    //       },
    //     },
    //   },
    // },
  )],
  resolve: {
    alias: [
      { find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url)) },
      { find: '@assets', replacement: fileURLToPath(new URL('./src/assets', import.meta.url)) },
      { find: '@controllers', replacement: fileURLToPath(new URL('./src/controllers', import.meta.url)) },
      { find: '@components', replacement: fileURLToPath(new URL('./src/components', import.meta.url)) },
      // { find: '@cmp', replacement: fileURLToPath(new URL('./src/shared/cmp', import.meta.url)) },
      // { find: '@stores', replacement: fileURLToPath(new URL('./src/shared/stores', import.meta.url)) },
      // { find: '@use', replacement: fileURLToPath(new URL('./src/shared/use', import.meta.url)) },
    ],
  },
  build: {
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name].[ext]',
      },
    },
  },

})
