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
