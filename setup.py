from setuptools import setup, find_packages
import re

REPO_URL = "https://github.com/Mohammedvaraliya/AutomaPy"

def read_description():
    with open("README.md") as f:
        header = "For more information, see the [GitHub Repository]" \
                 "({0}).".format(REPO_URL)
        filter_re = re.compile(r'.*\bPyPI\b.*')
        contents = header + "\n" + filter_re.sub("", f.read())
        return contents.strip()
    

VERSION = '1.1.7'
DESCRIPTION = 'This package refers to the topic of automata theory, which includes DFA, NDFA, Mealy machines, Moore machines and Finite state machine.'

# Setting up
setup(
    name="AutomaPy",
    version=VERSION,
    author="Mohammed Varaliya",
    author_email="<mohammedvaraliya2661392@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=read_description(),
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
        "Operating System :: POSIX :: Linux",
    ]
)
