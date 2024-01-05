import { env } from '$env/dynamic/private';

const base = env.API_URL || 'http://127.0.0.1:8000';

async function send(method: string, path: string, data?: any, token?: string) {
	return await fetch(`${base}/${path}`, {
		method: method,
		headers: {
			'Content-Type': 'application/json',
			Authorization: token ? `Bearer ${token}` : ''
		},
		body: data ? JSON.stringify(data) : undefined
	});
}

const api = {
	get: (path: string, token?: string) => {
		return send('GET', path, undefined, token);
	},

	del: (path: string, token?: string) => {
		return send('DELETE', path, undefined, token);
	},

	post: (path: string, data: any, token?: string) => {
		return send('POST', path, data, token);
	},

	put: (path: string, data: any, token?: string) => {
		return send('PUT', path, data, token);
	}
};

export default api;
