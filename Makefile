install: 
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

quick-install:
	poetry install
	poetry build
	poetry publish --dry-run
	pip install --user --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
