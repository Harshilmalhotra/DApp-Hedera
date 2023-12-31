<script lang="ts">
	import { TextInput, PasswordInput } from 'carbon-components-svelte';

	export let personalData: any = {};

	//  check if passwords match
	let passwordDoNotMatch = false;
	$: passwordDoNotMatch = personalData.pw2 && personalData.pw !== personalData.pw2 ? true : false;
</script>

<TextInput labelText="Name" placeholder="John Doe" bind:value={personalData.name} />
<TextInput labelText="Email" placeholder="john@doe.com" bind:value={personalData.email} />
<PasswordInput
	tooltipAlignment="start"
	tooltipPosition="left"
	labelText="Password"
	placeholder="Enter password..."
	bind:value={personalData.pw}
/>
<PasswordInput
	tooltipAlignment="start"
	tooltipPosition="left"
	labelText="Confirm password"
	placeholder="Enter password..."
	bind:value={personalData.pw2}
/>
{#if passwordDoNotMatch}
	<p>Passwords do not match.</p>
{/if}
