/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        'primary-dark': '#5C340C',
        'primary-light-1': '#A47B5A',
        'primary-light-2': '#DEBA9A',
        'primary': '#84542A',
      },
    },
  },
  plugins: [],
}
