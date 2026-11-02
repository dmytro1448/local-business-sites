"""Ремонт квартир «Метраж», Київ (вигаданий бізнес, демо для портфоліо)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
sys.path.insert(0, os.path.dirname(__file__))
from sitekit import build, default_layout, service_ld, faq_html, PHONE_SVG, read
from rooms import compare

SLUG = "remont-kyiv"
cfg = {
    "slug": SLUG,
    "base": f"https://dmytro1448.github.io/local-business-sites/{SLUG}/",
    "version": "3",
    "theme_color": "#f3ede4",
    "fonts": "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap",
    "business": {
        "type": "GeneralContractor",
        "name": "Метраж",
        "description": "Ремонт квартир під ключ у Києві: капітальний ремонт, ремонт у новобудовах, санвузли. Фіксований кошторис і поетапна оплата.",
        "phone": "+380000000000",
        "phone_display": "+380 00 000 00 00",
        "email": "koshtorys@example.com",
        "street": "вул. Велика Васильківська",
        "city": "Київ",
        "region": "Київ",
        "geo": (50.43120, 30.51630),
        "priceRange": "₴₴₴",
        "hours": [(["Mo", "Tu", "We", "Th", "Fr"], "09:00", "19:00"), (["Sa"], "10:00", "16:00")],
        "areas": ["Оболонський район", "Дарницький район", "Позняки", "Печерський район", "Голосіївський район"],
    },
    "nav": [("Роботи", "portfolio/"), ("Кошторис", "#koshtorys"), ("Етапи", "#etapy"), ("Послуги", "#poslugy"), ("Контакти", "kontakty/")],
    "footer_services": [("Капітальний ремонт", "posluhy/kapitalnyi-remont/"), ("Ремонт у новобудові", "posluhy/remont-v-novobudovi/"), ("Ремонт ванної", "posluhy/remont-vannoi/"), ("Портфоліо", "portfolio/")],
    "footer_areas": [("Оболонь", "rayony/obolon/"), ("Позняки", "rayony/pozniaky/")],
    "footer_blurb": "Ремонт квартир у Києві з фіксованим кошторисом. Власні бригади, технагляд на кожному об'єкті, гарантія 2 роки.",
    "callbar_alt": ("Кошторис", "#koshtorys"),
    "logo_text": "Метраж<small>ремонт квартир · Київ</small>",
    "logo_svg": '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="2" width="36" height="36" fill="#1c1a17"/><path d="M8 30V12l6 9 6-9v18M26 12h6M26 18h4M26 24h6M26 30h4" stroke="#f3ede4" stroke-width="2.4" fill="none"/></svg>',
}
layout = default_layout

CASES = [
    {"id": "c1", "kind": "living", "title": "Двокімнатна у сталінці на Печерську", "area": 58, "weeks": 14, "budget": "620 000 ₴ роботи",
     "task": "Стара проводка, криві стіни, дерев'яна підлога зі скрипом. Власниця хотіла світлу вітальню з кухнею і зберегти високі стелі.",
     "done": "Повна заміна електрики й сантехніки, вирівнювання стін по маяках, нова стяжка з тепловою підлогою на кухні, об'єднання кухні з вітальнею з погодженням перепланування.",
     "kw": {"wall": "#ece4d6", "accent": "#b5532d"}},
    {"id": "c2", "kind": "bath", "title": "Санвузол 4,2 м² на Оболоні", "area": 4.2, "weeks": 3, "budget": "118 000 ₴ роботи",
     "task": "Радянська плитка, протікання до сусідів, ванна, яка не вміщалась разом з пральною машиною.",
     "done": "Демонтаж до бетону, гідроізоляція з бортиками, інсталяція, прихований люк до лічильників, плитка 60×120 з мінімальними швами.",
     "kw": {"accent": "#2f5d62"}},
    {"id": "c3", "kind": "bedroom", "title": "Новобудова 41 м² на Позняках", "area": 41, "weeks": 10, "budget": "395 000 ₴ роботи",
     "task": "Квартира від забудовника без оздоблення, молода пара хотіла заїхати до осені й вкластись у бюджет.",
     "done": "Перегородки з газоблоку, розводка електрики під дизайн, стяжка, штукатурка, ламінат, фарбування. Підібрали матеріали в межах бюджету без втрати якості.",
     "kw": {"wall": "#e3e7e1", "accent": "#7a8c6e"}},
]


def calculator():
    return """
