.PHONY: setup-venv clean-pyc clean-test test style_n_lint checks

SRC_CODE:="src"
COVERAGE_THRESH:=55

help:
	@echo "Commands:"
	@echo "\tsetup_venv:          creates a virtual environment."
	@echo "\tclean:               cleans all unnecessary files."
	@echo "\ttest:                runs Pytest."
	@echo "\tstyle_n_lint:        executes style, lint and type formatting."
	@echo "\tchecks:              executes tests and style (RECOMMENDEED)."
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

style_n_lint:
	. venv/bin/activate && ruff ${SRC_CODE} --fix && mypy ${SRC_CODE}

checks: test clean style_n_lint
