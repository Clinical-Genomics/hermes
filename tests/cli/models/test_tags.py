import pytest

from cg_hermes.models.tags import TagMap


def test_instantiate_tag_map(tag_map_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a tag map

    # WHEN instantiating an object
    tag_map = TagMap.model_validate(tag_map_raw)

    # THEN assert that it was successfully created
    assert isinstance(tag_map, TagMap)


def test_tag_map_tags_validator(tag_map_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a tag map

    # GIVEN an incorrect tag
    tag_map_raw["tags"] = ["an_incorrect_tag"]

    # WHEN instantiating an object
    with pytest.raises(ValueError):
        TagMap.model_validate(tag_map_raw)

        # THEN an error is raised


def test_tag_map_usage_validator(tag_map_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a tag map

    # GIVEN an incorrect user
    tag_map_raw["used_by"] = ["an_incorrect_user"]

    # WHEN instantiating an object
    with pytest.raises(ValueError):
        TagMap.model_validate(tag_map_raw)

        # THEN an error is raised
