"""Fixtures for CLI tests."""

import pytest


@pytest.fixture()
def tag_map_raw() -> dict:
    return {
        "tags": ["annotation"],
        "is_mandatory": True,
        "used_by": ["cg"],
    }
