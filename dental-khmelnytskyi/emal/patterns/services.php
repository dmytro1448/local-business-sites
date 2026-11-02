<?php
/**
 * Title: Послуги (картки)
 * Slug: emal/services
 * Categories: emal
 */
$items = array(
	array( 'poslugy/implantatsiia/', 'Імплантація', 'Відновлення зуба під ключ: КТ, імплант, коронка. Хірург з досвідом понад 1 500 імплантацій.', 'від 24 000 ₴' ),
	array( 'poslugy/likuvannia-kariiesu/', 'Лікування карієсу', 'Пломби, які не видно. Лікування каналів під мікроскопом за 1-2 візити.', 'від 1 300 ₴' ),
	array( 'poslugy/profesiina-hihiiena/', 'Професійна гігієна', 'Ультразвук, Air Flow, полірування і фторування за 60 хвилин.', 'від 1 600 ₴' ),
);
?>
<!-- wp:group {"align":"full","className":"emal-sec","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-sec"><!-- wp:paragraph {"className":"emal-eyebrow"} -->
<p class="emal-eyebrow">Послуги</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">З чим до нас приходять найчастіше</h2>
<!-- /wp:heading -->
<!-- wp:columns {"className":"emal-cards"} -->
<div class="wp-block-columns emal-cards">
<?php foreach ( $items as $it ) : ?>
<!-- wp:column {"className":"emal-card"} -->
<div class="wp-block-column emal-card"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading"><a href="<?php echo emal_url( $it[0] ); ?>"><?php echo esc_html( $it[1] ); ?></a></h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p><?php echo esc_html( $it[2] ); ?></p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"emal-card__price"} -->
<p class="emal-card__price"><?php echo esc_html( $it[3] ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<?php endforeach; ?>
</div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
