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
