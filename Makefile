.PHONY: setup-venv clean-pyc clean-test test style lint checks

SRC_CODE:="src"
COVERAGE_THRESH:=55

help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment."
	@echo "\tclean:            cleans all unnecessary files."
	@echo "\ttest:             runs Pytest."
	@echo "\tstyle:            executes style, lint and type formatting."
	@echo "\tchecks:           executes tests and style (RECOMMENDEED)."
	@echo ""


setup-venv: # Create virtual env. You have to run this first!
	python3 -m venv venv && . venv/bin/activate
	pip install --upgrade pip
	pip install -e ".[dev]"


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc clean-test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test: clean # src is the source code
	. venv/bin/activate \
	&& pytest -svv --cov=${SRC_CODE} --cov-report=term-missing \
	--cov-fail-under ${COVERAGE_THRESH}

style:
	. venv/bin/activate && pylint ${SRC_CODE} && mypy ${SRC_CODE}

lint:
	. venv/bin/activate && black ${SRC_CODE} && isort ${SRC_CODE}

checks: test lint style clean
