"""Невеликий генератор статичних сайтів для локального бізнесу.

Кожен сайт описується Python-модулем у src/: конфіг бізнесу, сторінки, CSS і JS.
Генератор збирає HTML з однаковим каркасом: мета-теги, canonical, OG, JSON-LD,
шапка з мобільним меню, хлібні крихти, футер з NAP, sticky-кнопка дзвінка, sitemap.xml.
Усі внутрішні посилання відносні, тому сайт працює і локально, і на GitHub Pages.
"""
import json
import os
import re
from datetime import date
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_BASE = "https://dmytro1448.github.io/local-business-sites/"
DAYS = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday",
        "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def hours_spec(hours):
    """hours: list of (["Mo","Tu"], "08:00", "19:00")"""
    return [{"@type": "OpeningHoursSpecification",
             "dayOfWeek": [DAYS[d] for d in days], "opens": o, "closes": c}
            for days, o, c in hours]


def business_ld(cfg):
    b = cfg["business"]
    base = cfg["base"]
    data = {
        "@context": "https://schema.org",
        "@type": b["type"],
        "@id": base + "#business",
        "name": b["name"],
        "description": b["description"],
        "url": base,
        "telephone": b["phone"],
        "email": b.get("email"),
        "priceRange": b.get("priceRange"),
        "image": base + "og.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": b["street"],
            "addressLocality": b["city"],
            "addressRegion": b["region"],
            "postalCode": b.get("postal"),
            "addressCountry": "UA",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": b["geo"][0], "longitude": b["geo"][1]},
        "openingHoursSpecification": hours_spec(b["hours"]),
        "areaServed": [{"@type": "City", "name": b["city"]}] +
                      [{"@type": "Place", "name": a} for a in b.get("areas", [])],
    }
    if b.get("extra"):
        data.update(b["extra"])
    return {k: v for k, v in data.items() if v is not None}


def breadcrumbs_ld(cfg, crumbs):
    items = []
    for i, (name, path) in enumerate(crumbs, 1):
        items.append({"@type": "ListItem", "position": i, "name": name, "item": cfg["base"] + path})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                           for q, a in faqs]}


def service_ld(cfg, name, description, area=None, price=None):
    b = cfg["business"]
    d = {"@context": "https://schema.org", "@type": "Service", "name": name,
         "description": description, "provider": {"@id": cfg["base"] + "#business"},
         "areaServed": {"@type": "Place", "name": area} if area else {"@type": "City", "name": b["city"]}}
    if price:
        d["offers"] = {"@type": "Offer", "priceCurrency": "UAH", "price": str(price),
                       "description": "Ціна від"}
    return d


def faq_html(faqs, heading="Часті запитання"):
    items = "\n".join(
        f'<details class="faq__item"><summary>{escape(q)}</summary><div class="faq__a"><p>{a}</p></div></details>'
        for q, a in faqs)
    return f'<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">{heading}</h2>{items}</section>'


def rel_prefix(path):
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    return "../" * depth if depth else "./"


def render_page(cfg, page, layout):
    path = page["path"]
    root = rel_prefix(path)
    base = cfg["base"]
    url = base + path
    lds = [business_ld(cfg)]
    crumbs = page.get("crumbs")
    if crumbs:
        lds.append(breadcrumbs_ld(cfg, [("Головна", "")] + crumbs))
    if page.get("faq"):
        lds.append(faq_ld(page["faq"]))
    lds += page.get("ld", [])
    ld_html = "\n".join(
        '<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "</script>"
        for x in lds)

    crumbs_html = ""
    if crumbs:
        parts = [f'<li><a href="{root}">Головна</a></li>']
        for i, (name, p) in enumerate(crumbs):
            if i == len(crumbs) - 1:
                parts.append(f'<li><span aria-current="page">{escape(name)}</span></li>')
            else:
                parts.append(f'<li><a href="{root}{p}">{escape(name)}</a></li>')
        crumbs_html = f'<nav class="crumbs" aria-label="Хлібні крихти"><ol>{"".join(parts)}</ol></nav>'

    body = page["body"]
    if page.get("faq") and not page.get("faq_inline"):
        body += '<div class="wrap">' + faq_html(page["faq"]) + "</div>"

    html = layout(cfg=cfg, page=page, root=root, crumbs_html=crumbs_html, body=body)
    head = f"""<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(page['title'])}</title>
<meta name="description" content="{escape(page['description'])}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="uk_UA">
<meta property="og:site_name" content="{escape(cfg['business']['name'])}">
<meta property="og:title" content="{escape(page['title'])}">
<meta property="og:description" content="{escape(page['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{cfg['theme_color']}">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
{{preload}}
<style>{{inline_css}}</style>
{ld_html}
</head>
"""
    out = head.replace("{inline_css}", cfg["_css"]).replace("{preload}", cfg["_preload"]) + html
    return out.replace("{{root}}", root)


