<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData } from './$types';
  export let form: ActionData;
</script>

<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
  <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
    <form method="POST" use:enhance>
      <h1 class="text-5xl font-bold text-center">Login</h1>
      <label class="form-control mt-2">
        <div class="label">
          <span class="label-text">Email</span>
        </div>
        <input name="email" type="email" class="input input-bordered w-full" />
      </label>
      <label class="form-control mt-2">
        <div class="label">
          <span class="label-text">Password</span>
        </div>
        <input name="password" type="password" class="input input-bordered w-full" />
      </label>
      <button class="btn btn-primary btn-block mt-4">Login</button>
      <div class="py-4 text-center">
        <a href="/register" class="link">Create new account</a>
      </div>
      {#if form?.ok === false}
        <div role="alert" class="alert alert-error">
          <span>{form.error}</span>
        </div>
      {/if}
    </form>
  </div>
</div>