<section class="calc" id="koshtorys" aria-labelledby="calc-h">
  <div class="wrap calc__grid">
    <form id="est" class="calc__form">
      <p class="eyebrow">Кошторис за 1 хвилину</p>
      <h2 id="calc-h">Скільки коштуватиме і скільки триватиме</h2>
      <div class="field"><label for="e-area">Площа квартири, м²</label><input id="e-area" type="number" min="15" max="400" value="55" inputmode="numeric"></div>
      <fieldset class="field"><legend>Тип ремонту</legend>
        <div class="opts3">
          <label class="opt"><input type="radio" name="t" value="cosm" data-p="3200" data-w="3" data-k="25"><span><b>Косметичний</b><small>фарбування, підлога, без заміни комунікацій</small></span></label>
          <label class="opt"><input type="radio" name="t" value="cap" data-p="7600" data-w="7" data-k="12" checked><span><b>Капітальний</b><small>з електрикою, сантехнікою і вирівнюванням</small></span></label>
          <label class="opt"><input type="radio" name="t" value="des" data-p="10800" data-w="10" data-k="9"><span><b>За дизайн-проєктом</b><small>складні стелі, ніші, авторський нагляд</small></span></label>
        </div>
      </fieldset>
      <div class="row2">
        <div class="field"><label for="e-bld">Житло</label><select id="e-bld"><option value="1">Новобудова без оздоблення</option><option value="1.12">Вторинне (потрібен демонтаж)</option></select></div>
        <div class="field"><label for="e-bath">Санвузлів</label><select id="e-bath"><option>1</option><option>2</option><option>3</option></select></div>
      </div>
      <label class="check"><input type="checkbox" id="e-design"> <span>Потрібен дизайн-проєкт (900 ₴/м²)</span></label>
    </form>
    <div class="calc__out" aria-live="polite">
      <p class="eyebrow">Ваш орієнтир</p>
      <dl>
        <div><dt>Роботи</dt><dd id="o-work">—</dd></div>
        <div><dt>Матеріали, орієнтовно</dt><dd id="o-mat">—</dd></div>
        <div><dt>Строк</dt><dd id="o-weeks">—</dd></div>
      </dl>
      <div class="stages" id="o-stages" aria-label="Розподіл строку по етапах"></div>
      <p class="small">Це орієнтир за середніми цінами по Києву. Фіксований кошторис складаємо після безкоштовного заміру, і він не змінюється, якщо ви не змінюєте завдання.</p>
      <a class="btn btn--dark btn--block" href="{{root}}kontakty/#zamir">Замовити безкоштовний замір</a>
    </div>
  </div>
</section>"""


def booking_form(title="Замовити безкоштовний замір"):
    return f"""
