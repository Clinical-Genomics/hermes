"""Functions for parsing files"""

import logging
from copy import deepcopy
from typing import Dict, FrozenSet, Iterable, List

from cg_hermes.deliverables import Deliverables
from cg_hermes.models.pipeline_deliverables import CGDeliverables, TagBase
from cg_hermes.models.tags import CGTag

LOG = logging.getLogger(__name__)


def convert_to_cg_tag(tag_info: dict, subject_id: str, path: str) -> CGTag:
    """Convert tags from mip specific tags to CG tags"""
    tags = deepcopy(tag_info["tags"])
    tags.append(subject_id)
    tags.extend([tool for tool in tag_info["used_by"] if tool not in ["cg", "audit", "store"]])
    return CGTag(path=path, tags=tags)


def parse_deliverables(
    file_objects: List[TagBase], configs: Dict[FrozenSet[str], dict]
) -> Iterable[CGTag]:
    for file_object in file_objects:
        tags = file_object.tags
        if tags not in configs:
            LOG.warning("Could not find info for file %s", ", ".join(tags))
            continue
        conversion_info = configs[tags]
        yield convert_to_cg_tag(
            tag_info=conversion_info, subject_id=file_object.subject_id, path=file_object.path
        )
        if file_object.path_index:
            yield convert_to_cg_tag(
                tag_info=conversion_info,
                subject_id=file_object.subject_id,
                path=file_object.path_index,
            )


def convert_to_cg_deliverables(deliverables: Deliverables) -> CGDeliverables:
    tag_objs = parse_deliverables(deliverables.files, deliverables.configs)
    return CGDeliverables(pipeline=deliverables.pipeline.value, files=tag_objs)


if __name__ == "__main__":
    file_objs = [
        TagBase(
            **{
                "subject_id": "sample_id",
                "path": "path/to/file",
                "path_index": None,
                "tags": frozenset(["chanjo_sexcheck"]),
            }
        )
    ]

    cg_deliverables = parse_mip_deliverables(file_objs)
    for file_obj in cg_deliverables:
        print(file_obj)
