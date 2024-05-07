<script>
	import { Toaster } from '$lib/components/ui/sonner';
	import favicon16 from '$lib/images/icons/logo.svg?width=16&height=16&format=png';
	import favicon32 from '$lib/images/icons/logo.svg?width=32&height=32&format=png';
	import favicon96 from '$lib/images/icons/logo.svg?width=96&height=96&format=png';
	import favicon192 from '$lib/images/icons/logo.svg?width=192&height=192&format=png';

	import appleTouchIcon57 from '$lib/images/icons/logo.svg?width=57&height=57&format=png';
	import appleTouchIcon60 from '$lib/images/icons/logo.svg?width=60&height=60&format=png';
	import appleTouchIcon72 from '$lib/images/icons/logo.svg?width=72&height=72&format=png';
	import appleTouchIcon76 from '$lib/images/icons/logo.svg?width=76&height=76&format=png';
	import appleTouchIcon114 from '$lib/images/icons/logo.svg?width=114&height=114&format=png';
	import appleTouchIcon120 from '$lib/images/icons/logo.svg?width=120&height=120&format=png';
	import appleTouchIcon144 from '$lib/images/icons/logo.svg?width=144&height=144&format=png';
	import appleTouchIcon152 from '$lib/images/icons/logo.svg?width=152&height=152&format=png';
	import appleTouchIcon180 from '$lib/images/icons/logo.svg?width=180&height=180&format=png';

	import androidIcon192 from '$lib/images/icons/logo.svg?width=192&height=192&format=png';

	import mstile310 from '$lib/images/icons/logo.svg?width=310&height=310&format=png';

	const appBackgroundColor = '#FFFFFF';
	const themeColor = '#10B981';
</script>

<svelte:head>
	<link rel="icon" type="image/png" sizes="16x16" href={favicon16} />
	<link rel="icon" type="image/png" sizes="32x32" href={favicon32} />
	<link rel="icon" type="image/png" sizes="96x96" href={favicon96} />
	<link rel="icon" type="image/png" sizes="192x192" href={favicon192} />

	<link rel="apple-touch-icon" sizes="57x57" href={appleTouchIcon57} />
	<link rel="apple-touch-icon" sizes="60x60" href={appleTouchIcon60} />
	<link rel="apple-touch-icon" sizes="72x72" href={appleTouchIcon72} />
	<link rel="apple-touch-icon" sizes="76x76" href={appleTouchIcon76} />
	<link rel="apple-touch-icon" sizes="114x114" href={appleTouchIcon114} />
	<link rel="apple-touch-icon" sizes="120x120" href={appleTouchIcon120} />
	<link rel="apple-touch-icon" sizes="144x144" href={appleTouchIcon144} />
	<link rel="apple-touch-icon" sizes="152x152" href={appleTouchIcon152} />
	<link rel="apple-touch-icon" sizes="180x180" href={appleTouchIcon180} />

	<link rel="icon" type="image/png" sizes="192x192" href={androidIcon192} />
	<meta name="msapplication-TileImage" content={mstile310} />

	<meta name="msapplication-TileColor" content={appBackgroundColor} />
	<meta name="theme-color" content={themeColor} />
</svelte:head>

<Toaster richColors expand={true} />

<slot />
