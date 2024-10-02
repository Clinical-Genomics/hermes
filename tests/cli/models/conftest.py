"""Fixtures for CLI tests."""

import pytest


@pytest.fixture()
def tag_map_raw() -> dict:
    return {
        "tags": ["annotation"],
        "is_mandatory": True,
        "used_by": ["cg"],
    }


@pytest.fixture()
def file_base_raw() -> dict[str, str]:
    return {
        "path": "a_path",
        "tag": "a_tag",
        "id": "an_id",
    }


@pytest.fixture()
def balsamic_file_raw(file_base_raw: dict[str, str]) -> dict:
    return {
        "path": "a_path",
        "tag": ["a_tag"],
        "id": "an_id",
    }
