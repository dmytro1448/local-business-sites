<?php
/**
 * Title: Заклик до запису
 * Slug: emal/cta
 * Categories: emal
 */
$b = emal_business();
?>
<!-- wp:group {"className":"emal-cta","layout":{"type":"constrained"}} -->
<div class="wp-block-group emal-cta"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Запишіться на консультацію за 300 ₴</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Огляд, знімок за потреби і письмовий план лікування з цінами. Сума зараховується в лікування.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися онлайн</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_attr( emal_tel() ); ?>"><?php echo esc_html( $b['phone_display'] ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
