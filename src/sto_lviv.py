"""СТО «Бруківка Сервіс», Львів (вигаданий бізнес, демо для портфоліо)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from sitekit import build, default_layout, service_ld, faq_html, PHONE_SVG, read, ROOT

SLUG = "sto-lviv"
cfg = {
    "slug": SLUG,
    "base": f"https://dmytro1448.github.io/local-business-sites/{SLUG}/",
    "version": "3",
    "theme_color": "#14161a",
    "fonts": "https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&family=Golos+Text:wght@400;600&display=swap",
    "business": {
        "type": "AutoRepair",
        "name": "Бруківка Сервіс",
        "description": "СТО у Львові: технічне обслуговування, ремонт ходової, комп'ютерна діагностика легкових авто і кросоверів.",
        "phone": "+380000000000",
        "phone_display": "+380 00 000 00 00",
        "email": "zapys@example.com",
        "street": "вул. Стрийська",
        "city": "Львів",
        "region": "Львівська область",
        "geo": (49.80553, 24.01543),
        "priceRange": "₴₴",
        "hours": [(["Mo", "Tu", "We", "Th", "Fr"], "08:00", "19:00"), (["Sa"], "09:00", "16:00")],
        "areas": ["Сихів", "Левандівка", "Франківський район", "Личаківський район"],
    },
    "nav": [("Послуги", "#poslugy"), ("Калькулятор", "#kalkuliator"), ("Райони", "#rayony"), ("Контакти", "kontakty/")],
    "footer_services": [("ТО і заміна мастила", "posluhy/tekhobsluhovuvannia/"), ("Ремонт ходової", "posluhy/khodova/"), ("Комп'ютерна діагностика", "posluhy/diahnostyka/")],
    "footer_areas": [("СТО для Сихова", "rayony/sykhiv/"), ("СТО для Левандівки", "rayony/levandivka/")],
    "footer_blurb": "Незалежна СТО на Стрийській. Обслуговуємо легкові авто, кросовери і мікроавтобуси до 3,5 т.",
    "callbar_alt": ("Записатись", "kontakty/#zapys"),
    "logo_text": "Бруківка<small>сервіс · Львів</small>",
    "logo_svg": '<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 2l15.6 9v18L20 38 4.4 29V11z" fill="#ffb020"/><circle cx="20" cy="20" r="7.5" fill="#14161a"/><path d="M20 15.5v9M15.5 20h9" stroke="#ffb020" stroke-width="2.6" stroke-linecap="round"/></svg>',
}
layout = default_layout


WORKS = [
    ("oil", "Заміна мастила і масляного фільтра", 450, 0.5),
    ("filters", "Заміна повітряного і салонного фільтрів", 300, 0.4),
    ("pads", "Заміна гальмівних колодок (одна вісь)", 600, 1.0),
    ("brakefluid", "Заміна гальмівної рідини", 500, 0.7),
    ("diag", "Комп'ютерна діагностика", 400, 0.5),
    ("susp", "Перевірка ходової на підйомнику", 300, 0.5),
    ("plugs", "Заміна свічок запалювання", 400, 0.6),
    ("ac", "Заправка кондиціонера", 900, 0.8),
    ("timing", "Заміна ременя ГРМ з роликами", 2800, 3.0),
]
CLASSES = [
    ("a", "Малий клас (Skoda Fabia, Hyundai i20)", 1.0),
    ("c", "Середній клас (Octavia, Corolla, Golf)", 1.2),
    ("suv", "Кросовер / SUV (Tucson, RAV4, Duster)", 1.35),
    ("biz", "Бізнес-клас (Passat, Camry, BMW 5)", 1.5),
    ("van", "Мікроавтобус (Transit, Vito, Trafic)", 1.45),
]


def calculator():
    classes = "".join(f'<option value="{k}" data-k="{m}">{n}</option>' for k, n, m in CLASSES)
    works = "".join(
        f'<label class="work"><input type="checkbox" name="w" value="{k}" data-p="{p}" data-h="{h}"{" checked" if k in ("oil","filters","diag") else ""}><span class="work__n">{n}</span><span class="work__p">від {p} ₴</span></label>'
        for k, n, p, h in WORKS)
    return f"""