<form class="form card" data-demo id="zamir" aria-labelledby="zamir-h">
  <h2 id="zamir-h">{title}</h2>
  <div class="form-body">
    <p class="muted">Інженер приїде в зручний день, зробить заміри і за 3 робочі дні надішле детальний кошторис. Безкоштовно і без зобов'язань.</p>
    <div class="row2">
      <div class="field"><label for="f-name">Ім'я</label><input id="f-name" name="name" autocomplete="given-name" required><span class="err">Вкажіть ім'я</span></div>
      <div class="field"><label for="f-tel">Телефон</label><input id="f-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+380" required><span class="err">Перевірте номер телефону</span></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-district">Район</label><select id="f-district" name="district"><option>Оболонський</option><option>Дарницький</option><option>Печерський</option><option>Голосіївський</option><option>Інший</option></select></div>
      <div class="field"><label for="f-area">Площа, м²</label><input id="f-area" name="area" inputmode="numeric" placeholder="55"></div>
    </div>
    <div class="field"><label for="f-msg">Коментар</label><textarea id="f-msg" name="msg" placeholder="Тип будинку, бажані строки, чи є дизайн-проєкт"></textarea></div>
    <label class="check"><input type="checkbox" name="agree" required> <span>Погоджуюсь на обробку даних для зворотного дзвінка</span></label>
    <button class="btn btn--accent" type="submit">Надіслати</button>
  </div>
  <p class="form-ok" role="status">Дякуємо, {{name}}! Заявку отримано. Це демо-сайт, заявка нікуди не надсилається. На робочому сайті вона потрапляє в CRM, а інженер отримує нагадування про замір.</p>
