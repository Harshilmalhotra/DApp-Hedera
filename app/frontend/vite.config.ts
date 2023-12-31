import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()]
	// server: {
	//     watch: {
	//         usePolling: true,
	//     },
	//     host: true,
	//     strictPort: true,
	//     port: 4173,
	// }
};

export default config;
