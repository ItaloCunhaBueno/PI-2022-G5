<script>
	import '../app.css';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import * as Form from '$lib/components/ui/form/index.js';
	import { Input } from '$lib/components/ui/input';
	import MaterialSymbolsChatBubbleRounded from '~icons/material-symbols/chat-bubble-rounded';
	import MaterialSymbolsGroups2Rounded from '~icons/material-symbols/groups-2-rounded';
	import MaterialSymbolsVolunteerActivismRounded from '~icons/material-symbols/volunteer-activism-rounded';
	import MaterialSymbolsAlignHorizontalLeftRounded from '~icons/material-symbols/align-horizontal-left-rounded';
	import MaterialSymbolsShoppingCartRounded from '~icons/material-symbols/shopping-cart-rounded';
	import IcOutlineWhatsapp from '~icons/ic/outline-whatsapp';
</script>

<div class="flex flex-col w-full h-full">
	<nav class="sticky top-0 z-50 flex flex-col justify-center w-full h-full">
		<ul class="flex flex-grow gap-2 px-8 py-4 bg-primary !h-24 !max-h-24">
			<li class="flex items-center justify-start flex-1 p-1 text-3xl font-bold text-primary-foreground">Educador Físico</li>
			<li class="flex items-center justify-center">
				<Button variant="outline" class="!py-3 !px-6 text-base font-bold" href="#Contato">
					<span>ENTRE EM CONTATO</span>
				</Button>
			</li>
		</ul>
		<ul class="flex justify-center w-full gap-2 bg-neutral-800 !h-16 !max-h-16">
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

	<section id="QuemSomos" class="flex flex-wrap items-center w-full !min-h-[755px] bg-neutral-100">
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

	<section id="NossosProjetos" class="flex flex-wrap items-center w-full !min-h-[755px] bg-neutral-900 text-neutral-100">
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

	<section id="Resultados" class="flex flex-col w-full !min-h-[755px] p-8 bg-neutral-100 justify-center items-center gap-14">
		<!-- <div class="flex flex-col items-center w-full gap-2"> -->
		<p class="text-4xl font-bold">Resultados</p>
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
		<!-- </div> -->
	</section>

	<section id="Servicos" class="flex flex-col w-full !min-h-[755px] gap-14 p-8 bg-neutral-900 text-neutral-100 justify-center">
		<p class="text-4xl font-bold">Nossos serviços</p>
		<div class="flex items-center justify-center w-full gap-4">
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

	<section id="Contato" class="flex justify-center w-full !min-h-[755px] p-8 bg-neutral-100">
		<div class="flex flex-wrap w-full overflow-hidden rounded-lg lg:max-w-[60%]">
			<img class="object-cover w-full h-96 lg:w-auto lg:h-auto" src="https://dummyimage.com/475x732/aaaaaa/fff&text=placeholder" alt="" />
			<div class="flex flex-col justify-center flex-grow !min-w-[645px] !min-h-[732px] gap-2 p-8 text-xl text-white bg-primary">
				<p class="text-5xl font-bold">Entre em contato</p>
				<p>Informe seu e-mail ou telefone e retornaremos o mais breve possível.</p>
				<div class="flex flex-col gap-2 mt-4 text-2xl">
					<span class="font-bold">Nome</span>
					<Input class="h-14" type="text" id="nome" placeholder="Digite seu nome." />
					<span class="mt-2 font-bold">Telefone ou e-mail</span>
					<Input class="h-14" type="text" placeholder="Digite seu telefone ou e-mail." />
					<span class="mt-2 font-bold">Mensagem</span>
					<Textarea class="h-44" placeholder="Mensagem..." />
					<Button variant="outline" class="!py-3 !px-6 text-base font-bold text-black">ENVIAR</Button>
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
</div>
