# Gerson Institute Europe: website concept

Static design mockups for review, made before any real build work starts.

- `index.html`: start page of the clickable mockup (open this first)
- `home.html`, `sessions.html`, `myths-juice.html`: the mockup pages, linked to each other
- `board.html`: one-page overview (home page, mobile inquiry form, editor, SEO, inquiry routing, hosting)
- `concept-board.jpg`, `homepage-full.jpg`, `page-sessions.png`, `page-article.png`: images to share
- `assets/`: shared stylesheet, local fonts (Barlow and Fraunces, SIL Open Font License), images from the current gerson.hu site

## Browse it offline

1. Download the branch (GitHub → Code → Download ZIP) or clone it.
2. Open `concept/index.html` in any browser (double-click it).
3. Click through the pages. Fonts and images are stored locally, so no internet is needed.

The mockup is built for a computer screen (1280 px wide). The finished site will also adapt to phones.

## Share an online preview (Cloudflare Pages)

1. In Cloudflare: Workers & Pages → Create → Pages → Connect to Git → choose this repository.
2. Branch: `claude/gerson-therapy-website-hz5bdu`. Framework preset: None. Build command: leave empty. Build output directory: `concept`.
3. Deploy. The preview gets a free address like `gerson-concept.pages.dev`.

`_headers`, `robots.txt` and a `noindex` tag on every page keep the preview out of Google.

## Proposed stack

| Part | Choice | Why |
|---|---|---|
| Site | Astro (static) | Fast plain-HTML pages, built-in i18n routing, nothing to patch |
| Editing | Sveltia CMS (Decap-compatible), at `/admin` | Form-based editor, one tab per language, content stored as files in this repo |
| Hosting | Cloudflare Pages | Free tier, global CDN, automatic HTTPS, preview URL for every change |
| Inquiry form | Cloudflare Pages Function → email to info@gerson.hu (+ optional D1 storage, EU jurisdiction) | Europe, Asia and Africa go to info@gerson.hu; the Americas are referred to the Health Institute de Tijuana, Mexico |

## Guiding principles (shown on the home page)

1. Complementary, not alternative.
2. Evidence-informed, not promise-driven.
3. Personalised, not one-size-fits-all.
4. In cooperation with conventional medical care.
5. Focused on the whole person and lifestyle.
6. Safety and transparency first.

## Design references

- Method: Dr. Max Gerson's original method (primary sources: *A Cancer Therapy: Results of Fifty Cases*, 1958; *Meine Diät*, 4th ed. 1930; his articles and lectures)
- Look and feel: the current gerson.hu (cream and sand, leaf green, lotus mark, Barlow typeface)
- Structure of the Sessions block ("what's included" plus admission details): borrowed from the
  [Health Institute de Tijuana](https://gerson.org/health-institute-de-tijuana/) page, not its look

## To confirm before building

- Placeholders: phone number, address, session dates, the "what's included" list, the day-by-day week, length, languages and pricing
- Article wording, especially the "What the research says" section
- A higher-resolution logo file (the current one is 109×109 px)
- Accreditation wording, agreed with the Gerson Institute
- Which languages go live first (EN / HU / DE proposed)
- Recent photos of the centre, team and sessions
