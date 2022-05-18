import sys

from {{ cookiecutter.python_module_name }}.{{ cookiecutter.python_module_name }} import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