</form>"""


STAGES = [("Замір і кошторис", "Безкоштовно. Інженер фіксує стан квартири, ви отримуєте кошторис з переліком робіт і матеріалів.", "1 тиждень"),
          ("Договір", "Фіксована ціна, графік робіт і оплата етапами. Без авансу на всю суму.", "1-2 дні"),
          ("Чорнові роботи", "Демонтаж, перегородки, штукатурка, стяжка. Фотозвіт щопонеділка.", "30% строку"),
          ("Інженерія", "Електрика, сантехніка, вентиляція. Фото прихованих робіт до закриття стін.", "20% строку"),
          ("Чистові роботи", "Плитка, фарбування, підлога, двері, встановлення сантехніки і світла.", "40% строку"),
          ("Здача і гарантія", "Приймання за чек-листом, прибирання, гарантія 2 роки на всі роботи.", "фінал")]


def stages_html():
    return '<ol class="timeline">' + "".join(f'<li><h3>{t}</h3><p>{d}</p><span>{w}</span></li>' for t, d, w in STAGES) + "</ol>"


def case_card(c, full=False):
    extra = f'<dl class="case__facts"><div><dt>Площа</dt><dd>{str(c["area"]).replace(".", ",")} м²</dd></div><div><dt>Строк</dt><dd>{c["weeks"]} тиж.</dd></div><div><dt>Бюджет</dt><dd>{c["budget"]}</dd></div></dl>'
    body = f'<p><b>Завдання.</b> {c["task"]}</p><p><b>Що зробили.</b> {c["done"]}</p>' if full else f'<p>{c["task"]}</p>'
    return f'<article class="case" id="{c["id"]}">{compare(c["kind"], c["id"], **c["kw"])}<div class="case__txt"><h3>{c["title"]}</h3>{extra}{body}</div></article>'


FAQ = [
    ("Чи може кошторис зрости під час ремонту?", "Ні, якщо ви не змінюєте завдання. Ціна робіт фіксується в договорі. Додаткові роботи оформлюємо окремою угодою тільки за вашою згодою."),
    ("Як відбувається оплата?", "Етапами: перед початком кожного етапу ви оплачуєте тільки його. Матеріали купуємо за вашими чеками або ви купуєте самі за нашим списком."),
    ("Чи можна контролювати ремонт дистанційно?", "Так. Щопонеділка надсилаємо фото- і відеозвіт, а технагляд відповідає на питання в месенджері в робочий час."),
    ("Ви працюєте з дизайн-проєктом іншого дизайнера?", "Так. Перед стартом перевіряємо креслення на реалізованість і пропонуємо узгодити спірні вузли з дизайнером."),
    ("Яка гарантія?", "Два роки на всі виконані роботи. Якщо щось трапиться, приїжджаємо протягом 3 робочих днів."),
]


def home():
    svc = [("posluhy/kapitalnyi-remont/", "Капітальний ремонт", "Вторинне житло: демонтаж до бетону, нові комунікації, вирівнювання, чистова оздоба.", "від 7 600 ₴/м²"),
           ("posluhy/remont-v-novobudovi/", "Ремонт у новобудові", "Від стяжки до заїзду. Знаємо типові проблеми нових ЖК на Позняках і Осокорках.", "від 6 800 ₴/м²"),
           ("posluhy/remont-vannoi/", "Ремонт ванної", "Гідроізоляція, інсталяції, плитка великого формату. Від 3 тижнів.", "від 95 000 ₴")]
    svc_html = "".join(f'<li><a href="{{{{root}}}}{h}"><span class="n">0{i + 1}</span><h3>{t}</h3><p>{d}</p><span class="p">{p}</span></a></li>' for i, (h, t, d, p) in enumerate(svc))
    body = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__txt">
      <p class="eyebrow">Київ · ремонт квартир під ключ</p>
      <h1>Ремонт квартир у Києві з кошторисом, який не росте</h1>
      <p class="lead">Фіксуємо ціну і строк у договорі, оплата етапами, фотозвіт щотижня. Власні бригади й технагляд на кожному об'єкті.</p>
      <div class="hero__cta"><a class="btn btn--accent" href="#koshtorys">Розрахувати кошторис</a><a class="btn btn--line" href="{{{{root}}}}portfolio/">Дивитись роботи</a></div>
    </div>
    <figure class="hero__ba">{compare("living", "hero", wall="#ece4d6", accent="#b5532d")}<figcaption>Вітальня у сталінці на Печерську, 14 тижнів. Посуньте повзунок.</figcaption></figure>
  </div>
  <div class="wrap"><ul class="stats"><li><b>2 роки</b>гарантія на роботи</li><li><b>5 етапів</b>оплати замість авансу</li><li><b>щопонеділка</b>фото- і відеозвіт</li><li><b>3 дні</b>на детальний кошторис</li></ul></div>
</section>
{calculator()}
<section class="section" id="poslugy" aria-labelledby="svc-h"><div class="wrap"><p class="eyebrow">Послуги</p><h2 id="svc-h">Беремо квартиру повністю, від стін до світла</h2><ul class="svc">{svc_html}</ul></div></section>
<section class="section section--dark" aria-labelledby="cases-h"><div class="wrap"><div class="sec-head"><div><p class="eyebrow">Кейси</p><h2 id="cases-h">До і після</h2></div><a href="{{{{root}}}}portfolio/">Усі кейси →</a></div>
<div class="cases-row">{case_card(CASES[1])}{case_card(CASES[2])}</div><p class="small dim">Ілюстрації-схеми для демо. На реальному сайті тут фото з об'єктів.</p></div></section>
<section class="section" id="etapy" aria-labelledby="st-h"><div class="wrap"><p class="eyebrow">Як ми працюємо</p><h2 id="st-h">Шість етапів, кожен з чітким результатом</h2>{stages_html()}</div></section>
<section class="section section--paper" id="rayony" aria-labelledby="area-h"><div class="wrap areas"><div><p class="eyebrow">Райони</p><h2 id="area-h">Працюємо по всьому Києву</h2><p>Найбільше об'єктів у нас на Оболоні та Позняках, тому для них зібрали окремі сторінки з типовими будинками і цінами.</p></div>
<ul class="area-list"><li><a href="{{{{root}}}}rayony/obolon/">Оболонь <span>панельки 70-80-х і нові ЖК біля Дніпра</span></a></li><li><a href="{{{{root}}}}rayony/pozniaky/">Позняки <span>новобудови без оздоблення, Осокорки</span></a></li><li><span>Печерськ <span>сталінки і старий фонд</span></span></li><li><span>Голосіїв <span>новобудови і вторинка</span></span></li></ul></div></section>
<div class="wrap">{faq_html(FAQ)}</div>
<section class="section section--paper"><div class="wrap book">{booking_form()}<div class="book__aside"><h2>Або подзвоніть</h2><p>Відповімо на питання і запишемо на замір.</p><a class="btn btn--line" href="tel:{cfg['business']['phone']}">{PHONE_SVG}{cfg['business']['phone_display']}</a><p class="small muted">Пн-Пт 9:00-19:00, Сб 10:00-16:00</p></div></div></section>"""
    return {"path": "", "title": "Ремонт квартир у Києві під ключ з фіксованим кошторисом | Метраж",
            "description": "Ремонт квартир у Києві: капітальний, у новобудовах, ванні кімнати. Онлайн-калькулятор кошторису і строку, оплата етапами, гарантія 2 роки.",
            "body": body, "faq": FAQ, "faq_inline": True}


