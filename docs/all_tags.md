## ALIGNMENT TAGS

| Tag name   | Description                                                |
|------------|------------------------------------------------------------|
| bam        | Alignment file in BAM format                               |
| bam-index  | Index file for alignment file in BAM format                |
| bam-mt     | Alignment file in BAM format holding the reaads from chrMT |
| cram       | Alignment file in CRAM format                              |
| cram-index | Index file for alignment file in CRAM format               |

## ANALYSIS TAGS

| Tag name        | Description                                   |
|-----------------|-----------------------------------------------|
| autozyg         | Autozygous region                             |
| assembly        | Assembly                                      |
| bed             | Bed file                                      |
| bigwig          | Bigwig formated file                          |
| clinical        | Clinical subset                               |
| config          | Config file                                   |
| coverage        | Output with coverage information              |
| diagram         | Data diagram                                  |
| filtered        | Filtered data                                 |
| fracsnp         | Fraction of reads with snp                    |
| fusion          | Fusion transcripts                            |
| genes           | Related to genes                              |
| junction        | Junction data                                 |
| metrics         | Data metrics                                  |
| reference-info  | Information about references used in analysis |
| regions         | Output for regions                            |
| research        | Research set                                  |
| segments        | Output for segments                           |
| sites           | Output for sites                              |
| tcov            | Coverage output                               |
| tiddit-coverage | Coverage output from tiddit                   |
| visualization   | Visualizes data                               |

## FAMILY TAGS

| Tag name   | Description          |
|------------|----------------------|
| pedigree   | Pedigree information |
| ped        | Pedigree information |

## RAW DATA

| Tag name   | Description                         |
|------------|-------------------------------------|
| fastq      | Files with raw data in fastq format |

## REPORTING TAGS

| Tag name       | Description                               |
|----------------|-------------------------------------------|
| multiqc-html   | Multiqc report for the run in html format |
| multiqc-json   | Multiqc report for the run in json format |
| pdf            | Portable document format                  |
| sambamba-depth | Coverage information from sambamba        |
| vcf-report     | Results and QC from variant calling       |

## TOOL TAGS

| Tag name         | Description                                                   |
|------------------|---------------------------------------------------------------|
| arriba           | Fusion caller                                                 |
| asereadcounter   | Count reads mapping to heterozygous sites                     |
| chanjo           | Tool to keep track of coverage over specific regions          |
| chromograph      | Tool to create PNG images from BED and WIG files from mikaell |
| cnvkit           | Tool to call copy number variations                           |
| cyrius           | Tool to call the problematic CYP2D6 gene                      |
| deseq2           | Differential expression analysis with DESeq2                  |
| genotyper        | SNV indel caller from sention                                 |
| gffcompare       | Compare gff files                                             |
| haplotype-caller | Call snv and indels                                           |
| manta            | Tool to call structural variants                              |
| mitodel          | Tool to identify mitochondrial deletion signatures            |
| mutect           | Cancer variant caller                                         |
| peddy            | Tool to check pedigree and ancestral relations                |
| scope            | Call snv indels                                               |
| sention          | Sention algorithm                                             |
| star-fusion      | Fusion caller                                                 |
| strelka          | Cancer variant caller                                         |
| stringtie        | Transcript assembler                                          |
| upd              | Uniparent disomy caller from bjhall                           |
| vardict          | Cancer variant caller                                         |
| wisecondor       | NIPT caller                                                   |

## VALIDATION TAGS

| Tag name   | Description                      |
|------------|----------------------------------|
| ped-check  | Results from pedigree validation |
| qc-metrics | QC metrics from analysis         |
| sex-check  | Results from sex validation      |

## VARIANT TAGS

| Tag name               | Description                                         |
|------------------------|-----------------------------------------------------|
| cnv                    | Copy number variants                                |
| normal                 | Associated with normal sample                       |
| rhocall-viz            | Runs of homozygosity index                          |
| smn-calling            | Copy number calls for the SMN gene                  |
| snv-bcf                | Gvcf including all SNV variants                     |
| snv-gbcf               | Gvcf including all SNV variants                     |
| sv-bcf                 | Gvcf including all SV variants                      |
| sv-vcf                 | Variant call formated file with structural variants |
| sv-vcf-index           | Following index                                     |
| telomere-calling       | Variants from telomere calling                      |
| tmb                    | Tumor mutational burden information                 |
| tumor                  | Associated with tumor sample                        |
| upd                    | Uniparental disomy variants                         |
| vcf                    | Variant call formated file                          |
| vcf-index              | Following index                                     |
| vcf-snv-clinical       | SNV variants from clinical panels                   |
| vcf-snv-clinical-index | Following index                                     |
| vcf-snv-research       | SNV variants from whole genome                      |
| vcf-snv-research-index | Following index                                     |
| vcf-str                | Short tandem repeat variants                        |
| vcf-str-index          | Following index                                     |
| vcf-sv-clinical        | SV variants from clinical panels                    |
| vcf-sv-clinical-index  | Following index                                     |
| vcf-sv-research        | SV variants from whole genome                       |
| vcf-sv-research-index  | Following index                                     |
| vcf2cytosure           | Conversion from vcf format to cytosure format       |

