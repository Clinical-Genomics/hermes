"""Test to validate tag maps"""
import pytest
from pydantic.error_wrappers import ValidationError

from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.tags import ALL_TAGS
from cg_hermes.validate import validate_common_tags, validate_tag_map


def test_validate_no_is_mandatory():
    # GIVEN a tag without is_mandatory field
    tag = {"tags": ["cram"], "used_by": ["scout"], "mandatory": True}
    # GIVEN a tag map with the tag
    tag_map = {frozenset(["tags"]): tag}

    # WHEN validating the tag map
    with pytest.raises(ValidationError):
        # THEN assert a validation error is raised
        validate_tag_map(tags=tag_map)


def test_validate_correct_map():
    # GIVEN a tag that is correct
    tag = {"tags": ["cram"], "used_by": ["scout"], "is_mandatory": True}
    # GIVEN a tag map with the tag
    tag_map = {frozenset(["tags"]): tag}

    # WHEN validating the tag map
    result = validate_tag_map(tags=tag_map)

    # THEN assert result is True
    assert result is True


def test_validate_non_existing_tag():
    # GIVEN a non existing tag
    tag = "hej"
    assert tag not in ALL_TAGS

    tag_info = {"tags": [tag], "used_by": ["scout"], "is_mandatory": True}
    # GIVEN a tag map with the tag
    tag_map = {frozenset(["tags"]): tag_info}

    # WHEN validating the tag map
    with pytest.raises(ValidationError):
        # THEN assert a validation error is raised
        validate_tag_map(tags=tag_map)


def test_validate_cg_tags():
    # GIVEN the common CG tag map

    # WHEN validating the tag map
    result = validate_common_tags()

    # THEN assert that the tag map is correct
    assert result is True


def test_validate_mip_dna_tag_map():
    # GIVEN the mip tag map

    # WHEN validating the tag map
    result = validate_tag_map(tags=MIP_DNA_TAGS)

    # THEN assert that the tag map is correct
    assert result is True


def test_validate_fluffy_tag_map():
    # GIVEN the fluffy tag map

    # WHEN validating the tag map
    result = validate_tag_map(tags=FLUFFY_COMMON_TAGS)

    # THEN assert that the tag map is correct
    assert result is True