def inner(path, crumbs, title, desc, h1, lead, prose, aside=None, faq=None, ld=None, cls=""):
    body = f"""
<section class="phero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p></div></section>
<div class="wrap cols"><article class="prose">{prose}</article><aside class="side">{aside or booking_form()}</aside></div>"""
    return {"path": path, "title": title, "description": desc, "body": body, "crumbs": crumbs, "faq": faq, "ld": ld or [], "body_class": cls}


def price_aside(rows, note):
    r = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<div class="card"><h2 class="h3">Ціни на роботи</h2><table class="price"><tbody>{r}</tbody></table><p class="small muted">{note}</p><a class="btn btn--accent btn--block" href="{{{{root}}}}#koshtorys">Порахувати свою квартиру</a></div>'


def pages():
    out = [home()]
    out.append(inner("posluhy/kapitalnyi-remont/", [("Послуги", "#poslugy"), ("Капітальний ремонт", "posluhy/kapitalnyi-remont/")],
        "Капітальний ремонт квартири в Києві від 7600 грн/м² | Метраж",
        "Капітальний ремонт квартир у Києві: демонтаж, нова електрика і сантехніка, вирівнювання стін, чистова оздоба. Фіксований кошторис, гарантія 2 роки.",
        "Капітальний ремонт квартири", "Для вторинного житла, де треба міняти все: від проводки в стінах до підлоги. Строк 10-16 тижнів для двокімнатної квартири.",
        """<h2>Що входить</h2><ul><li>демонтаж старої оздоби, вивіз сміття;</li><li>нова електрика з окремими лініями на кухню і санвузол;</li><li>заміна труб водопостачання і каналізації;</li><li>вирівнювання стін по маяках, стяжка підлоги;</li><li>чистова оздоба, встановлення дверей, сантехніки й світла.</li></ul>
<h2>Чому стільки триває</h2><p>Найдовше сохнуть стяжка і штукатурка: прискорювати їх небезпечно, бо потім тріскається фарба і ламінат. Ми закладаємо технологічні паузи в графік і в цей час робимо інші роботи, щоб бригада не простоювала.</p>
<h2>Перепланування</h2><p>Якщо треба об'єднати кухню з кімнатою чи перенести двері, допомагаємо з проєктом і погодженням. Несучі стіни не чіпаємо без висновку конструктора.</p>""",
        price_aside([("Демонтаж, м²", "від 450 ₴"), ("Штукатурка по маяках, м²", "від 420 ₴"), ("Стяжка підлоги, м²", "від 380 ₴"), ("Електрика, точка", "від 450 ₴"), ("Укладання плитки, м²", "від 950 ₴")], "Ціни за роботу без матеріалів."),
        [("Чи можна жити в квартирі під час ремонту?", "Під час капітального ремонту ні: пил, відключення води й електрики. Для часткового ремонту можна домовитись про поетапну роботу.")],
        [service_ld(cfg, "Капітальний ремонт квартир", "Капітальний ремонт вторинного житла в Києві", price=7600)]))
    out.append(inner("posluhy/remont-v-novobudovi/", [("Послуги", "#poslugy"), ("Ремонт у новобудові", "posluhy/remont-v-novobudovi/")],
        "Ремонт квартири в новобудові Києва під ключ | Метраж",
        "Ремонт квартир у новобудовах Києва від 6800 грн/м²: перегородки, електрика, стяжка, чистова оздоба. Перевіряємо помилки забудовника до старту робіт.",
        "Ремонт у новобудові під ключ", "Отримали ключі від забудовника? Почнемо з перевірки квартири на приховані дефекти, а потім зробимо ремонт до заїзду.",
        """<h2>Спершу перевірка квартири</h2><p>До старту робіт інженер перевіряє геометрію стін, вікна, стяжку і вентиляцію. Знайдені дефекти фіксуємо актом, щоб ви могли вимагати їх виправлення від забудовника, а не платити за них самі.</p>
<h2>Типовий план робіт</h2><ul><li>перегородки з газоблоку або гіпсокартону;</li><li>розводка електрики й сантехніки під ваше планування меблів;</li><li>стяжка з шумоізоляцією, бо в нових монолітних будинках добре чути сусідів;</li><li>штукатурка, фарбування, підлога, двері.</li></ul>
<h2>Строки</h2><p>Однокімнатна 40-45 м² займає 8-10 тижнів, двокімнатна 10-13 тижнів. Графік з датами отримуєте разом з договором.</p>""",
        price_aside([("Перегородка з газоблоку, м²", "від 520 ₴"), ("Стяжка з шумоізоляцією, м²", "від 450 ₴"), ("Штукатурка, м²", "від 400 ₴"), ("Фарбування, м²", "від 220 ₴")], "Ціни за роботу без матеріалів."),
        [("Коли можна починати ремонт у новобудові?", "Після підключення будинку до постійного електропостачання і води. Якщо будинок ще дає усадку, радимо гнучкі рішення для стель і швів.")],
        [service_ld(cfg, "Ремонт квартир у новобудовах", "Ремонт квартир без оздоблення в новобудовах Києва", price=6800)]))
    out.append(inner("posluhy/remont-vannoi/", [("Послуги", "#poslugy"), ("Ремонт ванної", "posluhy/remont-vannoi/")],
        "Ремонт ванної кімнати і санвузла в Києві від 95 000 грн",
        "Ремонт ванної кімнати під ключ у Києві: гідроізоляція, інсталяції, плитка великого формату, приховані люки. Від 3 тижнів, гарантія 2 роки.",
        "Ремонт ванної кімнати під ключ", "Найскладніше приміщення в квартирі: вода, електрика і плитка на 4 квадратних метрах. Робимо так, щоб через рік не довелось переробляти.",
        f"""<figure class="inline-ba">{compare("bath", "svc", accent="#2f5d62")}<figcaption>Санвузол на Оболоні: 4,2 м², 3 тижні.</figcaption></figure>
<h2>Що робимо</h2><ul><li>демонтаж до бетону і перевірка стояків;</li><li>гідроізоляція підлоги з заведенням на стіни 20 см, у душовій зоні на всю висоту;</li><li>нові труби в штробах, колектор, фільтри;</li><li>інсталяції для унітазу і умивальника;</li><li>плитка з розкладкою, погодженою до старту.</li></ul>
<h2>Строк і ціна</h2><p>Стандартний санвузол 3-5 м² займає 3-4 тижні. Вартість робіт від 95 000 гривень залежно від формату плитки і кількості сантехніки.</p>""",
        price_aside([("Гідроізоляція, м²", "від 350 ₴"), ("Плитка до 60×60, м²", "від 950 ₴"), ("Плитка 60×120, м²", "від 1 400 ₴"), ("Монтаж інсталяції", "від 2 500 ₴"), ("Прихований люк", "від 1 800 ₴")], "Ціни за роботу без матеріалів."),
        [("Чи можна залишити стару ванну?", "Так, якщо вона в доброму стані. Чавунну ванну можна відреставрувати, це дешевше за нову.")],
        [service_ld(cfg, "Ремонт ванної кімнати", "Ремонт ванних кімнат і санвузлів у Києві", price=95000)]))
    out.append(portfolio())
    out.append(area("rayony/obolon/", "Оболонь", "Ремонт квартир на Оболоні: панельки і нові ЖК | Метраж",
        "Ремонт квартир на Оболоні: капітальний ремонт у панельних будинках 70-80-х і ремонт у нових ЖК біля Дніпра. Замір безкоштовно, фіксований кошторис.",
        "Ремонт квартир на Оболоні", "На Оболоні ми ведемо об'єкти постійно: від двокімнатних квартир у панельках біля Мінської до нових ЖК на набережній.",
        """<h2>Панельні будинки 70-80-х</h2><p>Типові проблеми: криві плити перекриття, алюмінієва проводка і сталеві стояки. Перед ремонтом радимо домовитись з ОСББ про заміну стояка, щоб не довелось відкривати нову плитку через рік.</p>
<h2>Нові ЖК біля Дніпра</h2><p>Тут важлива шумоізоляція і вентиляція, а також вимоги управителя будинку щодо графіка шумних робіт і вивозу сміття. Ці правила ми закладаємо у графік заздалегідь.</p>
<h2>Кейс на Оболоні</h2><p>Санвузол 4,2 м² за 3 тижні: демонтаж, гідроізоляція, інсталяція, плитка 60×120. <a href="{{root}}portfolio/#c2">Дивитись кейс</a></p>"""))
    out.append(area("rayony/pozniaky/", "Позняки", "Ремонт квартир на Позняках і Осокорках | Метраж",
        "Ремонт квартир у новобудовах на Позняках і Осокорках: від стяжки до заїзду за 8-12 тижнів. Перевірка квартири від забудовника, оплата етапами.",
        "Ремонт квартир на Позняках", "Позняки й Осокорки: багато новобудов без оздоблення. Робимо ремонт від голих стін до заїзду з фіксованим строком.",
        """<h2>Новобудови Дарницького району</h2><p>У нових будинках біля Позняків і Осокорків часто трапляються нерівні стяжки від забудовника і слабка вентиляція санвузлів. Ми перевіряємо це до старту і пропонуємо рішення в кошторисі, а не в процесі.</p>
<h2>Логістика</h2><p>Матеріали привозимо з баз на лівому березі, тому доставка займає 1-2 дні. Вивіз сміття організовуємо контейнером, погодженим з управителем будинку.</p>
<h2>Кейс на Позняках</h2><p>Квартира 41 м² для молодої пари за 10 тижнів у межах бюджету. <a href="{{root}}portfolio/#c3">Дивитись кейс</a></p>"""))
    out.append(contacts())
    return out


