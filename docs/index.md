# Hermes

Hermes :postal_horn: is a package to handle the communication between workflows and CG.

The name [Hermes][hermes-name] comes from greek mythology, he was considered to be the messenger between the humans and the gods, feel free to interpret that as you like:). Hermes was moving swiftly between the worlds aided by his winged sandals.

## Installation

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

# Usage

## Deliverables

Each workflow specifies its output, or result files, in some way. CG wants to have this input in a certain way to know how to fetch files from housekeeper etc. Hermes is used to convert the deliverables specification from the workflow to the CG format so that CG safely can store the information without parsing different files in different ways.

Also, this is the place where workflow developers can communicate around tags, what to deliver, etc. without understanding how CG works.

## Starting workflows

I think it would be a good idea to have Hermes starting the workflows as well as it is the workflow developers who know this best, following the reasoning above.

[hermes-name]: https://en.wikipedia.org/wiki/Hermes
[poetry]: https://python-poetry.org/docs/#installation
