<script>
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
	import { cn } from "$lib/utils.js.js";
	let className = undefined;
	export { className as class };
</script>

<DropdownMenuPrimitive.Separator
	class={cn("bg-muted -mx-1 my-1 h-px", className)}
	{...$$restProps}
/>