def area(path, name, title, desc, h1, lead, prose):
    prose += """<h2>Послуги</h2><ul class="link-list"><li><a href="{{root}}posluhy/kapitalnyi-remont/">Капітальний ремонт</a></li><li><a href="{{root}}posluhy/remont-v-novobudovi/">Ремонт у новобудові</a></li><li><a href="{{root}}posluhy/remont-vannoi/">Ремонт ванної</a></li></ul>"""
    return inner(path, [("Райони", "#rayony"), (name, path)], title, desc, h1, lead, prose,
                 booking_form("Замір на " + ("Оболоні" if name == "Оболонь" else "Позняках")), None,
                 [service_ld(cfg, "Ремонт квартир", desc, area=name + ", Київ", price=6800)])


def portfolio():
    cases = "".join(case_card(c, full=True) for c in CASES)
    body = f"""
<section class="phero"><div class="wrap"><h1>Кейси: ремонт квартир до і після</h1><p class="lead">Задача клієнта, що ми зробили, площа, строк і бюджет на роботи. Посуньте повзунок на зображенні, щоб порівняти.</p></div></section>
<div class="wrap section-sm"><div class="cases-list">{cases}</div><p class="small muted">Ілюстрації-схеми для демо-сайту. На реальному сайті тут фото з об'єктів і короткі відео.</p></div>"""
    return {"path": "portfolio/", "title": "Портфоліо: ремонт квартир у Києві до і після | Метраж",
            "description": "Кейси ремонту квартир у Києві: сталінка на Печерську, санвузол на Оболоні, новобудова на Позняках. Задача, рішення, строк і бюджет кожного об'єкта.",
            "body": body, "crumbs": [("Портфоліо", "portfolio/")]}


