"""Сантехнік «Кран і Ключ», Кам'янець-Подільський (вигаданий бізнес, демо для портфоліо)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from sitekit import build, default_layout, service_ld, faq_html, PHONE_SVG, read

SLUG = "plumber-kamianets"
cfg = {
    "slug": SLUG,
    "base": f"https://dmytro1448.github.io/local-business-sites/{SLUG}/",
    "version": "3",
    "theme_color": "#0b1f3a",
    "fonts": "https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700;800&display=swap",
    "business": {
        "type": "Plumber",
        "name": "Кран і Ключ",
        "description": "Аварійний сантехнік у Кам'янці-Подільському цілодобово: протікання, засори, заміна змішувачів, бойлерів і труб.",
        "phone": "+380000000000",
        "phone_display": "+380 00 000 00 00",
        "email": "vyklyk@example.com",
        "street": "просп. Грушевського",
        "city": "Кам'янець-Подільський",
        "region": "Хмельницька область",
        "geo": (48.67885, 26.58521),
        "priceRange": "₴",
        "hours": [(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], "00:00", "23:59")],
        "areas": ["Старе місто", "Новий план", "Польські фільварки", "Руські фільварки", "Підзамче", "Колибаївка", "Смотрич"],
    },
    "nav": [("Аварійний виклик", "posluhy/avariinyi-vyklyk/"), ("Ціни", "tsiny/"), ("Райони", "#rayony"), ("Контакти", "kontakty/")],
    "footer_services": [("Аварійний виклик", "posluhy/avariinyi-vyklyk/"), ("Прочистка каналізації", "posluhy/prochystka-kanalizatsii/"), ("Встановлення бойлера", "posluhy/ustanovka-boilera/"), ("Ціни", "tsiny/")],
    "footer_areas": [("Старе місто", "rayony/stare-misto/"), ("Новий план", "rayony/novyi-plan/")],
    "footer_blurb": "Двоє майстрів-сантехніків і черговий диспетчер. Виїжджаємо по Кам'янцю-Подільському та найближчих селах цілодобово.",
    "callbar_label": "Викликати майстра",
    "callbar_alt": ("Ціни", "tsiny/"),
    "logo_text": "Кран і Ключ<small>сантехнік 24/7</small>",
    "logo_svg": '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#c42d16"/><path d="M12 13h10a6 6 0 0 1 6 6v2h-5v-2a1 1 0 0 0-1-1H12z" fill="#fff"/><path d="M25.5 25c0 2-1.2 3.5-2.5 3.5S20.5 27 20.5 25s2.5-4.5 2.5-4.5 2.5 2.5 2.5 4.5z" fill="#ffd23f"/></svg>',
}
layout = default_layout

ETA = [("stare", "Старе місто", 20, 30), ("polski", "Польські фільварки", 15, 25), ("ruski", "Руські фільварки", 20, 30),
       ("novyi", "Новий план", 10, 20), ("pidzamche", "Підзамче", 20, 35), ("dovzhok", "Довжок і промзона", 25, 35),
       ("kolybaivka", "Колибаївка", 25, 40), ("smotrych", "Смотрич", 35, 50)]

PRICES = [
    ("Аварійні", [("Виїзд майстра по місту", "200"), ("Виїзд вночі (21:00-08:00)", "400"), ("Усунення протікання на з'єднанні", "від 300"), ("Заміна аварійного крана", "від 450"), ("Перекриття стояка з ЖЕК/ОСББ", "від 200")]),
    ("Каналізація", [("Прочистка засору мийки", "від 400"), ("Прочистка засору унітазу", "від 500"), ("Прочистка стояка тросом", "від 900"), ("Прочистка зовнішньої каналізації", "від 1 500")]),
    ("Змішувачі і сантехніка", [("Заміна змішувача", "від 400"), ("Встановлення унітазу", "від 900"), ("Встановлення інсталяції", "від 2 200"), ("Встановлення ванни або піддону", "від 1 200"), ("Заміна сифона", "від 250")]),
    ("Бойлери і труби", [("Встановлення бойлера до 100 л", "від 1 100"), ("Чистка бойлера від накипу", "від 700"), ("Заміна ТЕНа", "від 600"), ("Заміна труби, 1 м", "від 350"), ("Встановлення лічильника води", "від 500"), ("Встановлення фільтра", "від 450")]),
]


def eta_tool():
    opts = "".join(f'<option value="{k}" data-min="{a}" data-max="{b}">{n}</option>' for k, n, a, b in ETA)
    return f"""
