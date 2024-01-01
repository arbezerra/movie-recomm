restart: down up

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	docker compose -f test-docker-compose.yml up --build --exit-code-from test

