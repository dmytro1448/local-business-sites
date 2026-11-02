<?php
/**
 * Title: Сторінка: Імплантація
 * Slug: emal/page-implantatsiia
 * Categories: emal-pages
 * Inserter: no
 */
?>
<!-- wp:columns {"className":"emal-article"} -->
<div class="wp-block-columns emal-article"><!-- wp:column {"width":"62%","className":"emal-prose"} -->
<div class="wp-block-column emal-prose" style="flex-basis:62%">
<!-- wp:heading -->
<h2 class="wp-block-heading">Як проходить імплантація</h2>
<!-- /wp:heading -->
<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Консультація хірурга і КТ в день звернення, план з ціною і строками.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Встановлення імпланта під місцевою анестезією, 30-60 хвилин.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Приживлення 3-4 місяці. Тимчасова коронка, якщо зуб у зоні посмішки.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Сканування і фіксація постійної коронки з цирконію або металокераміки.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Скільки коштує</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Імплант з установкою від 15 000 гривень, під ключ з коронкою від 24 000 гривень. Ціна залежить від системи імпланта і потреби в нарощуванні кістки. Усе це видно на КТ ще до початку лікування, тому сума в плані не змінюється.</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Гарантія</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>На імпланти гарантія виробника довічна, на роботу хірурга і коронку 5 років за умови контрольних оглядів раз на рік.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column {"className":"emal-aside"} -->
<div class="wp-block-column emal-aside"><!-- wp:group {"className":"emal-card emal-card--sticky","layout":{"type":"default"}} -->
<div class="wp-block-group emal-card emal-card--sticky"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Ціни</h3>
<!-- /wp:heading -->
<?php echo emal_price_table( emal_prices()['Хірургія та імплантація'] ); // phpcs:ignore ?>
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"width":100} -->
<div class="wp-block-button has-custom-width wp-block-button__width-100"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- wp:group {"className":"emal-faq-wrap","layout":{"type":"constrained","contentSize":"820px"}} -->
<div class="wp-block-group emal-faq-wrap"><?php echo emal_faq_blocks( 'implantatsiia' ); // phpcs:ignore ?></div>
<!-- /wp:group -->
<!-- wp:pattern {"slug":"emal/cta"} /-->
