<script>
    import "../app.css";
    import { Button } from "$lib/components/ui/button/index.js";
    import MaterialSymbolsChatBubbleRounded from '~icons/material-symbols/chat-bubble-rounded'
    import MaterialSymbolsGroups2Rounded from '~icons/material-symbols/groups-2-rounded';
    import MaterialSymbolsVolunteerActivismRounded from '~icons/material-symbols/volunteer-activism-rounded'
    import MaterialSymbolsAlignHorizontalLeftRounded from '~icons/material-symbols/align-horizontal-left-rounded'
    import MaterialSymbolsShoppingCartRounded from '~icons/material-symbols/shopping-cart-rounded'
    import IcOutlineWhatsapp from '~icons/ic/outline-whatsapp'
</script>
<div class="flex flex-col w-full h-full">

    <nav class="flex-col w-full h-full flex justify-center sticky top-0 z-50">
        <ul class="flex flex-grow gap-2 px-8 py-4 bg-primary">
            <li class="p-1 items-center flex justify-start flex-1 text-primary-foreground font-bold text-2xl">Educador Físico</li>
            <li class="items-center flex justify-center">
                <Button variant="outline" class="font-bold text-xl px-8 flex gap-2" href="">
                    <span>ENTRE EM CONTATO</span>
                    <MaterialSymbolsChatBubbleRounded/>
                </Button>
            </li>
        </ul>
        <ul class="flex gap-2 justify-center w-full bg-neutral-800">
            <li class="items-center flex justify-center">
                <Button variant="link" class="text-white flex gap-2" href="#QuemSomos">
                    <MaterialSymbolsGroups2Rounded/>
                    <span>Quem Somos</span>
                </Button>
            </li>
            <li class="items-center flex justify-center">
                <Button variant="link" class="text-white flex gap-2" href="#NossosProjetos">
                    <MaterialSymbolsVolunteerActivismRounded/>
                    <span>Nossos Projetos</span>
                </Button>
            </li>
            <li class="items-center flex justify-center">
                <Button variant="link" class="text-white flex gap-2" href="">
                    <MaterialSymbolsAlignHorizontalLeftRounded/>
                    <span>Resultados</span>
                </Button>
            </li>
            <li class="items-center flex justify-center">
                <Button variant="link" class="text-white flex gap-2" href="">
                    <MaterialSymbolsShoppingCartRounded/>
                    <span>Serviços</span>
                </Button>
            </li>
    
        </ul>
    </nav>

    <section id="QuemSomos" class="w-full h-full flex gap-2 bg-neutral-100 items-center">
        <div class="flex flex-col gap-2 h-full w-full sm:w-1/2 justify-center p-8">
            <p class="text-4xl font-bold">Quem somos</p>
            <p class="text-2xl text-justify">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.</p>
        </div>
        <div class="flex flex-col h-full w-full sm:w-1/2 justify-center p-8 items-center">
            <img class="aspect-auto w-full" src="https://dummyimage.com/600x600/aaaaaa/fff&text=placeholder" alt="placeholder">
        </div>
    </section>

    <section id="NossosProjetos" class="w-full h-full flex gap-2 bg-neutral-900 items-center">
        <div class="relative flex flex-col h-full w-full sm:w-1/2 justify-center p-8 items-center">
            <img class="aspect-auto w-96 mr-32" src="https://dummyimage.com/1000x800/aaaaaa/fff&text=placeholder" alt="placeholder">
            <img class="aspect-auto w-96 ml-32" src="https://dummyimage.com/1000x800/aaaaaa/fff&text=placeholder" alt="placeholder">
            <img class="aspect-auto w-96 mr-32" src="https://dummyimage.com/1000x800/aaaaaa/fff&text=placeholder" alt="placeholder">
        </div>
        <div class="flex flex-col gap-2 h-full w-full sm:w-1/2 justify-center p-8">
            <p class="text-4xl font-bold text-neutral-100">Nossos projetos</p>
            <p class="text-2xl text-justify text-neutral-100">But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.</p>
        </div>
    </section>

    <footer class="flex gap-2 p-16 bg-primary items-center text-white text-lg">
        <div class="flex flex-col gap-4 w-full sm:w-1/2 items-start justify-center">
            <div class="flex flex-col gap-1 items-start justify-center">
                <span class="font-bold text-xl">Educador Físico</span>
                <span>CREF/SP 123456</span>
            </div>
            <div class="flex flex-col gap-1 items-start justify-center">
                <span class="font-bold text-xl">Educador Físico</span>
                <span>CREF/SP 123456</span>
            </div>
        </div>
        <div class="flex flex-col gap-4 w-full sm:w-1/2 items-end justify-center">
            <div class="flex flex-col gap-1 items-end justify-center">
                <span class="font-bold text-xl">Rua Ali Perto, 45</span>
                <span class="font-bold text-xl">Bairro Aquele, Mogi das Cruzes - SP</span>
            </div>
            <div class="flex flex-col gap-1 items-end justify-center">
                <div class="flex gap-2 items-center justify-center">
                    <IcOutlineWhatsapp/>
                    <span class="font-bold text-xl">(11) 91234-5678</span>
                </div>
                <div class="flex gap-2 items-center justify-center">
                    <IcOutlineWhatsapp/>
                    <span class="font-bold text-xl">(11) 91234-5678</span>
                </div>
            </div>
        </div>
    </footer>

</div>

