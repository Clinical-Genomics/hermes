"""Functions for parsing files"""

from copy import deepcopy
from typing import Iterable

from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.pipelines import Pipeline
from cg_hermes.models.pipeline_deliverables import (
    CGDeliverables,
    MipDeliverables,
    MipFile,
    PipelineDeliverables,
)
from cg_hermes.models.tags import CGTag


def convert_to_cg_tag(tag_info: dict, subject_id: str, path: str) -> CGTag:
    """Convert tags from mip specific tags to CG tags"""
    tags = deepcopy(tag_info["tags"])
    tags.append(subject_id)
    tags.extend([tool for tool in tag_info["used_by"] if tool not in ["cg", "audit", "store"]])
    return CGTag(path=path, tags=tags)


def parse_mip_deliverables(deliverables: MipDeliverables) -> Iterable[CGTag]:
    file_obj: MipFile
    for file_obj in deliverables.files:
        mip_tags = [file_obj.step]
        if file_obj.tag:
            mip_tags.append(file_obj.tag)
        conversion_info = MIP_DNA_TAGS[frozenset(mip_tags)]
        yield convert_to_cg_tag(
            tag_info=conversion_info, subject_id=file_obj.id, path=file_obj.path
        )
        if file_obj.path_index:
            yield convert_to_cg_tag(
                tag_info=conversion_info, subject_id=file_obj.id, path=file_obj.path_index
            )


def convert_to_cg_deliverables(
    deliverables: PipelineDeliverables, pipeline: Pipeline
) -> CGDeliverables:
    tag_objs = []
    if pipeline.value == "mip":
        tag_objs = parse_mip_deliverables(deliverables)
    return CGDeliverables(pipeline=pipeline.value, files=tag_objs)


if __name__ == "__main__":
    mip_deliverables = {
        "files": [
            {
                "format": "coverage",
                "id": "sample_id",
                "path": "path/to/file",
                "path_index": None,
                "step": "chanjo_sexcheck",
                "tag": None,
            }
        ]
    }
    deliverable_obj = MipDeliverables(**mip_deliverables)
    pipeline = Pipeline("mip")
    print(pipeline, pipeline.value)
    cg_deliverables = convert_to_cg_deliverables(deliverable_obj, pipeline)
    print(cg_deliverables)
