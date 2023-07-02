install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest .

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendif

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build