<section class="calc" id="kalkuliator" aria-labelledby="calc-h">
  <div class="wrap calc__grid">
    <div>
      <p class="kicker">Калькулятор ТО</p>
      <h2 id="calc-h">Порахуйте вартість робіт до приїзду</h2>
      <p class="muted">Ціни за роботу з урахуванням класу авто. Запчастини можна привезти свої або замовити в нас за ціною постачальника, без націнки на мастило.</p>
      <form class="calc__form" id="to-calc" aria-describedby="calc-note">
        <div class="field"><label for="cls">Клас автомобіля</label><select id="cls" name="cls">{classes}</select></div>
        <div class="presets" role="group" aria-label="Готові набори робіт">
          <button type="button" class="chip" data-set="oil,filters,diag">Базове ТО</button>
          <button type="button" class="chip" data-set="oil,filters,plugs,brakefluid,diag,susp">Велике ТО</button>
          <button type="button" class="chip" data-set="susp,pads">Перед зимою</button>
          <button type="button" class="chip" data-set="">Очистити</button>
        </div>
        <fieldset class="works"><legend class="sr-only">Роботи</legend>{works}</fieldset>
      </form>
    </div>
    <aside class="calc__out" aria-live="polite">
      <p class="calc__label">Робота, орієнтовно</p>
      <p class="calc__sum"><output id="calc-sum" for="to-calc">0</output> ₴</p>
      <dl class="calc__meta">
        <div><dt>Час на підйомнику</dt><dd id="calc-time">0 год</dd></div>
        <div><dt>Обрано робіт</dt><dd id="calc-count">0</dd></div>
      </dl>
      <p class="calc__note" id="calc-note">Точну суму майстер підтвердить після огляду. Якщо знайдемо щось ще, спершу дзвонимо вам, без погодження нічого не робимо.</p>
      <a class="btn btn--accent btn--block" id="calc-book" href="{{{{root}}}}kontakty/#zapys">Записатись з цим розрахунком</a>
    </aside>
  </div>
</section>"""


def booking_form(title="Запис на сервіс"):
    return f"""
<form class="form card" data-demo id="zapys" aria-labelledby="zapys-h">
  <h2 id="zapys-h">{title}</h2>
  <div class="form-body">
    <p class="muted">Залиште номер, адміністратор передзвонить протягом 15 хвилин у робочий час і підбере вільне вікно.</p>
    <div class="row2">
      <div class="field"><label for="f-name">Ім'я</label><input id="f-name" name="name" autocomplete="given-name" required><span class="err">Вкажіть ім'я</span></div>
      <div class="field"><label for="f-tel">Телефон</label><input id="f-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+380" required><span class="err">Перевірте номер телефону</span></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-car">Авто і рік</label><input id="f-car" name="car" placeholder="Skoda Octavia, 2017"></div>
      <div class="field"><label for="f-date">Бажана дата</label><input id="f-date" name="date" type="date" data-min-today></div>
    </div>
    <div class="field"><label for="f-msg">Що потрібно зробити</label><textarea id="f-msg" name="msg" placeholder="Наприклад: стукає спереду праворуч на нерівностях"></textarea></div>
    <label class="check"><input type="checkbox" name="agree" required> <span>Погоджуюсь на обробку даних для зворотного дзвінка</span></label>
    <button class="btn btn--accent" type="submit">Записатись</button>
  </div>
  <p class="form-ok" role="status">Дякуємо, {{name}}! Заявку прийнято. Це демо-сайт, тому заявка нікуди не надсилається, а на реальному сайті вона прийде адміністратору в Telegram і на пошту.</p>
</form>"""


def services_grid():
    items = [
        ("posluhy/tekhobsluhovuvannia/", "ТО і заміна мастила", "Мастило, фільтри, рідини за регламентом виробника. 40-60 хвилин, поки ви п'єте каву.", "від 450 ₴"),
        ("posluhy/khodova/", "Ремонт ходової", "Стуки, люфти, тягне вбік. Перевірка на підйомнику безкоштовна при ремонті.", "від 300 ₴"),
        ("posluhy/diahnostyka/", "Комп'ютерна діагностика", "Check Engine, помилки ABS і подушок. Роздруківка з розшифровкою.", "від 400 ₴"),
        (None, "Гальмівна система", "Колодки, диски, супорти, заміна рідини з прокачуванням.", "від 500 ₴"),
        (None, "Кондиціонер", "Заправка фреоном, перевірка на герметичність, антибактеріальна обробка.", "від 900 ₴"),
        (None, "Ремінь ГРМ", "Заміна комплектом з роликами і помпою, гарантія 12 місяців.", "від 2 800 ₴"),
    ]
    cards = []
    for href, t, d, p in items:
        title = f'<a href="{{{{root}}}}{href}">{t}</a>' if href else t
        cards.append(f'<li class="svc{" svc--link" if href else ""}"><h3>{title}</h3><p>{d}</p><p class="svc__price">{p}</p></li>')
    return f"""
