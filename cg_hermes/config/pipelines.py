from cgmodels.cg.constants import Pipeline, StrEnum


class AnalysisType(StrEnum):
    tumor_wgs = "tumor_wgs"
    tumor_normal_wgs = "tumor_normal_wgs"
    tumor_panel = "tumor_panel"
    tumor_normal_panel = "tumor_normal_panel"


BALSAMIC_PIPELINES = [Pipeline.BALSAMIC, Pipeline.BALSAMIC_QC, Pipeline.BALSAMIC_UMI]
