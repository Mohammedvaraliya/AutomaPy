from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'This package refers to the topic of automata theory, which includes DFA, NDFA, Mealy machines, and Moore machines.'
LONG_DESCRIPTION = 'The package contains a set of tools and algorithms for theoretical computer science, which could include automata theory as well as other topics.'

# Setting up
setup(
    name="theorytoolkit",
    version=VERSION,
    author="Mohammed Varaliya",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'DFA', 'NDFA',
              'Mealy machines', 'Moore machines', 'Automata', 'Theory of Computation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
