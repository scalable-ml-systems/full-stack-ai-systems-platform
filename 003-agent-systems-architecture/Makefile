.PHONY: install test type-check lint format validate

install:
	python -m pip install --upgrade pip setuptools wheel
	pip install -e ".[dev]"

test:
	pytest

type-check:
	mypy agent_control_plane workflow_profiles tests

lint:
	ruff check agent_control_plane workflow_profiles tests

format:
	ruff format agent_control_plane workflow_profiles tests

validate: lint type-check test
