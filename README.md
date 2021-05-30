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

        > pyenv --version
        pyenv version 2.0.0

        >pyenv install 3.7.2
        Downloading Python-3.7.2.tar.xz...
        ...
6. Set the installed Python version as your global interpreter.

        > pyenv global 3.7.2
        > which python
        /home/amiteshrai/.pyenv/shims/python

### Poetry

Poetry helps us manage our Python dependencies. Poetry makes sure that we have same versions of our Python dependencies installed across environments such as develop, staging, and production. Furthermore, Poetry can be used to publish Python dependencies as well.

#### Installing Poetry

1. Install poetry using [installer](https://github.com/python-poetry/poetry#installation).

        > curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

        Retrieving Poetry metadata

        # Welcome to Poetry!
        ...
2. Follow instructions on the terminal to update your environment variable for poetry.
3. Update your shell using `exec $SHELL`.
4. Check poetry version.

        > poetry --version
        Poetry version 1.1.6

#### Useful Poetry Commands

| Command  | Description |
| ------------- | ------------- |
| poetry new `[project-name]`  | Initialize a new Python project  |
| poetry init  | Create a `pyproject.toml` file interactively  |
| poetry install  | Install the dependencies inside the `pyproject.toml` file  |
| poetry add `[package-name]`  | Add a dependency to a virtual environment |
| poetry add -D `[package-name]`  | Add a dev dependency to a virtual environment  |
| poetry remove `[package-name]`  | Remove a dependency from a virtual environment  |
| poetry remove -D `[package-name]`  | Remove a dev dependency from a virtual environment  |

## Project Setup

Once the above tools are installed, initialize your Python project using **poetry** as:

    > mkdir -p python-workspace
    > cd python-workspace
    > poetry init --no-interaction

This will create a `pyproject.toml` file dependency configuration file specified in PEP 517 and 518

    [tool.poetry]
    name = "python-workspace"
    version = "0.1.0"
    description = ""
    authors = ["Amitesh Rai <xxxxx@XXX.com>"]

    [tool.poetry.dependencies]
    python = "^3.7"

    [tool.poetry.dev-dependencies]

    [build-system]
    requires = ["poetry-core>=1.0.0"]
    build-backend = "poetry.core.masonry.api"

### Creating And Managing Virtual Environments With Poetry

To prevent your current project dependencies from interfering with with the system-wide Python installation, an isolated virtual environment with specific Python version and set of dependencies is essential.

Poetry helps you with creating and managing virtual environments for your projects.

#### Create Virtual Environment

To create a virtual environment using Poetry, install the skeleton dependency using:

    > cd python-workspace
    > poetry install

Now a virtual environment dedicated to your project is created. Poetry has installed initial dependencies into it and also create a *lock* file named `poetry.lock`

#### Running Python In Virtual Environment

Since our virtual environment is already created, we can run a Python session inside it as:

    > poetry run python
    Python 3.7.2 (default, May 26 2021, 13:11:13)
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print("Hello Python")
    Hello Python
    >>>

### Installing Dependencies Using Poetry

Install dependencies using Poetry as:

    > poetry add requests click

Install development dependencies using Poetry as:

    > poetry add --dev flake8 autopep8 black pytest coverage[toml] pytest-cov nox

### Updating VSCode Python Interpreter Path

Once the virtual environment is created using Poetry, you can use Poetry to updated the VSCode with Python interpreter to be used for current project.

    > poetry env info --path
    /home/amiteshrai/.cache/pypoetry/virtualenvs/python-workspace-nQrJ2JzJ-py3.7

Use the output of the above command to update the Python interpreter using the command palette in VSCode
