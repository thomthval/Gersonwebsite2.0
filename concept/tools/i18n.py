#!/usr/bin/env python3
"""Builds the Hungarian, German and French versions of the mockup from the English pages.

  python3 tools/i18n.py extract   # list every text unit with its id (for translating)
  python3 tools/i18n.py check     # list units that are missing a translation
  python3 tools/i18n.py build     # write hu/, de/ and fr/ next to the English pages

Translations live in i18n/translations.txt:

  [id]
  hu: Magyar szöveg
  de: Deutscher Text
  fr: Texte français

An id is a short hash of the English text, so editing an English sentence
means adding its new translation. "same" keeps the English text.
"""
import hashlib, os, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['index.html', 'home.html', 'sessions.html', 'myths-juice.html']
LANGS = ['hu', 'de', 'fr']
INLINE = {'a', 'b', 'i', 'em', 'strong', 'sup', 'sub', 'br', 'span', 'small', 'u', 's', 'abbr', 'mark'}
SKIP = {'script', 'style', 'svg', 'noscript'}
LETTER = re.compile(r'[^\W\d_]')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def uid(text):
    return hashlib.sha1(norm(text).encode()).hexdigest()[:7]


def has_letters(s):
    return bool(LETTER.search(s))


def inline_only(tag):
    return all(d.name in INLINE for d in tag.descendants if isinstance(d, Tag))


def direct_text(tag):
    return any(isinstance(c, NavigableString) and not isinstance(c, Comment) and c.strip() for c in tag.children)


def units(soup):
    """Yields (kind, node, english) for every translatable piece of a page."""
    if soup.title and soup.title.string:
        yield 'title', soup.title, norm(soup.title.string)
    for m in soup.find_all('meta', attrs={'name': 'description'}):
        yield 'attr:content', m, norm(m['content'])
    for img in soup.find_all('img'):
        if img.get('alt', '').strip():
            yield 'attr:alt', img, norm(img['alt'])

    def visit(node):
        if node.name in SKIP or 'sw' in (node.get('class') or []):
            return
        if direct_text(node) and inline_only(node):
            html = norm(node.decode_contents())
            if has_letters(node.get_text()):
                yield 'html', node, html
            return
        for c in list(node.children):
            if isinstance(c, Tag):
                yield from visit(c)
            elif isinstance(c, NavigableString) and not isinstance(c, Comment) and c.strip() and has_letters(c):
                yield 'text', c, norm(c)
    yield from visit(soup.body)


def load_translations():
    path = os.path.join(ROOT, 'i18n', 'translations.txt')
    tr, cur = {}, None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'^\[([0-9a-f]{7})\]', line)
        if m:
            cur = tr.setdefault(m.group(1), {})
        elif cur is not None and re.match(r'^(hu|de|fr): ', line):
            cur[line[:2]] = line[4:].strip()
        elif cur is not None and line.strip() == 'same':
            for l in LANGS:
                cur[l] = None
    return tr


def parse(page):
    return BeautifulSoup(open(os.path.join(ROOT, page), encoding='utf-8').read(), 'html.parser')


def relink(soup, lang):
    """Pages sit one folder deeper; shared files and untranslated pages need ../"""
    def fix(url):
        if not url or url.startswith(('#', 'http:', 'https:', 'mailto:', 'tel:', 'data:', '../')):
            return url
        return url if url.split('#')[0] in PAGES else '../' + url
    for t in soup.find_all(True):
        for a in ('href', 'src'):
            if t.has_attr(a):
                t[a] = fix(t[a])
        if t.has_attr('style') and 'url(' in t['style']:
            t['style'] = re.sub(r'url\((?!["\']?(?:https?:|data:|\.\./))', 'url(../', t['style'])


def switcher(soup, page, lang):
    order = ['en'] + LANGS
    for sw in soup.select('.sw'):
        for a, target in zip(sw.find_all('a'), order):
            if target == lang:
                href = page
            elif lang == 'en':
                href = f'{target}/{page}'
            elif target == 'en':
                href = f'../{page}'
            else:
                href = f'../{target}/{page}'
            a['href'] = href
            a['class'] = ['on'] if target == lang else []
            if not a['class']:
                del a['class']


def build():
    tr = load_translations()
    missing = 0
    for lang in LANGS:
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        for page in PAGES:
            soup = parse(page)
            soup.html['lang'] = lang
            for kind, node, en in list(units(soup)):
                t = tr.get(uid(en), {})
                if lang not in t:
                    missing += 1
                    print(f'missing {lang} [{uid(en)}] {en[:70]}', file=sys.stderr)
                    continue
                if t[lang] is None:
                    continue
                if kind == 'title':
                    node.string = t[lang]
                elif kind.startswith('attr:'):
                    node[kind[5:]] = t[lang]
                elif kind == 'text':
                    lead = ' ' if node[:1].isspace() else ''
                    tail = ' ' if node[-1:].isspace() else ''
                    node.replace_with(NavigableString(lead + t[lang] + tail))
                else:
                    node.clear()
                    for c in list(BeautifulSoup(t[lang], 'html.parser').contents):
                        node.append(c)
            relink(soup, lang)
            switcher(soup, page, lang)
            with open(os.path.join(ROOT, lang, page), 'w', encoding='utf-8') as f:
                f.write(str(soup))
    print('built', ', '.join(LANGS), '·', missing, 'missing translations')


def extract(only_missing=False):
    tr = load_translations() if os.path.exists(os.path.join(ROOT, 'i18n', 'translations.txt')) else {}
    seen = set()
    for page in PAGES:
        for kind, node, en in units(parse(page)):
            i = uid(en)
            if i in seen:
                continue
            seen.add(i)
            if only_missing and all(l in tr.get(i, {}) for l in LANGS):
                continue
            print(f'[{i}] {page.split(".")[0]}: {en}')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'build'
    {'extract': extract, 'check': lambda: extract(True), 'build': build}[cmd]()
