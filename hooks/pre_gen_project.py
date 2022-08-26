import re
import sys

REPO_REGEX = r"^[a-zA-Z][-_a-zA-Z0-9]+$"
repo_name = "{{ cookiecutter.repo_name }}"
if not re.match(REPO_REGEX, repo_name):
    print("ERROR: %s is not a valid Python repo name!" % repo_name)
    sys.exit(1)

