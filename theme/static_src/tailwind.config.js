const colors = require('tailwindcss/colors');

module.exports = {
  content: [
    './templates/**/*.html',
    './**/*.html',
    './**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        gray: colors.gray,
        neutral: colors.neutral,
      },
    },
  },
  plugins: [],
};
