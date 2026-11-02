<?php
/**
 * Title: Сторінка: Головна
 * Slug: emal/page-home
 * Categories: emal-pages
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"emal/hero"} /-->
<!-- wp:pattern {"slug":"emal/trust"} /-->
<!-- wp:pattern {"slug":"emal/services"} /-->
<!-- wp:pattern {"slug":"emal/doctors"} /-->
<!-- wp:pattern {"slug":"emal/prices-short"} /-->
<!-- wp:group {"align":"full","className":"emal-sec emal-sec--faq","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull emal-sec emal-sec--faq"><?php echo emal_faq_blocks( 'home' ); // phpcs:ignore ?></div>
<!-- /wp:group -->
<!-- wp:pattern {"slug":"emal/booking"} /-->
