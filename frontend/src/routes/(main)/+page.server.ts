import type { PageServerLoad } from './$types';
import { redirect } from "@sveltejs/kit";
import api from '$lib/api';

export const load: PageServerLoad = async ({locals}) => {
    const response = await api.post('/recommend', {}, locals.token);
    console.log(response.status);
    if (response.status === 403) {
        throw redirect(302, '/logout');
    }
    return await response.json();
};