<section class="section" id="poslugy" aria-labelledby="svc-h">
  <div class="wrap">
    <p class="kicker">Послуги</p>
    <h2 id="svc-h">Що робимо щодня</h2>
    <ul class="svc-grid">{''.join(cards)}</ul>
  </div>
</section>"""


HERO_SVG = """<svg class="hero__art" viewBox="0 0 520 380" role="img" aria-label="Ілюстрація: автомобіль на підйомнику і стрілка тахометра">
<defs><linearGradient id="g1" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#2a2e36"/><stop offset="1" stop-color="#1b1e24"/></linearGradient></defs>
<rect x="10" y="10" width="500" height="360" rx="18" fill="url(#g1)" stroke="#353a44"/>
<g stroke="#2f343d" stroke-width="1">""" + "".join(f'<line x1="{x}" y1="10" x2="{x}" y2="370"/>' for x in range(50, 510, 40)) + """</g>
<g transform="translate(60 120)">
<path d="M20 120 L60 120 C64 98 80 86 100 86 C120 86 136 98 140 120 L270 120 C274 98 290 86 310 86 C330 86 346 98 350 120 L388 120 C396 120 400 114 400 106 L398 86 C396 72 386 64 372 62 L330 58 L282 22 C272 14 260 10 246 10 L130 10 C114 10 102 16 92 26 L62 56 L32 62 C20 64 12 74 12 86 L12 112 C12 116 16 120 20 120 Z" fill="#eef0f3"/>
<path d="M108 30 L136 22 L226 22 L226 56 L84 56 Z M240 22 L256 22 C264 22 272 26 278 32 L304 56 L240 56 Z" fill="#2a2e36"/>
<circle cx="100" cy="122" r="30" fill="#14161a"/><circle cx="100" cy="122" r="13" fill="#ffb020"/>
<circle cx="310" cy="122" r="30" fill="#14161a"/><circle cx="310" cy="122" r="13" fill="#ffb020"/>
</g>
<rect x="40" y="290" width="440" height="14" rx="3" fill="#ffb020"/>
<rect x="110" y="250" width="16" height="40" fill="#5b616c"/><rect x="394" y="250" width="16" height="40" fill="#5b616c"/>
<g transform="translate(420 78)"><circle r="46" fill="#14161a" stroke="#353a44" stroke-width="2"/>
<path d="M-34 18 A38 38 0 1 1 34 18" fill="none" stroke="#5b616c" stroke-width="5" stroke-linecap="round"/>
<path d="M14 -35 A38 38 0 0 1 34 18" fill="none" stroke="#ffb020" stroke-width="5" stroke-linecap="round"/>
<line x1="0" y1="0" x2="22" y2="-24" stroke="#eef0f3" stroke-width="4" stroke-linecap="round"/><circle r="5" fill="#eef0f3"/></g>
</svg>"""


def home():
    faqs = [
        ("Чи можна приїхати зі своїми запчастинами?", "Так. Приймаємо ваші запчастини і мастило, гарантія на роботу при цьому діє. Якщо деталь виявиться браком, заміну зробимо без повторної оплати роботи."),
        ("Скільки чекати, якщо записатись сьогодні?", "Заміну мастила і фільтрів зазвичай робимо в день звернення. На ремонт ходової чи ГРМ вільне вікно буває через 1-2 дні."),
        ("Чи збережеться гарантія дилера?", "Так. Ми використовуємо мастила і фільтри з допусками виробника, а в сервісну книжку ставимо печатку з переліком робіт і номерами деталей."),
        ("Як оплатити?", "Готівкою, карткою на терміналі або за рахунком для ФОП і компаній. Чек і акт виконаних робіт видаємо завжди."),
    ]
    reviews = "".join(
        f'<li class="rev"><p class="rev__stars" aria-label="Оцінка {s} з 5">{"★" * s}{"☆" * (5 - s)}</p><p>{t}</p><p class="rev__who">{w}</p></li>'
        for s, t, w in [
            (5, "Приклад відгуку: швидко замінили колодки, показали старі, пояснили, що диски ще походять.", "Демо-дані · Google"),
            (5, "Приклад відгуку: записався зранку, о 12:00 авто вже було готове, ціна як у калькуляторі.", "Демо-дані · Google"),
            (4, "Приклад відгуку: довелось чекати деталь один день, але попередили одразу і не тягнули.", "Демо-дані · Google"),
        ])
    body = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="kicker">СТО · Франківський район · біля Сихова</p>
      <h1>СТО на Стрийській: ТО, ходова і діагностика у Львові</h1>
      <p class="lead">Ремонтуємо легкові авто і кросовери з 2014 року. Ціну робіт називаємо до початку, старі деталі віддаємо вам, а звіт з фото надсилаємо в месенджер.</p>
      <div class="hero__cta">
        <a class="btn btn--accent" href="{{{{root}}}}kontakty/#zapys">Записатись на сервіс</a>
        <a class="btn btn--ghost" href="tel:{cfg['business']['phone']}">{PHONE_SVG}{cfg['business']['phone_display']}</a>
      </div>
      <ul class="trust">
        <li><b>6 міс</b> гарантія на роботи</li>
        <li><b>5 постів</b> без черги на тижні</li>
        <li><b>Пн-Сб</b> з 8:00</li>
      </ul>
    </div>
    {HERO_SVG}
  </div>
</section>
{services_grid()}
{calculator()}
<section class="section" aria-labelledby="steps-h">
  <div class="wrap">
    <p class="kicker">Як це працює</p>
    <h2 id="steps-h">Чотири кроки без сюрпризів у рахунку</h2>
    <ol class="steps">
      <li><h3>Запис</h3><p>Телефоном або через форму. Підбираємо час, коли буде вільний підйомник.</p></li>
      <li><h3>Огляд</h3><p>Майстер дивиться авто при вас і називає ціну робіт і деталей.</p></li>
      <li><h3>Ремонт</h3><p>Нові роботи тільки після вашого «так». Фото проміжних етапів у месенджер.</p></li>
      <li><h3>Видача</h3><p>Акт робіт, старі деталі, гарантійний талон і нагадування про наступне ТО.</p></li>
    </ol>
  </div>
</section>
<section class="section section--alt" id="rayony" aria-labelledby="area-h">
  <div class="wrap area">
    <div>
      <p class="kicker">Зона обслуговування</p>
      <h2 id="area-h">Зручно доїхати з півдня і заходу Львова</h2>
      <p>Ми на Стрийській, між Сиховом і центром. Більшість клієнтів приїжджають із Сихова, Левандівки, Франківського і Личаківського районів. Для тих, хто не може залишити роботу, є перегін авто нашим водієм.</p>
      <ul class="area__links">
        <li><a href="{{{{root}}}}rayony/sykhiv/"><b>Сихів</b><span>7-12 хв по Стрийській</span></a></li>
        <li><a href="{{{{root}}}}rayony/levandivka/"><b>Левандівка</b><span>20-25 хв через Городоцьку</span></a></li>
      </ul>
    </div>
    <svg class="area__map" viewBox="0 0 400 300" role="img" aria-label="Схема: розташування СТО між Сиховом і центром Львова">
      <rect width="400" height="300" rx="16" fill="#1d2026"/>
      <path d="M40 60 C120 90 160 150 200 170 S300 240 370 260" stroke="#353a44" stroke-width="14" fill="none" stroke-linecap="round"/>
      <path d="M30 200 C110 180 160 120 230 70" stroke="#353a44" stroke-width="10" fill="none" stroke-linecap="round"/>
      <circle cx="80" cy="200" r="34" fill="#2a2e36"/><text x="80" y="205" fill="#c9ced6" font-size="14" text-anchor="middle" font-family="sans-serif">Левандівка</text>
      <circle cx="330" cy="250" r="34" fill="#2a2e36"/><text x="330" y="255" fill="#c9ced6" font-size="14" text-anchor="middle" font-family="sans-serif">Сихів</text>
      <circle cx="200" cy="70" r="30" fill="#2a2e36"/><text x="200" y="75" fill="#c9ced6" font-size="14" text-anchor="middle" font-family="sans-serif">Центр</text>
      <circle cx="245" cy="190" r="14" fill="#ffb020"/><circle cx="245" cy="190" r="26" fill="none" stroke="#ffb020" stroke-opacity=".4" stroke-width="3"/>
      <text x="245" y="228" fill="#ffb020" font-size="13" text-anchor="middle" font-family="sans-serif" font-weight="700">Бруківка Сервіс</text>
    </svg>
  </div>
</section>
<section class="section" aria-labelledby="rev-h">
  <div class="wrap">
    <p class="kicker">Відгуки з Google-профілю</p>
    <h2 id="rev-h">Що пишуть клієнти</h2>
    <p class="muted small">Демо-блок: на реальному сайті тут автоматично виводяться останні відгуки з Google Business Profile.</p>
    <ul class="rev-grid">{reviews}</ul>
  </div>
</section>
<div class="wrap">{faq_html(faqs)}</div>
<section class="section section--alt" aria-label="Запис">
  <div class="wrap book">
    {booking_form()}
    <div class="book__info">
      <h2>Контакти</h2>
      <p><b>Адреса:</b> {cfg['business']['street']}, Львів (в'їзд з боку АЗС)</p>
      <p><b>Телефон:</b> <a href="tel:{cfg['business']['phone']}">{cfg['business']['phone_display']}</a></p>
      <p><b>Графік:</b> Пн-Пт 8:00-19:00, Сб 9:00-16:00</p>
      <a class="btn btn--ghost" href="{{{{root}}}}kontakty/">Як доїхати</a>
    </div>
  </div>
</section>"""
    return {"path": "", "title": "СТО у Львові на Стрийській: ТО, ходова, діагностика | Бруківка Сервіс",
            "description": "СТО на Стрийській у Львові: ТО за 40-60 хв, ремонт ходової, комп'ютерна діагностика. Калькулятор вартості робіт онлайн, гарантія 6 місяців.",
            "body": body, "faq": faqs, "faq_inline": True}