<div class="eta" aria-labelledby="eta-h">
  <p class="eta__live"><span class="dot" aria-hidden="true"></span> <span id="eta-status">Чергові майстри на зв'язку</span></p>
  <h2 id="eta-h" class="eta__h">Коли приїде майстер?</h2>
  <label class="eta__lbl" for="eta-area">Ваш район</label>
  <select id="eta-area">{opts}</select>
  <p class="eta__out" aria-live="polite">Орієнтовно <b id="eta-time">20-30 хв</b> <span id="eta-note">після дзвінка</span></p>
  <a class="btn btn--red btn--block btn--big" href="tel:{cfg['business']['phone']}">{PHONE_SVG}Викликати зараз</a>
  <p class="eta__fine" id="eta-fine">Виїзд по місту 200 ₴. Діагностика безкоштовна, якщо ремонт робимо ми.</p>
</div>"""


def price_tables(filterable=False):
    out = []
    for cat, rows in PRICES:
        r = "".join(f'<tr><td>{n}</td><td>{p} ₴</td></tr>' for n, p in rows)
        out.append(f'<div class="pcat"><h3>{cat}</h3><table class="ptable"><tbody>{r}</tbody></table></div>')
    search = ""
    if filterable:
        search = '<div class="psearch"><label for="psearch">Знайти послугу</label><input id="psearch" type="search" placeholder="Наприклад: бойлер, унітаз, засор" autocomplete="off"><p id="psearch-empty" class="muted" hidden>Нічого не знайшли. Подзвоніть, і ми назвемо ціну за хвилину.</p></div>'
    return search + '<div class="pgrid">' + "".join(out) + "</div>"


def wait_steps():
    return """<ol class="wait">
<li><b>Перекрийте воду.</b> Кран на вводі в квартиру зазвичай біля лічильника. Якщо він не тримає, перекрийте стояк або подзвоніть нам, підкажемо.</li>
<li><b>Вимкніть електрику</b> в зоні, куди тече вода, і бойлер, якщо протікає він.</li>
<li><b>Попередьте сусідів знизу</b> і зробіть фото: це знадобиться для ОСББ чи страхової.</li>
<li><b>Зберіть воду</b> ганчірками й тазом, відсуньте техніку і меблі.</li></ol>"""


def booking_form(title="Залишити заявку"):
    return f"""
<form class="form card" data-demo id="zayavka" aria-labelledby="zayavka-h">
  <h2 id="zayavka-h">{title}</h2>
  <div class="form-body">
    <p class="muted">Не аварія? Залиште заявку на планову роботу, і диспетчер передзвонить протягом 20 хвилин. Якщо тече вода, краще одразу дзвоніть.</p>
    <div class="row2">
      <div class="field"><label for="f-name">Ім'я</label><input id="f-name" name="name" autocomplete="given-name" required><span class="err">Вкажіть ім'я</span></div>
      <div class="field"><label for="f-tel">Телефон</label><input id="f-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+380" required><span class="err">Перевірте номер телефону</span></div>
    </div>
    <div class="field"><label for="f-job">Що сталося</label><select id="f-job" name="job"><option>Протікання</option><option>Засор</option><option>Заміна змішувача або сантехніки</option><option>Бойлер</option><option>Інше</option></select></div>
    <div class="field"><label for="f-msg">Адреса і деталі</label><textarea id="f-msg" name="msg" placeholder="Вулиця, поверх, що саме потрібно"></textarea></div>
    <label class="check"><input type="checkbox" name="agree" required> <span>Погоджуюсь на обробку даних для зворотного дзвінка</span></label>
    <button class="btn btn--red" type="submit">Надіслати заявку</button>
  </div>
  <p class="form-ok" role="status">Дякуємо, {{name}}! Заявку прийнято. Це демо-сайт, тому вона нікуди не надсилається. На робочому сайті диспетчер отримає її в Telegram з адресою і типом робіт.</p>
