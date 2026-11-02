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
