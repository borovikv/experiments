print:
	@echo "Do nothing"

install:
	pip install -r requirements.txt;

style:
	git diff master | flake8 --diff