def contacts():
    b = cfg["business"]
    body = f"""
<section class="phero"><div class="wrap"><h1>Контакти і запис на замір</h1><p class="lead">Безкоштовний замір і детальний кошторис за 3 робочі дні.</p></div></section>
<div class="wrap book section-sm">{booking_form()}<div class="book__aside"><h2>Офіс</h2><p>{b['street']}, Київ. Зустрічі за попереднім записом: покажемо зразки матеріалів і приклади кошторисів.</p>
<p><b>Телефон:</b> <a href="tel:{b['phone']}">{b['phone_display']}</a></p><p><b>Пошта:</b> <a href="mailto:{b['email']}">{b['email']}</a></p><p><b>Графік:</b> Пн-Пт 9:00-19:00, Сб 10:00-16:00</p></div></div>"""
    return {"path": "kontakty/", "title": "Контакти студії ремонту «Метраж» у Києві",
            "description": "Телефон, пошта, адреса офісу і графік студії ремонту квартир «Метраж» у Києві. Запис на безкоштовний замір онлайн.",
            "body": body, "crumbs": [("Контакти", "kontakty/")]}


JS = r"""
document.querySelectorAll('[data-ba]').forEach(function(b){
  var r=b.querySelector('.ba__range');
  function upd(){b.style.setProperty('--pos',r.value+'%');}
  r.addEventListener('input',upd); upd();
});
(function(){
  var f=document.getElementById('est'); if(!f) return;
  var names=['Чорнові','Інженерія','Чистові','Здача'], share=[.3,.2,.4,.1];
  function money(a,b){return fmt(a/1000)+'-'+fmt(b/1000)+' тис. ₴';}
  function calc(){
    var a=Math.max(15,Math.min(400,+f.querySelector('#e-area').value||0)), t=f.querySelector('input[name=t]:checked');
    var bld=+f.querySelector('#e-bld').value, baths=+f.querySelector('#e-bath').value;
    var work=a*(+t.dataset.p)*bld + (baths-1)*65000 + (f.querySelector('#e-design').checked?a*900:0);
    var mat=work*(t.value==='cosm'?0.6:t.value==='cap'?0.85:1.1);
    var weeks=Math.round((+t.dataset.w)+a/(+t.dataset.k)+(baths-1)*1.5+(bld>1?1:0));
    document.getElementById('o-work').textContent=money(work*0.92,work*1.08);
    document.getElementById('o-mat').textContent=money(mat*0.85,mat*1.2);
    document.getElementById('o-weeks').textContent=weeks+'-'+(weeks+2)+' тижнів';
    document.getElementById('o-stages').innerHTML=names.map(function(n,i){var w=Math.max(1,Math.round(weeks*share[i]));return '<div style="flex:'+share[i]+'"><span>'+n+'</span><b>'+w+' тиж.</b></div>';}).join('');
  }
  f.addEventListener('input',calc); f.addEventListener('change',calc); calc();
})();
"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#1c1a17"/><path d="M8 30V12l6 9 6-9v18M26 12h6M26 18h4M26 24h6M26 30h4" stroke="#f3ede4" stroke-width="2.4" fill="none"/></svg>'

if __name__ == "__main__":
    build(cfg, pages(), layout, read(os.path.join(os.path.dirname(__file__), "remont_kyiv.css")), JS, FAVICON)
