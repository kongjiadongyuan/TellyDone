from typing import List
import click

from .config import get_config
from .watch import execute as do_execute


@click.group()
@click.option("-C", "--config_path", default=None)
@click.pass_context
def cli(ctx, config_path: str):
    config = get_config(config_path)
    ctx.ensure_object(dict)
    ctx.obj["config"] = config


@cli.command(
    "exec", help="Execute TellyDone", context_settings={"ignore_unknown_options": True}
)
@click.argument("args", nargs=-1)
@click.pass_context
def execute(ctx, args: List[str]):
    config = ctx.obj["config"]
    do_execute(config, args)
