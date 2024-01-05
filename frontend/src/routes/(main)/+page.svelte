<script lang="ts">
  import { enhance } from '$app/forms';
  import { goto } from '$app/navigation';
  import type { PageData } from './$types';
  export let data: PageData;
</script>

<main class="p-4">
  <h1 class="text-5xl text-center mb-6">Recommendations</h1>
  <div class="grid grid-cols-1 md:grid-cols-5 gap-4 p-4">
    {#each data.movies as movie}
      <div class="card bg-base-100 shadow-xl">
        <figure>
          <img src="https://image.tmdb.org/t/p/original{movie.poster_path}" alt="Shoes" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">{movie.title}</h2>
          <p>{movie.overview}</p>
          <div class="card-actions">
            <form
              method="POST"
              use:enhance={() => {
                return async ({ result }) => {
                  if (result.type === 'redirect') {
                    // redirect without invalidating
                    await goto(result.location);
                  }
                };
              }}
            >
              <input name="id" type="hidden" value={movie.id} />
              <div class="rating align-middle">
                <input type="radio" name="stars" class="rating-hidden" checked />
                <input type="radio" name="stars" value="1" class="mask mask-star" />
                <input type="radio" name="stars" value="2" class="mask mask-star" />
                <input type="radio" name="stars" value="3" class="mask mask-star" />
                <input type="radio" name="stars" value="4" class="mask mask-star" />
                <input type="radio" name="stars" value="5" class="mask mask-star" />
              </div>
              <button type="submit" class="btn btn-primary ms-4">Save</button>
            </form>
          </div>
        </div>
      </div>
    {/each}
  </div>
  <div class="flex justify-center">
    <button class="btn btn-primary" on:click={() => goto('/', { invalidateAll: true })}
      >More Recommendations</button
    >
  </div>
</main>
