<?php
/**
 * Title: Футер з NAP і графіком
 * Slug: emal/footer
 * Categories: footer
 * Block Types: core/template-part/footer
 * Inserter: no
 */
$b = emal_business();
?>
<!-- wp:group {"align":"full","className":"emal-footer","layout":{"type":"constrained","contentSize":"1200px"}} -->
<div class="wp-block-group alignfull emal-footer"><!-- wp:columns {"className":"emal-footer__cols"} -->
<div class="wp-block-columns emal-footer__cols"><!-- wp:column {"width":"36%"} -->
<div class="wp-block-column" style="flex-basis:36%"><!-- wp:paragraph {"className":"emal-footer__name"} -->
<p class="emal-footer__name"><?php echo esc_html( $b['name'] ); ?></p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><?php echo esc_html( $b['street'] . ', ' . $b['city'] ); ?><br><a href="<?php echo esc_attr( emal_tel() ); ?>"><?php echo esc_html( $b['phone_display'] ); ?></a><br><a href="mailto:<?php echo esc_attr( $b['email'] ); ?>"><?php echo esc_html( $b['email'] ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"emal-footer__h"} -->
<p class="emal-footer__h">Послуги</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><a href="<?php echo emal_url( 'poslugy/implantatsiia/' ); ?>">Імплантація</a><br><a href="<?php echo emal_url( 'poslugy/likuvannia-kariiesu/' ); ?>">Лікування карієсу</a><br><a href="<?php echo emal_url( 'poslugy/profesiina-hihiiena/' ); ?>">Професійна гігієна</a><br><a href="<?php echo emal_url( 'tsiny/' ); ?>">Ціни</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"emal-footer__h"} -->
<p class="emal-footer__h">Райони</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><a href="<?php echo emal_url( 'rayony/vystavka/' ); ?>">Виставка</a><br><a href="<?php echo emal_url( 'rayony/ozerna/' ); ?>">Озерна</a><br><a href="<?php echo emal_url( 'rayony/' ); ?>">Усі райони</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"emal-footer__h"} -->
<p class="emal-footer__h">Графік</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><?php foreach ( $b['hours_text'] as $d => $t ) { echo esc_html( $d . ': ' . $t ) . '<br>'; } ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- wp:paragraph {"className":"emal-footer__note"} -->
<p class="emal-footer__note">© <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php echo esc_html( $b['name'] ); ?>. Демо-концепт для портфоліо, бізнес вигаданий. Лікарі, телефон і контакти фіктивні. <a href="https://dmytro1448.github.io/local-business-sites/">Інші роботи</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
<!-- wp:html -->
<div class="emal-callbar"><a class="emal-callbar__call" href="<?php echo esc_attr( emal_tel() ); ?>">Подзвонити</a><a class="emal-callbar__book" href="<?php echo emal_url( 'kontakty/' ); ?>#zapys">Записатися</a></div>
<!-- /wp:html -->
