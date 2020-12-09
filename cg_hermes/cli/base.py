import logging
from enum import Enum

import coloredlogs
import typer

from cg_hermes.cli import convert, export, validate

app = typer.Typer()

app.add_typer(convert.app, name="convert")
app.add_typer(validate.app, name="validate")
app.add_typer(export.app, name="export")


class LogLevel(str, Enum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"


@app.callback()
def main(loglevel: LogLevel = typer.Option(LogLevel.info, help="Set the log level")):
    """
    Manage users in the awesome CLI app.
    """
    coloredlogs.install(level=loglevel.value)