</form>"""


FAQ = [
    ("Скільки коштує виклик сантехніка?", "Виїзд по місту 200 гривень, вночі з 21:00 до 08:00 400 гривень. Якщо ремонт робимо ми, діагностика безкоштовна, а вартість роботи називаємо до її початку."),
    ("Ви справді приїжджаєте вночі?", "Так, один майстер чергує щоночі. Вночі робимо тільки те, що зупиняє аварію: перекриваємо, ставимо хомут чи кран. Повний ремонт переносимо на ранок, щоб не переплачувати за нічний тариф."),
    ("Чи є у вас запчастини з собою?", "В авто завжди є крани, хомути, гнучкі шланги, сифони, фітинги і троси для прочистки. Змішувач чи бойлер можна купити заздалегідь або доручити це нам."),
    ("Чи даєте гарантію?", "На роботу 12 місяців, на запчастини гарантія виробника. Видаємо чек і гарантійний талон."),
    ("Працюєте за межами міста?", "Так: Колибаївка, Смотрич, Жовтневе, Мукша та інші села поруч. Виїзд за місто від 300 гривень залежно від відстані."),
]


def home():
    body = f"""
<div class="alert"><div class="wrap alert__in"><b>Тече вода?</b> Перекрийте кран біля лічильника і дзвоніть: <a href="tel:{cfg['business']['phone']}">{cfg['business']['phone_display']}</a></div></div>
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="tag">Кам'янець-Подільський · 24/7 · без вихідних</p>
      <h1>Аварійний сантехнік у Кам'янці-Подільському. Приїзд від 20 хвилин</h1>
      <p class="lead">Протікання, засор, зламаний змішувач чи бойлер. Майстер вже в дорозі, поки ви перекриваєте воду. Ціну називаємо до початку роботи.</p>
      <ul class="hero__pts"><li>Виїзд від 200 ₴</li><li>Гарантія 12 місяців</li><li>Чек і талон</li></ul>
    </div>
    {eta_tool()}
  </div>
</section>
<section class="section" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h">З чим допомагаємо</h2>
    <ul class="tiles">
      <li class="tile tile--hot"><h3><a href="{{{{root}}}}posluhy/avariinyi-vyklyk/">Аварійний виклик</a></h3><p>Тече труба, прорвало шланг, затоплюєте сусідів. Цілодобово.</p><span>від 200 ₴</span></li>
      <li class="tile"><h3><a href="{{{{root}}}}posluhy/prochystka-kanalizatsii/">Прочистка каналізації</a></h3><p>Мийка, ванна, унітаз, стояк. Механічно, без «хімії».</p><span>від 400 ₴</span></li>
      <li class="tile"><h3><a href="{{{{root}}}}posluhy/ustanovka-boilera/">Бойлери</a></h3><p>Встановлення, чистка від накипу, заміна ТЕНа.</p><span>від 700 ₴</span></li>
      <li class="tile"><h3><a href="{{{{root}}}}tsiny/">Змішувачі і унітази</a></h3><p>Заміна, встановлення, інсталяції. Усі ціни в прайсі.</p><span>від 250 ₴</span></li>
    </ul>
  </div>
</section>
<section class="section section--navy" aria-labelledby="wait-h">
  <div class="wrap wait-grid">
    <div><h2 id="wait-h">Що робити, поки чекаєте майстра</h2><p class="muted-inv">Ці чотири кроки зменшують шкоду від протікання в рази. Якщо не знаєте, де кран, подзвоніть, диспетчер підкаже по телефону.</p></div>
    {wait_steps()}
  </div>
