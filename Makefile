PYTHON2_PATH=`which python2.7`

.PHONY: help clean delpyc tests flake quality

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  delpyc              -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  clean               -- to clean local repository from all stuff created during development"
	@echo "  flake               -- to launch Flake8 checking on boussole code (not the tests)"
	@echo "  tests               -- to launch tests using py.test"
	@echo "  quality             -- to launch Flake8 checking and tests with py.test"
	@echo "  release             -- to release new package on Pypi (WARNING)"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf dist emencia_django_bazar.egg-info project_test/.cache/ project_test/tests/__pycache__/

flake:
	flake8 --show-source bazar

tests:
	py.test -vv project_test/

quality: tests flake

release:
	python setup.py sdist
	python setup.py sdist upload
