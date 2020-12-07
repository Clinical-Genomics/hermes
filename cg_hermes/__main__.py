"""
cg_hermes.__main__

The main entry point for the command line interface.

Invoke as ``hermes`` (if installed)
or ``python -m cg_hermes`` (no install required).
"""
import sys

import coloredlogs

from cg_hermes.cli.base import app


def main():
    coloredlogs.install()
    sys.exit(app())


if __name__ == "__main__":
    main()
