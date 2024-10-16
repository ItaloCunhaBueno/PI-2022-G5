<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import logo from '$lib/images/icons/logo.svg';
	import textoplus from '$lib/images/icons/text_plus.svg';
	import seta from '$lib/images/icons/arrow_outward.svg';
	import asterisco from '$lib/images/icons/asterisk.svg';
	import local from '$lib/images/icons/home.svg';
	import acompanhamento from '$lib/images/icons/show_chart.svg';
	import treinos from '$lib/images/icons/fitness_center.svg';
	import dinamismo from '$lib/images/icons/animation.svg';
	import flag_br from '$lib/images/icons/flag_br.svg';
	import flag_us from '$lib/images/icons/flag_us.svg';
	import flag_es from '$lib/images/icons/flag_es.svg';
	import lang_br from '$lib/linguagens/br.json';
	import lang_us from '$lib/linguagens/us.json';
	import lang_es from '$lib/linguagens/es.json';
	import fotoPrincipal from '$lib/images/principal.jpg';
	import foto1 from '$lib/images/foto1.jpg';
	import foto2 from '$lib/images/foto2.jpg';
	import foto3 from '$lib/images/foto3.jpg';
	import foto4 from '$lib/images/foto4.jpg';
	import facebook from '$lib/images/icons/facebook.png';
	import instagram from '$lib/images/icons/instagram.png';
	import { scrollTo, scrollRef } from 'svelte-scrolling';

	let fontSize = '16';

	let enviando = false;
	let documento = null;

	let linguagem = 'br';
	let linguagens = {
		br: { icone: flag_br, texto: 'Português', arquivo: lang_br },
		us: { icone: flag_us, texto: 'Inglês', arquivo: lang_us },
		es: { icone: flag_es, texto: 'Espanhol', arquivo: lang_es }
	};
	$: lang_arquivo = linguagens[linguagem].arquivo;

	let nome = '';
	let telefone = '';
	let email = '';
	let texto = '';

	let valid_mensagem = {
		nome: false,
		telefone: false,
		email: false,
		texto: false
	};

	$: mudaTamanhoFonte(fontSize);

	onMount(() => {
		documento = document;
	});

	function mudaTamanhoFonte(tamanho) {
		if (!documento) {
			return;
		}
		document.documentElement.style.fontSize = `${tamanho}px`;
	}

	function validaCampo(input, tipo) {
		if (tipo == 'nome') {
			let valido = /^[A-ZÀ-Ÿ][A-zÀ-ÿ']+\s([A-zÀ-ÿ']\s?)*[A-ZÀ-Ÿ][A-zÀ-ÿ']+$/.test(input);
			if (valido) {
				valid_mensagem.nome = true;
			} else {
				valid_mensagem.nome = false;
			}
			return;
		}

		if (tipo == 'telefone') {
			let valido = /^\(\d{2}\) \d{4,5}-\d{4}$/gi.test(input);
			if (valido) {
				valid_mensagem.telefone = true;
			} else {
				valid_mensagem.telefone = false;
			}
			return;
		}

		if (tipo == 'email') {
			let valido = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(input);
			if (valido) {
				valid_mensagem.email = true;
			} else {
				valid_mensagem.email = false;
			}
			return;
		}

		if (tipo == 'texto') {
			if (input.length > 10) {
				valid_mensagem.texto = true;
			} else {
				valid_mensagem.texto = false;
			}
			return;
		}
	}

	function formataTelefone(input) {
		let valor = input.replace(/\D/g, '');
		valor = valor.replace(/(\d{2})(\d)/, '($1) $2');
		valor = valor.replace(/(\d)(\d{4})$/, '$1-$2');
		return valor;
	}

	async function enviar() {
		if (Object.values(valid_mensagem).includes(false)) {
			toast.error(lang_arquivo['55'], {
				description: lang_arquivo['56']
			});
			return;
		}

		enviando = true;

		let formdata = {
			id: null,
			nome: nome ? nome : null,
			telefone: telefone ? telefone : null,
			email: email ? email : null,
			texto: texto ? texto : null
		};

		try {
			const response = await fetch('/api/novamensagem', { method: 'POST', body: JSON.stringify(formdata), headers: { 'Content-Type': 'application/json' } });
			if (response.status == 200) {
				let resposta = await response.json();
				toast.success(lang_arquivo['57'], { description: resposta.mensagem });
				nome = '';
				telefone = '';
				email = '';
				texto = '';
				valid_mensagem = {
					nome: false,
					telefone: false,
					email: false,
					texto: false
				};
			} else {
				toast.error(lang_arquivo['58'], {
					description: lang_arquivo['59']
				});
			}
		} catch (error) {
			console.log(error);
			toast.error(lang_arquivo['58'], { description: error.message });
		}
		enviando = false;
	}
