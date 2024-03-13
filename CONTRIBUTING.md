# Contributing to Hermes 

To ensure consistency and compatibility within our tools, pipeline developers are encouraged to adhere to the following
guidelines when contributing to Hermes.

## Deliverables Format

Workflows must clearly define their deliverables in a [standardised format](https://atlas.scilifelab.se/infrastructure/dataflow/workflow/files_delivery/).

## Tags Format

Tags provide additional context or metadata about the workflow output files and play a crucial role in organising and 
categorising them within the repository and [CG].

When adding or modifying tags, please follow these guidelines:
  - Use descriptive tag names that accurately represent the file's purpose, domain, or functionality.
  - Tags should follow a consistent syntax, such as using lowercase letters and hyphens to separate words (e.g., 
    `qc-metrics`, `vcf-snv-clinical`).
  - Tags should uniquely describe a file to enable individual retrieval by other tools if needed. Therefore, strictly 
    avoid adding the same tag set to multiple files, as this can lead to ambiguity.
  - Ensure that the deliverables tag specification is compatible with the format required by CG for long-term storage
    (`long-term-storage`) and delivery (`clinical-delivery`).

## How to Contribute

If you would like to contribute, please follow these steps:
1. Create a new branch for your contribution.
2. Make your changes, ensuring adherence to the guidelines outlined above.
3. Submit a pull request, providing a clear description of the changes made and their purpose.
4. Test your changes thoroughly to ensure functionality and compatibility with [CG].

If you encounter any bugs, have feature requests, or would like to suggest improvements, please create an issue before
starting to work on them.

[CG]: https://github.com/Clinical-Genomics/cg
