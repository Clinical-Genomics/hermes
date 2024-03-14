# Contributing to Hermes 

To ensure consistency and compatibility within our tools, pipeline developers are encouraged to adhere to the following
guidelines when contributing to Hermes.

## Deliverables Format

Workflows must clearly define their deliverables in a [standardised format](https://atlas.scilifelab.se/infrastructure/dataflow/workflow/files_delivery/).

## Tags Format

Tags provide additional context or metadata about the workflow output files and play a crucial role in organising and 
categorising them within the repository and [CG].

When adding or modifying tags, please follow these guidelines:
  - Use descriptive names within tag sets that accurately represent the file's purpose, domain, or functionality.
  - Maintain a consistent syntax for individual tags, such as using lowercase letters and hyphens to separate words
    (e.g., `qc-metrics`, `vcf-snv-clinical`). Whenever possible, limit the tag syntax to a maximum of three words.
  - Ensure that each tag set uniquely describes a file to facilitate individual retrieval by other tools if needed.
    Therefore, strictly avoid adding the same tag list to multiple files to prevent ambiguity.
  - Ensure compatibility with the tag format required by [CG] for long-term storage (`long-term-storage`) and delivery 
    (`clinical-delivery`).

## How to Contribute

If you would like to contribute, please follow these steps:
1. Create a new branch for your contribution.
2. Make your changes, ensuring adherence to the guidelines outlined above.
3. Submit a pull request, providing a clear description of the changes made and their purpose.
4. Test your changes thoroughly to ensure functionality and compatibility with [CG].

If you encounter any bugs, have feature requests, or would like to suggest improvements, please create an issue before
starting to work on them.

[CG]: https://github.com/Clinical-Genomics/cg
