# Changelog

All notable changes to the Wright Wellness website project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-11-11

### Added
- **Team Member Headshots**: Added support for team member headshot images
  - Dr. Lacey Wright's headshot image added to team profile
  - Image display on team listing page and individual bio pages
  - Fallback to initials when no image is available
- **Enhanced Team Bio Pages**: Redesigned team member bio pages with modern card-based layout
  - Two-column layout with sticky sidebar for specialties and insurance
  - Badge/tag style display for specialties and insurance plans
  - Card-based sections with gradient backgrounds for special content
  - Support for extended bio content, specialties, insurance plans, and special sections
- **Pronouns Support**: Added pronouns field to team member profiles
  - Display pronouns (e.g., "she/her") on team member bio pages
- **Team Data Structure**: Extended TeamMember interface with optional fields
  - `image`: Optional path to headshot image
  - `pronouns`: Optional pronouns field
  - `specialties`: Array of specialty areas
  - `insurancePlans`: Array of accepted insurance plans
  - `fullBio`: Extended detailed bio content
  - `specialSections`: Special content sections (e.g., "WOMEN'S ISSUES", "MIND AND BODY")
  - `foundedYear`: Year practice was founded (for founders)

### Changed
- **Team Bio Page Design**: Complete redesign of team member bio pages
  - Modern magazine-style layout with improved visual hierarchy
  - Sidebar with quick reference information
  - Enhanced visual elements including shadows, rings, and gradient backgrounds
  - Improved responsive design for mobile and desktop

### Fixed
- Image positioning and zoom adjustments for Dr. Lacey Wright's headshot

## [1.1.0] - 2025-01-XX

### Added
- **Alternate Site Version**: Created a new alternate site design in `/alternate` folder
  - Modern landing page design with ChatGPT-inspired structure
  - Independent Astro project running on port 4323
  - New landing page featuring:
    - Enhanced hero section with reframed stigma messaging
    - Service cards with chips and descriptions
    - Team preview section
    - Mind-FULL content preview
    - Forms and Client Portal section
    - Comprehensive footer with contact info and navigation
  - Uses actual logo image instead of placeholder
  - Footer includes "Wright Wellness PLLC" branding

### Changed
- **Main Site**: Updated to version 1.1.0
- **Alternate Site**: Updated to version 1.1.0
- Landing page footer now includes contact information and navigation links
- Header and hero CTAs now point to Client Portal

### Fixed
- Corrected organization facts (woman-led, not BIPOC-led)
- Removed incorrect "100% Free Programming" claim
- Replaced placeholder logos with actual logo image
- Updated footer to show "Wright Wellness PLLC"

## [1.0.1] - Previous

### Added
- Initial site rebuild with Astro, Tailwind CSS, and TypeScript
- Homepage with hero section and content
- Navigation structure matching live site
- Footer component
- Logo integration
- Formspree integration for contact forms
- GitHub repository setup with standard documentation

### Changed
- Updated version from 1.0.0 to 1.0.1

## [1.0.0] - Initial Release

### Added
- Initial project setup
- Base layout structure
- Header and navigation components
- Footer component
- Homepage
- Brand kit integration