</section>
<section class="section" aria-labelledby="price-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="price-h">Ціни без сюрпризів</h2><a href="{{{{root}}}}tsiny/">Весь прайс →</a></div>
    {price_tables()}
  </div>
</section>
<section class="section section--grey" id="rayony" aria-labelledby="area-h">
  <div class="wrap">
    <h2 id="area-h">Їдемо по всьому місту і найближчих селах</h2>
    <ul class="chips">
      <li><a href="{{{{root}}}}rayony/stare-misto/">Старе місто</a></li>
      <li><a href="{{{{root}}}}rayony/novyi-plan/">Новий план</a></li>
      <li>Польські фільварки</li><li>Руські фільварки</li><li>Підзамче</li><li>Довжок</li><li>Колибаївка</li><li>Смотрич</li><li>Мукша</li>
    </ul>
  </div>
</section>
<div class="wrap">{faq_html(FAQ)}</div>
<section class="section section--grey"><div class="wrap book">{booking_form()}<div class="book__aside"><p class="big-phone-l">Аварійна лінія</p><a class="big-phone" href="tel:{cfg['business']['phone']}">{cfg['business']['phone_display']}</a><p class="muted">Цілодобово, без вихідних і свят. Відповідає диспетчер, а не автовідповідач.</p></div></div></section>"""
    return {"path": "", "title": "Сантехнік Кам'янець-Подільський 24/7: виклик за 30 хв | Кран і Ключ",
            "description": "Аварійний сантехнік у Кам'янці-Подільському цілодобово: протікання, засори, змішувачі, бойлери. Виїзд від 200 грн, приїзд за 20-40 хвилин, гарантія.",
            "body": body, "faq": FAQ, "faq_inline": True}


def inner(path, crumbs, title, desc, h1, lead, prose, aside=None, faq=None, ld=None):
    body = f"""
<section class="phero"><div class="wrap phero__in"><div><h1>{h1}</h1><p class="lead">{lead}</p></div>
<a class="btn btn--red btn--big" href="tel:{cfg['business']['phone']}">{PHONE_SVG}{cfg['business']['phone_display']}</a></div></section>
<div class="wrap cols"><article class="prose">{prose}</article><aside class="side">{aside or eta_tool()}</aside></div>"""
    return {"path": path, "title": title, "description": desc, "body": body, "crumbs": crumbs, "faq": faq, "ld": ld or []}


def pages():
    out = [home()]
    out.append(inner("posluhy/avariinyi-vyklyk/", [("Аварійний виклик", "posluhy/avariinyi-vyklyk/")],
        "Аварійний виклик сантехніка в Кам'янці-Подільському 24/7",
        "Цілодобовий аварійний виклик сантехніка в Кам'янці-Подільському: прорив труби, протікання, затоплення. Приїзд за 20-40 хвилин, виїзд від 200 грн.",
        "Аварійний виклик сантехніка цілодобово", "Прорвало трубу чи шланг, протікає бойлер, затоплюєте сусідів. Черговий майстер виїжджає одразу після дзвінка, вдень і вночі.",
        f"""<h2>Перші хвилини найважливіші</h2>{wait_steps()}
