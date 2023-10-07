
main: clean venv run

clean:
	rm -rf venv
	rm -rf __pycache__

venv:
	python3.11 -m venv venv
	./venv/bin/pip install -r requirements.txt

mypy: venv
	./venv/bin/mypy src/main.py


run:
	./venv/bin/python3 src/main.py >> build/result.txt

