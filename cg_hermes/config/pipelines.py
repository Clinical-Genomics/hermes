from enum import Enum


class Pipeline(str, Enum):
    mip = "mip"
    balsamic = "balsamic"
    microsalt = "microsalt"
    fluffy = "fluffy"
    cg = "cg"


class AnalysisType(str, Enum):
    tumor_wgs = "tumor_wgs"
    tumor_normal_wgs = "tumor_normal_wgs"
    tumor_panel = "tumor_panel"
    tumor_normal_panel = "tumor_normal_panel"
