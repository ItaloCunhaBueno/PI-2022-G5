<script>
	import '../app.css';
	import { toast } from 'svelte-sonner';
	import logo from '$lib/images/icons/logo.svg';
	import seta from '$lib/images/icons/arrow_outward.svg';
	import asterisco from '$lib/images/icons/asterisk.svg';
	import local from '$lib/images/icons/home.svg';
	import acompanhamento from '$lib/images/icons/show_chart.svg';
	import treinos from '$lib/images/icons/fitness_center.svg';
	import dinamismo from '$lib/images/icons/animation.svg';
	import fotoPrincipal from '$lib/images/principal.png';
	import foto1 from '$lib/images/foto1.png';
	import foto2 from '$lib/images/foto2.png';
	import foto3 from '$lib/images/foto3.png';
	import foto4 from '$lib/images/foto4.png';
	import facebook from '$lib/images/icons/facebook.png';
	import instagram from '$lib/images/icons/instagram.png';
	import { scrollTo, scrollRef } from 'svelte-scrolling';

	let enviando = false;

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
			toast.error('Por favor, preencha todos os campos.', {
				description: 'Um ou mais campos preenchidos não são válidos.'
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
				toast.success('SUCESSO', { description: resposta.mensagem });
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
				toast.error('ERRO', {
					description: 'Não foi possivel enviar a mensagem.'
				});
			}
		} catch (error) {
			console.log(error);
			toast.error('ERRO', { description: error.message });
		}
		enviando = false;
	}
</script>

