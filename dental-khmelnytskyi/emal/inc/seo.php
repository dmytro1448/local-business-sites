<?php
/**
 * Базове локальне SEO без плагінів: title, description, OG, noindex для демо,
 * JSON-LD Dentist + BreadcrumbList + FAQPage. На бойовому сайті це можна віддати Yoast/Rank Math,
 * але для невеликого сайту вистачає цих ~100 рядків.
 */
defined( 'ABSPATH' ) || exit;

/** Ключ сторінки в emal_pages(): для головної 'holovna', інакше slug. */
function emal_current_key() {
	if ( is_front_page() ) {
		return 'holovna';
	}
	if ( is_page() ) {
		return get_post_field( 'post_name', get_queried_object_id() );
	}
	return '';
}

add_filter( 'pre_get_document_title', function ( $title ) {
	$pages = emal_pages();
	$key   = emal_current_key();
	return isset( $pages[ $key ] ) ? $pages[ $key ]['seo'] : $title;
} );

function emal_description() {
	$pages = emal_pages();
	$key   = emal_current_key();
	if ( isset( $pages[ $key ] ) ) {
		return $pages[ $key ]['desc'];
	}
	return get_bloginfo( 'description' );
}

// Бізнес вигаданий, тому демо закрите від індексації.
add_filter( 'wp_robots', function ( $robots ) {
	$robots['noindex']  = true;
	$robots['nofollow'] = true;
	unset( $robots['max-image-preview'] );
	return $robots;
} );

add_action( 'wp_head', function () {
	$desc  = emal_description();
	$url   = is_singular() ? get_permalink() : home_url( '/' );
	$title = wp_get_document_title();
	echo '<meta name="description" content="' . esc_attr( $desc ) . '">' . "\n";
	echo '<meta property="og:type" content="website">' . "\n";
	echo '<meta property="og:locale" content="uk_UA">' . "\n";
	echo '<meta property="og:site_name" content="' . esc_attr( emal_business()['name'] ) . '">' . "\n";
	echo '<meta property="og:title" content="' . esc_attr( $title ) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr( $desc ) . '">' . "\n";
	echo '<meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
	echo '<meta name="theme-color" content="#1d6b64">' . "\n";
	// canonical для сторінок виводить ядро WordPress (rel_canonical).

	foreach ( emal_schema() as $data ) {
		echo '<script type="application/ld+json">' . wp_json_encode( $data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . '</script>' . "\n";
	}
}, 2 );

function emal_schema() {
	$b    = emal_business();
	$home = home_url( '/' );
	$out  = array();

	$hours = array();
	foreach ( $b['hours'] as $h ) {
		$hours[] = array( '@type' => 'OpeningHoursSpecification', 'dayOfWeek' => $h[0], 'opens' => $h[1], 'closes' => $h[2] );
	}
	$area = array( array( '@type' => 'City', 'name' => $b['city'] ) );
	foreach ( $b['areas'] as $a ) {
		$area[] = array( '@type' => 'Place', 'name' => $a . ', ' . $b['city'] );
	}
	$out[] = array(
		'@context'                  => 'https://schema.org',
		'@type'                     => 'Dentist',
		'@id'                       => $home . '#clinic',
		'name'                      => $b['name'],
		'url'                       => $home,
		'telephone'                 => $b['phone'],
		'email'                     => $b['email'],
		'priceRange'                => '₴₴',
		'medicalSpecialty'          => 'Dentistry',
		'address'                   => array( '@type' => 'PostalAddress', 'streetAddress' => $b['street'], 'addressLocality' => $b['city'], 'addressRegion' => $b['region'], 'addressCountry' => 'UA' ),
		'geo'                       => array( '@type' => 'GeoCoordinates', 'latitude' => $b['geo'][0], 'longitude' => $b['geo'][1] ),
		'openingHoursSpecification' => $hours,
		'areaServed'                => $area,
	);

	if ( is_page() && ! is_front_page() ) {
		$list = array();
		foreach ( emal_breadcrumb_items() as $i => $item ) {
			$list[] = array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $item[0], 'item' => $item[1] );
		}
		$out[] = array( '@context' => 'https://schema.org', '@type' => 'BreadcrumbList', 'itemListElement' => $list );
	}

	$pages = emal_pages();
	$key   = emal_current_key();
	$faq   = isset( $pages[ $key ]['faq'] ) ? $pages[ $key ]['faq'] : ( 'holovna' === $key ? 'home' : '' );
	if ( $faq ) {
		$qs = array();
		foreach ( emal_faqs()[ $faq ] as $qa ) {
			$qs[] = array( '@type' => 'Question', 'name' => $qa[0], 'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $qa[1] ) );
		}
		$out[] = array( '@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => $qs );
	}

	if ( isset( $pages[ $key ]['parent'] ) && 'poslugy' === $pages[ $key ]['parent'] ) {
		$out[] = array( '@context' => 'https://schema.org', '@type' => 'MedicalProcedure', 'name' => $pages[ $key ]['title'], 'description' => $pages[ $key ]['desc'], 'url' => get_permalink() );
	}
	return $out;
}
