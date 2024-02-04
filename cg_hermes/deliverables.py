"""Class to represent deliverables file."""
import copy
import logging
from typing import FrozenSet

from cg_hermes.config.balsamic import (
    BALSAMIC_TAGS,
    TUMOR_NORMAL_PANEL_TAGS,
    TUMOR_NORMAL_WGS_TAGS,
    TUMOR_ONLY_PANEL_TAGS,
    TUMOR_ONLY_WGS_TAGS,
)
from cg_hermes.config.balsamic_qc import (
    BALSAMIC_QC_TAGS,
    QC_TUMOR_NORMAL_PANEL_TAGS,
    QC_TUMOR_NORMAL_WGS_TAGS,
)
from cg_hermes.config.balsamic_umi import (
    BALSAMIC_UMI_TAGS,
    UMI_TUMOR_NORMAL_PANEL_TAGS,
    UMI_TUMOR_ONLY_PANEL_TAGS,
)
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.microsalt import MICROSALT_COMMON_TAGS
from cg_hermes.config.mip_dna import MIP_DNA_TAGS
from cg_hermes.config.mip_rna import MIP_RNA_TAGS
from cg_hermes.config.mutant import MUTANT_COMMON_TAGS
from cg_hermes.config.pipelines import AnalysisType
from cg_hermes.config.rnafusion import NXF_RNAFUSION_COMMON_TAGS
from cg_hermes.constants.workflow import Workflow
from cg_hermes.exceptions import MissingFileError
from cg_hermes.models import pipeline_deliverables
from cg_hermes.models.pipeline_deliverables import (
    BalsamicDeliverables,
    CGDeliverables,
    FluffyDeliverables,
    MicrosaltDeliverables,
    MipDeliverables,
    MutantDeliverables,
    PipelineDeliverables,
    RnafusionDeliverables,
    TagBase,
)
from cg_hermes.models.tags import CGTag, TagMap

LOG = logging.getLogger(__name__)


