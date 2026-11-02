"""Інлайн SVG-ілюстрації кімнат «до/після» для сайту ремонту (без фото, легкі)."""


def _frame(inner, label, uid):
    return (f'<svg viewBox="0 0 800 500" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid slice">'
            f'<defs><clipPath id="c{uid}"><rect width="800" height="500"/></clipPath></defs><g clip-path="url(#c{uid})">{inner}</g></svg>')


def before(kind, uid):
    wall = "#b8b3aa"
    s = [f'<rect width="800" height="500" fill="{wall}"/>',
         '<g stroke="#a39e95" stroke-width="2" opacity=".7"><path d="M60 80 l40 30 l-20 40"/><path d="M620 60 l-30 50 l25 30"/><path d="M380 200 l20 25"/></g>',
         '<rect x="0" y="380" width="800" height="120" fill="#8d877d"/>',
         '<g fill="#7f796f">' + "".join(f'<circle cx="{x}" cy="{y}" r="3"/>' for x, y in [(80, 420), (210, 450), (330, 410), (520, 470), (660, 430), (740, 465)]) + '</g>']
    if kind == "bath":
        s.append('<g opacity=".85">' + "".join(
            f'<rect x="{x}" y="{y}" width="58" height="38" fill="#d9d4c8" stroke="#a8a294"/>'
            for x in range(40, 340, 60) for y in range(200, 380, 40) if (x * y) % 7 != 0) + '</g>')
        s.append('<rect x="430" y="280" width="300" height="100" rx="10" fill="#e8e3d8" stroke="#a8a294" stroke-width="3"/><path d="M450 300h260" stroke="#c9c2b2" stroke-width="6"/>')
        s.append('<path d="M560 120v80" stroke="#6b665e" stroke-width="6"/><circle cx="560" cy="210" r="14" fill="#6b665e"/>')
    else:
        s.append('<rect x="470" y="90" width="220" height="200" fill="#d6dde2" stroke="#7d786f" stroke-width="10"/><path d="M580 90v200M470 190h220" stroke="#7d786f" stroke-width="8"/>')
        s.append('<path d="M150 0 C150 60 170 90 140 140" stroke="#333" stroke-width="4" fill="none"/><path d="M300 0 C300 40 280 70 310 110" stroke="#c0392b" stroke-width="4" fill="none"/>')
        s.append('<g transform="translate(110 300)"><path d="M0 0h60l-8 80h-44z" fill="#5d7380"/><ellipse cx="30" cy="0" rx="30" ry="7" fill="#4a5d68"/></g>')
        s.append('<g stroke="#9c7b52" stroke-width="10" stroke-linecap="round"><path d="M300 380 L360 170"/><path d="M400 380 L360 170"/></g><g stroke="#9c7b52" stroke-width="6"><path d="M320 310h64M330 250h50"/></g>')
    s.append('<rect x="0" y="0" width="800" height="500" fill="#3b3730" opacity=".12"/>')
    return _frame("".join(s), "До ремонту: голі стіни, стара оздоба, дроти", uid)


