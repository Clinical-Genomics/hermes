# Hermes 
![Tests][tests-badge] [![codecov][codecov-badge]][codecov-url][![CodeFactor][codefactor-badge]][codefactor-url][![Code style: black][black-badge]][black-url]

Hermes :postal_horn: is a package to handle the communication between workflows and CG.

The name [Hermes][hermes-name] comes from greek mythology, he was considered to be the messenger between the humans and the gods, feel free to interpret that as you like:). Hermes was moving swiftly between the worlds aided by his winged sandals.

## Local Installation 

### Pypi

```
pip install cg-hermes
```

### Github

Install [poetry][poetry]

```
git clone https://github.com/Clinical-Genomics/cg-hermes
poetry install 
```

## Contributing

Please check out our [guide for contributing to Hermes](CONTRIBUTING.md).

## Deployment

1. See [DEPLOYMENT.md](https://github.com/Clinical-Genomics/hermes/blob/main/DEPLOYMENT.md)

# Usage

## Deliverables

Each workflow specifies its output, or result files, in some way. CG wants to have this input in a certain way to know how to fetch files from housekeeper etc. Hermes is used to convert the deliverables specification from the workflow to the CG format so that CG safely can store the information without parsing different files in different ways.

Also, this is the place where workflow developers can communicate around tags, what to deliver etc without understanding how CG works.

## Starting workflows

I think it would be a good idea to have Hermes starting the workflows as well as it is the workflow developers who know this best, following the reasoning above.


[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black 
[codefactor-badge]: https://www.codefactor.io/repository/github/clinical-genomics/hermes/badge
[codefactor-url]: https://www.codefactor.io/repository/github/clinical-genomics/hermes
[tests-badge]: https://github.com/Clinical-Genomics/hermes/workflows/Tests/badge.svg
[codecov-badge]: https://codecov.io/gh/Clinical-Genomics/hermes/branch/main/graph/badge.svg?token=MA62EOQTX7
[codecov-url]: https://codecov.io/gh/Clinical-Genomics/hermes
[hermes-name]: https://en.wikipedia.org/wiki/Hermes
[poetry]: https://python-poetry.org/docs/#installation