class Deliverables:
    """Class with functionality to validate deliverables"""

    def __init__(
        self,
        deliverables: dict[str, list[dict[str, str]]],
        pipeline: Workflow,
        analysis_type: AnalysisType | None = None,
    ):
        self.raw_deliverables = deliverables
        self.pipeline = pipeline
        self.analysis_type = analysis_type
        self.bundle_id: str | None = None
        self.configs: dict[FrozenSet[str], TagMap]
        self.files: list[TagBase]
        self.file_identifiers: set[FrozenSet[str]]
        self.model: PipelineDeliverables
        self.set_pipeline_specific_variables()
        self.file_identifiers = {file_obj.tags for file_obj in self.files}

    def set_pipeline_specific_variables(self):
        LOG.info("Parsing deliverables for %s", self.pipeline)
        if self.pipeline == Workflow.FLUFFY:
            self.model: FluffyDeliverables = FluffyDeliverables.parse_obj(self.raw_deliverables)
            self.files = self.get_fluffy_files()
            self.configs = Deliverables.build_internal_tag_map(FLUFFY_COMMON_TAGS)
        elif Workflow.BALSAMIC in self.pipeline:
            self.model: BalsamicDeliverables = BalsamicDeliverables.parse_obj(self.raw_deliverables)
            self.files = self.get_balsamic_files()
            self.configs = Deliverables.build_internal_tag_map(self.get_balsamic_analysis_configs())
        elif self.pipeline == Workflow.MICROSALT:
            self.model: MicrosaltDeliverables = MicrosaltDeliverables.parse_obj(
                self.raw_deliverables
            )
            self.files = self.get_microsalt_files()
            self.configs = Deliverables.build_internal_tag_map(MICROSALT_COMMON_TAGS)
        elif self.pipeline == Workflow.MUTANT:
            self.model: MutantDeliverables = MutantDeliverables.parse_obj(self.raw_deliverables)
            self.files = self.get_mutant_files()
            self.configs = Deliverables.build_internal_tag_map(MUTANT_COMMON_TAGS)
        elif self.pipeline == Workflow.MIP_DNA:
            self.model: MipDeliverables = MipDeliverables.parse_obj(self.raw_deliverables)
            self.files = self.get_mip_files()
            self.configs = Deliverables.build_internal_tag_map(MIP_DNA_TAGS)
        elif self.pipeline == Workflow.MIP_RNA:
            self.model: MipDeliverables = MipDeliverables.parse_obj(self.raw_deliverables)
            self.files = self.get_mip_files()
            self.configs = Deliverables.build_internal_tag_map(MIP_RNA_TAGS)
        elif self.pipeline == Workflow.RNAFUSION:
            self.model: RnafusionDeliverables = RnafusionDeliverables.parse_obj(
                self.raw_deliverables
            )
            self.files = self.get_rnafusion_files()
            self.configs = Deliverables.build_internal_tag_map(NXF_RNAFUSION_COMMON_TAGS)
        else:
            raise Exception(
                "Invalid workflow ({}) set for Deliverables object".format(self.pipeline)
            )

    @staticmethod
    def build_internal_tag_map(tag_map: dict[FrozenSet[str], dict]) -> dict[FrozenSet[str], TagMap]:
        """Convert and validate a tag map to TagMap objects"""
        LOG.debug("Build internal tag map")
        internal_tag_map: dict[FrozenSet[str], TagMap] = dict()
        for pipeline_tags in tag_map:
            internal_tag_map[pipeline_tags] = TagMap.parse_obj(tag_map[pipeline_tags])
        return internal_tag_map

    @staticmethod
    def convert_to_cg_tag(conversion_info: TagMap, subject_id: str, path: str) -> CGTag:
        """Convert tags from workflow specific tags to CG tags"""
        cg_tags: list[str] = copy.deepcopy(conversion_info.tags)
        cg_tags.append(subject_id)
        cg_tags.extend(
            [tool for tool in conversion_info.used_by if tool not in ["cg", "audit", "store"]]
        )
        return CGTag(path=path, tags=cg_tags, mandatory=conversion_info.is_mandatory)

    def convert_to_cg_deliverables(self) -> CGDeliverables:
        """Convert workflow specific information from deliverables file to CG formatted information"""
        cg_files: list[CGTag] = []
        file_object: TagBase
        for file_object in self.files:
            pipeline_tags = file_object.tags
            if pipeline_tags not in self.configs:
                LOG.warning("Could not find info for file %s", ", ".join(pipeline_tags))
                continue
            conversion_info: TagMap = self.configs[pipeline_tags]
            if conversion_info.bundle_id is True:
                LOG.info("Set bundle id to %s", conversion_info.bundle_id)
                self.bundle_id = file_object.subject_id
            cg_files.append(
                Deliverables.convert_to_cg_tag(
                    conversion_info=conversion_info,
                    subject_id=file_object.subject_id,
                    path=file_object.path,
                )
            )
            if file_object.path_index:
                cg_files.append(
                    Deliverables.convert_to_cg_tag(
                        conversion_info=conversion_info,
                        subject_id=file_object.subject_id,
                        path=file_object.path_index,
                    )
                )
        return CGDeliverables(workflow=self.pipeline, files=cg_files, bundle_id=self.bundle_id)

    def get_balsamic_analysis_configs(self) -> dict[FrozenSet[str], dict]:
        """Extracts all the BALSAMIC mandatory files depending on the analysis workflow and type executed"""

        BALSAMIC_COMMON_TAGS = []
        tag_set = []
        if self.pipeline == Workflow.BALSAMIC:
            BALSAMIC_COMMON_TAGS = BALSAMIC_TAGS
            if self.analysis_type == AnalysisType.tumor_wgs:
                tag_set = TUMOR_ONLY_WGS_TAGS
            elif self.analysis_type == AnalysisType.tumor_normal_wgs:
                tag_set = TUMOR_NORMAL_WGS_TAGS
            elif self.analysis_type == AnalysisType.tumor_panel:
                tag_set = TUMOR_ONLY_PANEL_TAGS
            else:
                tag_set = TUMOR_NORMAL_PANEL_TAGS
        elif self.pipeline == Workflow.BALSAMIC_QC:
            BALSAMIC_COMMON_TAGS = BALSAMIC_QC_TAGS
            if self.analysis_type == AnalysisType.tumor_normal_wgs:
                tag_set = QC_TUMOR_NORMAL_WGS_TAGS
            elif self.analysis_type == AnalysisType.tumor_normal_panel:
                tag_set = QC_TUMOR_NORMAL_PANEL_TAGS
        elif self.pipeline == Workflow.BALSAMIC_UMI:
            BALSAMIC_COMMON_TAGS = BALSAMIC_UMI_TAGS
            if self.analysis_type == AnalysisType.tumor_panel:
                tag_set = UMI_TUMOR_ONLY_PANEL_TAGS
            else:
                tag_set = UMI_TUMOR_NORMAL_PANEL_TAGS

        updated_tags = copy.deepcopy(BALSAMIC_COMMON_TAGS)
        for tag_name in tag_set:
            tag_info = tag_set[tag_name]
            updated_tags[tag_name]["is_mandatory"] = tag_info["is_mandatory"]
        return updated_tags

    def validate_mandatory_files(self) -> None:
        """Validate that all mandatory files are present in deliverables"""
        missing_mandatory_files = []
        for file_tags in self.configs:
            if not self.configs[file_tags].is_mandatory:
                continue
            if file_tags not in self.file_identifiers:
                LOG.warning("Mandatory file (%s) is missing", ", ".join(file_tags))
                missing_mandatory_files.append(", ".join(file_tags))
        if missing_mandatory_files:
            raise MissingFileError(
                files=missing_mandatory_files, message="Deliverables is missing mandatory files"
            )

    def get_mip_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.MipFile
        files: list[TagBase] = []
        for file_obj in self.model.files:
            identifier = [file_obj.step]
            if file_obj.tag:
                identifier.append(file_obj.tag)
            files.append(
                TagBase(
                    tags=frozenset(identifier),
                    subject_id=file_obj.id,
                    path=file_obj.path,
                    path_index=file_obj.path_index,
                )
            )
        return files

    def get_microsalt_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.MicrosaltFile
        files: list[TagBase] = []
        for file_obj in self.model.files:
            identifier = [file_obj.step]
            if file_obj.tag:
                identifier.append(file_obj.tag)
            files.append(
                TagBase(
                    tags=frozenset(identifier),
                    subject_id=file_obj.id,
                    path=file_obj.path,
                )
            )
        return files

    def get_mutant_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.MutantFile
        files: list[TagBase] = []
        for file_obj in self.model.files:
            identifier = [file_obj.step]
            if file_obj.tag:
                identifier.append(file_obj.tag)
            files.append(
                TagBase(
                    tags=frozenset(identifier),
                    subject_id=file_obj.id,
                    path=file_obj.path,
                )
            )
        return files

    def get_fluffy_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.FileBase
        files: list[TagBase] = []
        for file_obj in self.model.files:
            identifier = frozenset([file_obj.tag.lower()])
            files.append(TagBase(tags=identifier, subject_id=file_obj.id, path=file_obj.path))
        return files

    def get_balsamic_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.BalsamicFile
        files: list[TagBase] = []
        for file_obj in self.model.files:
            sample_id: str = file_obj.id
            tag_sample_id: str = sample_id.replace("_", "-")
            # This is due to older balsamic format
            split_id: list[str] = sample_id.split("_")
            if len(split_id) > 2:
                sample_id = split_id[1]
                tag_sample_id: str = "-".join(split_id)
            identifier = frozenset(tag.lower() for tag in file_obj.tag if tag != tag_sample_id)

            LOG.debug("Found tag %s", identifier)
            files.append(TagBase(tags=identifier, subject_id=sample_id, path=file_obj.path))
        return files

    def get_rnafusion_files(self) -> list[TagBase]:
        file_obj: pipeline_deliverables.RnafusionFile
        files: list[TagBase] = []
        for file_obj in self.model.files:
            identifier = [file_obj.step]
            if file_obj.tag:
                identifier.append(file_obj.tag)
            files.append(
                TagBase(
                    tags=frozenset(identifier),
                    subject_id=file_obj.id,
                    path=file_obj.path,
                )
            )
        return files
