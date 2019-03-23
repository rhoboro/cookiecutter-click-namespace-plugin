import logging

import click

logger = logging.getLogger(__name__)


@click.group(name='{{cookiecutter.plugin}}')
@click.pass_context
def cli(ctx):
    """Command Group"""
    pass


@cli.command()
def sample():
    """Sample command"""
    click.echo("{{cookiecutter.plugin}}'s sample was called")


if __name__ == '__main__':
    cli()
