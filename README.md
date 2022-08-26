# Python Best Practices Cookiecutter

Best practices [cookiecutter](https://github.com/audreyr/cookiecutter) template as described in this [blogpost](https://sourcery.ai/blog/python-best-practices/).

## Features

- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hook that runs in :
  - pre-commit : Formatting and Sorting

- Deployment ready with [Docker](https://docker.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
  - on pull request / push
    - Linting and Static typing
    - Testing
    - Deployment Readiness
  - on push main branch
    - Release using semantic-release

## Quickstart

```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Explore code in jupyter notebook running in a docker container using vscode devcontainer feature :
pipx run cookiecutter gh:Julien-Fruteau/python-best-practices-cookiecutter --checkout jupyter-vscode-devcontainer
```


## Cookiecutter variables

- **project_name** : as displayed as the header of the repo README
- **repo_name** : the github slug, spaces are replaced automatically by dashes "-"
- **module_name** : the python module name, cannot have spaces nor dashes "-", hence replaced by underscores "_"
- **github_user_name** : used to set-up your local git config
- **github_organization** : default to user name but can be replaced if you are targetting an organization repo usage
- **github_user_email** : used to set-up your local git config
- **github_host** : used to configure the github remote origin hostname. Defaults to github.com. This can be useful if you use a [ssh-config-file](https://linuxize.com/post/using-the-ssh-config-file/) in order to address multiple github account from a single localhost (github does not allow the same public ssh key to be used by multiple accounts)