def after(kind, uid, wall="#e9e1d4", accent="#b5532d", floor="#c9a47c"):
    planks = "".join(f'<path d="M{x} 380 L{x - 60 + x // 10} 500" stroke="#b08a62" stroke-width="2"/>' for x in range(0, 900, 80))
    s = [f'<rect width="800" height="500" fill="{wall}"/>', f'<rect x="0" y="380" width="800" height="120" fill="{floor}"/>', planks,
         '<rect x="0" y="372" width="800" height="10" fill="#fff" opacity=".7"/>']
    if kind == "bath":
        s.append('<rect width="800" height="380" fill="#eef1f0"/>')
        s.append('<g stroke="#d5dbd9" stroke-width="2">' + "".join(f'<path d="M0 {y}H800"/>' for y in range(60, 380, 60)) + "".join(f'<path d="M{x} 0V380"/>' for x in range(120, 800, 120)) + '</g>')
        s.append('<rect x="0" y="380" width="800" height="120" fill="#5f6b6a"/>')
        s.append('<rect x="420" y="250" width="330" height="130" rx="40" fill="#fff" stroke="#c9d1cf" stroke-width="3"/>')
        s.append(f'<rect x="90" y="90" width="170" height="210" rx="85" fill="#dfe8ea" stroke="{accent}" stroke-width="6"/>')
        s.append(f'<rect x="80" y="300" width="190" height="80" rx="6" fill="{accent}"/><rect x="140" y="292" width="70" height="14" rx="7" fill="#fff"/>')
        s.append('<path d="M700 120v100" stroke="#333" stroke-width="5"/><path d="M680 120h40" stroke="#333" stroke-width="5"/>')
        s.append('<g transform="translate(330 300)"><rect x="0" y="0" width="40" height="80" rx="4" fill="#fff" stroke="#c9d1cf"/><path d="M20 0 C0 -40 40 -60 20 -90" stroke="#4f7a52" stroke-width="10" fill="none" stroke-linecap="round"/></g>')
    elif kind == "bedroom":
        s.append('<rect x="80" y="90" width="200" height="140" fill="#f7f3ec" stroke="#2b2925" stroke-width="6"/><path d="M100 200 L160 140 L200 180 L230 150 L260 200z" fill="#8aa29e"/>')
        s.append(f'<rect x="300" y="230" width="380" height="150" rx="10" fill="#f7f3ec"/><rect x="300" y="170" width="380" height="80" rx="16" fill="{accent}"/>')
        s.append('<rect x="330" y="215" width="120" height="40" rx="18" fill="#fff"/><rect x="530" y="215" width="120" height="40" rx="18" fill="#fff"/>')
        s.append('<rect x="300" y="300" width="380" height="80" fill="#d9cdb9"/>')
        s.append('<rect x="700" y="300" width="70" height="80" fill="#8b6b4a"/><path d="M735 300v-60" stroke="#2b2925" stroke-width="4"/><path d="M710 240h50l-10-40h-30z" fill="#f2d49b"/>')
    else:
        s.append('<rect x="480" y="70" width="240" height="230" fill="#dbe9f1" stroke="#fff" stroke-width="12"/><path d="M600 70v230" stroke="#fff" stroke-width="8"/>')
        s.append('<rect x="470" y="300" width="260" height="10" fill="#fff"/>')
        s.append(f'<g transform="translate(70 230)"><rect x="0" y="40" width="340" height="100" rx="24" fill="{accent}"/><rect x="20" y="0" width="300" height="70" rx="22" fill="{accent}" opacity=".85"/><rect x="20" y="140" width="12" height="18" fill="#2b2925"/><rect x="310" y="140" width="12" height="18" fill="#2b2925"/></g>')
        s.append('<rect x="120" y="80" width="140" height="110" fill="#f7f3ec" stroke="#2b2925" stroke-width="5"/><circle cx="190" cy="135" r="30" fill="#e3b26b"/>')
        s.append('<ellipse cx="240" cy="440" rx="220" ry="30" fill="#e6d8c3" opacity=".8"/>')
        s.append('<g transform="translate(700 320)"><path d="M-20 60h40l-6-60h-28z" fill="#2b2925"/><g fill="#5d8a5f"><ellipse cx="0" cy="-20" rx="18" ry="40"/><ellipse cx="-24" cy="-6" rx="12" ry="34" transform="rotate(-25)"/><ellipse cx="24" cy="-6" rx="12" ry="34" transform="rotate(25)"/></g></g>')
        s.append('<path d="M420 0v120" stroke="#2b2925" stroke-width="3"/><path d="M395 120h50l-8 30h-34z" fill="#2b2925"/><ellipse cx="420" cy="160" rx="60" ry="14" fill="#fff3cf" opacity=".6"/>')
    return _frame("".join(s), "Після ремонту: готовий інтер'єр", uid)


def compare(kind, uid, **kw):
    return f"""<div class="ba" data-ba>
  <div class="ba__img ba__after">{after(kind, uid + 'a', **kw)}</div>
  <div class="ba__img ba__before">{before(kind, uid + 'b')}</div>
  <span class="ba__tag ba__tag--l">До</span><span class="ba__tag ba__tag--r">Після</span>
  <span class="ba__line" aria-hidden="true"></span>
  <input class="ba__range" type="range" min="0" max="100" value="50" aria-label="Порівняти до і після: посуньте повзунок">
</div>"""
