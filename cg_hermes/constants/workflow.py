from enum import StrEnum


class Workflow(StrEnum):
    BALSAMIC_PON: str = "balsamic-pon"
    BALSAMIC_QC: str = "balsamic-qc"
    BALSAMIC_UMI: str = "balsamic-umi"
    BALSAMIC: str = "balsamic"
    DEMULTIPLEX: str = "demultiplex"
    FASTQ: str = "fastq"
    FLUFFY: str = "fluffy"
    MICROSALT: str = "microsalt"
    MIP_DNA: str = "mip-dna"
    MIP_RNA: str = "mip-rna"
    MUTANT: str = "mutant"
    RNAFUSION: str = "rnafusion"
    RSYNC: str = "rsync"
    SPRING: str = "spring"
    TAXPROFILER: str = "taxprofiler"


class AnalysisType(StrEnum):
    TUMOR_NORMAL_PANEL: str = "tumor_normal_panel"
    TUMOR_NORMAL_WGS: str = "tumor_normal_wgs"
    TUMOR_PANEL: str = "tumor_panel"
    TUMOR_WGS: str = "tumor_wgs"
