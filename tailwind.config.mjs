/** @type {import('tailwindcss').Config} */
export default {
  // 暗黑模式跟随系统 prefers-color-scheme
  darkMode: 'media',
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}'],
  theme: {
    extend: {
      colors: {
        brand: '#ff6900',
      },
    },
  },
  plugins: [],
};
