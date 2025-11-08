/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#7FAE5A',
          light: '#B7C98A',
        },
        secondary: {
          DEFAULT: '#7D4698',
        },
        neutral: {
          dark: '#333333',
          light: '#FFFFFF',
        },
      },
      fontFamily: {
        heading: ['Poppins', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        body: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'sans-serif'],
        accent: ['Merriweather', 'serif'],
      },
    },
  },
  plugins: [],
}

