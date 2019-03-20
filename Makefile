database:
	python db_creator.py

requirements:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run:
	python server.py runserver

migrate:
	python manage.py

lint:
	flake8
