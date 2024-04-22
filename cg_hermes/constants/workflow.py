from enum import StrEnum


class Workflow(StrEnum):
    BALSAMIC: str = "balsamic"
    BALSAMIC_PON: str = "balsamic-pon"
    BALSAMIC_QC: str = "balsamic-qc"
    BALSAMIC_UMI: str = "balsamic-umi"
    DEMULTIPLEX: str = "demultiplex"
    FASTQ: str = "fastq"
    FLUFFY: str = "fluffy"
    MICROSALT: str = "microsalt"
    MIP_DNA: str = "mip-dna"
    MIP_RNA: str = "mip-rna"
    MUTANT: str = "mutant"
    RAREDISEASE: str = "raredisease"
    RNAFUSION: str = "rnafusion"
    RSYNC: str = "rsync"
    SPRING: str = "spring"
    TAXPROFILER: str = "taxprofiler"
    TOMTE: str = "tomte"

    @classmethod
    def get_nf_workflows(cls) -> set:
        return {cls.RAREDISEASE, cls.RNAFUSION, cls.TAXPROFILER, cls.TOMTE}


class CancerAnalysisType(StrEnum):
    TUMOR_NORMAL_PANEL: str = "tumor_normal_panel"
    TUMOR_NORMAL_WGS: str = "tumor_normal_wgs"
    TUMOR_PANEL: str = "tumor_panel"
    TUMOR_WGS: str = "tumor_wgs"
