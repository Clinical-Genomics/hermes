## ALIGNMENT TAGS

| Tag name   | Description                                                |
|------------|------------------------------------------------------------|
| cram       | Alignment file in CRAM format                              |
| cram-index | Index file for alignment file in CRAM format               |
| bam        | Alignment file in BAM format                               |
| bam-index  | Index file for alignment file in BAM format                |
| bam-mt     | Alignment file in BAM format holding the reaads from chrMT |

## VARIANT TAGS

| Tag name               | Description                                   |
|------------------------|-----------------------------------------------|
| snv-gbcf               | Gvcf including all SNV variants               |
| snv-bcf                | Gvcf including all SNV variants               |
| sv-bcf                 | Gvcf including all SV variants                |
| upd                    | Uniparental disomy variants                   |
| vcf-snv-clinical       | SNV variants from clinical panels             |
| vcf-snv-clinical-index | Following index                               |
| vcf-sv-clinical        | SV variants from clinical panels              |
| vcf-sv-clinical-index  | Following index                               |
| vcf-snv-research       | SNV variants from whole genome                |
| vcf-snv-research-index | Following index                               |
| vcf-sv-research        | SV variants from whole genome                 |
| vcf-sv-research-index  | Following index                               |
| vcf-str                | Short tandem repeat variants                  |
| vcf-str-index          | Following index                               |
| rhocall-viz            | Runs of homozygosity index                    |
| smn-calling            | Copy number calls for the SMN gene            |
| telomere-calling       | Variants from telomere calling                |
| vcf2cytosure           | Conversion from vcf format to cytosure format |

## FAMILY TAGS

| Tag name   | Description          |
|------------|----------------------|
| pedigree   | Pedigree information |
| ped        | Pedigree information |

## REPORTING TAGS

| Tag name       | Description                               |
|----------------|-------------------------------------------|
| multiqc-html   | Multiqc report for the run in html format |
| multiqc-json   | Multiqc report for the run in json format |
| sambamba-depth | Coverage information from sambamba        |

## VALIDATION TAGS

| Tag name   | Description                      |
|------------|----------------------------------|
| sex-check  | Results from sex validation      |
| qc-metrics | QC metrics from analysis         |
| ped-check  | Results from pedigree validation |

## ANALYSIS TAGS

| Tag name        | Description                                   |
|-----------------|-----------------------------------------------|
| config          | Config file                                   |
| reference-info  | Information about references used in analysis |
| sites           | Output for sites                              |
| regions         | Output for regions                            |
| tcov            | Coverage output                               |
| tiddit-coverage | Coverage output from tiddit                   |
| bigwig          | Bigwig formated file                          |
| coverage        | Output with coverage information              |

## TOOL TAGS

| Tag name    | Description                                                   |
|-------------|---------------------------------------------------------------|
| chanjo      | Tool to keep track of coverage over specific regions          |
| peddy       | Tool to check pedigree and ancestral relations                |
| chromograph | Tool to create PNG images from BED and WIG files from mikaell |
| cyrius      | Tool to call the problematic CYP2D6 gene                      |
| upd         | Uniparent disomy caller from bjhall                           |

