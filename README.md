# Wright Wellness Website

A modern, responsive website for Wright Wellness PLLC, built with [Astro](https://astro.build), [Tailwind CSS](https://tailwindcss.com), and TypeScript.

## 🌐 Live Site

Visit [wrightwellness.me](https://wrightwellness.me)

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm (or yarn/pnpm)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/fdtorres1/wright-wellness.git
cd wright-wellness
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:4322](http://localhost:4322) in your browser.

## 📦 Build

To build the site for production:

```bash
npm run build
```

The built files will be in the `dist/` directory.

To preview the production build locally:

```bash
npm run preview
```

## 🚢 Deployment

This site is configured for deployment on [Vercel](https://vercel.com). Simply connect your GitHub repository to Vercel and it will automatically build and deploy.

### Manual Deployment

1. Build the project: `npm run build`
2. Deploy the `dist/` directory to your hosting provider

## 📁 Project Structure

```
/
├── public/
│   ├── favicon.svg
│   └── logo.jpg
├── src/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Navigation.astro
│   │   ├── Footer.astro
│   │   └── Logo.astro
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
├── tsconfig.json
└── package.json
```

## 🎨 Brand Colors

- **Primary Green**: `#7FAE5A`
- **Secondary Purple**: `#7D4698`
- **Accent Olive**: `#B7C98A`
- **Neutral Dark**: `#333333`
- **Neutral Light**: `#FFFFFF`

## 🔤 Typography

- **Headings**: Poppins (geometric sans-serif)
- **Body**: Inter (clean, readable sans-serif)
- **System Font Fallbacks**: Included for optimal performance

## 📝 Configuration

### Form Setup

The contact form and job application form use [Formspree](https://formspree.io). To configure:

1. Sign up for a free account at [Formspree.io](https://formspree.io)
2. Create forms and get your form IDs
3. Replace `YOUR_FORM_ID` in:
   - `src/pages/contact.astro`
   - `src/pages/join-our-team.astro`

### Environment Variables

No environment variables are currently required. All configuration is done through the codebase.

## 🛠️ Development

### Available Scripts

- `npm run dev` - Start development server on port 4322
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run astro` - Run Astro CLI commands

### Code Style

- TypeScript strict mode enabled
- Tailwind CSS for styling
- Astro components for templating

## 📄 License

Copyright © 2025 Wright Wellness PLLC. All rights reserved.

## 🤝 Contributing

This is a private project for Wright Wellness PLLC. For questions or issues, please contact the development team.

## 📞 Support

For website issues or questions:
- Email: office@wrightwellness.me
- Phone: 682-777-4325

---

Built with ❤️ using [Astro](https://astro.build)
