<?php
/**
 * Емаль: блокова тема для стоматологічної клініки.
 * Без конструкторів і важких плагінів: стилі з theme.json, кілька патернів, базове локальне SEO.
 */
defined( 'ABSPATH' ) || exit;

require_once __DIR__ . '/inc/data.php';
require_once __DIR__ . '/inc/seo.php';
require_once __DIR__ . '/inc/demo-setup.php';

add_action( 'after_setup_theme', function () {
	add_theme_support( 'editor-styles' );
	add_editor_style( 'assets/theme.css' );
	add_post_type_support( 'page', 'excerpt' );
} );

add_action( 'wp_enqueue_scripts', function () {
	$ver = wp_get_theme()->get( 'Version' );
	wp_enqueue_style( 'emal', get_theme_file_uri( 'assets/theme.css' ), array(), $ver );
	wp_enqueue_script( 'emal', get_theme_file_uri( 'assets/app.js' ), array(), $ver, array( 'strategy' => 'defer', 'in_footer' => true ) );
} );

// Шрифти локальні: підвантажуємо кириличний файл заголовків раніше, щоб не було стрибка макета.
add_action( 'wp_head', function () {
	printf( '<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n", esc_url( get_theme_file_uri( 'assets/fonts/onest-cyrillic.woff2' ) ) );
}, 1 );

add_action( 'init', function () {
	register_block_pattern_category( 'emal', array( 'label' => 'Емаль: стоматологія' ) );
	register_block_pattern_category( 'emal-pages', array( 'label' => 'Емаль: сторінки' ) );
} );

// Мова сторінки українська навіть без встановленого мовного пакета.
add_filter( 'language_attributes', function ( $output ) {
	return preg_replace( '/lang="[^"]*"/', 'lang="uk"', $output );
} );

/** Хлібні крихти: [emal_breadcrumbs] у шаблоні сторінки. */
add_shortcode( 'emal_breadcrumbs', function () {
	$items = emal_breadcrumb_items();
	if ( count( $items ) < 2 ) {
		return '';
	}
	$html = '<nav class="emal-crumbs" aria-label="Хлібні крихти"><ol>';
	$last = count( $items ) - 1;
	foreach ( $items as $i => $item ) {
		$html .= $i === $last
			? '<li><span aria-current="page">' . esc_html( $item[0] ) . '</span></li>'
			: '<li><a href="' . esc_url( $item[1] ) . '">' . esc_html( $item[0] ) . '</a></li>';
	}
	return $html . '</ol></nav>';
} );

function emal_breadcrumb_items() {
	$items = array( array( 'Головна', home_url( '/' ) ) );
	if ( is_page() && ! is_front_page() ) {
		$post = get_queried_object();
		foreach ( array_reverse( get_post_ancestors( $post ) ) as $id ) {
			$items[] = array( get_the_title( $id ), get_permalink( $id ) );
		}
		$items[] = array( get_the_title( $post ), get_permalink( $post ) );
	}
	return $items;
}
