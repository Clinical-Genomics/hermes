from enum import StrEnum


class Workflow(StrEnum):
    BALSAMIC: str = "balsamic"
    BALSAMIC_QC: str = "balsamic-qc"
    BALSAMIC_UMI: str = "balsamic-umi"
    BALSAMIC_PON: str = "balsamic-pon"
    DEMULTIPLEX: str = "demultiplex"
    FASTQ: str = "fastq"
    FLUFFY: str = "fluffy"
    MICROSALT: str = "microsalt"
    MIP_DNA: str = "mip-dna"
    MIP_RNA: str = "mip-rna"
    RNAFUSION: str = "rnafusion"
    RSYNC: str = "rsync"
    MUTANT: str = "mutant"
    SPRING: str = "spring"
    TAXPROFILER: str = "taxprofiler"


class AnalysisType(StrEnum):
    TUMOR_WGS: str = "tumor_wgs"
    TUMOR_NORMAL_WGS: str = "tumor_normal_wgs"
    TUMOR_PANEL: str = "tumor_panel"
    TUMOR_NORMAL_PANEL: str = "tumor_normal_panel"
