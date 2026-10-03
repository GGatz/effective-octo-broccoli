.PHONY: status day test run

status:
	python scripts/status.py

# usage: make day N=2
day:
	python -m pytest -m day$(N) -q

test:
	python -m pytest -q

run:
	python -m quartermaster
