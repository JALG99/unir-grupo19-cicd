FILE?= palabras.txt
DUP?= no

.PHONY: all $(MAKECMDGOALS) run-local

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes
	
run-local:
	python main.py $(FILE) $(DUP)