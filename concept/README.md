# Gerson Institute Europe: website concept

Static design mockups for review, made before any real build work starts.

- `concept-board.jpg`: one-page overview to share (home page, mobile inquiry form, editor, SEO, inquiry routing, hosting)
- `homepage-full.jpg`: the full home page, top to bottom
- `home.html` / `board.html`: the HTML source of the mockups (open in a browser)
- `assets/`: images taken from the current gerson.hu site

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

- Look and feel: the current gerson.hu (cream and sand, leaf green, lotus mark, Barlow typeface)
- Structure of the Sessions block ("what's included" plus admission details): borrowed from the
  [Health Institute de Tijuana](https://gerson.org/health-institute-de-tijuana/) page, not its look

## To confirm before building

- Placeholders: phone number, address, the "what a one-week session includes" list, length, languages and pricing
- A higher-resolution logo file (the current one is 109×109 px)
- Accreditation wording, agreed with the Gerson Institute
- Which languages go live first (EN / HU / DE proposed)
- Recent photos of the centre, team and sessions
