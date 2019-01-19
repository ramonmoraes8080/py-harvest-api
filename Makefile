.PHONY: tests
.ONSHELL:

loglevel=DEBUG
python=$$PWD/env/bin/python

export HARVEST_PA_ACCOUNT_ID=your_personalaccount_id
export HARVEST_PA_TOKEN=your_personalaccount_token

build:
	$(python) setup.py sdist bdist_wheel

tests:
	$(python) -m unittest tests
