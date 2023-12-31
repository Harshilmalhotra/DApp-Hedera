import type { PageServerLoad, Actions } from './$types';
import { redirect, error } from '@sveltejs/kit';
import { PUBLIC_API } from '$env/static/public';
import { PrivateKey } from '@hashgraph/sdk';

export const load = (async ({ cookies }) => {
	const auth_token = cookies.get('auth_token');
	if (auth_token) {
		return {
			props: {
				auth_token
			}
		};
	} else {
		throw redirect(303, '/login');
	}
}) satisfies PageServerLoad;

export const actions = {
	importWallet: async ({ cookies, request, fetch }) => {
		const formData = await request.formData();
		const private_key = formData.get('private_key');
		const external_id = formData.get('external_id');
		const body = JSON.stringify({ external_id, private_key });
		const response = await fetch(`${PUBLIC_API}/account/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Token ${cookies.get('auth_token')}`
			},
			body
		});
		const { status } = response;
		console.log('status', status);
		if (status === 200) {
			const json = await response.json();
			console.log(json);
			return json;
		} else {
			const html = await response.text();
			// return { html };
			throw error(status, html);
		}
	},

	logout: async ({ cookies, request, fetch }) => {
		const response = await fetch(`${PUBLIC_API}/auth/token/logout/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Token ${cookies.get('auth_token')}`
			}
		});

		if (!response.ok) throw error(500, 'Internal Server Error. Failed to fetch logout endpoint.');
		const { status } = response;
		if (status === 204) {
			cookies.delete('auth_token');
			redirect(303, '/');
		} else {
			const json = await response.json();
			throw error(status, json);
		}
	}
} satisfies Actions;
