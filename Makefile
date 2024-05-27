PY_CMD=python3.10

.PHONY: deps-dev
deps-dev:
	@$(PY_CMD) -m pip install -r requirements.dev.txt

.PHONY: deps
deps: deps-dev
	@$(PY_CMD) -m pip install -r requirements.txt


.PHONY: fmt
fmt:
	@black --config=pyproject.toml .
	@autoflake --config=pyproject.toml .
	@isort .

.PHONY: fmt-check
fmt-check:
	@black --config=pyproject.toml . --check
	@autoflake --config=pyproject.toml . --check
	@isort . --check-only

.PHONY: test-unit
test-unit:
	@pytest test_unit/

.PHONY: test-e2e
test-e2e:
	@pytest test_e2e/

.PHONY: pkg-build
pkg-build:
	@rm -rf build
	@rm -rf dist
	$(PY_CMD) setup.py sdist bdist_wheel

.PHONY: pkg-test
pkg-test:
	@$(PY_CMD) -m twine upload --repository testpypi dist/*


.PHONY: pkg-prod
pkg-prod:
	@$(PY_CMD) -m twine upload dist/*