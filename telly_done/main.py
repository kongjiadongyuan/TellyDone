from trogon import tui
from typing import List

import click


@click.group()
def cli():
    pass


@cli.command(
    "exec", help="Execute TellyDone", context_settings={"ignore_unknown_options": True}
)
@click.option("-S", "--silent", is_flag=True, help="Silent mode")
@click.argument("args", nargs=-1)
def execute(silent: bool, args: List[str]):
    pass


@cli.command(help="Configure TellyDone")
def config():
    from .config.ui import spawn_ui

    spawn_ui()


@cli.command(help="Tell TellyDone's configuration")
def env():
    pass
