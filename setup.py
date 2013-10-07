#from distutils.core import setup
from setuptools import setup

setup(
    name='Pybles',
    version='1.0.4',
    author='Guido Accardo',
    author_email='gaccardo@gmail.com',
    mantainer='Guido Accardo',
    mantainer_email='gaccardo@gmail.com',
    home_page='http://pypi.python.org/pypi/Pybles/',
    symmary='Module to represent tables in the terminal using python',
    platform='Multiarch',
    packages=['pybles'],
    url='http://pypi.python.org/pypi/Pybles/',
    license='LICENSE.txt',
    description='Module to represent tables in the terminal using python',
    long_description=open('README.txt').read(),
    install_requires=[
        "blessings >= 1.5.1",
    ],)
