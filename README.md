# platform-plugin-package

[![Build status](https://github.com/S3-Platform-Inc/s3-platform-plugin-package/workflows/test/badge.svg?branch=master&event=push)](https://github.com/S3-Platform-Inc/s3-platform-plugin-package/actions?query=workflow%3Atest)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/S3-Platform-Inc/s3-platform-plugin-package/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Bleeding edge [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template to create new python packages.

---

## Purpose

This project is used to scaffold a `s3p plugin` project structure.
Just like `poetry new` but better.

## Features

- Always [`up-to-date`](https://github.com/S3-Platform-Inc/s3-platform-plugin-package/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- Supports latest `python3.8+`
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) for optional static typing
- [`pytest`](https://github.com/pytest-dev/pytest) for testing
- [`flake8`](https://github.com/PyCQA/flake8) and [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide) for linting
- [`Github Actions`](https://docs.github.com/en/actions) as the default CI
- [`sphinx`](http://www.sphinx-doc.org/en/master/) and [`readthedocs.org`](https://readthedocs.org/) for documentation
- Easy update process, so your template will always be up-to-date

## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter jinja2-git lice
```

Then, create a project itself:

```bash
cookiecutter gh:S3-Platform-Inc/s3-platform-plugin-package
```

In order for the github actions to work smoothly (ie badge), you must, during the setup, use your github username in the `organization` field.

```bash
project_name [my-awesome-project]: foo-project
organization [wemake.services]: <github_username>
```

## License

MIT. See [LICENSE](https://github.com/S3-Platform-Inc/s3-platform-plugin-package/blob/master/LICENSE) for more details.


---
