ifneq (,$(wildcard ./.env))
	include .env 
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose -f HashGraphHub/docker-compose.yml up -d --build --remove-orphans

build_stripe:
	docker-compose -f HashGraphHub/docker-compose.yml up -d --build stripe-cli

up:
	docker-compose -f HashGraphHub/docker-compose.yml up 

down:
	docker-compose -f HashGraphHub/docker-compose.yml down

down_v:
	docker-compose -f HashGraphHub/docker-compose.yml down -v

logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs

app_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs app

api_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs api

celery_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs celery

redis_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs redis

beat_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs beat

db_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs db

flower_logs:
	docker-compose -f HashGraphHub/docker-compose.yml logs flower

migrate:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py migrate --noinput

makemigrations:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py makemigrations

shell:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py shell

superuser:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py createsuperuser

test:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py test

config:
	docker-compose -f HashGraphHub/docker-compose.yml exec api python manage.py runscript config

prune:
	docker system prune

enter_api:
	docker exec -it api bash

enter_app:
	docker exec -it app sh
