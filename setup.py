#from distutils.core import setup
from setuptools import setup
import textwrap

setup(
    name='Pybles',
    version='1.0.11',
    author='Guido Accardo',
    author_email='gaccardo@gmail.com',
    packages=['pybles'],
    url='http://pypi.python.org/pypi/Pybles/',
    license='GPLv2',
    description='Module to represent tables in the terminal using python',
    long_description=open('README.txt').read(),
    keywords="ssh networking console tools",
    classifiers = textwrap.dedent("""
        Operating System :: OS Independent
        Programming Language :: Python :: 2.7
        Topic :: System :: Systems Administration
        Topic :: System :: Networking
        Topic :: Utilities
        Topic :: Terminals
        Environment :: Console
        License :: OSI Approved :: GNU General Public License (GPL)
        """).strip().splitlines(),
    install_requires=[
        "blessings >= 1.5.1",
    ],)