<h2>Що робить майстер на місці</h2><p>Спочатку зупиняє воду і знаходить причину. Потім пропонує два варіанти: тимчасово закрити проблему, щоб дочекатись ранку, або одразу відремонтувати повністю. Ви обираєте, знаючи ціну обох.</p>
<h2>Типові аварії в Кам'янці</h2><ul><li>старі чавунні крани на вводі, які не тримають воду;</li><li>розірвані гнучкі шланги під мийкою і до бойлера;</li><li>протікання на старих сталевих стояках у будинках Нового плану;</li><li>засмічення каналізації в будинках Старого міста з глиняними трубами.</li></ul>""",
        faq=[("Скільки коштує нічний виклик?", "400 гривень за виїзд з 21:00 до 08:00. Роботи за звичайним прайсом."),
             ("Що як я не вдома, а тече в мене?", "Зателефонуйте голові ОСББ або в аварійну службу міста, щоб перекрили стояк, і нам. Приїдемо, щойно хтось відчинить квартиру.")],
        ld=[service_ld(cfg, "Аварійний виклик сантехніка", "Цілодобовий виїзд сантехніка в Кам'янці-Подільському", price=200)]))
    out.append(inner("posluhy/prochystka-kanalizatsii/", [("Прочистка каналізації", "posluhy/prochystka-kanalizatsii/")],
        "Прочистка каналізації в Кам'янці-Подільському від 400 грн",
        "Прочистка засорів у Кам'янці-Подільському: мийка, ванна, унітаз, стояк, зовнішня каналізація приватного будинку. Механічно тросом, від 400 грн.",
        "Прочистка каналізації і засорів", "Вода стоїть у мийці чи ванні, з'явився запах або булькає унітаз. Прочищаємо механічно тросом і показуємо, що саме було в трубі.",
        """<h2>Як ми прочищаємо</h2><p>Для мийок і ванн використовуємо ручний трос, для стояків і зовнішніх ліній електричну машину з насадками. Хімію не застосовуємо: вона рідко допомагає при жировій пробці і псує старі труби.</p>
<h2>Приватні будинки</h2><p>У приватному секторі Польських і Руських фільварків часто засмічується вулична лінія до вигрібної ями або колектора. Прочищаємо до 30 метрів і підказуємо, чи варто міняти ділянку труби.</p>
<h2>Як не допустити повторного засору</h2><ul><li>поставте сітку на злив мийки;</li><li>не зливайте жир після смаження;</li><li>раз на місяць проливайте трубу гарячою водою.</li></ul>""",
        aside=price_tables_single("Каналізація"),
        faq=[("Чи дасте гарантію на прочистку?", "Якщо засор повернеться протягом 30 днів з тієї ж причини, приїдемо безкоштовно.")],
        ld=[service_ld(cfg, "Прочистка каналізації", "Механічна прочистка засорів у Кам'янці-Подільському", price=400)]))
    out.append(inner("posluhy/ustanovka-boilera/", [("Встановлення бойлера", "posluhy/ustanovka-boilera/")],
        "Встановлення і ремонт бойлера в Кам'янці-Подільському",
        "Встановлення, чистка і ремонт бойлерів у Кам'янці-Подільському: монтаж за 2-3 години, захисна група, чистка накипу, заміна ТЕНа. Від 700 грн.",
        "Встановлення і обслуговування бойлерів", "Встановимо новий бойлер за 2-3 години з захисною групою, або почистимо старий від накипу, щоб він знову грів швидко.",
        """<h2>Встановлення</h2><p>Перевіряємо, чи витримає стіна вагу бойлера з водою, ставимо надійні анкери, запобіжний клапан, кран зливу і гнучкі підводки. Після монтажу наповнюємо, перевіряємо на протікання і вмикаємо при вас.</p>
<h2>Чистка від накипу</h2><p>Вода в Кам'янці жорстка, тому бойлер варто чистити раз на рік-півтора. Ознаки: довше гріє, шумить, тече тонка вода з крана гарячої. Чистка займає близько години, заодно міняємо магнієвий анод.</p>""",
        aside=price_tables_single("Бойлери і труби"),
        faq=[("Чи можна встановити бойлер, куплений самостійно?", "Так. Порадимо, що докупити для монтажу: зазвичай це підводки, запобіжний клапан і кран."),
             ("Скільки служить ТЕН?", "При жорсткій воді й без чистки 3-5 років. З регулярною чисткою значно довше.")],
        ld=[service_ld(cfg, "Встановлення бойлера", "Монтаж і обслуговування бойлерів у Кам'янці-Подільському", price=700)]))
    out.append(prices_page())
    out.append(area("rayony/stare-misto/", "Старе місто",
        "Сантехнік у Старому місті Кам'янця-Подільського 24/7",
        "Сантехнік для Старого міста Кам'янця-Подільського: старі будинки, глиняні й чавунні труби, вузькі вулиці. Приїзд за 20-30 хвилин, цілодобово.",
        "Сантехнік у Старому місті", "Будинки Старого міста мають свої особливості: старі мережі, вузькі вулиці й обмеження для робіт у пам'ятках. Ми працюємо тут щотижня.",
        """<h2>Особливості старих будинків</h2><p>У багатьох будинках на острові Старого міста ще лишились чавунні стояки і глиняні каналізаційні труби. Вони крихкі, тому ми прочищаємо їх обережно, без потужних машин, і не міняємо ділянки без потреби.</p>
<h2>Як ми доїжджаємо</h2><p>Через Новопланівський міст до Старого міста 20-30 хвилин. У туристичний сезон, коли вулиці біля Ратуші й фортеці перекриті, паркуємось на найближчій дозволеній ділянці й доносимо інструмент.</p>
<h2>Ремонт у пам'ятках архітектури</h2><p>Якщо будинок має статус пам'ятки, не чіпаємо фасадні стіни і прокладаємо нові труби всередині приміщень. За потреби підкажемо, з ким погоджувати роботи.</p>"""))
    out.append(area("rayony/novyi-plan/", "Новий план",
        "Сантехнік на Новому плані в Кам'янці-Подільському 24/7",
        "Сантехнік на Новому плані в Кам'янці-Подільському: заміна стояків, змішувачів, бойлерів у багатоповерхівках. Приїзд за 10-20 хвилин, цілодобово.",
        "Сантехнік на Новому плані", "Ми базуємось на Грушевського, тому на Новий план приїжджаємо найшвидше: 10-20 хвилин удень і вночі.",
        """<h2>Типові завдання в багатоповерхівках</h2><p>Більшість будинків Нового плану збудовані в 1970-80-х роках. Сталеві стояки й крани на вводі тут вже відпрацювали своє, тому найчастіше ми міняємо крани, ділянки стояків і гнучкі підводки.</p>
<h2>Заміна стояків з ОСББ</h2><p>Заміну стояка погоджуємо з ОСББ або керуючою компанією: домовляємось про відключення води, попереджаємо сусідів оголошенням і робимо роботу за 3-4 години.</p>"""))
    out.append(contacts())
    return out


