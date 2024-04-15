| Taxprofiler tags                       | Mandatory | HK tags                             | Used by                              |
|----------------------------------------|-----------|-------------------------------------|--------------------------------------|
| kraken2, kraken2_combined_report       | True      | kraken2, combined-report            | clinical-delivery, long-term-storage |
| kraken2, kraken2_report                | True      | kraken2, metagenomics-report        | clinical-delivery, long-term-storage |
| krona, krona_kraken_plot               | True      | kraken2, krona, visualization       | clinical-delivery, long-term-storage |
| krona, krona_centrifuge_plot           | True      | centrifuge, krona, visualization    | clinical-delivery                    |
| bracken, bracken_combined_report       | True      | bracken, combined-report            | clinical-delivery                    |
| bracken, bracken_report                | True      | bracken, metagenomics-report        | clinical-delivery                    |
| centrifuge, centrifuge_combined_report | True      | centrifuge, combined-report         | clinical-delivery                    |
| centrifuge_report, centrifuge          | True      | centrifuge, metagenomics-report     | clinical-delivery                    |
| report, multiqc-html                   | True      | multiqc-html                        | clinical-delivery, long-term-storage |
| multiqc-json                           | True      | multiqc-json                        | clinical-delivery, long-term-storage |
| qc-metrics                             | True      | qc-metrics                          | cg, long-term-storage                |
| software-versions                      | True      | software-versions                   | cg                                   |
| multiqc-general-stats, multiqc         | True      | qc-metrics, multiqc, general-stats  | janus                                |
| multiqc-fastp, multiqc                 | True      | qc-metrics, multiqc, fastp          | janus                                |
| multiqc-samtools-stats, multiqc        | True      | qc-metrics, multiqc, samtools-stats | janus                                |
| multiqc-kraken, multiqc                | True      | qc-metrics, multiqc, kraken2        | janus                                |