
.PHONY: setup compute

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

setup: ## Setup environment
	virtualenv --python python3 venv

compute: ## Compute data
	. venv/bin/activate
	python compute.py
