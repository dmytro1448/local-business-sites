<?php
/**
 * Title: Онлайн-запис і контакти
 * Slug: emal/booking
 * Categories: emal
 */
$b = emal_business();
?>
<!-- wp:group {"align":"full","className":"emal-sec emal-sec--deep","anchor":"zapys","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div id="zapys" class="wp-block-group alignfull emal-sec emal-sec--deep"><!-- wp:columns {"className":"emal-split"} -->
<div class="wp-block-columns emal-split"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:heading -->
<h2 class="wp-block-heading">Запис на прийом</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Оберіть послугу і зручний день. Адміністратор передзвонить протягом 15 хвилин у робочий час і підтвердить точний час візиту.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"emal-nap"} -->
<p class="emal-nap"><strong>Адреса:</strong> <?php echo esc_html( $b['street'] . ', ' . $b['city'] ); ?>, 2 поверх<br><strong>Телефон:</strong> <a href="<?php echo esc_attr( emal_tel() ); ?>"><?php echo esc_html( $b['phone_display'] ); ?></a><br><strong>Графік:</strong> Пн-Пт 9:00-20:00, Сб 9:00-15:00</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:html -->
<form class="emal-form" data-demo novalidate aria-label="Форма запису на прийом">
<div class="emal-form__body">
<div class="emal-row"><p class="emal-field"><label for="z-name">Ім'я</label><input id="z-name" name="name" autocomplete="given-name" required><span class="emal-err">Вкажіть ім'я</span></p>
<p class="emal-field"><label for="z-tel">Телефон</label><input id="z-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+380" required><span class="emal-err">Перевірте номер</span></p></div>
<div class="emal-row"><p class="emal-field"><label for="z-svc">Послуга</label><select id="z-svc" name="service"><option>Консультація</option><option>Лікування карієсу</option><option>Професійна гігієна</option><option>Імплантація</option><option>Гострий біль</option></select></p>
<p class="emal-field"><label for="z-doc">Лікар</label><select id="z-doc" name="doctor"><option>Будь-який вільний</option><option>Ірина Ткачук</option><option>Андрій Савчук</option><option>Марта Ковальчук</option><option>Олег Гнатюк</option></select></p></div>
<div class="emal-row"><p class="emal-field"><label for="z-date">Бажана дата</label><input id="z-date" name="date" type="date" data-min-today></p>
<p class="emal-field"><label for="z-time">Час</label><select id="z-time" name="time"><option>Ранок (9-12)</option><option>День (12-16)</option><option>Вечір (16-20)</option></select></p></div>
<p class="emal-check"><input id="z-ok" type="checkbox" name="agree" required><label for="z-ok">Погоджуюсь на обробку даних для зворотного дзвінка</label></p>
<button type="submit" class="emal-submit">Записатися</button>
</div>
<p class="emal-ok" role="status" tabindex="-1">Дякуємо, {name}! Заявку прийнято. Це демо-сайт, тому вона нікуди не надсилається. На робочому сайті заявка потрапляє адміністратору в CRM і Telegram.</p>
</form>
<!-- /wp:html --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
