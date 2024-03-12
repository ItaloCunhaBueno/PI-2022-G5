<script>
    import "../app.css";
    import { Button } from "$lib/components/ui/button/index.js";
</script>

<div class="absolute flex flex-col flex-grow gap-2 p-2 bottom-0 top-0 left-0 right-0">
    <div class="flex p-2 rounded bg-neutral-100">
        <ul class="flex flex-grow gap-2">
            <li class="p-1 items-center flex justify-start flex-1">Pedro</li>
            <li class="items-center flex justify-center"><Button variant="outline" href="/">Inicio</Button></li>
            <li class="items-center flex justify-center"><Button variant="outline" href="/sobre">Sobre</Button></li>
            <li class="items-center flex justify-center"><Button variant="outline" href="/contato">Contato</Button></li>
        </ul>
    </div>
    <div class="flex flex-col flex-1 p-2 rounded bg-neutral-100">
        <slot/>
    </div>
</div>