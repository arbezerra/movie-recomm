import type { PageServerLoad } from './$types';
import { redirect, type Actions } from "@sveltejs/kit";
import api from '$lib/api';

export const load: PageServerLoad = async ({ locals }) => {
    const response = await api.post('/recommend', {}, locals.token);
    console.log(response.status);
    if (response.status === 403) {
        throw redirect(302, '/logout');
    }
    return await response.json();
};

export const actions: Actions = {
    default: async ({ request, locals }) => {
        const data = await request.formData();
        const id = data.get('id');
        const stars = data.get('stars');
        console.log(data);
        if (stars === 'on') {
            return { ok: true }
        }
        const response = await api.post(`/movie/${id}/star`, { stars }, locals.token);

        console.log(await response.text());

        if (response.status === 403) {
            throw redirect(302, '/logout');
        }

        return {
            ok: true
        }
    }

};
