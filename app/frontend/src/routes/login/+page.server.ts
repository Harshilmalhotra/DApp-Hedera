import type { Actions } from './$types';
import { PUBLIC_API } from '$env/static/public';
import { redirect, error } from '@sveltejs/kit';

export const actions = {
	login: async ({ cookies, request, fetch }) => {
		const formData = await request.formData();
		const email = formData.get('email');
		const password = formData.get('password');

		const body = JSON.stringify({ email, password });
		const response = await fetch(`${PUBLIC_API}/auth/token/login/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body
		});
		if (!response.ok) throw error(500, 'Error fetching /token/login end point');
		const { status } = response;
		console.log(status, 'status');
		if (status === 200) {
			const json = await response.json();
			const { auth_token } = json;
			cookies.set('auth_token', auth_token);
			throw redirect(302, '/account');
		} else {
			throw error(500, 'Failed to get auth token');
		}
	},

	logout: async ({ cookies, request, fetch }) => {}
} satisfies Actions;
