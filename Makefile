setup-environment:
	@echo "Create conda environment for use case - activate with conda activate"
	@conda env create -f environment.yaml

setup-src:
	@echo "Installing src in development mode for use anywhere in this environment"
	pip install -e .

create-requirements:
	@echo "Create requirements.txt excluding custom packages"
	pip list --format=freeze > requirements.txt --exclude-editable

run-pre-commit:
	@echo "Run all files in repository through pre-commit"
	pre-commit run --all-files
