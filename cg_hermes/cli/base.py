import typer

from cg_hermes.cli import convert, export, validate

app = typer.Typer()

app.add_typer(convert.app, name="convert")
app.add_typer(validate.app, name="validate")
app.add_typer(export.app, name="export")
