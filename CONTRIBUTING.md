# Contributing to Building Detection
As a contributor, here are the guidelines we would like you to follow:


## Pull Request Process
Please submit all contributions via pull request. 


### Minimum code requirements 
All pull request must met basic requirements as tested via [CI](https://github.com/linz/building-detection/blob/master/.github/workflows/ci.yml).
Merging to master is blocked until all CI tests pass.

The code requirements follow LINZ's default Python project requirements and are summarised below. For more detail on LINZ's python project 
requirements please see [https://github.com/linz/template-python-hello-world](https://github.com/linz/template-python-hello-world)


#### Commit message
This repository uses [Conventional Commits](https://www.conventionalcommits.org/)

We have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that
are easy to follow when looking through the project history.

##### Type
Must be one of the following:

- build: Changes that affect the build system or external dependencies
- ci: Changes to our CI configuration files and scripts
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- style: Changes that do not affect the meaning of the code
- test: Adding missing tests or correcting existing tests

#### Formatting 
Formatting is handled by black.

Black is an uncompromising Python code formatting tool. It takes a Python file as an input, and provides a reformatted 
Python file as an output, using rules that are a strict subset of PEP 8. It offers very little in the way of 
configuration (line length being the main exception) in order to achieve formatting consistency. 
It is deterministic - it will always produce the same output from the same inputs.

The line length configuration is stored in pyproject.toml.
 

#### Linting
Linting is handled by pylint.

Pylint checks Python files in order to detect syntax errors and potential bugs (unreachable code / unused variables)
and provide refactoring help

The configuration is stored in .pylintrc.

#### Sorting
Import sorting is handled by isort.

isort sorts Python imports alphabetically within their respective sections:

1. Standard library imports
2. Related third party imports
3. Local application / library specific imports

isort has many configuration options but these can cause inconsistencies with Black, so must be carefully assessed. 
The configurations within this repository will provide consistently ordered / formatted imports.

The configuration is stored in pyproject.toml.

#### Line Length
Line length needs to be consistently configured for formatting, linting and while sorting imports. In order to change
the line length for a specific project, it will need to be updated in the following locations:

    .pylintrc
    pyproject.toml
