# Movie Recommender System

This is a POC of a movie recommendation system. It uses a Content-Based
approach by mapping the movie features into a 2d space using UMAP, then
with a SVR it predicts the 5 star rating based on the user's previus ratings.

## Usage

1. Copy the env file and change the values accordingly.

```bash
cp .env.example .env
```

2. Then start the services with:

```bash
make up
```

3. Open [http://localhost:5173](http://localhost:5173) in your browser.

4. Create an account

5. Rate the movies. Firstly, the system will recommend randomly.
From 3 rated movies it will recommend based on your preference.

## Tests

You can start the tests using

```bash
make test
```
