<script lang="ts">
	import {
		ComposedModal,
		ModalHeader,
		ModalBody,
		ModalFooter,
		TextInput,
		PasswordInput
	} from 'carbon-components-svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	const switchToSignUp = () => {
		dispatch('switchToSignUp', null);
	};

	export let open: boolean;

	let checked = false;
	let email = '';
	let pw = '';

	const submit = (e) => {
		console.log(e);
	};

	$: checked = email && pw ? true : false;
</script>

<ComposedModal bind:open on:submit={submit} preventCloseOnClickOutside>
	<ModalHeader label="Sign in" title="Login to your account" />
	<ModalBody hasForm>
		<TextInput labelText="Email" placeholder="john@doe.com" bind:value={email} />
		<PasswordInput
			tooltipAlignment="start"
			tooltipPosition="left"
			labelText="Password"
			placeholder="Enter password..."
			bind:value={pw}
		/>
	</ModalBody>
	<ModalFooter
		secondaryButtonText={"Don't have an account? Sign up"}
		on:click:button--secondary={switchToSignUp}
		primaryButtonText="Proceed"
		primaryButtonDisabled={!checked}
	/>
</ComposedModal>
