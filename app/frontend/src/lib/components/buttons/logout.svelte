<script lang="ts">
	import { Button, Form } from 'carbon-components-svelte';
</script>

<Form method="POST" action="/account?/logout">
	<Button kind="danger" type="submit">Logout</Button>
</Form>
