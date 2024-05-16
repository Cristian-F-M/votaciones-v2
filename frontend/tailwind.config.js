/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    screens: {
      'm-2xl': {'max': '1535px'},
      'm-xl': {'max': '1279px'},
      'm-lg': {'max': '1023px'},
      'm-md': {'max': '767px'},
      'm-sm': {'max': '639px'},
      ...defaultTheme.screens,
    }
  },
  plugins: [],
}