</script>

<div class="bg-shade-10 flex flex-col gap-16 notebook:gap-[8rem] w-full h-full rounded-2xl">
	<header class="flex justify-between items-center px-6 py-4 mx-auto mt-8 w-full max-w-7xl">
		<a href="/">
			<img src={logo} alt="logo" class="" />
		</a>

		<nav class="hidden tablet:block">
			<ul class="font-text text-base text-shade-40 flex space-x-14 items-center tracking-[0.009rem]">
				<li><a use:scrollTo={{ ref: 'profissional', duration: 1000, offset: -80 }} id="id-profissionalButton" href="#profissional">{lang_arquivo['1']}</a></li>
				<li><a use:scrollTo={{ ref: 'funcionamento', duration: 1000, offset: -80 }} id="id-funcionamentoButton" href="#funcionamento">{lang_arquivo['2']}</a></li>
				<li><a use:scrollTo={{ ref: 'beneficios', duration: 1000, offset: -80 }} id="id-beneficiosButton" href="#beneficios">{lang_arquivo['3']}</a></li>
			</ul>
		</nav>
		<div class="flex gap-2 justify-center items-center">
			<button use:scrollTo={{ ref: 'contato', duration: 1000 }} id="id-contatoButton" href="#contato" class="flex items-center space-x-[-0.625rem]">
				<div class="px-6 py-3 text-shade-40 font-text font-medium leading-5 tracking-[0.006rem] bg-color-50 rounded-[2.5rem] btn-contact">{lang_arquivo['4']}</div>
				<div class="flex justify-center w-10 h-10 rounded-full bg-color-50">
					<img alt="seta" src={seta} width="18" height="18" />
				</div>
			</button>
			<DropdownMenu.Root>
				<DropdownMenu.Trigger asChild let:builder>
					<Button variant="link" size="icon" builders={[builder]} class="flex justify-center w-10 h-10 rounded-full bg-color-50 !p-0"><img alt="tamanho do texto" src={textoplus} width="24" height="24" /></Button>
				</DropdownMenu.Trigger>
				<DropdownMenu.Content>
					<DropdownMenu.Label>{lang_arquivo['5']}</DropdownMenu.Label>
					<DropdownMenu.Separator />
					<DropdownMenu.RadioGroup bind:value={fontSize}>
						<DropdownMenu.RadioItem value="16">{lang_arquivo['6']}</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="18">{lang_arquivo['7']}</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="22">{lang_arquivo['8']}</DropdownMenu.RadioItem>
					</DropdownMenu.RadioGroup>
				</DropdownMenu.Content>
			</DropdownMenu.Root>

			<DropdownMenu.Root>
				<DropdownMenu.Trigger asChild let:builder>
					<Button variant="link" size="icon" builders={[builder]} class="flex justify-center w-10 h-10 rounded-full bg-color-50 !p-0"><img alt="linguagem da página" src={linguagens[linguagem].icone} width="24" height="24" /></Button>
				</DropdownMenu.Trigger>
				<DropdownMenu.Content>
					<DropdownMenu.Label>{lang_arquivo['9']}</DropdownMenu.Label>
					<DropdownMenu.Separator />
					<DropdownMenu.RadioGroup bind:value={linguagem}>
						<DropdownMenu.RadioItem value="br">
							<div class="flex gap-2 justify-center items-center">
								<img alt="linguagem da página" src={linguagens['br'].icone} width="24" height="24" />
								Português
							</div>
						</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="es">
							<div class="flex gap-2 justify-center items-center">
								<img alt="linguagem da página" src={linguagens['es'].icone} width="24" height="24" />
								Español
							</div>
						</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="us">
							<div class="flex gap-2 justify-center items-center">
								<img alt="linguagem da página" src={linguagens['us'].icone} width="24" height="24" />
								English
							</div>
						</DropdownMenu.RadioItem>
					</DropdownMenu.RadioGroup>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>
	</header>
	<section class="mx-auto w-full max-w-7xl flex flex-col gap-8 notebook:gap-[1rem] max-[85.375rem]:px-6">
		<div class="flex flex-col gap-4 justify-between h-full notebook:gap-0 notebook:flex-row notebook:items-center">
			<div>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Pedro</h2>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Salvarani</h2>
			</div>
			<div class="flex flex-wrap self-end notebook:max-w-[33.75rem]">
				<p class="font-text text-base text-shade-40 tracking-[0.031rem]">
					{lang_arquivo['10']}<strong>{lang_arquivo['11']}</strong>.
				</p>
			</div>
		</div>
		<img class="rounded-3xl notebook:rounded-2xl" alt="Homem adulto professor de Educação Física" src={fotoPrincipal} />
	</section>
	<section class="mx-auto max-[85.375rem]:px-6 w-full max-w-7xl">
		<div class="flex flex-col gap-4 justify-between items-center px-16 py-6 rounded-2xl tablet:gap-0 tablet:flex-row bg-color-50">
			<h5 class="text-2xl text-center font-heading text-shade-40">{lang_arquivo['12']}</h5>
			<img alt="asterisco" src={asterisco} />
			<h5 class="text-2xl text-center font-heading text-shade-40">{lang_arquivo['13']}</h5>
			<img alt="asterisco" src={asterisco} />
			<h5 class="text-2xl text-center font-heading text-shade-40">{lang_arquivo['14']}</h5>
		</div>
	</section>
	<section id="profissional" use:scrollRef={'profissional'} class="mx-auto w-full max-w-7xl flex flex-col gap-6 notebook:gap-0 notebook:flex-row notebook:justify-between notebook:items-center h-full max-[85.375rem]:px-6">
		<h3 class="self-start text-2xl uppercase font-heading text-shade-40">{lang_arquivo['15']}</h3>
		<div class="flex flex-col notebook:max-w-[44.625rem] gap-4">
			<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">
				{lang_arquivo['16']}<strong>{lang_arquivo['17']}</strong>.
			</p>
			<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">
				{lang_arquivo['18']}<strong>{lang_arquivo['19']}</strong>{lang_arquivo['20']}
			</p>
		</div>
	</section>
	<section id="funcionamento" use:scrollRef={'funcionamento'} class="mx-auto w-full max-w-7xl flex flex-col gap-10 justify-between max-[85.375rem]:px-6">
		<h3 class="text-2xl uppercase font-heading text-shade-40">{lang_arquivo['21']}</h3>
		<div class="grid grid-cols-1 gap-8 justify-between items-center tablet:grid-cols-2 notebook:flex">
			<div class="notebook:max-w-[18.5rem] notebook:max-h-[18.5rem] tablet:min-h-[18.5rem] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="local e horário" src={local} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[1.375rem] leading-7">{lang_arquivo['22']}</h4>
					<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">{lang_arquivo['23']}</p>
				</div>
			</div>
			<div class="notebook:max-w-[18.5rem] notebook:max-h-[18.5rem] tablet:min-h-[18.5rem] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="acompanhamento" src={acompanhamento} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[1.375rem] leading-7">{lang_arquivo['24']}</h4>
					<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">{lang_arquivo['25']}</p>
				</div>
			</div>
			<div class="notebook:max-w-[18.5rem] notebook:max-h-[18.5rem] tablet:min-h-[18.5rem] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="treinos" src={treinos} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[1.375rem] leading-7">{lang_arquivo['26']}</h4>
					<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">{lang_arquivo['27']}</p>
				</div>
			</div>
			<div class="notebook:max-w-[18.5rem] notebook:max-h-[18.5rem] tablet:min-h-[18.5rem] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="dinamismo" src={dinamismo} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[1.375rem] leading-7">{lang_arquivo['28']}</h4>
					<p class="font-text text-base text-neutral-80 tracking-[0.031rem]">{lang_arquivo['29']}</p>
				</div>
			</div>
		</div>
	</section>
	<section id="beneficios" use:scrollRef={'beneficios'} class="mx-auto w-full max-w-7xl flex flex-col tablet:flex-row justify-between items-center h-full max-[85.375rem]:px-6">
		<div class="flex flex-col gap-6 self-start">
			<h3 class="self-start text-2xl uppercase font-heading text-shade-40">{lang_arquivo['30']}</h3>
			<p class="font-text text-base text-neutral-80 tracking-[0.031rem] notebook:max-w-[280px]">{lang_arquivo['31']}<strong>{lang_arquivo['32']}</strong>{lang_arquivo['33']}</p>
		</div>
		<div class="flex flex-col w-full notebook:max-w-[620px]">
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">01</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['34']}</p>
			</div>
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">02</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['35']}</p>
			</div>
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">03</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['36']}</p>
			</div>
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">04</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['37']}</p>
			</div>
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">05</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['38']}</p>
			</div>
			<div class="flex gap-6 items-center px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">06</h5>
				<p class="font-medium font-text text-base/5">{lang_arquivo['39']}</p>
			</div>
		</div>
	</section>
	<section class="flex gap-8 flex-col notebook:flex-row justify-between items-center mx-auto w-full max-w-7xl max-[85.375rem]:px-6">
		<img class="rounded-2xl" alt="Homem idoso se exercitando dentro de casa" src={foto1} width="290" />
		<img class="rounded-2xl" alt="Casal de idosos se exercitando" src={foto2} width="290" />
		<img class="rounded-2xl" alt="Mulher idosa se exercitando" src={foto3} width="290" />
		<img class="rounded-2xl" alt="Homem idoso se exercitando dentro de casa" src={foto4} width="290" />
	</section>
	<section id="contato" use:scrollRef={'contato'} class="flex flex-col gap-[3rem] w-full mx-auto max-w-7xl max-[85.375rem]:px-6">
		<h4 class="font-text text-[1.375rem] text-neutral-40 leading-7 uppercase">{lang_arquivo['40']}</h4>
		<div class="flex flex-col gap-10">
			<div>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">{lang_arquivo['41']}</h2>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">{lang_arquivo['42']}</h2>
			</div>
			<form class="flex flex-col gap-8 w-full max-w-[39rem] self-end">
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[0.006rem] placeholder-shade-40"
						type="text"
						id="id-nomeInput"
						placeholder={lang_arquivo['43']}
						bind:value={nome}
						on:keyup={() => {
							validaCampo(nome, 'nome');
						}}
						required
					/>
					{#if !valid_mensagem.nome && nome.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[0.006rem]">{lang_arquivo['44']}</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[0.006rem] placeholder-shade-40"
						type="tel"
						id="id-telefoneInput"
						placeholder={lang_arquivo['45']}
						bind:value={telefone}
						on:keyup={() => {
							telefone = formataTelefone(telefone);
							validaCampo(telefone, 'telefone');
						}}
						required
					/>
					{#if !valid_mensagem.telefone && telefone.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[0.006rem]">{lang_arquivo['46']}</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[0.006rem] placeholder-shade-40"
						type="email"
						id="id-emailInput"
						placeholder={lang_arquivo['47']}
						bind:value={email}
						on:keyup={() => {
							validaCampo(email, 'email');
						}}
					/>
					{#if !valid_mensagem.email && email.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[0.006rem]">{lang_arquivo['48']}</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<textarea
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[0.006rem] placeholder-shade-40"
						rows="5"
						id="id-msgInput"
						placeholder={lang_arquivo['49']}
						bind:value={texto}
						on:keyup={() => {
							validaCampo(texto, 'texto');
						}}
						required
					/>
					{#if !valid_mensagem.texto && texto.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[0.006rem]">{lang_arquivo['50']}</span>
					{/if}
				</div>
				{#if !enviando}
					<button class="mt-3 bg-color-50 py-4 rounded-2xl font-text text-base/5 font-medium tracking-[0.006rem] text-shade-40" id="id-enviarMsgButton" on:click={() => enviar()}>{lang_arquivo['51']}</button>
				{:else}
					<button class="mt-3 bg-color-50 py-4 rounded-2xl font-text text-base/5 font-medium tracking-[0.006rem] text-shade-40" on:click={() => enviar()}>{lang_arquivo['52']}</button>
				{/if}
			</form>
		</div>
	</section>
	<footer class="bg-shade-20 py-[3.25rem] rounded-b-2xl">
		<div class="w-full mx-auto max-w-7xl max-[85.375rem]:px-6 flex flex-col">
			<div class="flex flex-col gap-4">
				<h4 class="text-2xl font-heading text-neutral-50">{lang_arquivo['53']}</h4>
				<div class="flex flex-col gap-1">
					<p class="font-text text-shade-40 text-base tracking-[0.031rem]">pedrosalvarani@email.com</p>
					<p class="font-text text-shade-40 text-base tracking-[0.031rem]">11 99999-9999</p>
				</div>
			</div>
			<div class="flex gap-4 mx-auto">
				<a href="https://www.facebook.com" target="_blank"><img alt="facebook" src={facebook} /></a>
				<a href="https://www.instagram.com" target="_blank"><img alt="instagram" src={instagram} /></a>
			</div>
			<div class="flex flex-col mx-auto mt-[6.25rem]">
				<p class="text-center font-text text-shade-40 text-base tracking-[0.031rem]">Copyright Pedro Salvarani - 0000000000000000 - 2024</p>
				<p class="text-center font-text text-shade-40 text-base tracking-[0.031rem]">{lang_arquivo['54']}</p>
			</div>
		</div>
	</footer>
</div>
