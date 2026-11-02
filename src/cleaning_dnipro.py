"""Клінінг «Ясно», Дніпро (вигаданий бізнес, демо для портфоліо)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from sitekit import build, default_layout, service_ld, faq_html, PHONE_SVG, read

SLUG = "cleaning-dnipro"
cfg = {
    "slug": SLUG,
    "base": f"https://dmytro1448.github.io/local-business-sites/{SLUG}/",
    "version": "3",
    "theme_color": "#0d6f65",
    "fonts": "https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Manrope:wght@400;600;700&display=swap",
    "business": {
        "type": "ProfessionalService",
        "name": "Ясно Клінінг",
        "description": "Клінінгова служба в Дніпрі: підтримуюче, генеральне прибирання і прибирання після ремонту квартир і будинків.",
        "phone": "+380000000000",
        "phone_display": "+380 00 000 00 00",
        "email": "hello@example.com",
        "street": "просп. Дмитра Яворницького",
        "city": "Дніпро",
        "region": "Дніпропетровська область",
        "geo": (48.46642, 35.04620),
        "priceRange": "₴₴",
        "hours": [(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], "08:00", "21:00")],
        "areas": ["Соборний район", "Шевченківський район", "Лівий берег", "Індустріальний район", "Амур-Нижньодніпровський район"],
        "extra": {"knowsAbout": ["генеральне прибирання", "прибирання після ремонту", "мийка вікон"]},
    },
    "nav": [("Ціни", "#kalkuliator"), ("Послуги", "#poslugy"), ("Райони", "#rayony"), ("Питання", "#faq-h"), ("Контакти", "kontakty/")],
    "footer_services": [("Генеральне прибирання", "posluhy/heneralne-prybyrannia/"), ("Прибирання після ремонту", "posluhy/pislia-remontu/"), ("Підтримуюче прибирання", "posluhy/pidtrymuiuche/")],
    "footer_areas": [("Соборний район", "rayony/sobornyi/"), ("Лівий берег", "rayony/livyi-bereh/")],
    "footer_blurb": "Прибираємо квартири, будинки і невеликі офіси в Дніпрі щодня з 8:00 до 21:00. Свої засоби і техніка.",
    "callbar_alt": ("Розрахувати", "#kalkuliator"),
    "logo_text": "ясно<small>клінінг у Дніпрі</small>",
    "logo_svg": '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#0d6f65"/><path d="M20 8l2.6 7.4L30 18l-7.4 2.6L20 28l-2.6-7.4L10 18l7.4-2.6z" fill="#fff"/><circle cx="29" cy="28" r="3" fill="#ffb4a2"/></svg>',
}
layout = default_layout

TYPES = [("support", "Підтримуюче", 38, "Пил, підлоги, кухня, санвузол"),
         ("general", "Генеральне", 75, "Все, включно з плиткою, фасадами і шафами"),
         ("renov", "Після ремонту", 95, "Будівельний пил, затирка, фарба")]
EXTRAS = [("windows", "Мийка вікон", 180, "вікно", True), ("fridge", "Холодильник всередині", 350, None, False),
          ("oven", "Духовка всередині", 400, None, False), ("balcony", "Балкон або лоджія", 450, None, False),
          ("iron", "Прасування", 300, "год", True), ("sofa", "Хімчистка дивана", 900, None, False)]


def calculator(compact=False):
    types = "".join(
        f'<label class="seg"><input type="radio" name="type" value="{k}" data-p="{p}"{" checked" if k == "general" else ""}><span><b>{n}</b><small>{p} ₴/м²</small></span></label>'
        for k, n, p, d in TYPES)
    extras = []
    for k, n, p, unit, qty in EXTRAS:
        if qty:
            extras.append(f'<div class="extra extra--qty"><span class="extra__n">{n}<small>{p} ₴/{unit}</small></span>'
                          f'<span class="qty"><button type="button" data-step="-1" aria-label="Менше: {n}">−</button>'
                          f'<input type="number" name="{k}" value="0" min="0" max="30" data-p="{p}" aria-label="{n}, кількість" inputmode="numeric">'
                          f'<button type="button" data-step="1" aria-label="Більше: {n}">+</button></span></div>')
        else:
            extras.append(f'<label class="extra"><input type="checkbox" name="{k}" data-p="{p}"><span class="extra__n">{n}<small>{p} ₴</small></span></label>')
    return f"""
