import re
import sys


def validate_project_name():
    """
    This validator is used to ensure that `project-name` is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or hyphens.
    Ends with a lowercase letter or number.

    Valid example: `school_project3`.
    """
    MODULE_REGEX = r'^[a-z][a-z0-9\-]+[a-z0-9]$'
    MODULE_NAME = '{{ cookiecutter.project_name }}'

    if not re.match(MODULE_REGEX, MODULE_NAME):
        # Validates project's module name:
        message = [
            'ERROR: The project slug {0} is not a valid Python module name.',
            'Start with a lowercase letter.',
            'Followed by any lowercase letters, numbers or hyphens (-).',
            'End with a lowercase letter or number.',
        ]
        if '_' in MODULE_NAME:
            message.append('Do not use underscores (_) in your project name.')
        raise ValueError(' '.join(message).format(MODULE_NAME))


def validate_project_slug():
    """
    This validator is used to ensure that `project_slug` is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or hyphens.
    Ends with a lowercase letter or number.

    Valid example: `school_project3`.
    """
    MODULE_REGEX = r'^[a-z][a-z0-9\-]+[a-z0-9]$'
    MODULE_NAME = '{{ cookiecutter.project_name }}'

    if not re.match(MODULE_REGEX, MODULE_NAME):
        # Validates project's module name:
        message = [
            'ERROR: The project slug {0} is not a valid Python module name.',
            'Start with a lowercase letter.',
            'Followed by any lowercase letters, numbers or hyphens (-).',
            'End with a lowercase letter or number.',
        ]
        if '_' in MODULE_NAME:
            message.append('Do not use underscores (-) in your project name.')
        raise ValueError(' '.join(message).format(MODULE_NAME))


validators = (
    validate_project_name,
    validate_project_slug,
)

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)  # noqa: WPS421
        sys.exit(1)