<?php
/**
 * Title: Сторінка: Лікування карієсу
 * Slug: emal/page-kariies
 * Categories: emal-pages
 * Inserter: no
 */
?>
<!-- wp:columns {"className":"emal-article"} -->
<div class="wp-block-columns emal-article"><!-- wp:column {"width":"62%","className":"emal-prose"} -->
<div class="wp-block-column emal-prose" style="flex-basis:62%">
<!-- wp:heading -->
<h2 class="wp-block-heading">Лікуємо без болю</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Перед уколом наносимо аплікаційний анестетик, а сам укол робимо тонкою голкою зі швидкістю, яка не викликає дискомфорту. Якщо вам страшно, скажіть про це адміністратору: запишемо на довший прийом з перервами.</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Як ставимо пломбу</h2>
<!-- /wp:heading -->
<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Ізолюємо зуб кофердамом, щоб пломба трималась довше.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Видаляємо уражені тканини під збільшенням.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Відновлюємо форму шарами фотополімеру під колір вашої емалі.</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Шліфуємо і перевіряємо прикус.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Коли потрібне лікування каналів</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Якщо болить уночі чи від гарячого, карієс дійшов до нерва. Тоді лікуємо канали під мікроскопом за 1-2 візити і закриваємо зуб реставрацією або коронкою.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column {"className":"emal-aside"} -->
<div class="wp-block-column emal-aside"><!-- wp:group {"className":"emal-card emal-card--sticky","layout":{"type":"default"}} -->
<div class="wp-block-group emal-card emal-card--sticky"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Ціни</h3>
<!-- /wp:heading -->
<?php echo emal_price_table( emal_prices()['Терапія'] ); // phpcs:ignore ?>
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"width":100} -->
<div class="wp-block-button has-custom-width wp-block-button__width-100"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- wp:group {"className":"emal-faq-wrap","layout":{"type":"constrained","contentSize":"820px"}} -->
<div class="wp-block-group emal-faq-wrap"><?php echo emal_faq_blocks( 'kariies' ); // phpcs:ignore ?></div>
<!-- /wp:group -->
<!-- wp:pattern {"slug":"emal/cta"} /-->
