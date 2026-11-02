<?php
/**
 * Title: Ціни коротко
 * Slug: emal/prices-short
 * Categories: emal
 */
$p    = emal_prices();
$rows = array( $p['Діагностика'][0], $p['Терапія'][0], $p['Терапія'][3], $p['Гігієна'][0], $p['Хірургія та імплантація'][3], $p['Ортопедія'][1] );
?>
<!-- wp:group {"align":"full","className":"emal-sec","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-sec"><!-- wp:columns {"className":"emal-split"} -->
<div class="wp-block-columns emal-split"><!-- wp:column {"width":"38%"} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:paragraph {"className":"emal-eyebrow"} -->
<p class="emal-eyebrow">Ціни</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Ціни відкриті, без «уточнюйте у адміністратора»</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Більшість пацієнтів шукають ціну ще до дзвінка. Тому показуємо основні позиції прямо тут, а повний прайс на окремій сторінці.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'tsiny/' ); ?>">Повний прайс</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><?php echo emal_price_table( $rows ); // phpcs:ignore ?></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
