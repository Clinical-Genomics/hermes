## ALIGNMENT TAGS

| Tag name   | Description                                                |
|------------|------------------------------------------------------------|
| bam        | Alignment file in BAM format                               |
| bam-index  | Index file for alignment file in BAM format                |
| bam-mt     | Alignment file in BAM format holding the reaads from chrMT |
| cram       | Alignment file in CRAM format                              |
| cram-index | Index file for alignment file in CRAM format               |

## ANALYSIS TAGS

| Tag name         | Description                                           |
|------------------|-------------------------------------------------------|
| aspcf-plot       | Plot of LogR and BAF values                           |
| assembly         | Assembly                                              |
| autozyg          | Autozygous region                                     |
| bed              | Bed file                                              |
| bed-index        | Following index                                       |
| bigwig           | Bigwig formated file                                  |
| circular-plot    | Circular plot                                         |
| clinical         | Clinical subset                                       |
| config           | Config file                                           |
| coverage         | Output with coverage information                      |
| filtered         | Filtered data                                         |
| first-pass       | Data metrics first pass                               |
| fracsnp          | Fraction of reads with snp                            |
| fusion           | Fusion transcripts                                    |
| genes            | Related to genes                                      |
| germline-plot    | Plot of LogR and BAF values for normal sample         |
| junction         | Junction data                                         |
| metrics          | Data metrics                                          |
| profile-plot     | Copy number profile plot                              |
| qc-cram          | QC alignment file in CRAM format                      |
| qc-cram-index    | QC index file for alignment file in CRAM format       |
| raw-profile-plot | Copy number profile without rounding to whole numbers |
| reference-info   | Information about references used in analysis         |
| regions          | Output for regions                                    |
| research         | Research set                                          |
| scatter-plot     | Scatter plot                                          |
| second-pass      | Data metrics second pass                              |
| segments         | Output for segments                                   |
| sites            | Output for sites                                      |
| sunrise-plot     | Sunrise plot                                          |
| tcov             | Coverage output                                       |
| tiddit-coverage  | Coverage output from tiddit                           |
| tumor-plot       | Plot of LogR and BAF values for tumor sample          |
| umi              | Files related to UMI workflow                         |
| umi-cram         | UMI consensus filtered cram file                      |
| umi-cram-index   | Index for the UMI consensus filtered cram file        |
| vcf-fusion       | Converted RNA fusion file to SV VCF                   |
| visualization    | Visualizes data                                       |

## FAMILY TAGS

| Tag name   | Description          |
|------------|----------------------|
| ped        | Pedigree information |
| pedigree   | Pedigree information |

## RAW DATA

| Tag name       | Description                         |
|----------------|-------------------------------------|
| fasta          | Files with raw data in fasta format |
| fastq          | Files with raw data in fastq format |
| forward-strand | Reads from forward strand           |
| reverse-strand | Reads from reverse strand           |
| rna            | Data generated from RNA samples     |
| unpaired-reads | Reads that could not be paired      |

## REPORTING TAGS

| Tag name            | Description                                                    |
|---------------------|----------------------------------------------------------------|
| audit               | Audit file                                                     |
| cnv-report          | CNV variant calling report                                     |
| csv                 | Comma separated values                                         |
| combined-report     | A combined report of taxonomic classification from all samples |
| deliverable         | Deliverables file                                              |
| delivery-report     | Delivery report with result for upload to Scout                |
| gene-counts         | STAR read counts output per gene                               |
| metagenomics-report | Report describing taxonomic classification results             |
| multiqc             | MultiQC related files                                          |
| multiqc-html        | MultiQC analysis report in HTML format                         |
| multiqc-json        | MultiQC analysis report in JSON format                         |
| pdf                 | Portable document format                                       |
| picard-alignment    | High level metrics about the alignment of reads                |
| picard-duplicates   | Metrics calculated during marking duplicates                   |
| picard-hs           | Metrics for the analysis of target-capture sequencing          |
| picard-insert-size  | Metrics about the insert size distribution                     |
| picard-wgs          | Metrics for evaluating the performance of WGS analysis         |
| qc-report           | Results and QC                                                 |
| sambamba-depth      | Coverage information from sambamba                             |
| samtools-stats      | Comprehensive statistics from alignment file                   |
| software-versions   | Versions of software used in analysis                          |
| summary             | Overview file without detailed information                     |
| tsv                 | Tab separated values                                           |
| vcf-report          | Results and QC from variant calling                            |

## TOOL TAGS

