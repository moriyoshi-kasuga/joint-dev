/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.{js,css}",
    "./app/**/*.py",
  ],
  theme: {
    colors: {
      primary: "#5c6ac4",
      secondary: "#ecc94b",
    },
    extend: {},
  },
  plugins: [],
};
