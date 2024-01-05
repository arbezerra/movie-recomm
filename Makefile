restart: down up

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	docker compose -f docker-compose.test.yml up --build --exit-code-from test

train:
	docker compose -f docker-compose.train.yml run --build train
