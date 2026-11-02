<?php
/**
 * Title: Прайс повний
 * Slug: emal/prices
 * Categories: emal
 */
?>
<!-- wp:group {"align":"full","className":"emal-sec","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-sec"><!-- wp:group {"className":"emal-prices","layout":{"type":"default"}} -->
<div class="wp-block-group emal-prices">
<?php foreach ( emal_prices() as $cat => $rows ) : ?>
<!-- wp:group {"className":"emal-pricecat","layout":{"type":"default"}} -->
<div class="wp-block-group emal-pricecat"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading"><?php echo esc_html( $cat ); ?></h3>
<!-- /wp:heading -->
<?php echo emal_price_table( $rows ); // phpcs:ignore ?>
</div>
<!-- /wp:group -->
<?php endforeach; ?>
</div>
<!-- /wp:group -->
<!-- wp:paragraph {"className":"emal-small"} -->
<p class="emal-small">Ціни вказані «від» і залежать від клінічної ситуації. Точну суму лікар фіксує в плані лікування до початку робіт.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
