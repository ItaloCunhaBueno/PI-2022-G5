<script>
	import '../app.css';
	import { Button } from '$lib/components/ui/button/index.js';
	import { toast } from 'svelte-sonner';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import { Input } from '$lib/components/ui/input';
	import logo from '$lib/images/logo-projeto.svg';
	import MaterialSymbolsGroups2Rounded from '~icons/material-symbols/groups-2-rounded';
	import MaterialSymbolsVolunteerActivismRounded from '~icons/material-symbols/volunteer-activism-rounded';
	import MaterialSymbolsAlignHorizontalLeftRounded from '~icons/material-symbols/align-horizontal-left-rounded';
	import MaterialSymbolsShoppingCartRounded from '~icons/material-symbols/shopping-cart-rounded';
	import IcOutlineWhatsapp from '~icons/ic/outline-whatsapp';
	import LineMdLoadingTwotoneLoop from '~icons/line-md/loading-twotone-loop';

	function fadein(node, direction) {
		const observer = new IntersectionObserver((entries) => {
			if (entries[0].isIntersecting) {
				node.classList.add(`fade-in-${direction}`);
				node.style.opacity = '1';
			} else {
				node.classList.remove(`fade-in-${direction}`);
				node.style.opacity = '0';
			}
		});

		observer.observe(node);

		return {
			destroy() {
				node.classList.remove(`fade-in-${direction}`);
				node.style.opacity = '0';
				observer.disconnect();
			}
		};
	}

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
			const response = await fetch('/api/app/novamensagem', { method: 'POST', body: JSON.stringify(formdata), headers: { 'Content-Type': 'application/json' } });
			let resposta = await response.json();
			if (resposta.status == 200) {
				toast.success(resposta.mensagem);
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
			}
		} catch (error) {
			console.log(error);
			toast.error(error.message);
		}
		enviando = false;
	}
</script>