def service_page(path, name, title, desc, h1, lead, price, blocks, faqs, table):
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in table)
    body = f"""
<section class="phero">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero__cta"><a class="btn btn--accent" href="{{{{root}}}}kontakty/#zapys">Записатись</a><a class="btn btn--ghost" href="tel:{cfg['business']['phone']}">{PHONE_SVG}Подзвонити</a></div>
  </div>
</section>
<div class="wrap cols">
  <article class="prose">{blocks}</article>
  <aside class="side">
    <div class="card">
      <h2 class="h3">Ціни на роботи</h2>
      <div class="tbl-wrap"><table class="price"><tbody>{rows}</tbody></table></div>
      <p class="small muted">Ціни для малого класу. Для кросоверів і бізнес-класу коефіцієнт 1,2-1,5.</p>
      <a class="btn btn--accent btn--block" href="{{{{root}}}}#kalkuliator">Розрахувати для свого авто</a>
    </div>
  </aside>
</div>"""
    return {"path": path, "title": title, "description": desc, "body": body, "faq": faqs,
            "crumbs": [("Послуги", "#poslugy"), (name, path)],
            "ld": [service_ld(cfg, name, desc, price=price)]}


def pages():
    out = [home()]
    out.append(service_page(
        "posluhy/tekhobsluhovuvannia/", "ТО і заміна мастила",
        "Технічне обслуговування авто у Львові, заміна мастила від 450 грн",
        "ТО авто у Львові на Стрийській: заміна мастила і фільтрів за 40-60 хвилин, мастила з допусками виробника, печатка в сервісну книжку. Від 450 грн.",
        "Технічне обслуговування і заміна мастила", "Планове ТО за регламентом виробника за 40-60 хвилин. Працюємо з вашими або нашими витратниками, у сервісну книжку ставимо печатку.", 450,
        """<h2>Що входить у базове ТО</h2>
<ul><li>заміна моторного мастила і масляного фільтра;</li><li>заміна повітряного і салонного фільтрів;</li><li>перевірка рівня і стану рідин: антифриз, гальмівна, омивач;</li><li>огляд гальм, шин і ходової на підйомнику;</li><li>зчитування помилок сканером і скидання сервісного інтервалу.</li></ul>
<h2>Коли робити ТО</h2>
<p>Для більшості бензинових авто інтервал 10-15 тисяч кілометрів або раз на рік. Якщо ви їздите переважно містом з пробками, як на Городоцькій чи Наукової в години пік, ми радимо скорочувати інтервал до 8-10 тисяч: двигун довго працює на холостих, і мастило старіє швидше, ніж показує одометр.</p>
<h2>Мастило без націнки</h2>
<p>Ми не заробляємо на мастилі: продаємо його за ціною постачальника, а оплату беремо тільки за роботу. Так вам простіше порівняти нашу ціну з іншими СТО.</p>""",
        [("Скільки триває заміна мастила?", "40-60 хвилин разом з оглядом. Можна зачекати в зоні відпочинку з кавою і Wi-Fi."),
         ("Яке мастило ви заливаєте?", "Те, що вказано в регламенті виробника для вашого двигуна, з відповідним допуском. Марку погоджуємо з вами заздалегідь.")],
        [("Заміна мастила і фільтра", "450 ₴"), ("Заміна повітряного фільтра", "150 ₴"), ("Заміна салонного фільтра", "150 ₴"), ("Заміна свічок (4 шт.)", "400 ₴"), ("Заміна антифризу", "600 ₴")]))
    out.append(service_page(
        "posluhy/khodova/", "Ремонт ходової",
        "Ремонт ходової частини у Львові: діагностика і заміна деталей",
        "Ремонт ходової у Львові: стуки, люфти, авто тягне вбік. Перевірка на підйомнику, заміна амортизаторів, сайлентблоків, кульових і стійок. Гарантія 6 міс.",
        "Ремонт ходової частини", "Стукає на ямах, авто тягне вбік або «плаває» на швидкості? Знайдемо причину на підйомнику і відремонтуємо за день.", 300,
        """<h2>Симптоми, з якими приїжджають найчастіше</h2>
<ul><li>стук спереду на нерівностях і трамвайних коліях;</li><li>кермо не повертається в центр або є люфт;</li><li>нерівномірний знос шин;</li><li>скрип при повороті керма на місці.</li></ul>
<h2>Як ми ремонтуємо</h2>
<p>Спочатку огляд на підйомнику з перевіркою люфтів монтуванням. Майстер показує вам знайдені проблеми наживо або на фото і пише перелік з цінами. Міняємо тільки те, що справді зношено, і пояснюємо, що може почекати до наступного сезону.</p>
<p>Після ремонту ходової обов'язково робимо розвал-сходження: без нього нові деталі і шини зношуються швидше. Сходження робимо на місці, на 3D-стенді.</p>""",
        [("Перевірка ходової платна?", "Окремо 300 грн. Якщо ремонт робите в нас, огляд безкоштовний."),
         ("За скільки зробите?", "Типовий ремонт передньої підвіски займає 2-4 години. Якщо деталі треба замовити, привозять наступного ранку.")],
        [("Перевірка ходової", "300 ₴"), ("Заміна амортизатора (1 шт.)", "500 ₴"), ("Заміна стійки стабілізатора", "250 ₴"), ("Заміна кульової опори", "450 ₴"), ("Розвал-сходження", "600 ₴")]))
    out.append(service_page(
        "posluhy/diahnostyka/", "Комп'ютерна діагностика",
        "Комп'ютерна діагностика авто у Львові від 400 грн",
        "Комп'ютерна діагностика авто у Львові: горить Check Engine, помилки ABS, Airbag, коробки. Дилерські сканери, роздруківка з поясненням, від 400 грн.",
        "Комп'ютерна діагностика авто", "Загорівся Check Engine чи інша лампа на панелі? Зчитаємо помилки дилерським сканером і пояснимо людською мовою, що з ними робити.", 400,
        """<h2>Що перевіряємо</h2>
<ul><li>двигун: пропуски запалювання, датчики, паливна система;</li><li>автоматична коробка і роботи;</li><li>ABS, ESP, подушки безпеки;</li><li>електроніка кузова і клімат.</li></ul>
<h2>Що ви отримуєте</h2>
<p>Роздруківку з кодами помилок і короткий висновок майстра: що критично, що можна відкласти, а що виявилось випадковою помилкою після заміни акумулятора. Помилки не стираємо «щоб не горіло», поки не знайдена причина.</p>
<h2>Перевірка перед купівлею</h2>
<p>Купуєте вживане авто? Приїжджайте разом із продавцем: за годину перевіримо електроніку, ходову і реальний пробіг за даними блоків керування.</p>""",
        [("Скільки триває діагностика?", "Зчитування помилок займає 20-30 хвилин. Пошук складної несправності в електриці може тривати 1-2 години, ціну погодимо заздалегідь."),
         ("Чи можна перевірити авто перед купівлею?", "Так, комплексна перевірка займає близько години і коштує 900 грн.")],
        [("Зчитування помилок", "400 ₴"), ("Діагностика двигуна з осцилографом", "800 ₴"), ("Перевірка перед купівлею", "900 ₴"), ("Пошук несправності електрики, год", "600 ₴")]))
    out += [area_page(*a) for a in AREAS]
    out.append(contacts())
    return out


