all: create-venv install-deps

create-venv:
	python3 -m venv venv
	@echo "Virtual environment created!"

install-deps:
	venv/bin/pip install -r requirements.txt

0:
	@venv/bin/python3 src/ex00.py

1:
	@venv/bin/python3 src/ex01.py

2:
	@venv/bin/python3 src/ex02.py

3:
	@venv/bin/python3 src/ex03.py

4:
	@venv/bin/python3 src/ex04.py

5:
	@venv/bin/python3 src/ex05.py