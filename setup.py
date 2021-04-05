# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='character-reverse',
    version='0.1.5',
    author='Shen Zhang',
    author_email='zhangshen20@hotmail.com',
    description='Reverse a string',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zhangshen20/character-reverse.git',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    zip_safe=False)
