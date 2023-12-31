<script lang="ts">
	import {
		TextInput,
		PasswordInput,
		Form,
		Button,
		Grid,
		Row,
		Column
	} from 'carbon-components-svelte';

	import InfoModal from '$lib/components/modal/infoModal.svelte';

	import type {ActionData} from "./$types"

	export let personalData: any = {
		firstName: '',
		lastName: '',
		email: '',
		pw: '',
		pw2: ''
	};

	//  check if passwords match
	let passwordDoNotMatch = false;
	$: passwordDoNotMatch = personalData.pw2 && personalData.pw !== personalData.pw2 ? true : false;
	$: disabled =
		personalData.firstName &&
		personalData.lastName &&
		personalData.email &&
		personalData.pw &&
		personalData.pw2 &&
		!passwordDoNotMatch
			? false
			: true;

	export let form: ActionData

	let formSubmitModal = false

	$: console.log(form)

</script>


{#if form !== null}
<InfoModal
	heading="Form submitted"
	content={form.message}
/>
{/if}

<Form method="POST">
	<Grid noGutter fullWidth>
		<Row>
			<Column>
				<TextInput
					labelText="First Name"
					placeholder="John"
					name="first_name"
					bind:value={personalData.firstName}
				/>
			</Column>
			<Column>
				<TextInput
					labelText="Last Name"
					placeholder="Doe"
					name="last_name"
					bind:value={personalData.lastName}
				/>
			</Column>
		</Row>
	</Grid>

	<TextInput
		labelText="Email"
		name="email"
		placeholder="john@doe.com"
		bind:value={personalData.email}
	/>
	<PasswordInput
		tooltipAlignment="start"
		tooltipPosition="left"
		labelText="Password"
		placeholder="Enter password..."
		name="password"
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

	<Button type="submit" {disabled}>Sign Up</Button>
</Form>
