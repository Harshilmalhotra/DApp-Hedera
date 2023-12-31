import type { Actions } from './$types';
import { PUBLIC_API } from '$env/static/public';
import { redirect, error } from '@sveltejs/kit';

export const actions = {
	default: async ({ cookies, request, fetch }) => {
		const formData = await request.formData();
		const first_name = formData.get('first_name');
		const last_name = formData.get('last_name');
		const email = formData.get('email');
		const password = formData.get('password');

		const body = JSON.stringify({ email, password, first_name, last_name });

		console.log(body);

		const response = await fetch(`${PUBLIC_API}/auth/users/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body
		}).catch((e) => {
			console.log('fetch error');
			console.error(e);
			throw error(500, String(e));
		});

		// if (!response.ok) throw error(500, 'Error fetching /auth/users end point');
		const json = await response.json();
		console.log(json);
		const { status } = response;

		if (status === 201) {
			return {
				success: true,
				message: 'Sign up successful. Please check your email for a verification link.'
			};
		} else {
			return {
				success: false,
				message: JSON.stringify(json)
			};
		}
	}
} satisfies Actions;