<div class="calc" id="kalkuliator">
  <form id="clean-calc" class="calc__form" aria-labelledby="calc-h">
    <h2 id="calc-h" class="calc__title">Розрахуйте прибирання</h2>
    <fieldset class="segs"><legend class="lbl">Тип прибирання</legend>{types}</fieldset>
    <div class="area-row">
      <label class="lbl" for="area">Площа, м²</label>
      <div class="area-ctl"><input type="range" id="area-r" min="20" max="250" step="5" value="60" aria-label="Площа, повзунок"><input type="number" id="area" min="20" max="500" value="60" inputmode="numeric"></div>
    </div>
    <details class="extras"{" open" if not compact else ""}><summary class="lbl">Додаткові послуги</summary><div class="extras__list">{''.join(extras)}</div></details>
    <div class="opts">
      <label class="check"><input type="checkbox" name="eco"> <span>Еко-засоби без хлору і запаху (+10%)</span></label>
      <div class="freq"><label class="lbl" for="freq">Як часто</label><select id="freq" name="freq"><option value="0">Разово</option><option value="0.1">Раз на 2 тижні (−10%)</option><option value="0.15">Щотижня (−15%)</option></select></div>
    </div>
    <div class="calc__out" aria-live="polite">
      <div><p class="calc__sum"><output id="c-sum">0</output> ₴</p><p class="calc__meta" id="c-meta">—</p></div>
      <a class="btn btn--accent" id="c-book" href="{{{{root}}}}kontakty/#zayavka">Замовити</a>
    </div>
    <p class="calc__fine">Мінімальне замовлення 1 500 ₴. Виїзд по Дніпру безкоштовний, за місто від 200 ₴.</p>
  </form>
</div>"""


def booking_form(title="Заявка на прибирання"):
    return f"""
<form class="form card" data-demo id="zayavka" aria-labelledby="zayavka-h">
  <h2 id="zayavka-h">{title}</h2>
  <div class="form-body">
    <p class="muted">Менеджер перетелефонує протягом 10 хвилин, уточнить деталі й підтвердить ціну. Передоплата не потрібна.</p>
    <div class="row2">
      <div class="field"><label for="f-name">Ім'я</label><input id="f-name" name="name" autocomplete="given-name" required><span class="err">Вкажіть ім'я</span></div>
      <div class="field"><label for="f-tel">Телефон</label><input id="f-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+380" required><span class="err">Перевірте номер телефону</span></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-street">Район або вулиця</label><input id="f-street" name="street" placeholder="Наприклад, Тополя-2"></div>
      <div class="field"><label for="f-date">Дата</label><input id="f-date" name="date" type="date" data-min-today></div>
    </div>
    <div class="field"><label for="f-msg">Коментар</label><textarea id="f-msg" name="msg" placeholder="Площа, тип прибирання, що важливо"></textarea></div>
    <label class="check"><input type="checkbox" name="agree" required> <span>Погоджуюсь на обробку даних для зворотного дзвінка</span></label>
    <button class="btn btn--accent" type="submit">Надіслати заявку</button>
  </div>
  <p class="form-ok" role="status">Дякуємо, {{name}}! Заявку прийнято. Це демо-сайт: заявка нікуди не надсилається. На робочому сайті вона одразу потрапляє менеджеру в CRM і Telegram.</p>
