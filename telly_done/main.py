from typing import List
import click

from .config import get_config
from .plugins import execute as do_execute
from .plugins import watch as do_watch


@click.group()
@click.option("-C", "--config_path", default=None)
@click.pass_context
def cli(ctx, config_path: str):
    config = get_config(config_path)
    ctx.ensure_object(dict)
    ctx.obj["config"] = config


@cli.command(
    "exec", help="Execute Command", context_settings={"ignore_unknown_options": True}
)
@click.argument("args", nargs=-1)
@click.pass_context
def execute(ctx, args: List[str]):
    config = ctx.obj["config"]
    do_execute(config, args)


@cli.command("watch", help="Watch Process")
@click.option(
    "-C",
    "--continuous",
    is_flag=True,
    default=False,
    help="Continuously notify when process is alive",
)
@click.option("-I", "--interval", type=int, default=1800, help="Notify interval")
@click.argument("pid", type=int, required=True, nargs=1)
@click.pass_context
def watch(ctx, pid: int, continuous: bool, interval: int):
    config = ctx.obj["config"]
    config.setdefault("watch", {})

    watch_config = {
        "continuous": continuous,
        "interval": interval,
    }

    config["watch"].update(watch_config)

    do_watch(config, pid)
