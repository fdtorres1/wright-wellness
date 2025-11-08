# Wright Wellness Website

A modern website for Wright Wellness PLLC, built with Astro, Tailwind CSS, and TypeScript.

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:4321](http://localhost:4321) in your browser.

## 📦 Build

To build the site for production:

```bash
npm run build
```

The built files will be in the `dist/` directory.

## 🚢 Deployment

This site is configured for deployment on Vercel. Simply connect your repository to Vercel and it will automatically build and deploy.

### Form Setup

The contact form and job application form use Formspree. You'll need to:

1. Sign up for a free account at [Formspree.io](https://formspree.io)
2. Create forms and get your form IDs
3. Replace `YOUR_FORM_ID` in:
   - `src/pages/contact.astro`
   - `src/pages/join-our-team.astro`

## 📁 Project Structure

```
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Navigation.astro
│   │   └── Footer.astro
│   ├── data/
│   │   └── team.ts
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── contact.astro
│   │   ├── join-our-team.astro
│   │   ├── team/
│   │   ├── services/
│   │   └── forms/
│   └── styles/
│       └── global.css
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

## 🎨 Brand Colors

- Primary Green: `#7FAE5A`
- Secondary Purple: `#7D4698`
- Accent Olive: `#B7C98A`
- Neutral Dark: `#333333`
- Neutral Light: `#FFFFFF`

## 📝 Notes

- Blog functionality is intentionally excluded for now
- Images are placeholders - replace with actual assets
- Form IDs need to be configured for Formspree integration

