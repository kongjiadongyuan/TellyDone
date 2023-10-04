from trogon import tui
from typing import List

import click


@tui(command="interactive", help="TellyDone TUI")
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
    pass


@cli.command(help="Tell TellyDone's configuration")
def env():
    pass
