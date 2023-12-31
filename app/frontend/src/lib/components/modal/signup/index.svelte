<script lang="ts">
	import {
		ComposedModal,
		ModalHeader,
		ModalBody,
		ModalFooter,
		TextInput,
		PasswordInput,
		ProgressIndicator,
		ProgressStep
	} from 'carbon-components-svelte';
	import PersonalData from './personalData/index.svelte';
	import HederaWallet from './hederaWallet/index.svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	const switchToLogin = () => {
		dispatch('switchToLogin', true);
	};

	export let open: boolean;

	let checked = false;
	let formContent: any = {
		personalData: {},
		hederaData: {}
	};
	let currentIndex = 0;

	const submit = (e: Event) => {
		e.preventDefault();
		switch (currentIndex) {
			case 0:
				currentIndex = 1;
				break;
			default:
				console.log('SUBMITTED');
		}
	};

	// check if all fields are filled
	$: checked =
		formContent.personalData.name &&
		formContent.personalData.email &&
		formContent.personalData.pw &&
		formContent.personalData.pw2 &&
		formContent.personalData.pw === formContent.personalData.pw2
			? true
			: false;
</script>

<ComposedModal bind:open on:submit={submit} preventCloseOnClickOutside>
	<ModalHeader label="Sign up" title="Create an account">
		<ProgressIndicator {currentIndex} spaceEqually>
			<ProgressStep
				complete
				label="Step 1"
				description="The progress indicator will listen for clicks on the steps"
			/>
			<ProgressStep
				complete
				label="Step 2"
				description="The progress indicator will listen for clicks on the steps"
			/>
		</ProgressIndicator>
	</ModalHeader>

	<ModalBody hasForm>
		{#if currentIndex === 0}
			<PersonalData bind:personalData={formContent.personalData} />
		{/if}
		{#if currentIndex === 1}
			<HederaWallet bind:hederaData={formContent.hederaData} />
		{/if}
	</ModalBody>
	<ModalFooter
		secondaryButtonText={'Already have an account? Sign in'}
		on:click:button--secondary={switchToLogin}
		primaryButtonText="Proceed"
		primaryButtonDisabled={!checked}
	/>
</ComposedModal>

<style lang="scss">
	:global(.bx--form-item) {
		margin-bottom: 1rem;
	}
</style>
