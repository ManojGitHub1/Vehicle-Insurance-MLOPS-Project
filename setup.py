# -e .
# local package gets installed in our env (e.g:- src folder)
# setup.py and pyproject.toml should be present in the same folder (helps in package installation)
# So the modules/functions in src folder can be imported/communicated in other places (outside src folder)

from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Manoj jivanagi",
    author_email="jjivanagimanoj@gmail.com",
    packages=find_packages()
)