def price_tables_single(cat):
    rows = dict(PRICES)[cat]
    r = "".join(f'<tr><td>{n}</td><td>{p} ₴</td></tr>' for n, p in rows)
    return f'<div class="card"><h2 class="h3">Ціни: {cat.lower()}</h2><table class="ptable"><tbody>{r}</tbody></table><a class="btn btn--red btn--block" href="tel:{cfg["business"]["phone"]}">{PHONE_SVG}Подзвонити</a><p class="small muted">Всі ціни на сторінці <a href="{{{{root}}}}tsiny/">прайсу</a>.</p></div>'


def area(path, name, title, desc, h1, lead, prose):
    prose += """<h2>Послуги в районі</h2><ul class="link-list"><li><a href="{{root}}posluhy/avariinyi-vyklyk/">Аварійний виклик</a></li><li><a href="{{root}}posluhy/prochystka-kanalizatsii/">Прочистка каналізації</a></li><li><a href="{{root}}posluhy/ustanovka-boilera/">Встановлення бойлера</a></li></ul>"""
    return inner(path, [("Райони", "#rayony"), (name, path)], title, desc, h1, lead, prose,
                 ld=[service_ld(cfg, "Послуги сантехніка", desc, area=name + ", Кам'янець-Подільський", price=200)])


