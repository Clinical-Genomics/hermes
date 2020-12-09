"""Code for validating files from different sources"""
import copy
import logging
from typing import Dict, FrozenSet, List, Optional, Set

from cg_hermes import config
from cg_hermes.config.pipelines import AnalysisType, Pipeline
from cg_hermes.config.tags import COMMON_TAG_CATEGORIES
from cg_hermes.exceptions import MissingFileError
from cg_hermes.models import pipeline_deliverables
from cg_hermes.models.pipeline_deliverables import (
    BalsamicDeliverables,
    FluffyDeliverables,
    MipDeliverables,
    PipelineDeliverables,
)
from cg_hermes.models.tags import TagMap

LOG = logging.getLogger(__name__)


class DeliverablesValidator:
    """Class with functionality to validate deliverables"""

    def __init__(
        self,
        deliverables: Dict[str, List[Dict[str, str]]],
        pipeline: Pipeline,
        analysis_type: Optional[AnalysisType] = None,
    ):
        self.raw_deliverables = deliverables
        self.pipeline = pipeline
        self.analysis_type = analysis_type
        self.configs: Dict[FrozenSet[str], dict]
        self.file_identifiers: Set[FrozenSet[str]]
        if self.pipeline == Pipeline.fluffy:
            LOG.info("Parsing deliverables for fluffy")
            self.model: FluffyDeliverables = FluffyDeliverables.parse_obj(self.raw_deliverables)
            self.file_identifiers = self.get_fluffy_files()
            self.configs = config.fluffy.FLUFFY_COMMON_TAGS
        elif self.pipeline == Pipeline.balsamic:
            LOG.info("Parsing deliverables for balsamic")
            self.model: BalsamicDeliverables = BalsamicDeliverables.parse_obj(self.raw_deliverables)
            self.file_identifiers = self.get_balsamic_files()
            self.configs = self.get_balsamic_analysis_configs()
        else:
            LOG.info("Parsing deliverables for mip")
            self.model: MipDeliverables = MipDeliverables.parse_obj(self.raw_deliverables)
            self.file_identifiers = self.get_mip_files()
            self.configs = config.mip.MIP_DNA_TAGS

    def get_balsamic_analysis_configs(self) -> Dict[FrozenSet[str], dict]:
        if self.analysis_type == AnalysisType.tumor_wgs:
            tag_set = config.balsamic.TUMOR_ONLY_WGS_TAGS
        elif self.analysis_type == AnalysisType.tumor_normal_wgs:
            tag_set = config.balsamic.TUMOR_NORMAL_WGS_TAGS
        elif self.analysis_type == AnalysisType.tumor_panel:
            tag_set = config.balsamic.TUMOR_ONLY_PANEL_TAGS
        else:
            tag_set = config.balsamic.TUMOR_NORMAL_PANEL_TAGS

        updated_tags = copy.deepcopy(config.balsamic.BALSAMIC_COMMON_TAGS)
        for tag_name in tag_set:
            tag_info = tag_set[tag_name]
            updated_tags[tag_name]["is_mandatory"] = tag_info["is_mandatory"]
        return updated_tags

    def validate_deliverables(self) -> PipelineDeliverables:
        self.validate_mandatory_files()
        return self.model

    def validate_mandatory_files(self) -> None:
        """Validate that all mandatory files are present in deliverables"""
        missing_mandatory_files = []
        for file_tags in self.configs:
            if not self.configs[file_tags]["is_mandatory"]:
                continue
            if file_tags not in self.file_identifiers:
                LOG.warning("Mandatory file (%s) is missing", ", ".join(file_tags))
                missing_mandatory_files.append(", ".join(file_tags))

        if missing_mandatory_files:
            raise MissingFileError(
                files=missing_mandatory_files, message="Deliverables is missing mandatory files"
            )

    def get_mip_files(self) -> Set[FrozenSet[str]]:
        file_obj: pipeline_deliverables.MipFile
        files: Set[FrozenSet[str]] = set()
        for file_obj in self.model.files:
            identifier = [file_obj.step]
            if file_obj.tag:
                identifier.append(file_obj.tag)
            files.add(frozenset(identifier))
        return files

    def get_fluffy_files(self) -> Set[FrozenSet[str]]:
        file_obj: pipeline_deliverables.FileBase
        files: Set[FrozenSet[str]] = set()
        for file_obj in self.model.files:
            files.add(frozenset([file_obj.tag.lower()]))
        return files

    def get_balsamic_files(self) -> Set[FrozenSet[str]]:
        file_obj: pipeline_deliverables.BalsamicFile
        files: Set[FrozenSet[str]] = set()
        for file_obj in self.model.files:
            sample_id: str = file_obj.id
            tag_sample_id: str = sample_id.replace("_", "-")
            tags = frozenset(
                [tag.lower() for tag in file_obj.tag.split(",") if tag != tag_sample_id]
            )
            LOG.debug("Found tag %s", tags)
            files.add(tags)
        return files


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
