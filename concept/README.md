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
| Inquiry form | Cloudflare Pages Function → email (+ optional D1 storage, EU jurisdiction) | Routes Americas to the Gerson Institute (San Diego), everything else to the Europe inbox |

## To confirm before building

- Text marked as placeholder: phone number, address, reply-time promise, session details
- A higher-resolution logo file (the current one is 109×109 px)
- Accreditation wording, agreed with the Gerson Institute
- Which languages go live first (EN / HU / DE proposed)
- Recent photos of the centre, team and sessions