<div class="bg-shade-10 flex flex-col gap-[132px] w-full h-full rounded-2xl">
	<header class="mx-auto mt-8 max-w-7xl flex justify-between items-center w-full px-6 py-4">
		<a href="/">
			<img src={logo} alt="logo" class="" />
		</a>
		<nav>
			<ul class="font-text text-base text-shade-40 flex space-x-14 items-center tracking-[.15px]">
				<li>O Profissional</li>
				<li>Como Funciona</li>
				<li>Benefícios</li>
				<li>Resultados</li>
			</ul>
		</nav>
		<button class="flex items-center space-x-[-10px]">
			<div class="px-6 py-3 text-shade-40 font-text font-medium leading-5 tracking-[.1px] bg-color-50 rounded-[40px] btn-contact">
				Entre em contato
			</div>
			<div class="flex justify-center w-10 h-10 bg-color-50 rounded-full">
				<img  alt="test" src="../src\lib\images\arrow_outward.svg" width="18" height="18" />
			</div>			
		</button>
	</header>
	<section class="mx-auto w-full max-w-7xl flex flex-col gap-16 max-[1366px]:px-6">
		<div class="flex justify-between items-center h-full">
			<div>
				<h2 class="font-heading text-shade-40 text-8xl">Pedro</h2>
				<h2 class="font-heading text-shade-40 text-8xl">Salvarani</h2>
			</div>
			<div class="flex flex-wrap self-end max-w-[540px]">
				<p class="font-text text-base text-shade-40 tracking-[.5px]">Com mais de 20 anos de experiência, Pedro é um renomado professor de Educação Física, <strong>com especialização em Pilates e atividade física voltada para o envelhecimento</strong>.</p>
			</div>
		</div>
		<img alt="" src="../src\lib\images\AdobeStock_369344205 1.png" />
	</section>
	<section class="mx-auto max-[1366px]:px-6 w-full max-w-7xl">
		<div class="flex justify-between items-center bg-color-50 px-16 py-6 rounded-2xl">
			<h5 class="font-heading text-2xl text-shade-40">Atendimento à domicilio</h5>
			<img alt="" src="../src\lib\images\asterisk.svg" />
			<h5 class="font-heading text-2xl text-shade-40">Comodidade</h5>
			<img alt="" src="../src\lib\images\asterisk.svg" />
			<h5 class="font-heading text-2xl text-shade-40">Exercícios personalizados</h5>
		</div>
	</section>	
	<section class="mx-auto w-full max-w-7xl flex justify-between items-center h-full max-[1366px]:px-6">
		<h3 class="font-heading text-shade-40 text-2xl uppercase self-start">O profissional</h3>
		<div class="flex flex-col max-w-[714px] gap-4">
			<p class="font-text text-base text-neutral-80 tracking-[.5px]">Pedro Salvarani tem 49 anos e é professor de Educação Física. Graduou-se pela Universidade de Mogi das Cruzes e possui pós-graduação em Educação Especial, além de formação em <strong>Pilates e Atividade Física aplicada no Envelhecimento</strong>.</p>
			<p class="font-text text-base text-neutral-80 tracking-[.5px]">Com mais de 20 anos de experiência na área, Pedro atuou em escolas, clínicas e academias.
				No entanto, foi através do <strong>atendimento domiciliar</strong> que encontrou a oportunidade de desenvolver treinos com total eficiência. Acompanhando, orientando, motivando e evoluindo, ele alcançou resultados satisfatórios na vida de pessoas que acreditaram nele, mas, sobretudo, em si mesmas.</p>
		</div>
	</section>
	<section class="mx-auto w-full max-w-7xl flex flex-col gap-10 justify-between max-[1366px]:px-6">
		<h3 class="font-heading text-shade-40 text-2xl uppercase">Como funciona</h3>
		<div class="flex justify-between items-center gap-8">
			<div class="w-[296px] h-[296px] p-8 bg-shade-20 flex flex-col gap-6">
				<img alt="" src="../src\lib\images\home.svg" width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Local e Horário</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Os treinos são realizados na sua residência ou no espaço que lhe seja favorável, com horários flexíveis e que se ajustam à sua rotina diária.</p>
				</div>
			</div>
			<div class="w-[296px] h-[296px] p-8 bg-shade-20 flex flex-col gap-6">
				<img alt="" src="../src\lib\images\show_chart.svg" width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Acompanhamento</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Acompanhamento em tempo integral permitindo melhor orientação, correção e segurança na prática da atividade.</p>
				</div>
			</div>
			<div class="w-[296px] h-[296px] p-8 bg-shade-20 flex flex-col gap-6">
				<img alt="" src="../src\lib\images\fitness_center.svg" width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Treinos</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">Nossos planos de treino são elaborados de maneira 100% individual a partir de uma minuciosa avaliação.</p>
				</div>
			</div>
			<div class="w-[296px] h-[296px] p-8 bg-shade-20 flex flex-col gap-6">
				<img alt="" src="../src\lib\images\animation.svg" width="48" />
				<div class="flex flex-col gap-3">
					<h4 class="font-text text-[22px] leading-7">Dinamismo</h4>
					<p class="font-text text-base text-neutral-80 tracking-[.5px]">A diversificação e evolução dos exercícios são realizados rotineiramente, o que torna as aulas dinâmicas.</p>
				</div>
			</div>
		</div>
	</section>
	<section class="mx-auto w-full max-w-7xl flex justify-between items-center h-full max-[1366px]:px-6">
		<div class="flex flex-col gap-6 self-start">
			<h3 class="font-heading text-shade-40 text-2xl uppercase self-start">Benefícios</h3>
			<p class="font-text text-base text-neutral-80 tracking-[.5px] max-w-[280px]">Saúde e Bem-Estar Personalizados: Descubra os <strong>Benefícios Exclusivos</strong> do Treinamento Domiciliar</p>
		</div>
		<div class="flex flex-col w-full max-w-[620px]">
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">01</h5>
				<p class="font-text font-medium text-base/5">Aumento da disposição e autoestima</p>
			</div>
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">02</h5>
				<p class="font-text font-medium text-base/5">Previne e reduz mortalidade por doenças crônicas</p>
			</div>
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">03</h5>
				<p class="font-text font-medium text-base/5">Aumenta força e resistência muscular</p>
			</div>
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">04</h5>
				<p class="font-text font-medium text-base/5">Reduz sintomas depressivos</p>
			</div>
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">05</h5>
				<p class="font-text font-medium text-base/5">Diminuição do risco de lesões</p>
			</div>
			<div class="flex items-center py-6 px-4 gap-6 border-b border-neutral-20">
				<h5 class="font-heading text-[28px]/9 text-color-80">06</h5>
				<p class="font-text font-medium text-base/5">Treino personalizado e individual</p>
			</div>
		</div>		
	</section>
	<section class="flex gap-8 mx-auto w-full max-w-7xl flex max-[1366px]:px-6">
		<img class="rounded-2xl" alt="" src="../src\lib\images\istockphoto-1239568544-1024x1024 1.png" />
		<img class="rounded-2xl" alt="" src="../src\lib\images\idosos-se-exercitando_4 1.png" />
		<img class="rounded-2xl" alt="" src="../src\lib\images\Se__nior-03 1.png" />
		<img class="rounded-2xl" alt="" src="../src\lib\images\depositphotos_249590430-stock-photo-happy-mature-people-doing-exercises 1.png" />
	</section>
	<section class="flex flex-col gap-[52px] w-full mx-auto max-w-7xl max-[1366px]:px-6">
		<h4 class="font-text text-[22px] text-neutral-40 leading-7 uppercase">Contato</h4>
		<div class="flex flex-col gap-10">
			<div>
				<h2 class="font-heading text-shade-40 text-8xl">Vamos</h2>
				<h2 class="font-heading text-shade-40 text-8xl">Conversar?</h2>
			</div>
			<form class="flex flex-col gap-8 w-full max-w-[624px] self-end">
				<input class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40" type="text" placeholder="Seu nome*">
				<input class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40" type="text" placeholder="Telefone*">
				<input class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px] placeholder-shade-40" type="text" placeholder="E-mail">
				<textarea class="focus:outline-none font-text font-medium text-base/5 text-shade-40 py-5 px-2 border-b border-neutral-20 tracking-[.1px]" rows="5">Sua mensagem*</textarea>
			</form>			
		</div>
	</section>
	<footer class="bg-shade-20 py-[52px] rounded-b-2xl">
		<div class="w-full mx-auto max-w-7xl max-[1366px]:px-6 flex flex-col">
			<div class="flex flex-col gap-4">
				<h4 class="font-heading text-2xl text-neutral-50">Nosso contato</h4>
				<div class="flex flex-col gap-1">
					<p class="font-text text-shade-40 text-base tracking-[.5px]">pedrosalvarani@email.com</p>
					<p class="font-text text-shade-40 text-base tracking-[.5px]">11 99999-9999</p>
				</div>
			</div>
			<div class="flex gap-4 mx-auto">				
				<img alt="" src="../src\lib\images\facebook-logo-blue-circle-large-transparent-png 1.png" />
				<img alt="" src="../src\lib\images\pngegg 1.png" />
			</div>
			<div class="flex flex-col mx-auto mt-[100px]">
				<p class="text-center font-text text-shade-40 text-base tracking-[.5px]">Copyright Pedro Salvarani - 0000000000000000 - 2024</p>
				<p class="text-center font-text text-shade-40 text-base tracking-[.5px]">Todos os direitos reservados</p>
			</div>
		</div>
	</footer>