</form>"""


FAQ_HOME = [
    ("Чи потрібно бути вдома під час прибирання?", "Ні. Багато клієнтів залишають ключі консьєржу або передають їх кур'єром. Після прибирання надсилаємо фотозвіт і повертаємо ключі тим самим способом."),
    ("Ваші засоби безпечні для дітей і тварин?", "Базові засоби професійні, з сертифікатами для побутового використання. Якщо в домі малюк, алергік чи тварини, оберіть опцію еко-засобів без хлору і різкого запаху."),
    ("Що, як мені не сподобається результат?", "Повідомте протягом 24 годин, і ми безкоштовно приїдемо переробити проблемні місця. Це прописано в договорі."),
    ("Як формується фінальна ціна?", "Ціна з калькулятора базова. Менеджер уточнює стан квартири по фото або відео і фіксує суму до виїзду. На місці ціна не росте."),
    ("Скільки людей приїде і на скільки годин?", "Залежить від площі й типу. Квартиру 60 м² на генеральне прибирання двоє клінерів роблять за 5-6 годин."),
    ("Ви прибираєте офіси?", "Так, офіси до 300 м² у вечірній час або вихідні. Для регулярного прибирання укладаємо договір з ФОП або ТОВ."),
]

SPARKLE = '<svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1l2.6 8.4L23 12l-8.4 2.6L12 23l-2.6-8.4L1 12l8.4-2.6z"/></svg>'


def home():
    rooms = [
        ("kitchen", "Кухня", ["знежирення фасадів і фартуха", "плита, мийка, змішувач до блиску", "мікрохвильовка всередині", "столи, підвіконня, плінтуси"]),
        ("bath", "Санвузол", ["плитка і шви без нальоту", "ванна, душова, скло кабіни", "унітаз з усіх боків", "дзеркала і сантехніка без розводів"]),
        ("rooms", "Кімнати", ["пил з усіх поверхонь і техніки", "пилосос і вологе миття підлоги", "дзеркала і скляні поверхні", "заправлення ліжок, складання речей"]),
    ]
    tabs = "".join(f'<button role="tab" type="button" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{n}</button>' for i, (k, n, _) in enumerate(rooms))
    panels = "".join(
        f'<div role="tabpanel" id="p-{k}" aria-labelledby="t-{k}" tabindex="0"{"" if i == 0 else " hidden"}><ul class="ticks">' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"
        for i, (k, n, items) in enumerate(rooms))
    svc = [("posluhy/pidtrymuiuche/", "Підтримуюче", "Раз на тиждень або два: підлоги, пил, кухня, санвузол. Для тих, хто цінує вихідні.", "від 38 ₴/м²", "c1"),
           ("posluhy/heneralne-prybyrannia/", "Генеральне", "Від стелі до плінтусів: шафи всередині, плитка, фасади, вікна за бажанням.", "від 75 ₴/м²", "c2"),
           ("posluhy/pislia-remontu/", "Після ремонту", "Будівельний пил, затирка і фарба. Квартира готова до заїзду за день.", "від 95 ₴/м²", "c3")]
    cards = "".join(f'<li class="scard scard--{c}"><h3><a href="{{{{root}}}}{h}">{t}</a></h3><p>{d}</p><p class="scard__p">{p}</p></li>' for h, t, d, p, c in svc)
    body = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__txt">
      <p class="pill">{SPARKLE} Дніпро · щодня з 8:00 до 21:00</p>
      <h1>Прибирання квартир у Дніпрі з ціною до приїзду</h1>
      <p class="lead">Порахуйте вартість за хвилину, а ми приїдемо зі своїми засобами і технікою. Фіксуємо ціну заздалегідь і переробляємо безкоштовно, якщо щось не так.</p>
      <ul class="facts">
        <li><b>24 год</b><span>гарантія переробки</span></li>
        <li><b>0 ₴</b><span>передоплата</span></li>
        <li><b>2-4</b><span>клінери на виїзді</span></li>
      </ul>
    </div>
    {calculator()}
  </div>
</section>
<section class="section" id="poslugy" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h">Три формати прибирання</h2>
    <ul class="scards">{cards}</ul>
  </div>
</section>
<section class="section section--tint" aria-labelledby="inc-h">
  <div class="wrap inc">
    <div>
      <h2 id="inc-h">Що входить у генеральне прибирання</h2>
      <p class="muted">Чек-лист, за яким працюють клінери. Ви отримуєте його в месенджер перед виїздом і можете відмітити, на що звернути особливу увагу.</p>
    </div>
    <div class="tabs">
      <div role="tablist" aria-label="Приміщення" class="tabs__list">{tabs}</div>
      {panels}
    </div>
  </div>
</section>
<section class="section" id="rayony" aria-labelledby="area-h">
  <div class="wrap">
    <h2 id="area-h">Працюємо по всьому Дніпру</h2>
    <p class="muted wide">Клінери живуть у різних районах міста, тому на виїзд у межах Дніпра потрібно 30-60 хвилин. Окремі сторінки для районів, звідки найбільше замовлень:</p>
    <ul class="areas">
      <li><a href="{{{{root}}}}rayony/sobornyi/"><b>Соборний район</b><span>Нагірний, Тополя, Перемога. Сталінки й новобудови</span></a></li>
      <li><a href="{{{{root}}}}rayony/livyi-bereh/"><b>Лівий берег</b><span>Лівобережний, Березинка, Ломівка</span></a></li>
      <li><span><b>Шевченківський</b><span>центр, Мандриківка</span></span></li>
      <li><span><b>Індустріальний</b><span>Сокіл, Придніпровськ</span></span></li>
      <li><span><b>Новокодацький</b><span>Парус, Покровський</span></span></li>
      <li><span><b>Передмістя</b><span>Ігрень, Підгороднє, від 200 ₴</span></span></li>
    </ul>
  </div>
</section>
<div class="wrap">{faq_html(FAQ_HOME)}</div>
<section class="section section--tint"><div class="wrap book">{booking_form()}<div class="book__aside"><h2>Зручніше голосом?</h2><p>Подзвоніть, і менеджер порахує ціну по телефону за 2-3 хвилини.</p><a class="btn btn--ghost" href="tel:{cfg['business']['phone']}">{PHONE_SVG}{cfg['business']['phone_display']}</a><p class="muted small">Щодня з 8:00 до 21:00</p></div></div></section>"""
    return {"path": "", "title": "Клінінг у Дніпрі: прибирання квартир з онлайн-ціною | Ясно",
            "description": "Прибирання квартир і будинків у Дніпрі: підтримуюче від 38 грн/м², генеральне, після ремонту. Онлайн-калькулятор, фіксована ціна, гарантія 24 години.",
            "body": body, "faq": FAQ_HOME, "faq_inline": True}


