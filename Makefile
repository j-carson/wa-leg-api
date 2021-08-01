.PHONY: venv_check install stubs test docs


venv_check:
	@if test $(origin VIRTUAL_ENV) == undefined; then echo 'NOT IN VIRTUAL ENVIRONMENT!' && exit 1; fi
	@echo venv dir is  $(VIRTUAL_ENV)
	
install: venv_check
	pip install -e .

stubs: venv_check
	pip install -e .[dev]
	cd wa_leg_api && python make_stubs.py 
	# initial auto-generated stubs won't pass, but second time through should work
	pre-commit run --all-files || pre-commit run --all-files

test: venv_check
	pip install -e .[dev]
	pre-commit run --all-files
	pytest tests


docs: venv_check
	pip install -e .[docs]
	$(MAKE) -C docs html
