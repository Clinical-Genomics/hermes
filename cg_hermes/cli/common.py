"""Store common utilities."""

import json
import logging
from json.decoder import JSONDecodeError
from pathlib import Path

import typer
import yaml
from yaml.parser import ParserError

LOG = logging.getLogger(__name__)


def get_deliverables(deliverables_file: Path) -> dict[str, list[dict[str, str]]]:
    """
    Open file and load into a dictionary. Try to first open YAML, then JSON.

    Raises:
        typer.Abort: If the file cannot be parsed as YAML or JSON.
    """
    with open(deliverables_file, "r") as handle:
        try:
            deliverables = yaml.load(handle, Loader=yaml.SafeLoader)
        except ParserError as error:
            LOG.error(error)
            LOG.warning(f"File {deliverables_file} is not in YAML format")
            try:
                deliverables = json.load(handle)
            except JSONDecodeError as error:
                LOG.error(error)
                LOG.warning(f"File {deliverables_file} is not in JSON format")
                LOG.warning("Can not parse file")
                raise typer.Abort()
        return deliverables