def inner(path, crumbs, title, desc, h1, lead, prose, aside, faq=None, ld=None):
    body = f"""
<section class="phero"><div class="wrap"><h1>{h1}</h1><p class="lead">{lead}</p></div></section>
<div class="wrap cols"><article class="prose">{prose}</article><aside class="side">{aside}</aside></div>"""
    return {"path": path, "title": title, "description": desc, "body": body, "crumbs": crumbs, "faq": faq, "ld": ld or []}


def svc_page(path, name, title, desc, h1, lead, prose, faq, price):
    aside = calculator(compact=True)
    return inner(path, [("Послуги", "#poslugy"), (name, path)], title, desc, h1, lead,
                 prose + f'<p><a class="btn btn--accent" href="{{{{root}}}}kontakty/#zayavka">Замовити {name.lower()}</a></p>',
                 aside, faq, [service_ld(cfg, name, desc, price=price)])


def pages():
    out = [home()]
    out.append(svc_page("posluhy/heneralne-prybyrannia/", "Генеральне прибирання",
        "Генеральне прибирання квартири в Дніпрі від 75 грн/м² | Ясно",
        "Генеральне прибирання квартир і будинків у Дніпрі: кухня, санвузол, шафи всередині, вікна. Від 75 грн/м², фіксована ціна, свої засоби і техніка.",
        "Генеральне прибирання квартири", "Коли треба привести дім до ладу повністю: перед святами, після зими, при переїзді або перед продажем квартири.",
        """<h2>Що ми робимо</h2><p>Генеральне прибирання охоплює все, що є в базовому, плюс зони, до яких зазвичай не доходять руки: фасади і внутрішні полиці шаф, верх кухонних модулів, плитка і шви, батареї, двері й вимикачі, люстри до висоти 3 метрів.</p>
<h2>Скільки триває</h2><p>Квартира 50-70 м² займає 5-7 годин у двох клінерів. Для будинку від 120 м² відправляємо бригаду з трьох-чотирьох людей, щоб закінчити за один день.</p>
<h2>Що взяти до уваги</h2><ul><li>Вікна рахуються окремо: мийка з двох боків, рами і підвіконня.</li><li>Хімчистку меблів робимо в той самий день окремою машиною.</li><li>Якщо прибирання перед продажем, можемо зробити фото квартири для оголошення.</li></ul>""",
        [("Чи миєте ви люстри і стелі?", "Так, до висоти 3 метри з драбини. Кришталеві люстри миємо вручну, це оцінюється окремо за фото."),
         ("Потрібно звільнити шафи?", "Ні, клінери акуратно виймуть речі, протруть полиці і складуть усе назад.")], 75))
    out.append(svc_page("posluhy/pislia-remontu/", "Прибирання після ремонту",
        "Прибирання після ремонту в Дніпрі від 95 грн/м² | Ясно",
        "Прибирання квартири після ремонту в Дніпрі: будівельний пил, затирка, фарба, клей. Промислові пилососи, від 95 грн/м², готово до заїзду за день.",
        "Прибирання після ремонту", "Будівельний пил осідає всюди, навіть у закритих шафах. Ми прибираємо його в три проходи, щоб він не повертався через тиждень.",
        """<h2>Як ми працюємо</h2><p>Спершу промисловий пилосос з HEPA-фільтром прибирає основний пил зі стель, стін і підлоги. Потім ручне очищення: затирка з плитки, плями фарби з вікон, сліди скотчу і клею. Фінальний прохід вологий, з мікрофіброю, щоб не лишалось сірого нальоту.</p>
<h2>Новобудови Лівого берега і Тополі</h2><p>Ми регулярно прибираємо квартири в нових ЖК після здачі ключів: там часто лишається бетонний пил у вентиляції та на підвіконнях. Перед прибиранням перевіряємо, чи вимкнені ремонтні роботи у квартирі, інакше результат не втримається.</p>
<h2>Що не робимо</h2><p>Не вивозимо будівельне сміття і не знімаємо застиглий розчин зі стін. Якщо таке є, підкажемо перевізника.</p>""",
        [("Коли замовляти прибирання після ремонту?", "Коли всі мокрі роботи закінчені й техніка встановлена. Інакше доведеться прибирати двічі."),
         ("Чи впораєтесь за один день?", "Квартиру до 80 м² так. Для більших площ або дуже брудних об'єктів може знадобитись другий день.")], 95))
    out.append(svc_page("posluhy/pidtrymuiuche/", "Підтримуюче прибирання",
        "Підтримуюче прибирання квартири в Дніпрі від 38 грн/м² | Ясно",
        "Регулярне прибирання квартири в Дніпрі: щотижня або раз на два тижні зі знижкою до 15%. Постійний клінер, від 38 грн/м², оплата після прибирання.",
        "Підтримуюче прибирання", "Щоб вдома було чисто без витрачених вихідних. Постійний клінер, який знає вашу квартиру і ваші побажання.",
        """<h2>Що входить</h2><ul><li>вологе прибирання підлог і пилососіння килимів;</li><li>пил з поверхонь, техніки й підвіконь;</li><li>кухня: плита, мийка, стільниці, фасади ззовні;</li><li>санвузол: сантехніка, дзеркала, плитка біля ванни;</li><li>винести сміття і заправити ліжка.</li></ul>
<h2>Регулярність зі знижкою</h2><p>При прибиранні раз на два тижні знижка 10%, щотижня 15%. До вас приїжджає той самий клінер, а якщо він захворів, попереджаємо заздалегідь і пропонуємо заміну.</p>""",
        [("Чи можна змінити день прибирання?", "Так, попередьте за 24 години в месенджері, і ми перенесемо без доплат."),
         ("Як оплачувати регулярне прибирання?", "Після кожного прибирання карткою або готівкою, чи раз на місяць за рахунком.")], 38))
    out.append(area_page("rayony/sobornyi/", "Соборний район",
        "Клінінг у Соборному районі Дніпра: Нагірний, Тополя, Перемога",
        "Прибирання квартир у Соборному районі Дніпра: Нагірний, Тополя, Перемога. Виїзд за 30-40 хвилин, сталінки і новобудови, фіксована ціна.",
        "Прибирання квартир у Соборному районі",
        "Нагорка, Тополя, Перемога, Лоцманка: доїжджаємо за 30-40 хвилин. Знаємо специфіку і сталінок з високими стелями, і нових ЖК.",
        """<h2>Особливості району</h2><p>У сталінках Нагірного стелі 3-3,5 метра і великі дерев'яні вікна, тому беремо драбину і закладаємо більше часу на мийку вікон. На Тополі й Перемозі переважно панельні будинки, де головне завдання кухня і санвузол.</p>
<h2>Паркування і доступ</h2><p>У центрі Нагірного буває складно з паркуванням, тому клінери часто приїжджають громадським транспортом із засобами в сумках, а техніку завозить водій окремо. На ціну це не впливає.</p>"""))
    out.append(area_page("rayony/livyi-bereh/", "Лівий берег",
        "Клінінг на Лівому березі Дніпра: прибирання квартир | Ясно",
        "Прибирання квартир на Лівому березі Дніпра: Лівобережний, Березинка, Ломівка. Прибирання новобудов після ремонту, виїзд за 40-60 хвилин.",
        "Прибирання квартир на Лівому березі",
        "Лівобережний, Березинка, Ломівка, Східний: тут багато новобудов, тому найчастіше нас кличуть прибрати квартиру після ремонту перед заїздом.",
        """<h2>Новобудови і перший заїзд</h2><p>Після здачі ключів у нових ЖК на Лівобережному лишається бетонний пил у вентиляційних решітках, на підвіконнях і всередині шаф-купе. Прибираємо в три проходи, щоб пил не повертався.</p>
<h2>Як швидко приїдемо</h2><p>Через мости в години пік дорога займає до години, тому на Лівий берег плануємо виїзди на ранок або другу половину дня. Час підтверджуємо заздалегідь і попереджаємо, якщо затримуємось.</p>"""))
    out.append(contacts())
    return out


