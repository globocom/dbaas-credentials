.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc
	rm -fr htmlcov/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 dbaas_credentials tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source dbaas_credentials setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/dbaas_credentials.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ dbaas_credentials
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

release_globo:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://artifactory.globoi.com/artifactory/api/pypi/pypi-local dist/*

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

fake_deploy:
	rm /Users/$(USER)/.virtualenvs/dbaas/lib/python2.7/site-packages/dbaas_credentials/*.pyc
	cp -r dbaas_credentials/ /Users/$(USER)/.virtualenvs/dbaas/lib/python2.7/site-packages/dbaas_credentials/
