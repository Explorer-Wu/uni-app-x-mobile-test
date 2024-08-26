init:
	poetry install

test:
	poetry run pytest --cov=./ --cov-report=xml

.PHONY: init test