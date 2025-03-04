#setup package a local package

from setuptools import find_packages, setup
setup(
    name = 'Genarative Ai Projects',
    version = '0.0.0',
    author = 'Ashutosh Chaudhary',
    autjor_email = 'ashutosh.chaudhary790@gmail.com',
    package = find_packages(),  # it will find __init__.py and when it present it consider it as a local package.
    install_requires = []
)