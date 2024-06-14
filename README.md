# Python Number Prettifier

Python number prettifier.

# Overview

The program will "prettify" numbers greater than or equal to a million by appending a string representation of the unit with the truncated number. 

Although the program is intended to be ran locally, docker was chosen to allow the program to run on more machines without needing to set up python to ensure that system pip was not being used, and that the correct python version was being selected. This means that other contributors and users are able to run the code without even needing python installed locally. Further, tests are able to be ran inside of the docker container, allowing us to further extend our code and allow testing via github actions.

# Getting started

First ensure that `docker` and `docker-cli` are installed.

```
git clone https://github.com/natehalsey/python-number-prettifier
```

Afterward, simply run:

```
make docker.run
```

To run the program.

# Tests

Tests can be ran inside of a docker container by running `make docker.test`, or directly in a local development environment by running `make test`.

# Linting

Linting can be performed in a local development environemnt by running `make lint.check`, and any linting issues can automatically be fixed by running `make lint.fix`.

# Local Development

## pyenv

Before doing any local development, you need to have pyenv installed locally. You can follow the directions here: https://github.com/pyenv/pyenv to install the latest version of pyenv, which allows us to manage multiple python versions.

Then simply `. .script/bootstrap` to bootstrap the environment and begin developing.

## Updating requirements

To update requirements, simply add the requirement to `requirements.in` and then run `make requirements` to re-generate `requirements.txt`. 
