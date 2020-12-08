"""Code for validating files from different sources"""
import logging
from typing import Dict, FrozenSet, List, Set

from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.tags import COMMON_TAG_CATEGORIES
from cg_hermes.exceptions import MissingFileError
from cg_hermes.models.pipeline_deliverables import BalsamicDeliverables, MipDeliverables
from cg_hermes.models.tags import TagMap

LOG = logging.getLogger(__name__)


def validate_mandatory_files(file_identifiers: Set[FrozenSet[str]], config: dict) -> List[str]:
    missing_mandatory_files = []
    for file_tags in config:
        if not config[file_tags]["is_mandatory"]:
            continue
        if file_tags not in file_identifiers:
            LOG.warning("Mandatory file (%s) is missing", ", ".join(file_tags))
            missing_mandatory_files.append(", ".join(file_tags))
    return missing_mandatory_files


def validate_mip_deliverables(deliverables: Dict[str, List[Dict[str, str]]]) -> MipDeliverables:
    """Validate that the deliverables is following the mip specifications

    Mip creates unique identifiers for files by using either both 'step' and 'tag' or only 'step'

    """
    model: MipDeliverables = MipDeliverables.parse_obj(deliverables)
    file_identifiers: Set[FrozenSet[str]] = set()
    for file_obj in model.files:
        identifier = [file_obj.step]
        if file_obj.tag:
            identifier.append(file_obj.tag)
        file_identifiers.add(frozenset(identifier))

    missing_files = validate_mandatory_files(file_identifiers, config=MIP_DNA_TAGS)
    if missing_files:
        raise MissingFileError(
            files=missing_files, message="Deliverables is missing mandatory files"
        )

    return model


def validate_balsamic_deliverables(
    deliverables: Dict[str, List[Dict[str, str]]]
) -> BalsamicDeliverables:
    """Validate that the deliverables is following the balsamic specifications"""
    model = BalsamicDeliverables.parse_obj(deliverables)

    return model


def validate_common_tags() -> bool:
    """Validate the common tags"""
    for category in COMMON_TAG_CATEGORIES:
        tag_map: Dict[str, Dict[str, str]] = COMMON_TAG_CATEGORIES[category]
        for tag_name in tag_map:
            try:
                assert isinstance(tag_map[tag_name], dict)
            except AssertionError as err:
                LOG.warning("Tag %s in %s is on the wrong format", tag_name, category.upper())
                raise err
            try:
                assert "description" in tag_map[tag_name]
            except AssertionError as err:
                LOG.warning("Tag %s in %s does not have a description", tag_name, category.upper())
                raise err
    return True


def validate_tag_map(tags: Dict[FrozenSet[str], dict]) -> bool:
    """Validate if a tag map is on the correct format"""
    for pipeline_tags in tags:
        assert isinstance(pipeline_tags, frozenset)
        TagMap.validate(tags[pipeline_tags])
    return True


if __name__ == "__main__":
    tags = {frozenset(["tags"]): {"tags": ["cram"], "used_by": ["scout"], "mandatory": True}}
    validate_tag_map(tags)