<div class="bg-shade-10 flex flex-col gap-16 notebook:gap-[132px] w-full h-full rounded-2xl">
	<header class="flex items-center justify-between w-full px-6 py-4 mx-auto mt-8 max-w-7xl">
		<a href="/">
			<img src={logo} alt="logo" class="" />
		</a>
		<nav class="hidden tablet:block">
			<ul class="font-text text-base text-shade-40 flex space-x-14 items-center tracking-[.15px]">
				<li><a use:scrollTo={{ ref: 'profissional', duration: 1000, offset: -80 }} href="#profissional">O Profissional</a></li>
				<li><a use:scrollTo={{ ref: 'funcionamento', duration: 1000, offset: -80 }} href="#funcionamento">Como Funciona</a></li>
				<li><a use:scrollTo={{ ref: 'beneficios', duration: 1000, offset: -80 }} href="#beneficios">Benefícios</a></li>
			</ul>
		</nav>
		<button use:scrollTo={{ ref: 'contato', duration: 1000 }} class="flex items-center space-x-[-10px]">
			<div class="px-6 py-3 text-shade-40 font-text font-medium leading-5 tracking-[.1px] bg-color-50 rounded-[40px] btn-contact">Entre em contato</div>
			<div class="flex justify-center w-10 h-10 rounded-full bg-color-50">
				<img alt="seta" src={seta} width="18" height="18" />
			</div>
		</button>
	</header>
	<section class="mx-auto w-full max-w-7xl flex flex-col gap-8 notebook:gap-16 max-[1366px]:px-6">
		<div class="flex flex-col justify-between h-full gap-4 notebook:gap-0 notebook:flex-row notebook:items-center">
			<div>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Pedro</h2>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Salvarani</h2>
			</div>
			<div class="flex flex-wrap self-end notebook:max-w-[540px]">
				<p class="font-text text-base text-shade-40 tracking-[.5px]">Com mais de 20 anos de experiência, Pedro é um renomado professor de Educação Física, <strong>com especialização em Pilates e atividade física voltada para o envelhecimento</strong>.</p>
			</div>
		</div>
		<img alt="Homem adulto se exercitando dentro de casa" src={fotoPrincipal} />
	</section>
	<section class="mx-auto max-[1366px]:px-6 w-full max-w-7xl">
		<div class="flex flex-col items-center justify-between gap-4 px-16 py-6 tablet:gap-0 tablet:flex-row bg-color-50 rounded-2xl">
			<h5 class="text-2xl font-heading text-shade-40">Atendimento à domicilio</h5>
			<img alt="asterisco" src={asterisco} />
			<h5 class="text-2xl font-heading text-shade-40">Comodidade</h5>
			<img alt="asterisco" src={asterisco} />
			<h5 class="text-2xl font-heading text-shade-40">Exercícios personalizados</h5>
		</div>
	</section>
	<section id="profissional" use:scrollRef={'profissional'} class="mx-auto w-full max-w-7xl flex flex-col gap-6 notebook:gap-0 notebook:flex-row notebook:justify-between notebook:items-center h-full max-[1366px]:px-6">
		<h3 class="self-start text-2xl uppercase font-heading text-shade-40">O profissional</h3>
		<div class="flex flex-col notebook:max-w-[714px] gap-4">
			<p class="font-text text-base text-neutral-80 tracking-[.5px]">
				Pedro Salvarani tem 49 anos e é professor de Educação Física. Graduou-se pela Universidade de Mogi das Cruzes e possui pós-graduação em Educação Especial, além de formação em <strong>Pilates e Atividade Física aplicada no Envelhecimento</strong>.
			</p>
			<p class="font-text text-base text-neutral-80 tracking-[.5px]">
				Com mais de 20 anos de experiência na área, Pedro atuou em escolas, clínicas e academias. No entanto, foi através do <strong>atendimento domiciliar</strong> que encontrou a oportunidade de desenvolver treinos com total eficiência. Acompanhando, orientando,
				motivando e evoluindo, ele alcançou resultados satisfatórios na vida de pessoas que acreditaram nele, mas, sobretudo, em si mesmas.
			</p>
		</div>
	</section>
	<section id="funcionamento" use:scrollRef={'funcionamento'} class="mx-auto w-full max-w-7xl flex flex-col gap-10 justify-between max-[1366px]:px-6">
		<h3 class="text-2xl uppercase font-heading text-shade-40">Como funciona</h3>
		<div class="grid items-center justify-between grid-cols-1 gap-8 tablet:grid-cols-2 notebook:flex">
			<div class="notebook:max-w-[296px] notebook:max-h-[296px] tablet:min-h-[296px] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="local e horário" src={local} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Local e Horário</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Os treinos são realizados na sua residência ou no espaço que lhe seja favorável, com horários flexíveis e que se ajustam à sua rotina diária.</p>
				</div>
			</div>
			<div class="notebook:max-w-[296px] notebook:max-h-[296px] tablet:min-h-[296px] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="acompanhamento" src={acompanhamento} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Acompanhamento</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Acompanhamento em tempo integral permitindo melhor orientação, correção e segurança na prática da atividade.</p>
				</div>
			</div>
			<div class="notebook:max-w-[296px] notebook:max-h-[296px] tablet:min-h-[296px] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="treinos" src={treinos} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Treinos</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Nossos planos de treino são elaborados de maneira 100% individual a partir de uma minuciosa avaliação.</p>
				</div>
			</div>
			<div class="notebook:max-w-[296px] notebook:max-h-[296px] tablet:min-h-[296px] p-8 bg-shade-20 flex flex-col gap-6 rounded-2xl">
				<img alt="dinamismo" src={dinamismo} width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Dinamismo</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">A diversificação e evolução dos exercícios são realizados rotineiramente, o que torna as aulas dinâmicas.</p>
				</div>
			</div>
		</div>
	</section>
	<section id="beneficios" use:scrollRef={'beneficios'} class="mx-auto w-full max-w-7xl flex flex-col tablet:flex-row justify-between items-center h-full max-[1366px]:px-6">
		<div class="flex flex-col self-start gap-6">
			<h3 class="self-start text-2xl uppercase font-heading text-shade-40">Benefícios</h3>
			<p class="font-text text-base text-neutral-80 tracking-[.5px] notebook:max-w-[280px]">Saúde e Bem-Estar Personalizados: Descubra os <strong>Benefícios Exclusivos</strong> do Treinamento Domiciliar</p>
		</div>
		<div class="flex flex-col w-full notebook:max-w-[620px]">
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">01</h5>
				<p class="font-medium font-text text-base/5">Aumento da disposição e autoestima</p>
			</div>
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">02</h5>
				<p class="font-medium font-text text-base/5">Previne e reduz mortalidade por doenças crônicas</p>
			</div>
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">03</h5>
				<p class="font-medium font-text text-base/5">Aumenta força e resistência muscular</p>
			</div>
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">04</h5>
				<p class="font-medium font-text text-base/5">Reduz sintomas depressivos</p>
			</div>
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">05</h5>
				<p class="font-medium font-text text-base/5">Diminuição do risco de lesões</p>
			</div>
			<div class="flex items-center gap-6 px-4 py-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">06</h5>
				<p class="font-medium font-text text-base/5">Treino personalizado e individual</p>
			</div>
		</div>
	</section>
	<section class="flex flex-col notebook:flex-row gap-8 mx-auto w-full max-w-7xl max-[1366px]:px-6">
		<img class="rounded-2xl" alt="Homem idoso se exercitando dentro de casa" src={foto1} />
		<img class="rounded-2xl" alt="Casal de idosos se exercitando" src={foto2} />
		<img class="rounded-2xl" alt="Homem idoso se exercitando" src={foto3} />
		<img class="rounded-2xl" alt="Casal de idosos se exercitando na academia" src={foto4} />
	</section>
	<section id="contato" use:scrollRef={'contato'} class="flex flex-col gap-[52px] w-full mx-auto max-w-7xl max-[1366px]:px-6">
		<h4 class="font-text text-[22px] text-neutral-40 leading-7 uppercase">Contato</h4>
		<div class="flex flex-col gap-10">
			<div>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Vamos</h2>
				<h2 class="text-6xl font-heading text-shade-40 tablet:text-8xl">Conversar?</h2>
			</div>
			<form class="flex flex-col gap-8 w-full max-w-[624px] self-end">
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40"
						type="text"
						placeholder="Seu nome*"
						bind:value={nome}
						on:keyup={() => {
							validaCampo(nome, 'nome');
						}}
						required
					/>
					{#if !valid_mensagem.nome && nome.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[.1px]">Por favor, digite um nome válido.</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40"
						type="tel"
						placeholder="Telefone*"
						bind:value={telefone}
						on:keyup={() => {
							telefone = formataTelefone(telefone);
							validaCampo(telefone, 'telefone');
						}}
						required
					/>
					{#if !valid_mensagem.telefone && telefone.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[.1px]">Por favor, digite um telefone válido.</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<input
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40"
						type="email"
						placeholder="E-mail"
						bind:value={email}
						on:keyup={() => {
							validaCampo(email, 'email');
						}}
					/>
					{#if !valid_mensagem.email && email.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[.1px]">Por favor, digite um e-mail válido.</span>
					{/if}
				</div>
				<div class="flex flex-col gap-2">
					<textarea
						class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40"
						rows="5"
						placeholder="Sua mensagem*"
						bind:value={texto}
						on:keyup={() => {
							validaCampo(texto, 'texto');
						}}
						required
					/>
					{#if !valid_mensagem.texto && texto.length > 0}
						<span class="font-text text-sm ml-2 text-red-500 tracking-[.1px]">Por favor, digite uma mensagem.</span>
					{/if}
				</div>
				{#if !enviando}
					<button class="mt-3 bg-color-50 py-4 rounded-2xl font-text text-base/5 font-medium tracking-[.1px] text-shade-40" on:click={() => enviar()}>Enviar mensagem</button>
				{:else}
					<button class="mt-3 bg-color-50 py-4 rounded-2xl font-text text-base/5 font-medium tracking-[.1px] text-shade-40" on:click={() => enviar()}>Enviando...</button>
				{/if}
			</form>
		</div>
	</section>
	<footer class="bg-shade-20 py-[52px] rounded-b-2xl">
		<div class="w-full mx-auto max-w-7xl max-[1366px]:px-6 flex flex-col">
			<div class="flex flex-col gap-4">
				<h4 class="text-2xl font-heading text-neutral-50">Nosso contato</h4>
				<div class="flex flex-col gap-1">
					<p class="font-text text-shade-40 text-base tracking-[.5px]">pedrosalvarani@email.com</p>
					<p class="font-text text-shade-40 text-base tracking-[.5px]">11 99999-9999</p>
				</div>
			</div>
			<div class="flex gap-4 mx-auto">
				<a href="https://www.facebook.com" target="_blank"><img alt="facebook" src={facebook} /></a>
				<a href="https://www.instagram.com" target="_blank"><img alt="instagram" src={instagram} /></a>
			</div>
			<div class="flex flex-col mx-auto mt-[100px]">
				<p class="text-center font-text text-shade-40 text-base tracking-[.5px]">Copyright Pedro Salvarani - 0000000000000000 - 2024</p>
				<p class="text-center font-text text-shade-40 text-base tracking-[.5px]">Todos os direitos reservados</p>
			</div>
		</div>
	</footer>
</div>
