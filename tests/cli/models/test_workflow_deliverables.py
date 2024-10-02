import pytest

from cg_hermes.models.tags import TagMap
from cg_hermes.models.workflow_deliverables import FileBase


def test_instantiate_file_base(file_base_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a file base

    # WHEN instantiating an object
    file_base = FileBase.model_validate(file_base_raw)

    # THEN assert that it was successfully created
    assert isinstance(file_base, FileBase)


def test_tag_map_tags_validator_tag(tag_map_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a tag map

    # GIVEN an incorrect tag
    tag_map_raw["tags"] = ["an_incorrect_tag"]

    # WHEN instantiating an object
    with pytest.raises(ValueError):
        TagMap.model_validate(tag_map_raw)

        # THEN an error is raised
