# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

About changelog [here](https://keepachangelog.com/en/1.0.0/)

## [1.2.0]
### Added
- New deployment instructions using bumpversion and poetry

## [1.0.0]
### Added
- Adds tags for mip-rna

## [0.10.1]
### Added
- BALSAMIC: optional tag for clinical sv deliveries

## [0.10.0]
### Added:
- MIP-rna: Tags to store files from MIP-rna

## [0.9.1]
### Changed:
- MUTANT: Hotfix to accomodate step-tag structure

## [0.9.0]
### Changed:
- MUTANT: Finalized the is_required tags
- MUTANT: Changed some reports to aggregate forms
### Added:
- MUTANT: KS tag for files specifically requested by KS/Clinical routine

## [0.8.0]
### Changed:
- BALSAMIC: All the normal tag maps changed to germline to correctly reflect the purpose of file
### Added:
- BALSAMIC: All the sets with annotated-somatic-vcf-\* have somatic tag to them
### Removed:
- BALSAMIC: annotated-somatic-vcf-pass and annotated-somatic-vcf-pass-index tags

## [0.7.0]
### Changed
- Updated deliverables for BALSAMIC 7.1.7 

## [0.6.0]
### Changed
- Mutant output files made optional. 
### Added  
- New optional/placeholder tags for pangolin delivery reports.
- New optional/placeholder tags for multiqc report

## [0.5.0]
### Changed
- Pangolin output from mutant is optional

## [0.4.0]
### Added
- Support same pipeline format as cg

## [0.3.0]
### Added
- Added support for the mutant pipeline
### Fixed
- Invalid pipeline in the self-test now defaults to error intead of mip

## [0.2.2]
### Added
- Substituted a balsamic coverage-qc-report tag
### Fixed

### Changed

## [0.2.1]

### Changed

- Change so that same file is choosen as scout snv upload vcf for all analyses

## [0.2]

### Added

- Add a delivery-report tag to balsamic

## [0.1.4]

### Changed

- Make mutect output optional for balsamic panel

## [0.1.3]

### Changed

- Hermes convert deliverables now sends a mandatory field as response

## [0.1.2]
### Added

### Fixed

- Use dicts instead of ifs

### Changed

- Update to new balsamic deliverables format

## [0.1.1]
Test publish with Github Actions


## [0.1.0]
### Added
- Converts deliverable files to CG format
