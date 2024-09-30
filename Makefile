install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff check *.py

format:	
	black *.py 

test:
	python -m pytest -cov=main main_test.py
		
all: install lint format test

extract:
	python python_main.py extract

load: 
	python python_main.py load