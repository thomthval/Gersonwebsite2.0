# Gerson Institute Europe: website concept

Static design mockups for review, made before any real build work starts.

- `index.html`: start page of the clickable mockup (open this first)
- `home.html`, `sessions.html`, `myths-juice.html`: the English pages, linked to each other
- `hu/`, `de/`, `fr/`: the same pages in Hungarian, German and French (generated, see below)
- `board.html`: one-page overview (home page, mobile inquiry form, editor, SEO, inquiry routing, hosting)
- `DESIGN-NOTES.md`: why each section looks the way it does, what was left out, and the open questions
- `concept-board.jpg`, `homepage-full.jpg`, `homepage-full-hu.jpg`, `page-sessions.png`, `page-article.png`: images to share
- `scroll-demo-hu.mp4`: 40-second screen recording of the Hungarian home page, showing the motion
- `assets/`: shared styles, the motion layer (`motion.css`, `motion.js`), local fonts (Barlow and Fraunces, SIL Open Font License)
- `assets/photos/`: photos from the current gerson.hu media library, resized

## Browse it offline

1. Download the branch (GitHub → Code → Download ZIP) or clone it.
2. Open `concept/index.html` in any browser (double-click it).
3. Click through the pages and switch languages with EN · HU · DE · FR in the menu. Fonts and images are stored locally, so no internet is needed.

Scroll slowly to see the motion. Add `?static` to a page address to switch all animation off (used for the screenshots).

The mockup is built for a computer screen (1280 px wide). The finished site will also adapt to phones.

## Share an online preview (Cloudflare Pages)

1. In Cloudflare: Workers & Pages → Create → Pages → Connect to Git → choose this repository.
2. Branch: `claude/gerson-therapy-website-hz5bdu`. Framework preset: None. Build command: leave empty. Build output directory: `concept`.
3. Deploy. The preview gets a free address like `gerson-concept.pages.dev`.

`_headers`, `robots.txt` and a `noindex` tag on every page keep the preview out of Google.

## Translations

English is the source. `i18n/translations.txt` holds the Hungarian, German and French text, one block per sentence.

    python3 tools/i18n.py check   # sentences that still need a translation
    python3 tools/i18n.py build   # regenerate hu/, de/ and fr/

After changing an English sentence, run `check`, add the new translation, then run `build`. The script needs `beautifulsoup4`.

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

See the "Open questions" list in `DESIGN-NOTES.md`.