</div>

<!-- <div class="flex flex-col w-full h-full">
	<nav class="sticky top-0 z-50 flex flex-col justify-center w-full h-full">
		<ul class="flex flex-grow gap-2 py-4 px-8 bg-primary !h-24 !max-h-24 items-center">
			<div class="!h-12 p-1 bg-white rounded-full aspect-square">
				<a href="/">
					<img src={logo} alt="logo" class="" />
				</a>
			</div>
			<li class="flex items-center justify-start flex-1 p-1 text-3xl font-bold text-primary-foreground">Educador Físico</li>
			<li class="flex items-center justify-center">
				<Button variant="outline" class="!py-3 !px-6 text-base font-bold" href="#Contato">
					<span>ENTRE EM CONTATO</span>
				</Button>
			</li>
		</ul>
		<ul class="flex flex-wrap justify-center w-full gap-2 bg-neutral-800 !min-h-16">
			<li class="flex items-center justify-center">
				<Button variant="link" class="flex gap-2 text-2xl text-white" href="#QuemSomos">
					<MaterialSymbolsGroups2Rounded />
					<span class="">Quem Somos</span>
				</Button>
			</li>
			<li class="flex items-center justify-center">
				<Button variant="link" class="flex gap-2 text-2xl text-white" href="#NossosProjetos">
					<MaterialSymbolsVolunteerActivismRounded />
					<span class="">Nossos Projetos</span>
				</Button>
			</li>
			<li class="flex items-center justify-center">
				<Button variant="link" class="flex gap-2 text-2xl text-white" href="#Resultados">
					<MaterialSymbolsAlignHorizontalLeftRounded />
					<span class="">Resultados</span>
				</Button>
			</li>
			<li class="flex items-center justify-center">
				<Button variant="link" class="flex gap-2 text-2xl text-white" href="#Servicos">
					<MaterialSymbolsShoppingCartRounded />
					<span class="">Serviços</span>
				</Button>
			</li>
		</ul>
	</nav>

	<section id="QuemSomos" class="flex fade-in-left opacity-0 flex-wrap items-center w-full !min-h-[755px] bg-neutral-100" use:fadein={'left'}>
		<div class="flex flex-col justify-center w-full h-full gap-4 p-8 sm:w-1/2">
			<p class="text-5xl font-bold">Quem somos</p>
			<p class="text-xl text-justify">
				But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of
				human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.
			</p>
		</div>
		<div class="flex flex-col items-center justify-center w-full h-full p-8 sm:w-1/2">
			<img class="object-contain rounded-lg" src="https://dummyimage.com/645x584/aaaaaa/fff&text=placeholder" alt="placeholder" />
		</div>
	</section>

	<section id="NossosProjetos" class="flex fade-in-right opacity-0 flex-wrap items-center w-full !min-h-[755px] bg-neutral-900 text-neutral-100" use:fadein={'right'}>
		<div class="w-full h-full p-8 overflow-hidden sm:w-1/2">
			<div class="flex flex-col items-center gap-2 lg:gap-0">
				<img class="object-cover w-full lg:w-auto lg:mr-[32%] rounded-lg" src="https://dummyimage.com/320x240/aaaaaa/fff&text=placeholder" alt="placeholder" />
				<img class="object-cover w-full lg:w-auto lg:ml-[32%] rounded-lg" src="https://dummyimage.com/320x240/aaaaaa/fff&text=placeholder" alt="placeholder" />
				<img class="object-cover w-full lg:w-auto lg:mr-[32%] rounded-lg" src="https://dummyimage.com/320x240/aaaaaa/fff&text=placeholder" alt="placeholder" />
			</div>
		</div>
		<div class="flex flex-col justify-center w-full h-full gap-4 p-8 sm:w-1/2">
			<p class="text-5xl font-bold">Projetos</p>
			<p class="text-xl text-justify">
				But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of
				human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.
			</p>
		</div>
	</section>

	<section id="Resultados" class="flex fade-in-left opacity-0 flex-col w-full !min-h-[755px] p-8 bg-neutral-100 justify-center items-center gap-14" use:fadein={'left'}>
		<p class="text-5xl font-bold">Resultados</p>
		<div class="flex flex-wrap w-full overflow-hidden rounded-lg lg:max-w-[60%] bg-pink-300">
			<div class="flex flex-col flex-grow w-full gap-2 p-8 min-h-[480px] bg-primary text-primary-foreground sm:w-auto">
				<p class="text-2xl font-bold">Benefícios na saúde:</p>
				<div class="flex flex-col items-start justify-center w-full gap-2 px-4 text-xl">
					<span>Resultados #1</span>
					<span>Resultados #2</span>
					<span>Resultados #3</span>
					<span>Resultados #4</span>
					<span>Resultados #5</span>
				</div>
			</div>
			<img class="sm:w-[60%] h-auto w-full object-cover" src="https://dummyimage.com/740x480/aaaaaa/fff&text=placeholder" alt="placeholder" />
		</div>
	</section>

	<section id="Servicos" class="flex fade-in-right opacity-0 flex-col w-full !min-h-[755px] gap-14 p-8 bg-neutral-900 text-neutral-100 justify-center" use:fadein={'right'}>
		<p class="text-5xl font-bold">Nossos serviços</p>
		<div class="flex flex-wrap items-center justify-center w-full gap-4">
			<Card.Root class="flex flex-col w-full lg:w-[360px] lg:h-[320px] justify-between rounded-lg">
				<Card.Header>
					<Card.Title class="text-4xl">Plano A</Card.Title>
					<Card.Description class="text-xl text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc fringilla urna a condimentum porttitor. Proin commodo orci lobortis, auctor ipsum eget, suscipit massa.</Card.Description>
				</Card.Header>
				<Card.Footer class="flex justify-start text-4xl font-bold">R$ 20,00</Card.Footer>
			</Card.Root>
			<Card.Root class="flex flex-col w-full lg:w-[360px] lg:h-[480px] justify-between rounded-lg">
				<Card.Header>
					<Card.Title class="text-4xl">Plano B</Card.Title>
					<Card.Description class="text-xl text-justify"
						>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc fringilla urna a condimentum porttitor. Proin commodo orci lobortis, auctor ipsum eget, suscipit massa. Vestibulum dolor justo, varius ac mauris non, lobortis accumsan nunc. Mauris
						maximus tincidunt diam in gravida.
					</Card.Description>
				</Card.Header>
				<Card.Footer class="flex justify-start text-4xl font-bold">R$ 20,00</Card.Footer>
			</Card.Root>
			<Card.Root class="flex flex-col w-full lg:w-[360px] lg:h-[320px] justify-between rounded-lg">
				<Card.Header>
					<Card.Title class="text-4xl">Plano C</Card.Title>
					<Card.Description class="text-xl text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc fringilla urna a condimentum porttitor. Proin commodo orci lobortis, auctor ipsum eget, suscipit massa.</Card.Description>
				</Card.Header>
				<Card.Footer class="flex justify-start text-4xl font-bold">R$ 20,00</Card.Footer>
			</Card.Root>
		</div>
	</section>

	<section id="Contato" class="flex fade-in-left opacity-0 justify-center w-full !min-h-[755px] p-8 bg-neutral-100" use:fadein={'left'}>
		<div class="flex flex-wrap w-full overflow-hidden rounded-lg sm:max-w-[90%]">
			<img class="object-cover w-full h-96 xl:w-auto xl:h-auto" src="https://dummyimage.com/475x732/aaaaaa/fff&text=placeholder" alt="" />
			<div class="flex flex-col justify-center flex-grow !min-w-[350px] !min-h-[732px] gap-2 p-8 text-xl text-white bg-primary">
				<p class="text-5xl font-bold">Entre em contato</p>
				<p>Informe seu e-mail e telefone que retornaremos o mais breve possível.</p>
				<div class="flex flex-col gap-2 mt-4 text-2xl">
					<span class="font-bold">Nome Completo</span>
					<Input
						class="h-14"
						type="text"
						id="nome"
						placeholder="Digite seu nome."
						bind:value={nome}
						on:keyup={() => {
							validaCampo(nome, 'nome');
						}}
						required
					/>
					{#if !valid_mensagem.nome}
						<span class="text-sm text-red-500">Por favor, digite um nome válido.</span>
					{/if}
					<span class="mt-2 font-bold">E-mail</span>
					<Input
						class="h-14"
						type="email"
						placeholder="Digite seu e-mail."
						bind:value={email}
						on:keyup={() => {
							validaCampo(email, 'email');
						}}
						required
					/>
					{#if !valid_mensagem.email}
						<span class="text-sm text-red-500">Por favor, digite um e-mail válido.</span>
					{/if}
					<span class="mt-2 font-bold">Telefone</span>
					<Input
						class="h-14"
						type="tel"
						placeholder="(##) #####-#### ou (##) ####-####"
						bind:value={telefone}
						on:keyup={() => {
							telefone = formataTelefone(telefone);
							validaCampo(telefone, 'telefone');
						}}
						required
					/>
					{#if !valid_mensagem.telefone}
						<span class="text-sm text-red-500">Por favor, digite um telefone válido.</span>
					{/if}
					<span class="mt-2 font-bold">Mensagem</span>
					<Textarea
						class="h-44"
						placeholder="Mensagem..."
						bind:value={texto}
						on:keyup={() => {
							validaCampo(texto, 'texto');
						}}
						required
					/>
					{#if !valid_mensagem.texto}
						<span class="text-sm text-red-500">Por favor, digite uma mensagem.</span>
					{/if}
					{#if !enviando}
						<Button variant="outline" class="!py-3 !px-6 text-base font-bold text-black mt-2" on:click={() => enviar()}>ENVIAR</Button>
					{:else}
						<Button variant="outline" disabled class="!py-3 !px-6 text-base font-bold text-black mt-2" on:click={() => enviar()}><LineMdLoadingTwotoneLoop class="pr-2 text-2xl" /></Button>
					{/if}
				</div>
			</div>
		</div>
	</section>

	<footer class="flex items-center gap-2 p-16 text-base text-white bg-primary !min-h-[304px]">
		<div class="flex flex-col items-start justify-center w-full gap-4 sm:w-1/2">
			<div class="flex flex-col items-start justify-center gap-1">
				<span class="text-2xl font-bold">Educador Físico</span>
				<span>CREF/SP 123456</span>
			</div>
			<div class="flex flex-col items-start justify-center gap-1">
				<span class="text-2xl font-bold">Educador Físico</span>
				<span>CREF/SP 123456</span>
			</div>
		</div>
		<div class="flex flex-col items-end justify-center w-full gap-4 sm:w-1/2">
			<div class="flex flex-col items-end justify-center gap-1">
				<span class="text-xl font-bold">Rua Ali Perto, 45</span>
				<span class="text-xl font-bold">Bairro Aquele, Mogi das Cruzes - SP</span>
			</div>
			<div class="flex flex-col items-end justify-center gap-1">
				<div class="flex items-center justify-center gap-2">
					<IcOutlineWhatsapp />
					<span class="text-xl font-bold">(11) 91234-5678</span>
				</div>
				<div class="flex items-center justify-center gap-2">
					<IcOutlineWhatsapp />
					<span class="text-xl font-bold">(11) 91234-5678</span>
				</div>
			</div>
		</div>
	</footer>
</div> -->

<style>
	@keyframes fade-in-left {
		0% {
			transform: translateX(-50px);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
	@keyframes fade-in-right {
		0% {
			transform: translateX(50px);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
	.fade-in-left {
		animation: fade-in-left 1s cubic-bezier(0.39, 0.575, 0.565, 1) 0.5s both;
	}
	.fade-in-right {
		animation: fade-in-right 1s cubic-bezier(0.39, 0.575, 0.565, 1) 0.5s both;
	}
</style>
