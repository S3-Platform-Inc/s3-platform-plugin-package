from typing import Type

import pytest

from src.{{ cookiecutter.project_slug }}.{{ cookiecutter.source_uniq_name }} import {{ cookiecutter.payload_name }} as imported_payload_class


@pytest.fixture(scope="module")
def fix_plugin_class() -> Type[imported_payload_class]:
    return imported_payload_class
