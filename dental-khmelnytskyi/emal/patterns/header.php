<?php
/**
 * Title: Шапка сайту
 * Slug: emal/header
 * Categories: header
 * Block Types: core/template-part/header
 * Inserter: no
 */
$b = emal_business();
?>
<!-- wp:html -->
<a class="emal-skip" href="#main">Перейти до змісту</a>
<!-- /wp:html -->
<!-- wp:group {"align":"full","className":"emal-header","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-header"><!-- wp:group {"className":"emal-header__in","layout":{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between"}} -->
<div class="wp-block-group emal-header__in"><!-- wp:html -->
<a class="emal-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" aria-label="<?php echo esc_attr( $b['name'] ); ?>: на головну"><svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true"><circle cx="20" cy="20" r="20" fill="#1d6b64"/><path d="M20 11.5c-1.6-1.3-3-1.8-4.8-1.8-3.7 0-6.2 2.6-6.2 7 0 3.6 1.6 6 2.2 10 .5 3.3 1.1 6.8 3 6.8 2 0 2-5.3 4.3-5.3h3c2.3 0 2.3 5.3 4.3 5.3 1.9 0 2.5-3.5 3-6.8.6-4 2.2-6.4 2.2-10 0-4.4-2.5-7-6.2-7-1.8 0-3.2.5-4.8 1.8z" fill="#fff"/></svg><span>Емаль<small>стоматологія · Хмельницький</small></span></a>
<!-- /wp:html -->
<!-- wp:navigation {"overlayMenu":"mobile","className":"emal-nav","layout":{"type":"flex","justifyContent":"right"}} /-->
<!-- wp:buttons {"className":"emal-header__cta"} -->
<div class="wp-block-buttons emal-header__cta"><!-- wp:button {"className":"emal-btn-call"} -->
<div class="wp-block-button emal-btn-call"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_attr( emal_tel() ); ?>"><?php echo esc_html( $b['phone_display'] ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