def area_page(path, name, title, desc, h1, lead, prose):
    prose += """<h2>Популярні послуги в районі</h2><ul class="link-list"><li><a href="{{root}}posluhy/heneralne-prybyrannia/">Генеральне прибирання</a></li><li><a href="{{root}}posluhy/pislia-remontu/">Прибирання після ремонту</a></li><li><a href="{{root}}posluhy/pidtrymuiuche/">Підтримуюче прибирання</a></li></ul>"""
    return inner(path, [("Райони", "#rayony"), (name, path)], title, desc, h1, lead, prose,
                 booking_form("Заявка: " + name), None,
                 [service_ld(cfg, "Прибирання квартир", desc, area=name + ", Дніпро", price=38)])


def contacts():
    b = cfg["business"]
    body = f"""
<section class="phero"><div class="wrap"><h1>Контакти і заявка на прибирання</h1><p class="lead">Залиште заявку або подзвоніть, менеджер перетелефонує протягом 10 хвилин.</p></div></section>
<div class="wrap book book--page">{booking_form()}
<div class="book__aside"><h2>Ясно Клінінг</h2>
<p><b>Офіс:</b> {b['street']}, Дніпро (прийом заявок, зустрічі за домовленістю)</p>
<p><b>Телефон:</b> <a href="tel:{b['phone']}">{b['phone_display']}</a></p>
<p><b>Пошта:</b> <a href="mailto:{b['email']}">{b['email']}</a></p>
<p><b>Працюємо:</b> щодня з 8:00 до 21:00</p>
<p class="muted small">Служба виїзна: клінери приїжджають до вас. Для бізнесу працюємо за договором з ФОП або ТОВ.</p></div></div>"""
    return {"path": "kontakty/", "title": "Контакти клінінгової служби в Дніпрі | Ясно Клінінг",
            "description": "Телефон, пошта і графік клінінгової служби «Ясно» в Дніпрі. Заявка на прибирання онлайн, зворотний дзвінок протягом 10 хвилин.",
            "body": body, "crumbs": [("Контакти", "kontakty/")]}


