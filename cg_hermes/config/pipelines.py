from enum import StrEnum


class AnalysisType(StrEnum):
    tumor_wgs = "tumor_wgs"
    tumor_normal_wgs = "tumor_normal_wgs"
    tumor_panel = "tumor_panel"
    tumor_normal_panel = "tumor_normal_panel"
