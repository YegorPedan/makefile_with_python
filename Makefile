
main: clean venv run

clean:
	rm -rf venv
	rm -rf __pycache__
	rm -rf .mypy_cache

venv:
	python3.11 -m venv venv
	./venv/bin/pip install -r requirements.txt

mypy: venv
	./venv/bin/mypy src/main.py
	./venv/bin/mypy tests/test_main.py

pylint: venv
	./venv/bin/pylint src/main.py
	./venv/bin/pylint tests/test_main.py

pytest: venv
	./venv/bin/pytest tests/test_main.py


run:
	./venv/bin/python3 src/main.py >> build/result.txt

