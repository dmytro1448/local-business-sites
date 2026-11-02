<?php
/**
 * Title: Головний екран клініки
 * Slug: emal/hero
 * Categories: emal
 */
$b = emal_business();
?>
<!-- wp:group {"align":"full","className":"emal-hero","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-hero"><!-- wp:columns {"verticalAlignment":"center","className":"emal-hero__cols"} -->
<div class="wp-block-columns are-vertically-aligned-center emal-hero__cols"><!-- wp:column {"verticalAlignment":"center","width":"56%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:56%"><!-- wp:paragraph {"className":"emal-eyebrow"} -->
<p class="emal-eyebrow">Хмельницький · центр · Пн-Сб</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Стоматологія у Хмельницькому, де лікують без болю і без сюрпризів у ціні</h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"emal-lead"} -->
<p class="emal-lead">План лікування з цінами ще до першого свердління. Сучасна анестезія, мікроскоп і гарантія до 5 років на роботи.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися на консультацію</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_attr( emal_tel() ); ?>"><?php echo esc_html( $b['phone_display'] ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->
<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:html -->
<div class="emal-hero__art" role="img" aria-label="Ілюстрація: здоровий зуб і графік прийому">
<svg viewBox="0 0 420 380" aria-hidden="true"><circle cx="210" cy="190" r="170" fill="#dcefe9"/><circle cx="330" cy="70" r="34" fill="#f6d4ca"/>
<path d="M210 92c-14-11-27-16-42-16-33 0-55 23-55 62 0 32 14 54 20 90 4 30 10 61 27 61 18 0 18-48 38-48h24c20 0 20 48 38 48 17 0 23-31 27-61 6-36 20-58 20-90 0-39-22-62-55-62-15 0-28 5-42 16z" fill="#fff" stroke="#1d6b64" stroke-width="6"/>
<path d="M165 120c8-14 22-20 36-18" stroke="#9fd2c6" stroke-width="10" stroke-linecap="round" fill="none"/>
<path d="M318 210l6 16 16 6-16 6-6 16-6-16-16-6 16-6z" fill="#e2725b"/></svg>
<p class="emal-chip emal-chip--a"><b>до 5 років</b> гарантія</p>
<p class="emal-chip emal-chip--b"><b>300 ₴</b> консультація і план</p>
</div>
<!-- /wp:html --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
