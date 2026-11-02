/* shared: mobile menu, demo forms, number format */
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    var close = function () { nav.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); };
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('is-open')) { close(); btn.focus(); } });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
  }

  // Demo forms: validate on the client and show a success state. Nothing is sent anywhere.
  document.querySelectorAll('form[data-demo]').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      form.querySelectorAll('[required]').forEach(function (el) {
        var field = el.closest('.field') || el.parentElement;
        var ok = el.type === 'checkbox' ? el.checked : el.value.trim() !== '';
        if (ok && el.type === 'tel') ok = el.value.replace(/\D/g, '').length >= 10;
        field.classList.toggle('is-invalid', !ok);
        el.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok && !firstBad) firstBad = el;
      });
      if (firstBad) { firstBad.focus(); return; }
      var name = form.querySelector('[name="name"]');
      var msg = form.querySelector('.form-ok');
      if (msg && name && name.value.trim()) {
        msg.innerHTML = msg.innerHTML.replace('{name}', name.value.trim().split(' ')[0].replace(/[<>&]/g, ''));
      }
      form.classList.add('is-sent');
      if (msg) { msg.setAttribute('tabindex', '-1'); msg.focus(); }
    });
    form.addEventListener('input', function (e) {
      var f = e.target.closest('.field');
      if (f && f.classList.contains('is-invalid')) { f.classList.remove('is-invalid'); e.target.setAttribute('aria-invalid', 'false'); }
    });
  });

  // Prefill a date input with tomorrow and block past dates
  document.querySelectorAll('input[type="date"][data-min-today]').forEach(function (el) {
    var d = new Date(); d.setDate(d.getDate() + 1);
    var iso = d.toISOString().slice(0, 10);
    el.min = new Date().toISOString().slice(0, 10);
    if (!el.value) el.value = iso;
  });
})();
function fmt(n) { return Math.round(n).toLocaleString('uk-UA').replace(/,/g, ' '); }


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
