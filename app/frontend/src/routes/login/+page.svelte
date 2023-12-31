<script lang="ts">
	import {
		ComposedModal,
		ModalHeader,
		ModalBody,
		ModalFooter,
		Form,
		Button,
		TextInput,
		PasswordInput
	} from 'carbon-components-svelte';

	let email = '';
	let pw = '';

	$: disabled = email && pw ? false : true;
</script>

<!-- <ComposedModal bind:open on:submit={submit} preventCloseOnClickOutside>
	<ModalHeader label="Sign in" title="Login to your account" />
	<ModalBody hasForm> -->
<Form method="POST" action="?/login">
	<TextInput labelText="Email" name="email" placeholder="john@doe.com" bind:value={email} />
	<PasswordInput
		tooltipAlignment="start"
		tooltipPosition="left"
		name="password"
		labelText="Password"
		placeholder="Enter password..."
		bind:value={pw}
	/>
	<Button type="submit" {disabled}>Log In</Button>
</Form>
