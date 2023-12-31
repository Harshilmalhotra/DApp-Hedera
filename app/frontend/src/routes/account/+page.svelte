<script lang="ts">
	import { Grid, Row, Column } from 'carbon-components-svelte';
	import ImportWallet from '$lib/components/forms/importWallet.svelte';
	import Logout from '$lib/components/buttons/logout.svelte';
	import type { PageData, ActionData } from './$types';

	export let data: PageData;
	export let form: ActionData;
	console.log('Page data', data);

	console.log('Form data', form);
</script>

<Grid fullWidth>
	{#if form}
		<Row>
			<Column>
				<h2>Account {form.external_id} added!</h2>
			</Column>
		</Row>
	{/if}
	<Row>
		<Column>
			<ImportWallet />
		</Column>
	</Row>
	<Row padding>
		<Column>
			<Logout />
		</Column>
	</Row>
</Grid>

<style lang="scss">
	// :global(.bx--grid) {
	// 	padding-left: 1rem !important;
	// 	padding-right: 1rem !important;
	// }
</style>
