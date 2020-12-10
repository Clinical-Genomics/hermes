"""Code for validating files from different sources"""
import logging
from typing import Dict, FrozenSet, List, Optional

from cg_hermes.config.pipelines import AnalysisType, Pipeline
from cg_hermes.config.tags import COMMON_TAG_CATEGORIES
from cg_hermes.deliverables import Deliverables
from cg_hermes.models.tags import TagMap

LOG = logging.getLogger(__name__)


def get_deliverables_obj(
    deliverables: Dict[str, List[Dict[str, str]]],
    pipeline: Pipeline,
    analysis_type: Optional[AnalysisType] = None,
) -> Deliverables:
    if pipeline == Pipeline.balsamic:
        if not analysis_type:
            LOG.info("Please specify analysis type for balsamic")
            raise SyntaxError
    deliverables_obj = Deliverables(
        deliverables=deliverables, pipeline=pipeline, analysis_type=analysis_type
    )
    return deliverables_obj


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


def validate_tag_map(tag_map: Dict[FrozenSet[str], dict]) -> bool:
    """Validate if a tag map is on the correct format"""
    for pipeline_tags in tag_map:
        assert isinstance(pipeline_tags, frozenset)
        TagMap.validate(tag_map[pipeline_tags])
    return True


if __name__ == "__main__":
    tags = {frozenset(["tags"]): {"tags": ["cram"], "used_by": ["scout"], "mandatory": True}}
    validate_tag_map(tags)
