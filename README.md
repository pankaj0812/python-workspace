# Python Workspace

This repository holds all the practice materials and examples of Python programming. Each folder in the repository contains a specific topic with examples and relevant resources for further learning.

## Setting Up Python Development Environment

Setting up a Python development environment can be overkill sometimes. But as your application grows, these are usually very helpful.
There are certain tools that I've found useful. The given instructions are for Ubuntu and can vary for other operating systems.

## Tools

We will install and use following tools for our development.

### Pyenv

Pyenv helps us manage multiple versions of Python interpreters. This also allows us to change the default version of the Python interpreter to one that is not the system interpreter. For example, Ubuntu 20.04 has a Python interpreter version 3.8+.

#### Installing Pyenv

1. Install prerequisites from [here](https://github.com/pyenv/pyenv/wiki/Common-build-problems).
2. Install pyenv using the [installer](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation).
3. Follow [instructions](https://github.com/pyenv/pyenv#basic-github-checkout) to update *.bashrc* with **pyenv** environment variables.
4. Restart your shell using `exec $SHELL`.
5. Validate **pyenv** version and install required Python version as given below:

        $ pyenv --version
        pyenv version 2.0.0

        $pyenv install 3.7.2
        Downloading Python-3.7.2.tar.xz...
        ...
6. Set the installed Python version as your global interpreter.

        $ pyenv global 3.7.2
        $ which python
        /home/amiteshrai/.pyenv/shims/python

### Poetry

Poetry helps us manage our Python dependencies. Poetry makes sure that we have same versions of our Python packages installed across environments such as develop, staging, and production. Furthermore, Poetry can be used to publish Python packages as well.

#### Installing Poetry

1. Install poetry using [installer](https://github.com/python-poetry/poetry#installation).

        $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

        Retrieving Poetry metadata

        # Welcome to Poetry!
        ...
2. Follow instructions on the terminal to update your environment variable for poetry.
3. Update your shell using `exec $SHELL`.
4. Check poetry version.

        $ poetry --version
        Poetry version 1.1.6
