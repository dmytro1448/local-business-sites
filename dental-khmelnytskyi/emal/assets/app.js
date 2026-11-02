/* Демо-форма запису: перевірка полів і повідомлення про успіх. Нікуди не надсилає дані. */
(function () {
  document.querySelectorAll('form.emal-form[data-demo]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = null;
      form.querySelectorAll('[required]').forEach(function (el) {
        var ok = el.type === 'checkbox' ? el.checked : el.value.trim() !== '';
        if (ok && el.type === 'tel') ok = el.value.replace(/\D/g, '').length >= 10;
        el.parentElement.classList.toggle('is-invalid', !ok);
        el.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok && !bad) bad = el;
      });
      if (bad) { bad.focus(); return; }
      var name = form.querySelector('[name="name"]').value.trim().split(' ')[0].replace(/[<>&]/g, '');
      var msg = form.querySelector('.emal-ok');
      msg.textContent = msg.textContent.replace('{name}', name);
      form.classList.add('is-sent');
      msg.focus();
    });
    form.addEventListener('input', function (e) {
      var p = e.target.parentElement;
      if (p.classList.contains('is-invalid')) { p.classList.remove('is-invalid'); e.target.setAttribute('aria-invalid', 'false'); }
    });
  });
  document.querySelectorAll('input[type="date"][data-min-today]').forEach(function (el) {
    var d = new Date(); el.min = d.toISOString().slice(0, 10);
    d.setDate(d.getDate() + 1); if (!el.value) el.value = d.toISOString().slice(0, 10);
  });
})();
