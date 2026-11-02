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
