Here is a **brand‑kit** for Wright Wellness that distills the look and feel of the current site into reusable guidelines for your redesign.  The kit pulls directly from the existing content (with citations) and translates it into practical assets you can hand off to a designer or feed into a headless CMS.

### Brand identity & messaging

Wright Wellness positions itself as a warm, inclusive and empowering mental‑health practice.  The site greets visitors with a forest photograph and a huge “Welcome” heading, followed by reflective language that acknowledges stigma (“You are Weak. Shameful. Broken. Crazy.”) and then reframes help‑seeking as “STRENGTH, COURAGE, and ACCEPTANCE”.  A call to action invites users to “Take a step today towards a healthier you”.  This creates a tone of honesty, empathy and empowerment, which should be preserved.  The brand voice is:

* **Compassionate & non‑judgmental:** Recognizes clients’ struggles and normalizes seeking help.
* **Empowering:** Emphasizes inner strength, courage and acceptance.
* **Inviting & hopeful:** Encourages small steps toward wellness and growth.
* **Inclusive:** Offers content in English and Spanish; acknowledges diverse services and practitioners.

#### Tagline / mission

* *“Take a step today towards a healthier you”*.
* Mission: To create a safe space where asking for help is seen as strength and self‑compassion.

### Visual identity

#### Logo

* **Symbol:** Stylized tree/leaf motif.  The leaves are light‑green and the trunk is purple.
* **Usage:** Pairs with “Wright Wellness” wordmark in a simple sans‑serif; often appears on a white background.
* **Application:** Use the logo in the header and footer; allow for a horizontal version (wordmark plus icon) and a standalone icon for favicons or social avatars.

#### Color palette

| Role          | Hue (approx.) | Hex (approx.) | Notes                                                                           |
| ------------- | ------------- | ------------- | ------------------------------------------------------------------------------- |
| Primary       | Natural green | `#7FAE5A`     | matches leaf icon; conveys growth, nature & calm                                |
| Secondary     | Deep purple   | `#7D4698`     | comes from the trunk in the logo; used sparingly for accents, links and buttons |
| Accent        | Soft olive    | `#B7C98A`     | used in backgrounds or hover states to complement primary green                 |
| Neutral dark  | Charcoal      | `#333333`     | used for body text; ensures readability                                         |
| Neutral light | White         | `#FFFFFF`     | primary background color; keeps pages airy and clean                            |

*These codes are approximations based on visual sampling of the live site; adjust with a color picker during implementation for exact matches.*

#### Typography

| Use              | Font family                                                       | Characteristics / fallback                                           |
| ---------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| Headings         | Sans‑serif (e.g., **Montserrat**, **Poppins**, or Proxima Nova**) | Tall, rounded, friendly; used for page titles like “Welcome”.        |
| Body copy        | Humanist sans‑serif (e.g., **Lato** or **Open Sans**)             | Readable at small sizes; conveys warmth without being overly formal. |
| Accents / quotes | Optional serif (e.g., **Merriweather**)                           | Can be used for pull‑quotes or emphasis to evoke reflection.         |
| Fallbacks        | `sans-serif`, `serif`                                             | Ensure graceful degradation across devices.                          |

Notes: The existing site appears to use a geometric sans for headings and a lighter sans for body text; confirm using CSS inspector when implementing.

#### Imagery & graphics

* **Nature & growth:** Use photos of forests, leaves and sunlight (as seen on the home page) to evoke calm and renewal.
* **People‑centric:** Include images of diverse individuals engaging in counseling, yoga, or self‑care to convey community and inclusivity.
* **Minimalist icons:** Use simple line icons for navigation and services; ensure they match the line weight and colors of the brand palette.

#### Layout & UI

* **Clean whitespace:** The current site uses generous spacing and large headings, which give breathing room.  Preserve this airy feeling.
* **Simple navigation:** A top bar lists key sections (Home, Team, Services & Fees, Forms, Mind‑FULL Content, Contact, Join Our Team), with dropdown folders for subsections.  A mobile menu button toggles the nav.
* **Call‑to‑action buttons:** Use accent colors (green/purple) and friendly rounded corners; text like “Learn more” should stand out while staying on brand.

### Brand assets to prepare for Cursor

1. **Logo files:** Export the tree/leaf wordmark in SVG and PNG formats.  Provide horizontal, stacked and icon‑only versions.
2. **Color tokens:** Define the hex codes above in a design‑token system for reuse across CSS/JS (e.g., `--color-primary`, `--color-secondary`).
3. **Typography presets:** Include the chosen font families via Google Fonts or self‑hosted files; set heading sizes (e.g., H1 large, H2 medium) and body text sizes (16 px baseline).
4. **Content archetypes:** Provide markdown/MDX for pages, team bios and blog posts (as already scraped) so Cursor can generate pages easily.
5. **Imagery guidelines:** Curate a small library of royalty‑free nature photos and diverse lifestyle images; specify when to use each.
