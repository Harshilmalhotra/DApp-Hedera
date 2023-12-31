<script lang="ts">
	import 'carbon-components-svelte/css/all.css';

	import {
		Header,
		HeaderUtilities,
		HeaderAction,
		HeaderPanelLinks,
		HeaderPanelDivider,
		HeaderPanelLink,
		SideNav,
		SideNavItems,
		SideNavMenu,
		SideNavMenuItem,
		SideNavLink,
		SkipToContent,
		Content,
		Theme
	} from 'carbon-components-svelte';
	import SettingsAdjust from 'carbon-icons-svelte/lib/SettingsAdjust.svelte';
	import UserAvatarFilledAlt from 'carbon-icons-svelte/lib/UserAvatarFilledAlt.svelte';
	import Signup from '$lib/components/modal/signup/index.svelte';
	import Login from '$lib/components/modal/login.svelte';

	let isSideNavOpen = false;
	let isOpen1 = false;
	let isOpen2 = false;
	let okay = false;

	let signUpOpen = false;
	let logInOpen = false;

	const switchToLogin = (event: CustomEvent) => {
		signUpOpen = false;
		logInOpen = true;
	};

	const switchToSignup = (event: CustomEvent) => {
		signUpOpen = true;
		logInOpen = false;
	};
</script>

<Signup on:switchToLogin={switchToLogin} bind:open={signUpOpen} />
<Login on:switchToSignUp={switchToSignup} bind:open={logInOpen} />

<Header company="IBM" platformName="Carbon Svelte" bind:isSideNavOpen>
	<svelte:fragment slot="skip-to-content">
		<SkipToContent />
	</svelte:fragment>
	<HeaderUtilities>
		<div class="toggle-theme">
			<Theme
				render="toggle"
				toggle={{
					themes: ['g10', 'g90'],
					labelA: 'Enable dark mode',
					labelB: 'Enable dark mode',
					hideLabel: true,
					size: 'sm'
				}}
				persist
				persistKey="__carbon-theme"
			/>
		</div>

		<HeaderAction bind:isOpen={isOpen1} icon={SettingsAdjust}>
			<HeaderPanelLinks>
				<HeaderPanelDivider>Theme</HeaderPanelDivider>
				<HeaderPanelLink>Hello</HeaderPanelLink>
			</HeaderPanelLinks>
		</HeaderAction>

		<HeaderAction icon={UserAvatarFilledAlt} bind:isOpen={isOpen2}>
			<HeaderPanelLinks>
				<HeaderPanelDivider>Authentication</HeaderPanelDivider>
				<HeaderPanelLink href="/login">Log in</HeaderPanelLink>
				<HeaderPanelLink href="/signup">Register</HeaderPanelLink>

				<HeaderPanelDivider>Switcher subject 2</HeaderPanelDivider>
				<HeaderPanelLink>Switcher item 1</HeaderPanelLink>
				<HeaderPanelLink>Switcher item 2</HeaderPanelLink>
				<HeaderPanelLink>Switcher item 3</HeaderPanelLink>
				<HeaderPanelLink>Switcher item 4</HeaderPanelLink>
				<HeaderPanelLink>Switcher item 5</HeaderPanelLink>
			</HeaderPanelLinks>
		</HeaderAction>
	</HeaderUtilities>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
	<SideNavItems>
		<SideNavLink href="/account" text="My Account" />
		<SideNavLink text="Link 2" />
		<SideNavLink text="Link 3" />
		<SideNavMenu text="Menu">
			<SideNavMenuItem href="/info" text="INfo" />
			<SideNavMenuItem href="/" text="Link 2" />
			<SideNavMenuItem href="/" text="Link 3" />
		</SideNavMenu>
	</SideNavItems>
</SideNav>

<Content>
	<slot />
</Content>

<style lang="scss">
	.toggle-theme {
		display: inline-block;
		// justify-content: center;
		// align-items: center;
		margin-top: 14px;
		margin-right: 14px;
		padding: 0;
		border: 0;
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		background: none;
		width: 156px;
	}
</style>
