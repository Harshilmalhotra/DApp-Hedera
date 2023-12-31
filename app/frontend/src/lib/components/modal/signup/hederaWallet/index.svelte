<script lang="ts">
	import { Button, TextInput, PasswordInput } from 'carbon-components-svelte';
	import CreateAccount from './createAccount.svelte';
	import ImportAccount from './importAccount.svelte';
	export let hederaData: any = {};
	let type = 'import';
</script>

<!-- {#if type === 'create'}
	<CreateAccount />
{/if} -->
{#if type === 'import'}
	<ImportAccount />
{/if}

<!-- <div class="btn-container">
	<Button size="field" on:click={() => (type = 'create')}>Create Hedera Account</Button>
	<Button size="field" on:click={() => (type = 'import')} kind="secondary"
		>Import Hedera Account</Button
	>
</div> -->
<style lang="scss">
	.btn-container {
		display: flex;
		justify-content: center;
		gap: 0.5rem;
	}
</style>