AREAS = [
    ("rayony/sykhiv/", "Сихів", "СТО біля Сихова: 7-12 хвилин по Стрийській | Бруківка Сервіс",
     "СТО для мешканців Сихова: 7-12 хвилин по Стрийській, ТО, ходова, діагностика. Перегін авто нашим водієм від 200 грн, якщо ви на роботі.",
     "СТО для водіїв із Сихова",
     "Від Сихівської чи Червоної Калини до нас 7-12 хвилин по Стрийській, без заїзду в центр. Можна залишити авто зранку і забрати після роботи.",
     """<h2>Як доїхати із Сихова</h2>
<p>Рухайтесь Стрийською в бік центру. Після естакади тримайтесь правої смуги, в'їзд на СТО з боку АЗС, вказівник «Бруківка Сервіс». Парковка для клієнтів на території.</p>
<h2>Перегін авто, якщо немає часу</h2>
<p>Наш водій забере авто біля будинку на Сихові, а ввечері поверне назад. Вартість 200 грн в обидва боки. Ключі й документи передаєте особисто, акт приймання підписуємо на місці.</p>
<h2>Що найчастіше роблять сихівчани</h2>
<p>Через стан доріг на Зеленій і Хуторівці частіше за все звертаються з ходовою: стійки стабілізатора, сайлентблоки, сходження. Другий за популярністю запит: ТО перед поїздкою на Карпати.</p>"""),
    ("rayony/levandivka/", "Левандівка", "СТО для Левандівки і Залізничного району | Бруківка Сервіс",
     "СТО для мешканців Левандівки: 20-25 хвилин через Городоцьку, запис на зручний час, перегін авто. ТО, ходова, діагностика з гарантією.",
     "СТО для водіїв із Левандівки",
     "З Левандівки до нас 20-25 хвилин через Городоцьку і Любінську. Записуйтесь на час, коли вільний підйомник, щоб не чекати на місці.",
     """<h2>Як доїхати з Левандівки</h2>
<p>Найшвидше в непіковий час через Любінську і Наукову на Стрийську. У години пік зручніше записатись на 8:00 або після 17:00, тоді дорога займе до 25 хвилин.</p>
<h2>Забір авто з Левандівки</h2>
<p>Перегін працює і для Залізничного району: 300 грн в обидва боки. Зручно, якщо ви працюєте біля дому або не хочете стояти в заторах на Городоцькій.</p>
<h2>Комерційний транспорт</h2>
<p>Багато клієнтів з Левандівки працюють на мікроавтобусах. Ми обслуговуємо Transit, Vito, Trafic і Sprinter до 3,5 т, а для ФОП працюємо за рахунком з актом.</p>"""),
]


