# Wright Wellness Website

Official website for Wright Wellness PLLC - a mental health and wellness practice in Arlington, Texas.

## 📋 Project Overview

This repository contains two versions of the Wright Wellness website:

1. **Main Site** (Root directory) - Traditional rebuild matching the current live site
2. **Alternate Site** (`/alternate` folder) - Modern redesign with new landing page

Both sites are built with:
- **Astro** - Static site generator
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm

### Main Site

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:4322](http://localhost:4322) in your browser.

### Alternate Site

1. Navigate to the alternate directory:
```bash
cd alternate
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:4323](http://localhost:4323) in your browser.

## 📦 Build

### Main Site
```bash
npm run build
```

### Alternate Site
```bash
cd alternate
npm run build
```

Built files will be in the `dist/` directory for each project.

## 🚢 Deployment

Both sites are configured for deployment on Vercel. Simply connect your repository to Vercel and it will automatically build and deploy.

### Main Site
- Deploy from root directory
- Port: 4322 (development)

### Alternate Site
- Deploy from `/alternate` directory
- Port: 4323 (development)

## 📁 Project Structure

### Main Site (Root)
```
wright_wellness/
├── src/
│   ├── components/     # Reusable components (Header, Footer, Logo, Navigation)
│   ├── layouts/        # Page layouts
│   ├── pages/          # Site pages
│   └── styles/         # Global styles
├── public/             # Static assets (images, logos)
├── package.json
└── README.md
```

### Alternate Site
```
alternate/
├── src/
│   ├── components/     # Reusable components
│   ├── layouts/       # Page layouts
│   ├── pages/         # Site pages
│   └── styles/        # Global styles
├── public/            # Static assets
├── package.json
└── README.md
```

## 🎨 Brand Colors

- **Primary Green**: `#7FAE5A`
- **Primary Light**: `#B7C98A`
- **Secondary Purple**: `#7D4698`
- **Neutral Dark**: `#333333`
- **Neutral Light**: `#FFFFFF`

## 📝 Forms

Contact forms use Formspree. Update the form IDs in:
- `src/pages/contact.astro`
- `src/pages/join-our-team.astro`
- `alternate/src/pages/index.astro` (if contact form is added)

Replace `YOUR_FORM_ID` with your actual Formspree form ID.

## 🔗 Important Links

- **Client Portal**: https://wrightwellness.clientsecure.me/
- **Email**: office@wrightwellness.me
- **Phone**: 682-777-4325
- **Address**: 1398 W. Mayfield Rd., Suite 220, Arlington, TX 76015

## 📄 Version History

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

## 📚 Documentation

- [Brand Kit](./wright_wellness_brand_kit.md) - Design guidelines and brand identity
- [CHANGELOG.md](./CHANGELOG.md) - Version history and changes

## 🤝 Contributing

This is a private project for Wright Wellness PLLC. For changes or updates, please contact the development team.

## 📞 Support

For technical issues or questions about the website, please contact the development team.

## 📜 License

Copyright © 2025 Wright Wellness PLLC. All rights reserved.

---

**Current Version**: 1.3.0
