import { redirect, type Actions } from "@sveltejs/kit";
import api from '$lib/api';

export const actions: Actions = {
    default: async ({ request, cookies }) => {
        const data = await request.formData();
        const result: { ok: boolean, error: string | undefined } = {
            ok: true,
            error: undefined,
        }

        if (!data.get('email') || !data.get('password')) {
            result.ok = false;
            result.error = "Email or passwor invalid";
            return result;
        }

        const response = await api.post('auth', {
            email: data.get('email'),
            password: data.get('password')
        });

        if (response.status !== 200) {
            result.ok = false;
            result.error = "Email and password doesn't match"
            return result;
        }

        const token = await response.json();

        cookies.set('token', token.token, { path: '/' });

        throw redirect(302, '/');

    }

};