def prices_page():
    body = f"""
<section class="phero"><div class="wrap phero__in"><div><h1>Ціни на послуги сантехніка</h1><p class="lead">Вартість роботи без матеріалів. Точну суму майстер називає після огляду, до початку робіт.</p></div>
<a class="btn btn--red btn--big" href="tel:{cfg['business']['phone']}">{PHONE_SVG}{cfg['business']['phone_display']}</a></div></section>
<div class="wrap section-sm">{price_tables(filterable=True)}
<p class="muted small">Ціни актуальні для Кам'янця-Подільського. Виїзд за місто від 300 ₴. Матеріали за чеком магазину, без націнки.</p></div>"""
    return {"path": "tsiny/", "title": "Ціни на послуги сантехніка в Кам'янці-Подільському",
            "description": "Прайс сантехніка в Кам'янці-Подільському: виїзд від 200 грн, прочистка від 400 грн, заміна змішувача від 400 грн, бойлер від 1100 грн. Без прихованих доплат.",
            "body": body, "crumbs": [("Ціни", "tsiny/")]}


def contacts():
    b = cfg["business"]
    body = f"""
<section class="phero"><div class="wrap"><h1>Контакти сантехніка</h1><p class="lead">Аварія: дзвоніть одразу. Планова робота: залиште заявку.</p></div></section>
<div class="wrap book section-sm">{booking_form()}<div class="book__aside"><p class="big-phone-l">Аварійна лінія 24/7</p><a class="big-phone" href="tel:{b['phone']}">{b['phone_display']}</a>
<p><b>База:</b> {b['street']}, Кам'янець-Подільський</p><p><b>Пошта:</b> <a href="mailto:{b['email']}">{b['email']}</a></p><p class="muted small">Офісу для відвідувачів немає: майстри працюють на виїзді.</p></div></div>"""
    return {"path": "kontakty/", "title": "Контакти: сантехнік у Кам'янці-Подільському | Кран і Ключ",
            "description": "Телефон аварійної лінії сантехніка в Кам'янці-Подільському, цілодобово. Заявка на планові роботи онлайн, зворотний дзвінок протягом 20 хвилин.",
            "body": body, "crumbs": [("Контакти", "kontakty/")]}


JS = r"""
(function(){
  var sel=document.getElementById('eta-area'); if(!sel) return;
  var t=document.getElementById('eta-time'), fine=document.getElementById('eta-fine'), st=document.getElementById('eta-status');
  var h=new Date().getHours(), night=h>=21||h<8;
  try{var saved=localStorage.getItem('eta-area'); if(saved) sel.value=saved;}catch(e){}
  function upd(){
    var o=sel.selectedOptions[0], a=+o.dataset.min, b=+o.dataset.max;
    if(night){a+=10;b+=10;}
    t.textContent=a+'-'+b+' хв';
    fine.textContent=night?'Зараз діє нічний тариф: виїзд 400 ₴ (з 21:00 до 08:00).':'Виїзд по місту 200 ₴. Діагностика безкоштовна, якщо ремонт робимо ми.';
    try{localStorage.setItem('eta-area',sel.value);}catch(e){}
  }
  st.textContent=night?'Черговий нічний майстер на зв\'язку':'Майстри на зв\'язку, зараз '+String(h).padStart(2,'0')+':'+String(new Date().getMinutes()).padStart(2,'0');
  sel.addEventListener('change',upd); upd();
})();
(function(){
  var q=document.getElementById('psearch'); if(!q) return;
  var rows=[].slice.call(document.querySelectorAll('.ptable tr')), empty=document.getElementById('psearch-empty');
  q.addEventListener('input',function(){
    var v=q.value.trim().toLowerCase(), n=0;
    rows.forEach(function(r){var ok=!v||r.textContent.toLowerCase().indexOf(v)>-1;r.hidden=!ok;if(ok)n++;});
    document.querySelectorAll('.pcat').forEach(function(c){c.hidden=!c.querySelector('tr:not([hidden])');});
    empty.hidden=n>0;
  });
})();
"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#c42d16"/><path d="M12 13h10a6 6 0 0 1 6 6v2h-5v-2a1 1 0 0 0-1-1H12z" fill="#fff"/></svg>'

if __name__ == "__main__":
    build(cfg, pages(), layout, read(os.path.join(os.path.dirname(__file__), "plumber_kp.css")), JS, FAVICON)
