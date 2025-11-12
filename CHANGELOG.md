# Changelog

All notable changes to the Wright Wellness website project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.2] - 2025-01-XX

### Added
- **Footer Attribution**: Added "Designed by Elaren Studios" credit in footer
- **Crisis Hotline Link**: Made 988 crisis hotline number clickable with phone dialer link

### Changed
- **Footer Styling**: Attribution text matches copyright notice styling (same font size and color)

## [1.3.1] - 2025-01-XX

### Added
- **Dr. Dana Shafir Profile Enhancement**: Complete profile update with comprehensive information
  - Added 12 specialties (Depression, Anxiety, Women's Issues, Parenting, Premarital Counseling, Chronic Health Issues, Adjustment/Grief, Relationships, Health/Lifestyle Coaching, Body Image, Adolescents, Mind-Body Wellness)
  - Added insurance plans (Blue Cross Blue Shield, Cigna/Evernorth)
  - Added service fees (Diagnostic Evaluation $165, Individual Psychotherapy $135, Family Psychotherapy Initial $175, Family Psychotherapy Follow-up $145)
  - Added full detailed bio content
  - Added HEALTH COACHING special section with quotes from Andrew Weil and Terry Guillemets
  - Added service notes about health coaching and telehealth availability
  - Added headshot image (`/team/dana-shafir.jpg`)
- **Team Member Status Fields**: New optional fields for team member profiles
  - `notAcceptingClients`: Boolean flag to indicate when a clinician is not accepting new clients
  - `withWrightWellnessSince`: Year the clinician joined Wright Wellness
- **Instagram Social Link**: Added Instagram icon and link to footer
  - Links to `https://instagram.com/wrightwellnesstx`
  - Includes hover effect with brand purple color

### Changed
- **Team Page Styling**: Team member names now display in black (`var(--ink)`) for better visibility
- **Team Bio Pages**: Enhanced to display "not accepting new clients" notices
  - Red warning text in header section
  - Prominent sidebar notice card for better visibility
- **Team Bio Pages**: Added display for "with Wright Wellness since [year]" information
- **Special Sections Rendering**: Improved to preserve line breaks and quotes using `whitespace-pre-line`

## [1.3.0] - 2025-01-XX

### Added
- **Conditional Navigation**: Different navigation behavior for homepage vs. other pages
  - Homepage shows simple hash-link navigation (Services, Team, Forms, Mind‑FULL, Contact, Client Portal)
  - Other pages show full navigation with dropdown submenus (Services & Fees, Forms)
  - "Join Our Team" link appears on non-homepage pages
  - CTA button links to #contact on homepage, Client Portal on other pages

### Changed
- **Header Logo**: Increased logo size from 40px to 56px for better visibility
- **Navigation Structure**: Simplified homepage navigation while maintaining full site navigation on other pages
- **Header Component**: Enhanced to conditionally render appropriate navigation based on current page

## [1.2.0] - 2025-11-11

### Added
- **Service Fees on Team Bio Pages**: Added support for displaying individual clinician service fees
  - New `ServiceFee` interface for service/price pairs
  - Optional `fees`, `serviceDescription`, and `serviceNotes` fields in TeamMember interface
  - "Services & Fees" card in team bio page sidebar
  - Dr. Lacey Wright's fees added to her profile page
  - Support for service notes (e.g., Walk and Talk Therapy, Telehealth availability)
  - Clean table-like display of services and prices

### Changed
- **Team Bio Pages**: Enhanced sidebar with service fees information
  - Fees displayed in organized card format with clear pricing
  - Service descriptions and notes included for context

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

