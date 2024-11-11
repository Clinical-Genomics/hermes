import logging
from enum import StrEnum
from typing import Optional

import coloredlogs
import typer

from cg_hermes.cli import convert, export, validate
from cg_hermes.constants.hermes import HERMES_VERSION

app = typer.Typer(no_args_is_help=True)

app.add_typer(convert.app, name="convert")
app.add_typer(validate.app, name="validate")
app.add_typer(export.app, name="export")

LOG = logging.getLogger(__name__)


class LogLevel(StrEnum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"


def version_callback(value: bool):
    if value:
        typer.echo(f"hermes version: {HERMES_VERSION}")
        raise typer.Exit()


@app.callback()
def main(
    loglevel: LogLevel = typer.Option(LogLevel.info, help="Set the log level"),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    ),
):
    """
    Manage users in the awesome CLI app.
    """
    LOG.info("Running hermes")
    coloredlogs.install(level=loglevel)