JS = r"""
(function(){
  var f=document.getElementById('clean-calc'); if(!f) return;
  var area=f.querySelector('#area'), range=f.querySelector('#area-r'), sum=document.getElementById('c-sum'), meta=document.getElementById('c-meta');
  function calc(){
    var a=Math.max(20,Math.min(500,+area.value||0)), t=f.querySelector('input[name=type]:checked'), p=a*(+t.dataset.p), extras=[];
    f.querySelectorAll('.extra input').forEach(function(i){
      if(i.type==='checkbox'&&i.checked){p+=+i.dataset.p;extras.push(i.closest('.extra').querySelector('.extra__n').firstChild.textContent);}
      if(i.type==='number'&&+i.value>0){p+=(+i.value)*(+i.dataset.p);extras.push(i.closest('.extra').querySelector('.extra__n').firstChild.textContent+' ×'+i.value);}
    });
    if(f.eco.checked) p*=1.1;
    p*=1-(+f.freq.value);
    p=Math.max(1500,Math.round(p/10)*10);
    var rate={support:16,general:6,renov:5}[t.value], team=Math.min(4,Math.max(1,Math.ceil(a/(t.value==='support'?70:35)))), hrs=Math.max(2,Math.round(a/rate/team*2)/2);
    sum.textContent=fmt(p);
    meta.textContent=team+' '+(team===1?'клінер':'клінери')+' · близько '+String(hrs).replace('.',',')+' год';
    try{sessionStorage.setItem('clean-calc',t.parentNode.querySelector('b').textContent+' прибирання, '+a+' м²'+(extras.length?', '+extras.join(', '):'')+'. Орієнтовно '+fmt(p)+' грн.');}catch(e){}
  }
  range.addEventListener('input',function(){area.value=range.value;calc();});
  area.addEventListener('input',function(){range.value=area.value;calc();});
  f.addEventListener('change',calc);
  f.querySelectorAll('[data-step]').forEach(function(b){b.addEventListener('click',function(){var i=b.parentNode.querySelector('input');i.value=Math.max(0,Math.min(30,(+i.value||0)+(+b.dataset.step)));calc();});});
  calc();
})();
(function(){ // tabs with arrow-key support
  var list=document.querySelector('[role=tablist]'); if(!list) return;
  var tabs=[].slice.call(list.querySelectorAll('[role=tab]'));
  function sel(t){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute('aria-controls')).hidden=!on;});t.focus();}
  tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t);});t.addEventListener('keydown',function(e){if(e.key==='ArrowRight')sel(tabs[(i+1)%tabs.length]);if(e.key==='ArrowLeft')sel(tabs[(i-1+tabs.length)%tabs.length]);});});
})();
(function(){var m=document.getElementById('f-msg');if(!m||location.hash!=='#zayavka')return;try{var v=sessionStorage.getItem('clean-calc');if(v)m.value=v;}catch(e){}})();
"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#0d6f65"/><path d="M20 8l2.6 7.4L30 18l-7.4 2.6L20 28l-2.6-7.4L10 18l7.4-2.6z" fill="#fff"/></svg>'

if __name__ == "__main__":
    build(cfg, pages(), layout, read(os.path.join(os.path.dirname(__file__), "cleaning_dnipro.css")), JS, FAVICON)
