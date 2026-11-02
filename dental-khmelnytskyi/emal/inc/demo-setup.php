<?php
/**
 * Демо-наповнення: створює сторінки з патернів, головну, меню і ЧПУ.
 * Запускається при активації теми і з blueprint.json у WordPress Playground.
 * Повторний запуск безпечний: існуючі сторінки не дублюються.
 */
defined( 'ABSPATH' ) || exit;

function emal_demo_setup() {
	update_option( 'permalink_structure', '/%postname%/' );
	update_option( 'blogname', emal_business()['name'] );
	update_option( 'blogdescription', 'Стоматологія у центрі Хмельницького' );

	$ids = array();
	foreach ( emal_pages() as $slug => $p ) {
		$parent   = isset( $p['parent'] ) ? ( $ids[ $p['parent'] ] ?? 0 ) : 0;
		$existing = get_page_by_path( $parent ? get_post_field( 'post_name', $parent ) . '/' . $slug : $slug );
		$data     = array(
			'post_type'    => 'page',
			'post_status'  => 'publish',
			'post_title'   => $p['title'],
			'post_name'    => $slug,
			'post_parent'  => $parent,
			'menu_order'   => $p['order'],
			'post_excerpt' => $p['desc'],
			'post_content' => '<!-- wp:pattern {"slug":"emal/' . $p['pattern'] . '"} /-->',
		);
		if ( $existing ) {
			$data['ID'] = $existing->ID;
			$ids[ $slug ] = wp_update_post( $data );
		} else {
			$ids[ $slug ] = wp_insert_post( $data );
		}
		if ( 'holovna' === $slug ) {
			update_post_meta( $ids[ $slug ], '_wp_page_template', 'page-wide' );
		}
	}

	update_option( 'show_on_front', 'page' );
	update_option( 'page_on_front', $ids['holovna'] );

	// Меню шапки: навігаційний блок без ref бере найновіше меню wp_navigation.
	$links = array(
		array( 'Послуги', 'poslugy' ),
		array( 'Лікарі', 'likari' ),
		array( 'Ціни', 'tsiny' ),
		array( 'Райони', 'rayony' ),
		array( 'Контакти', 'kontakty' ),
	);
	$content = '';
	foreach ( $links as $l ) {
		$content .= '<!-- wp:navigation-link {"label":"' . $l[0] . '","type":"page","id":' . (int) $ids[ $l[1] ] . ',"url":"' . esc_url( get_permalink( $ids[ $l[1] ] ) ) . '","kind":"post-type"} /-->';
	}
	$nav = get_posts( array( 'post_type' => 'wp_navigation', 'title' => 'Меню Емаль', 'post_status' => 'publish', 'numberposts' => 1 ) );
	$nav_data = array( 'post_type' => 'wp_navigation', 'post_status' => 'publish', 'post_title' => 'Меню Емаль', 'post_content' => $content );
	if ( $nav ) {
		$nav_data['ID'] = $nav[0]->ID;
		wp_update_post( $nav_data );
	} else {
		wp_insert_post( $nav_data );
	}

	// Прибираємо стартовий контент WordPress, щоб він не потрапляв у сайт.
	foreach ( array( 'hello-world' => 'post', 'sample-page' => 'page' ) as $slug => $type ) {
		$p = get_page_by_path( $slug, OBJECT, $type );
		if ( $p ) {
			wp_trash_post( $p->ID );
		}
	}
	flush_rewrite_rules();
	return $ids;
}

add_action( 'after_switch_theme', function () {
	if ( ! get_page_by_path( 'kontakty' ) ) {
		emal_demo_setup();
	}
} );