| Tag name              | Description                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------|
| arriba                | Fusion caller                                                                             |
| ascatngs              | Tool to identify somatically acquired copy-number alterations                             |
| asereadcounter        | Count reads mapping to heterozygous sites                                                 |
| bracken               | Tool to compute the abundance of species and is companion program to kraken2              |
| centrifuge            | Taxonomic sequence classifier for metagenomic sequences                                   |
| chanjo                | Tool to keep track of coverage over specific regions                                      |
| chromograph           | Tool to create PNG images from BED and WIG files from mikaell                             |
| cnvkit                | Tool to call copy number variations                                                       |
| cnvpytor              | Tool for CNV/CNA analysis from depth-of-coverage by mapped reads                          |
| cyrius                | Tool to call the problematic CYP2D6 gene                                                  |
| deepvariant           | Variantcaller                                                                             |
| delly                 | Cancer structural variant prediction tool                                                 |
| deseq2                | Differential expression analysis with DESeq2                                              |
| dnascope              | Call snv indels                                                                           |
| expansionhunter       | Call repeat expansions                                                                    |
| fastp                 | Preprocessing tool for FastQ files                                                        |
| fusioncatcher         | Fusion caller                                                                             |
| fusioncatcher-summary | Fusion caller summary                                                                     |
| fusioninspector       | Fusion inspection                                                                         |
| genotyper             | SNV indel caller from sention                                                             |
| gens                  | CNV visualization tool                                                                    |
| gffcompare            | Compare gff files                                                                         |
| haplotype-caller      | Call snv and indels                                                                       |
| kraken2               | Taxonomic sequence classifier that assigns taxonomic labels to metagenomic DNA sequences  |
| manta                 | Tool to call structural variants                                                          |
| mitodel               | Tool to identify mitochondrial deletion signatures                                        |
| nextclade             | Viral genome clade assignment                                                             |
| peddy                 | Tool to check pedigree and ancestral relations                                            |
| picard                | Picard set of bioinformatic tools                                                         |
| pizzly                | Fusion caller                                                                             |
| retroseq              | Mobile element caller                                                                     |
| salmon-quant          | Transcript quantification                                                                 |
| sention               | Sention algorithm                                                                         |
| somalier              | Tool for sample-swap and relatedness checks                                               |
| squid                 | Fusion caller                                                                             |
| star-fusion           | Fusion caller                                                                             |
| stringtie             | Transcript assembler                                                                      |
| svdb                  | Tool to merge SV vcf files from multiple variant callers                                  |
| tiddit                | Tool to identify chromosomal rearrangements                                               |
| tnscope               | Call snv indels                                                                           |
| tnscope-umi           | Call snv indels for umi                                                                   |
| upd                   | Uniparent disomy caller from bjhall                                                       |
| vardict               | Cancer variant caller                                                                     |
| wisecondor            | NIPT caller                                                                               |

## VALIDATION TAGS

| Tag name   | Description                      |
|------------|----------------------------------|
| ped-check  | Results from pedigree validation |
| qc-metrics | QC metrics from analysis         |
| sex-check  | Results from sex validation      |

## VARIANT TAGS

| Tag name                      | Description                                         |
|-------------------------------|-----------------------------------------------------|
| cnv                           | Copy number variants                                |
| germline                      | Associated with germline variants                   |
| mobile-elements               | Mobile elements                                     |
| normal                        | Associated with normal sample                       |
| rhocall-viz                   | Runs of homozygosity index                          |
| smn-calling                   | Copy number calls for the SMN gene                  |
| snv                           | Single nucleotide variants and short indels         |
| snv-bcf                       | Gvcf including all SNV variants                     |
| snv-gbcf                      | Gvcf including all SNV variants                     |
| somatic                       | Associated with somatic variants                    |
| sv                            | Structural variants                                 |
| sv-bcf                        | Gvcf including all SV variants                      |
| sv-vcf                        | Variant call formated file with structural variants |
| sv-vcf-index                  | Following index                                     |
| telomere-calling              | Variants from telomere calling                      |
| tmb                           | Tumor mutational burden information                 |
| tumor                         | Associated with tumor sample                        |
| upd                           | Uniparental disomy variants                         |
| variants                      | File pertaining variant information in some way     |
| vcf                           | Variant call formated file                          |
| vcf-index                     | Following index                                     |
| vcf-snv                       | SNV variant call formated file                      |
| vcf-snv-clinical              | SNV variants from clinical panels                   |
| vcf-snv-clinical-index        | Following index                                     |
| vcf-snv-filtered              | SNV variants filtered by BALSAMIC                   |
| vcf-snv-filtered-index        | Following index                                     |
| vcf-snv-germline-normal       | SNV germline normal variants                        |
| vcf-snv-germline-normal-index | Following index                                     |
| vcf-snv-germline-tumor        | SNV germline tumor variants                         |
| vcf-snv-germline-tumor-index  | Following index                                     |
| vcf-snv-index                 | Following index                                     |
| vcf-snv-research              | SNV variants from whole genome                      |
| vcf-snv-research-index        | Following index                                     |
| vcf-str                       | Short tandem repeat variants                        |
| vcf-str-index                 | Following index                                     |
| vcf-sv                        | SV variant call formated file                       |
| vcf-sv-clinical               | SV variants from clinical panels                    |
| vcf-sv-clinical-index         | Following index                                     |
| vcf-sv-germline-normal        | SV germline normal variants                         |
| vcf-sv-germline-normal-index  | Following index                                     |
| vcf-sv-germline-tumor         | SV germline tumor variants                          |
| vcf-sv-germline-tumor-index   | Following index                                     |
| vcf-sv-index                  | Following index                                     |
| vcf-sv-research               | SV variants from whole genome                       |
| vcf-sv-research-index         | Following index                                     |
| vcf-umi-snv                   | Raw SNV UMI variant formatted file                  |
| vcf-umi-snv-clinical          | SNV UMI variants from clinical panels               |
| vcf-umi-snv-clinical-index    | Following index                                     |
| vcf-umi-snv-index             | Following index                                     |
| vcf-umi-snv-research          | SNV UMI variant formatted file                      |
| vcf-umi-snv-research-index    | Following index                                     |
| vcf2cytosure                  | Conversion from vcf format to cytosure format       |
