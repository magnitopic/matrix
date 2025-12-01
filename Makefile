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

6:
	@venv/bin/python3 src/ex06.py

7:
	@venv/bin/python3 src/ex07.py

8:
	@venv/bin/python3 src/ex08.py

9:
	@venv/bin/python3 src/ex09.py

10:
	@venv/bin/python3 src/ex10.py

11:
	@venv/bin/python3 src/ex11.py

12:
	@venv/bin/python3 src/ex12.py

13:
	@venv/bin/python3 src/ex13.py

14:
	@venv/bin/python3 src/ex14.py

15:
	@venv/bin/python3 src/ex15.py