def build(cfg, pages, layout, css, js, favicon):
    out_dir = os.path.join(ROOT, cfg["slug"])
    common_css = read(os.path.join(ROOT, "tools", "common.css"))
    common_js = read(os.path.join(ROOT, "tools", "common.js"))
    font_css, preload = self_host_fonts(cfg, out_dir)
    full_css = minify_css(font_css + "\n" + common_css + "\n" + css)
    write(os.path.join(out_dir, "assets", "style.css"), full_css.replace("{{root}}assets/", "../"))
    cfg["_css"] = full_css
    cfg["_preload"] = preload
    write(os.path.join(out_dir, "assets", "app.js"), common_js + "\n" + js)
    write(os.path.join(out_dir, "assets", "favicon.svg"), favicon)
    seen = set()
    for p in pages:
        assert p["path"] not in seen, p["path"]
        seen.add(p["path"])
        assert 25 <= len(p["title"]) <= 70, (p["path"], len(p["title"]), p["title"])
        assert 70 <= len(p["description"]) <= 170, (p["path"], len(p["description"]))
        target = os.path.join(out_dir, p["path"], "index.html")
        write(target, render_page(cfg, p, layout))
    today = date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{cfg['base']}{p['path']}</loc><lastmod>{today}</lastmod></url>" for p in pages)
    write(os.path.join(out_dir, "sitemap.xml"),
          f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write(os.path.join(out_dir, "robots.txt"),
          f"# Демо-концепт: сайт закрито від індексації мета-тегом noindex\nUser-agent: *\nAllow: /\nSitemap: {cfg['base']}sitemap.xml\n")
    print(f"built {cfg['slug']}: {len(pages)} pages")


def footer_disclaimer(root):
    return (f'<p class="demo-note">Демо-концепт для портфоліо, бізнес вигаданий. '
            f'Телефон і контакти фіктивні. <a href="{root}../">Інші роботи</a></p>')


def phone_link(cfg, cls="", label=None):
    b = cfg["business"]
    return f'<a class="{cls}" href="tel:{b["phone"]}">{label or b["phone_display"]}</a>'


PHONE_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>')

DAY_UA = {"Mo": "Пн", "Tu": "Вт", "We": "Ср", "Th": "Чт", "Fr": "Пт", "Sa": "Сб", "Su": "Нд"}


def hours_text(hours):
    rows = []
    for days, o, c in hours:
        d = DAY_UA[days[0]] + ("–" + DAY_UA[days[-1]] if len(days) > 1 else "")
        t = "цілодобово" if (o, c) == ("00:00", "23:59") else f"{o}–{c}"
        rows.append(f"<li><span>{d}</span> <span>{t}</span></li>")
    return "<ul class=\"hours\">" + "".join(rows) + "</ul>"


def default_layout(cfg, page, root, crumbs_html, body):
    b = cfg["business"]
    path = page["path"]
    items = []
    for label, p in cfg["nav"]:
        cur = (p == path) or (p and path.startswith(p) and p.endswith("/"))
        items.append(f'<li><a href="{root}{p}"{" aria-current=\"page\"" if cur else ""}>{label}</a></li>')
    svc = "".join(f'<li><a href="{root}{p}">{escape(n)}</a></li>' for n, p in cfg["footer_services"])
    areas = "".join(f'<li><a href="{root}{p}">{escape(n)}</a></li>' for n, p in cfg["footer_areas"])
    alt_label, alt_path = cfg["callbar_alt"]
    crumbs_block = f'<div class="wrap crumbs-wrap">{crumbs_html}</div>' if crumbs_html else ""
    return f"""<body class="{cfg['slug']} {page.get('body_class','')}">
<a class="skip" href="#main">Перейти до змісту</a>
<header class="hdr">
  <div class="wrap hdr__in">
    <a class="logo" href="{root}">{cfg['logo_svg']}<span>{cfg['logo_text']}</span></a>
    <nav class="nav" id="site-nav" aria-label="Головне меню"><ul>{''.join(items)}</ul></nav>
    <a class="hdr__phone" href="tel:{b['phone']}">{PHONE_SVG}<span>{b['phone_display']}</span></a>
    <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false"><span></span><b class="sr-only">Меню</b></button>
  </div>
</header>
<main id="main">
{crumbs_block}
{body}
</main>
<footer class="ftr">
  <div class="wrap ftr__grid">
    <div class="ftr__brand">
      <p class="ftr__name">{escape(b['name'])}</p>
      <p>{escape(cfg['footer_blurb'])}</p>
      <address>{escape(b['street'])}, {escape(b['city'])}<br><a href="tel:{b['phone']}">{b['phone_display']}</a><br><a href="mailto:{b['email']}">{b['email']}</a></address>
    </div>
    <div><p class="ftr__h">Послуги</p><ul>{svc}</ul></div>
    <div><p class="ftr__h">Райони</p><ul>{areas}</ul></div>
    <div><p class="ftr__h">Графік</p>{hours_text(b['hours'])}</div>
  </div>
  <div class="wrap ftr__bottom">
    <p>© {date.today().year} {escape(b['name'])}</p>
    {footer_disclaimer(root)}
  </div>
</footer>
<div class="callbar">
  <a class="callbar__call" href="tel:{b['phone']}">{PHONE_SVG}{cfg.get('callbar_label','Подзвонити')}</a>
  <a class="callbar__alt" href="{root}{alt_path}">{alt_label}</a>
</div>
<script src="{root}assets/app.js?v={cfg['version']}" defer></script>
</body>
</html>
"""


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


def self_host_fonts(cfg, out_dir):
    """Завантажує woff2 (кирилиця + латиниця) з Google Fonts у assets/fonts і повертає @font-face.
    Так немає блокуючого запиту до сторонніх доменів, а головний шрифт можна підвантажити заздалегідь."""
    import urllib.request
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
    req = urllib.request.Request(cfg["fonts"], headers={"User-Agent": ua})
    css = urllib.request.urlopen(req).read().decode()
    out, seen, first = [], {}, None
    os.makedirs(os.path.join(out_dir, "assets", "fonts"), exist_ok=True)
    for subset, block in re.findall(r"/\* (\S+) \*/\s*(@font-face \{.*?\})", css, re.S):
        if subset not in ("cyrillic", "latin"):
            continue
        url = re.search(r"url\((\S+?)\)", block).group(1)
        fam = re.search(r"font-family: '([^']+)'", block).group(1)
        if url not in seen:
            name = re.sub(r"[^a-z0-9]+", "-", fam.lower()) + f"-{subset}-{len(seen)}.woff2"
            path = os.path.join(out_dir, "assets", "fonts", name)
            if not os.path.exists(path):
                urllib.request.urlretrieve(url, path)
            seen[url] = name
        name = seen[url]
        if subset == "cyrillic":
            first = (first or []) + ([name] if name not in (first or []) else [])
        out.append(block.replace(url, "{{root}}assets/fonts/" + name))
    preload = "".join(f'<link rel="preload" href="{{{{root}}}}assets/fonts/{n}" as="font" type="font/woff2" crossorigin>' for n in (first or []))
    return "\n".join(out), preload
