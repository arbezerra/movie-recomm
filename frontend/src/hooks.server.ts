import { env } from '$env/dynamic/private';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	const token = event.cookies.get('token');

	if (token) {
		const jwt = JSON.parse(atob(token.split('.')[1]));
		if (Date.now() / 1000 < jwt.exp) {
			event.locals.token = token;
		} else {
			event.cookies.delete('token', { path: '/' });
		}
	}
	return await resolve(event);
};
