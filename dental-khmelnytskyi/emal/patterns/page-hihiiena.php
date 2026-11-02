<?php
/**
 * Title: Сторінка: Професійна гігієна
 * Slug: emal/page-hihiiena
 * Categories: emal-pages
 * Inserter: no
 */
?>
<!-- wp:columns {"className":"emal-article"} -->
<div class="wp-block-columns emal-article"><!-- wp:column {"width":"62%","className":"emal-prose"} -->
<div class="wp-block-column emal-prose" style="flex-basis:62%">
<!-- wp:heading -->
<h2 class="wp-block-heading">Що входить у чистку</h2>
<!-- /wp:heading -->
<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Ультразвукове зняття зубного каменю, в тому числі під яснами.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Air Flow: видалення нальоту від кави, чаю і цигарок.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Полірування пастами, щоб наліт не накопичувався швидко.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Фторування і рекомендації щодо щітки та нитки.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Навіщо це робити</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Зубний камінь не прибирається щіткою і з часом призводить до кровоточивості ясен і запаху з рота. Чистка раз на пів року дешевша і приємніша, ніж лікування пародонтиту.</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Чи боляче</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Зазвичай ні. Якщо ясна чутливі, використовуємо аплікаційну анестезію або гель.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column {"className":"emal-aside"} -->
<div class="wp-block-column emal-aside"><!-- wp:group {"className":"emal-card emal-card--sticky","layout":{"type":"default"}} -->
<div class="wp-block-group emal-card emal-card--sticky"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Ціни</h3>
<!-- /wp:heading -->
<?php echo emal_price_table( emal_prices()['Гігієна'] ); // phpcs:ignore ?>
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"width":100} -->
<div class="wp-block-button has-custom-width wp-block-button__width-100"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- wp:group {"className":"emal-faq-wrap","layout":{"type":"constrained","contentSize":"820px"}} -->
<div class="wp-block-group emal-faq-wrap"><?php echo emal_faq_blocks( 'hihiiena' ); // phpcs:ignore ?></div>
<!-- /wp:group -->
<!-- wp:pattern {"slug":"emal/cta"} /-->
