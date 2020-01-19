
.DEFAULT_GOAL := default

default:
	@ echo "make migration -e NAME=\"migration name\" #  create new migration"
	@ echo "make migrate                            #  migrate DB to last revision"

migration:
	docker-compose exec pdf_parser bash -c "python manage.py makemigrations"

migrate:
	docker-compose exec pdf_parser bash -c "python manage.py migrate"

