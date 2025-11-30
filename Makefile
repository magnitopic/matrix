all: create-venv install-deps

create-venv:
	python3 -m venv venv
	@echo "Virtual environment created!"

install-deps:
	venv/bin/pip install -r requirements.txt
