Title: Configuring Visual Studio Code and Python (2020)
Date: 2020-01-01
Category: Blog
Tags: Development;
Slug: vs-code-python-setup
Status: published

[TOC]

# Problem Statement

The problems we are trying to solve

* reproducibility, keeping track of installed packages
* multiple Python environments, maintaining independency between different projects and versions
* dependency hell with python packages
* readability, auto formatting
* static checking, run-time error catching
* unit testing
* remembering how the hell you set it up last time

### Tool List

* Poetry
* Visual Studio/Jupyter Lab
* Black
* mypy
* flake8
* pytest

# Intention

I'm writing this blog post to myself, mostly to remind myself what I did last time to configure my environment.  Tools change often, and if I decide there is a better way, I'll update this post.  These are my current set of tools that I use routinely for Machine Learning, Data Analysis, and Software Engineering.  If you've been in the Data Science and Python world for more than a day, you're probably very familiar with the plethora of ways to manage Python environments.  There's Conda, pip, pipenv, virtualenv, etc.  I've been a very happy pipenv user for a while now (technologically speaking), and have had very few issues with it, however, it's pretty much a defunct package and Poetry is the latest solution on the scene.  I've been skeptical of migrating since I haven't had issues with pipenv yet, but the momentum of Poetry seems to be gaining and I've recently updated my tooling to use Poetry.  Jump to the [tldr](#tldr-quick-and-dirty-setup) for the steps and not the explanation.

# My Solution

Poetry is a dependency and package manager, and a virtual environment manager.  That's how I use it, but it includes some very nice package publishing capabilities that I may explore one of these days.  As it it, I will discuss only the parts of it I find useful for my workflow.  Maintaining a reproducible environment for others to build out is essential to good Data Science and Engineering.  Poetry helps with that in to-date, the nicest fashion.

In terms of working environment, I'm a happy Visual Studio Code user.  It's very extensible, free, and looks nice.  The support is growing as well, so there's always someone who's come before me with a solution to nearly every problem I've faced.  I also use Jupyter Lab when I want a more haphazard quick-and-dirty analysis environment, or I want too build out a report.  VS Code has a Python Interactive window now, which keeps a lot of the functionality of Jupyter Notebooks without the horrific issue of output being saved in your source file.  I do concede that for tutorials, demonstrations, and reports that it is very handy to have your output and source in a single file, but most of the time it bad practice.  For example, it makes diffing revisions difficult if the only thing that has changed is your output and not the source.  Additionally, IPYNBs are stored as JSON and is very difficult to diff.

As one enters into the real of non-hacker code, it's important to maintain coding standards in terms of formatting and testing.  So I'll demonstrate how to configure flake8 and black for automatic code linting and auto-formatting.  Additionally, I'm a very strong believer in static type checking, it reduces run time errors and finds things that unit tests cannot often.  I know many Python and JavaScript users abhor the concept of static type checking, often claiming that it slows the language down, or development, or that proper unit tests should find these cases.  I do concede that static typing is slower and that ideally we should have enough unit test coverage to catch any runtime errors, but reality is that most developers spend more time debugging and maintaining than greenfield development.  The little bit of slowdown to ensure that static typing is done is minimal, additionally, the best of the best still miss unit test coverage, lets be realistic.  We're human developers, if there's an automatic way to test something, we should.  So, on that note and off my soap box, lets setup mypy for static type checking too!

## Poetry
### Poetry Init
Start by having Poetry create our project directory, if your project already exists, skip this step, it's *nice* but not *required*

```
$ poetry new demo-project
Created package demo_project in demo-project
$ cd demo-project/
$ ls
README.rst	demo_project	pyproject.toml	tests
```

Now let's `init` poetry and configure our environment.  We can manually edit the pyproject.toml file directly, or remove it and use the handy interactive menu.  I'm doing the interactive menu here, but use what makes sense to you.  If you ran `poetry new` above then this file needs deleted before `poetry init` works, *FYI*.

I'm removing my pyproject.toml for demo purposes
```
$ rm pyproject.toml
```

Kick off the interactive init process and set your values for Name, Version, etc.  I typically elect not to do the interactive dependency and do it manually afterwards.
```
$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [demo-project]:  
Version [0.1.0]:  
Description []:  Demo Project
Author [None, n to skip]:  Ken Farr
License []:  MIT
Compatible Python versions [^3.7]:  3.8

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your dev dependencies (require-dev) interactively (yes/no) [yes] no
```

when finished the following is displayed.

```
Generated file

[tool.poetry]
name = "demo-project"
version = "0.1.0"
description = "Demo Project"
authors = ["Ken Farr"]
license = "MIT"

[tool.poetry.dependencies]
python = "3.8"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```
### Poetry Shell
Let's enter our new environment for the first time, this is similar to `virtualenv` and `pipenv`
```
$ poetry shell
The currently activated Python version 3.7.5 is not supported by the project (3.8).
Trying to find and use a compatible version. 
Using python3 (3.8.0)
Creating virtualenv demo-project-QzaOhq8Q-py3.8 in /Users/kfarr/Library/Caches/pypoetry/virtualenvs
Spawning shell within /Users/kfarr/Library/Caches/pypoetry/virtualenvs/demo-project-QzaOhq8Q-py3.8

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$ . /Users/kfarr/Library/Caches/pypoetry/virtualenvs/demo-project-QzaOhq8Q-py3.8/bin/activate
(demo-project-QzaOhq8Q-py3.8) bash-3.2$ 
```
There's a notice that 3.7 isn't supported (I manually selected 3.8) and that 3.8 was found.  We see the environment being created, take note of where this is, we will need to tell VS Code where to find all of our Poetry virtual environments the first time (and only the first time).

### Poetry Packages

Now lets add some typical production dependencies: `pandas, scikit-learn`
```
(demo-project-QzaOhq8Q-py3.8) bash-3.2$ poetry add pandas scikit-learn
Using version ^0.25.3 for pandas
Using version ^0.22 for scikit-learn

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file


Package operations: 8 installs, 0 updates, 0 removals

  - Installing numpy (1.18.0)
  - Installing six (1.13.0)
  - Installing joblib (0.14.1)
  - Installing python-dateutil (2.8.1)
  - Installing pytz (2019.3)
  - Installing scipy (1.4.1)
  - Installing pandas (0.25.3)
  - Installing scikit-learn (0.22)
(demo-project-QzaOhq8Q-py3.8) bash-3.2$ 
```
If we were making a package for publishing (which is what Poetry supports) we want to avoid putting development only packages in the main `tool.poetry.dependencies` requirements, instead we add them to the `tool.poetry.dev-dependencies` requirements.  Lets add our development packages now.  *NOTE: if you generate plots from your package then you'll need `matplotlib` in your main dependencies and not your dev dependencies.  I use it for EDA plotting, so it's a dev dependency here.  Do what makes sense for you*

***Notice the --dev***

```
(demo-project-QzaOhq8Q-py3.8) bash-3.2$ poetry add --dev matplotlib flake8 black mypy jupyterlab pytest
Using version ^3.1.2 for matplotlib
Using version ^3.7.9 for flake8
Using version ^19.10b0 for black
Using version ^0.761 for mypy
Using version ^1.2.4 for jupyterlab
Using version ^5.3.2 for pytest

Updating dependencies
Resolving dependencies... (1.2s)

Writing lock file


Package operations: 63 installs, 0 updates, 0 removals

  - Installing decorator (4.4.1)
  - Installing ipython-genutils (0.2.0)
  - Installing attrs (19.3.0)
  - Installing parso (0.5.2)
  - Installing ptyprocess (0.6.0)
  - Installing pyrsistent (0.15.6)
  - Installing traitlets (4.3.3)
  - Installing wcwidth (0.1.7)
  - Installing appnope (0.1.0)
  - Installing backcall (0.1.0)
  - Installing jedi (0.15.2)
  - Installing jsonschema (3.2.0)
  - Installing jupyter-core (4.6.1)
  - Installing markupsafe (1.1.1)
  - Installing pexpect (4.7.0)
  - Installing pickleshare (0.7.5)
  - Installing prompt-toolkit (3.0.2)
  - Installing pygments (2.5.2)
  - Installing pyzmq (18.1.1)
  - Installing tornado (6.0.3)
  - Installing webencodings (0.5.1)
  - Installing bleach (3.1.0)
  - Installing defusedxml (0.6.0)
  - Installing entrypoints (0.3)
  - Installing ipython (7.10.2)
  - Installing jinja2 (2.10.3)
  - Installing jupyter-client (5.3.4)
  - Installing mistune (0.8.4)
  - Installing nbformat (4.4.0)
  - Installing pandocfilters (1.4.2)
  - Installing testpath (0.4.4)
  - Installing ipykernel (5.1.3)
  - Installing nbconvert (5.6.1)
  - Installing prometheus-client (0.7.1)
  - Installing send2trash (1.5.0)
  - Installing terminado (0.8.3)
  - Installing json5 (0.8.5)
  - Installing notebook (6.0.2)
  - Installing pyparsing (2.4.6)
  - Installing appdirs (1.4.3)
  - Installing click (7.0)
  - Installing cycler (0.10.0)
  - Installing jupyterlab-server (1.0.6)
  - Installing kiwisolver (1.1.0)
  - Installing mccabe (0.6.1)
  - Installing more-itertools (8.0.2)
  - Installing mypy-extensions (0.4.3)
  - Installing packaging (19.2)
  - Installing pathspec (0.6.0)
  - Installing pluggy (0.13.1)
  - Installing py (1.8.0)
  - Installing pycodestyle (2.5.0)
  - Installing pyflakes (2.1.1)
  - Installing regex (2019.12.20)
  - Installing toml (0.10.0)
  - Installing typed-ast (1.4.0)
  - Installing typing-extensions (3.7.4.1)
  - Installing black (19.10b0)
  - Installing flake8 (3.7.9)
  - Installing jupyterlab (1.2.4)
  - Installing matplotlib (3.1.2)
  - Installing mypy (0.761)
  - Installing pytest (5.3.2)
(demo-project-QzaOhq8Q-py3.8) bash-3.2$
```

## Visual Studio Code

Rock-On, our packages and environment are now setup.  The rest of this document is how I configure my Visual Studio Code to do auto-linting and auto-formatting for my lazy self.

### VS Code <-> Virtual Environment
Launch VS Code and lets get our Python environment configured first.

* Open the _Settings_ menu using `CMD+,`
* Search for *python.venvPath*
* Enter your path, if on OSX it should be similar to `~/Library/Caches/pypoetry/virtualenvs`
* Set the current Python environment to the one created by Poetry

[![GIF: setting VENV Path and Selecting Python Environment](/media/2020/py_env.gif){ width=750px }](/media/2020/py_env.gif)

### VS Code _flake8_ Linting

Create a `demo_project/demo.py` file with the following contents

```python
#Test File
def add(a:int, b:int)->int:
      return a+b

print(add('1', 2))
```

There are multiple issues with this that we would expect _flake8_ to find.  Lets get it configured.  

* Open _Settings_ menu with `CMD+,`
* Search for *python.linting.flake8*
* Enable Flake8
* Click _Add Item_ and paste `--max-line-length=88` to make Flake8 and Black align in character length
* Observe linting errors in violation of PEP8

[![GIF: Enabling Flake8](/media/2020/flake8.gif){ width=750px }](/media/2020/flake8.gif)

### VS Code _black_ auto formatting
Well, knowing we have an issue is great, but can we automatically fix them?  That's what black does.

* Open _Settings_ menu with `CMD+,`
* Search for *editor.formatOnSave*
* Enable _Format On Save_
* Search for *python.formatting.provider*
* Set to _black_
* Save document and observe fixed errors

[![GIF: Enabling Black](/media/2020/black.gif){ width=750px }](/media/2020/black.gif)

### VS Code _mypy_ static linting

Lets setup some static type checking now with _mypy_

* Open _Settings_ menu with `CMD+`
* Search for *python.linting.mypyEnabled*
* Enable _Whether to lint Python files using mypy_
* Go back to _demo.py_ and observe the static type checking error
* Fix the error by removing the quotes around

[![GIF: Enabling mypy](/media/2020/mypy.gif){ width=750px }](/media/2020/mypy.gif)

### VS Code _pytest_ unit testing

Alright, now lets setup our unit test environment

Copy the following into `tests/test_demo_project.py`

```python
from demo_project import __version__, demo


def test_version():
    assert __version__ == "0.1.0"


def test_demo():
    assert demo.add(1, 1) == 2
    assert demo.add(2, -1) == 1
```

Save, and observe the black auto-formatter append a new line, nifty!

Now let's set it up in VSCode

* Open _Settings_ menu with `CMD+,`
* Search for *python.testing.pytestEnabled*
* Enable _Enable testing using pytest
* Navigate to the newly added beaker icon for tests
* Run tests and observe their success

[![GIF: Enabling pytest](/media/2020/pytest.gif){ width=750px }](/media/2020/pytest.gif)

# tldr: Quick and Dirty Setup

The quick and dirty for setting up a new project

* Poetry
    * `poetry new demo-project`
    * `cd demo-project`
    * `rm pyproject.toml`
    * `poetry init`
    * _populate required entries_
    * `poetry shell`
    * `poetry add pandas scikit-learn`
    * `poetry add --dev matplotlib flake8 black mypy jupyterlab pytest`
* Launch VS Code
* Open the _Settings_ menu using `CMD+,`
* Search _python.venvPath_
    * Set to `~/Library/Caches/pypoetry/virtualenvs`
* Search _python.linting.flake8_
    * Check *Flake8 Enabled*
    * Add Item `--max-line-length=88`
* Search _editor.formatOnSave_
    * Check *Format On Save*
* Search _python.formatting.provider_
    * Set to `black`
* Search _python.linting.mypyEnabled_
    * Check *Mypy Enabled*
* Search _python.testing.pytestEnabled_
    * Check *Pytest Enabled*

[![GIF: All Steps](/media/2020/quick.gif){ width=750px }](/media/2020/quick.gif)
