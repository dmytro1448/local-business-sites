<?php
/**
 * Title: Лікарі
 * Slug: emal/doctors
 * Categories: emal
 */
$docs = array(
	array( 'ІТ', '#1d6b64', 'Ірина Ткачук', 'Головна лікарка, терапевт-ендодонтист', 'Стаж 14 років. Лікування каналів під мікроскопом, складні реставрації.' ),
	array( 'АС', '#e2725b', 'Андрій Савчук', 'Хірург-імплантолог', 'Стаж 11 років. Імплантація, синус-ліфтинг, видалення зубів мудрості.' ),
	array( 'МК', '#7b9e87', 'Марта Ковальчук', 'Ортодонт', 'Стаж 8 років. Брекети й елайнери для підлітків і дорослих.' ),
	array( 'ОГ', '#134a45', 'Олег Гнатюк', 'Ортопед', 'Стаж 16 років. Коронки, вініри, протезування на імплантах.' ),
);
?>
<!-- wp:group {"align":"full","className":"emal-sec emal-sec--mint","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-sec emal-sec--mint"><!-- wp:paragraph {"className":"emal-eyebrow"} -->
<p class="emal-eyebrow">Команда</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Лікарі, до яких можна записатися напряму</h2>
<!-- /wp:heading -->
<!-- wp:columns {"className":"emal-docs"} -->
<div class="wp-block-columns emal-docs">
<?php foreach ( $docs as $d ) : ?>
<!-- wp:column {"className":"emal-doc"} -->
<div class="wp-block-column emal-doc"><!-- wp:html -->
<svg class="emal-doc__ava" viewBox="0 0 120 120" role="img" aria-label="Аватар: <?php echo esc_attr( $d[2] ); ?>"><rect width="120" height="120" rx="60" fill="<?php echo esc_attr( $d[1] ); ?>"/><text x="60" y="72" text-anchor="middle" font-family="Lora, serif" font-size="38" font-weight="600" fill="#fff"><?php echo esc_html( $d[0] ); ?></text></svg>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading"><?php echo esc_html( $d[2] ); ?></h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"emal-doc__role"} -->
<p class="emal-doc__role"><?php echo esc_html( $d[3] ); ?></p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><?php echo esc_html( $d[4] ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<?php endforeach; ?>
</div>
<!-- /wp:columns -->
<!-- wp:paragraph {"className":"emal-small"} -->
<p class="emal-small">Лікарі вигадані для демо-сайту. На реальному сайті тут фото команди і посилання на сертифікати.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
