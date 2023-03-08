from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.3'
DESCRIPTION = 'This package refers to the topic of automata theory, which includes DFA, NDFA, Mealy machines, Moore machines and Finite state machine.'

# Setting up
setup(
    name="AutomaPy",
    version=VERSION,
    author="Mohammed Varaliya",
    author_email="<mohammedvaraliya2661392@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'DFA', 'NDFA',
              'Mealy machines', 'Moore machines', 'Automata', 'Theory of Computation', 'Finite State Machine', 'Finite Automaton'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