def area_page(path, name, title, desc, h1, lead, blocks):
    body = f"""
<section class="phero">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero__cta"><a class="btn btn--accent" href="{{{{root}}}}kontakty/#zapys">Записатись</a><a class="btn btn--ghost" href="tel:{cfg['business']['phone']}">{PHONE_SVG}Подзвонити</a></div>
  </div>
</section>
<div class="wrap cols">
  <article class="prose">{blocks}
  <h2>Послуги для району {name}</h2>
  <ul class="link-list"><li><a href="{{{{root}}}}posluhy/tekhobsluhovuvannia/">ТО і заміна мастила</a></li><li><a href="{{{{root}}}}posluhy/khodova/">Ремонт ходової</a></li><li><a href="{{{{root}}}}posluhy/diahnostyka/">Комп'ютерна діагностика</a></li></ul>
  </article>
  <aside class="side">{booking_form("Записатись з району " + name)}</aside>
</div>"""
    return {"path": path, "title": title, "description": desc, "body": body,
            "crumbs": [("Райони", "#rayony"), (name, path)],
            "ld": [service_ld(cfg, "Ремонт і обслуговування авто", desc, area=name + ", Львів")]}


def contacts():
    b = cfg["business"]
    body = f"""
<section class="phero"><div class="wrap"><h1>Контакти і запис на СТО</h1><p class="lead">Запишіться онлайн або подзвоніть. Відповідаємо в робочий час протягом 15 хвилин.</p></div></section>
<div class="wrap book">
  {booking_form()}
  <div class="book__info">
    <h2>Як нас знайти</h2>
    <p><b>Адреса:</b> {b['street']}, Львів. В'їзд з боку АЗС, вказівник «Бруківка Сервіс».</p>
    <p><b>Телефон:</b> <a href="tel:{b['phone']}">{b['phone_display']}</a></p>
    <p><b>Пошта:</b> <a href="mailto:{b['email']}">{b['email']}</a></p>
    <p><b>Графік:</b> Пн-Пт 8:00-19:00, Сб 9:00-16:00, Нд вихідний</p>
    <p class="small muted">На реальному сайті тут вбудована Google-карта з міткою з Google Business Profile, яка завантажується за кліком, щоб не гальмувати сторінку.</p>
  </div>
</div>"""
    return {"path": "kontakty/", "title": "Контакти і онлайн-запис на СТО у Львові | Бруківка Сервіс",
            "description": "Адреса, телефон і графік СТО «Бруківка Сервіс» на Стрийській у Львові. Онлайн-запис на ТО, ремонт ходової і діагностику.",
            "body": body, "crumbs": [("Контакти", "kontakty/")]}


