SHELL:=/bin/bash

install-dev: ## Install dev dependencies
	@echo installing python venv with python version {python_version}
	@pipenv install --dev --python "{python_version}"

git-init: ## Init repo
	@echo "Initialize git repo"
	@git init
# git-config: ## Configure git repo
	@echo "Commit README"
	@git add README.md
	@git commit -m "first commit"
	@echo "Switch from master to main branch"
	@git branch -M main
	@echo "Set-up local git config user name "{{ cookiecutter.github_user_name }}" and email "{{ cookiecutter.github_user_email }}""
	@git config --local user.name "{{ cookiecutter.github_user_name }}"
	@git config --local user.email "{{ cookiecutter.github_user_email }}"
	@echo "Set-up remote git origin git@github.com:"{{ cookiecutter.github_organization }}"/"{{ cookiecutter.repo_name}}".git"
	@git remote add origin git@github.com:"{{ cookiecutter.github_organization }}"/"{{ cookiecutter.repo_name}}".git

git-config: ## Configure git hooks from .githooks folder
	@echo "Configure git pre-commit hooks with local .githooks folder"
	@git config core.hooksPath .githooks

git-post-init-commit: ## Git commit
	@echo "Make post init commit"
	@git add . && \
	 git commit -m "chore(setup): done"
	@echo "Local: Setup Complete"
	@echo "TODO : Create remote repo git@github.com:"{{ cookiecutter.github_organization }}"/"{{ cookiecutter.repo_name}}""

fmt: ## Format
	@pipenv run isort . && \
	 pipenv run black .

analysis: ## Run flake8 and typecheck analysis
	@pipenv run flake8 --exclude node_modules && \
	 pipenv run mypy

init: install-dev git-init git-config git-post-init-commit## Check prerequesites, init-repo, and set up git config

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

objects:= @ls modules

.PHONY: all
