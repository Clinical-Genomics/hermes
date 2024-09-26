from pydantic.v1 import validator
from pydantic.v1.main import BaseModel

from cg_hermes.constants.tags import ALL_TAGS, USAGE_TAGS


class TagMap(BaseModel):
    tags: list[str]
    is_mandatory: bool
    used_by: list[str]
    bundle_id: bool | None = False

    @validator("tags", each_item=True)
    def check_tags(cls, tag):
        assert tag in ALL_TAGS, f"{tag} not a valid tag"
        return tag

    @validator("used_by", each_item=True)
    def check_usage(cls, usage):
        assert usage in USAGE_TAGS, f"{usage} not a valid usage"
        return usage


class CGTag(BaseModel):
    path: str
    tags: list[str]
    mandatory: bool