JS = r"""
(function(){
  var f=document.getElementById('to-calc'); if(!f) return;
  var cls=f.querySelector('#cls'), sum=document.getElementById('calc-sum'), time=document.getElementById('calc-time'), cnt=document.getElementById('calc-count'), book=document.getElementById('calc-book');
  function calc(){
    var k=parseFloat(cls.selectedOptions[0].dataset.k), p=0,h=0,names=[];
    f.querySelectorAll('input[name=w]:checked').forEach(function(i){p+=+i.dataset.p;h+=+i.dataset.h;names.push(i.parentNode.querySelector('.work__n').textContent);});
    p=Math.round(p*k/10)*10; h=h*(k>1.3?1.2:1);
    sum.textContent=fmt(p); time.textContent=(Math.round(h*2)/2).toString().replace('.',',')+' год'; cnt.textContent=names.length;
    try{sessionStorage.setItem('to-calc',cls.selectedOptions[0].text+': '+names.join(', ')+'. Орієнтовно '+fmt(p)+' грн.');}catch(e){}
  }
  f.addEventListener('change',calc);
  f.querySelectorAll('[data-set]').forEach(function(b){b.addEventListener('click',function(){var s=b.dataset.set.split(',');f.querySelectorAll('input[name=w]').forEach(function(i){i.checked=s.indexOf(i.value)>-1;});calc();});});
  calc();
})();
(function(){ // prefill booking form with the calculator result
  var m=document.getElementById('f-msg'); if(!m||m.value) return;
  try{var v=sessionStorage.getItem('to-calc'); if(v&&location.hash==='#zapys') m.value=v;}catch(e){}
})();
"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><path d="M20 2l15.6 9v18L20 38 4.4 29V11z" fill="#ffb020"/><circle cx="20" cy="20" r="7.5" fill="#14161a"/></svg>'

if __name__ == "__main__":
    css = read(os.path.join(os.path.dirname(__file__), "sto_lviv.css"))
    build(cfg, pages(), layout, css, JS, FAVICON)
