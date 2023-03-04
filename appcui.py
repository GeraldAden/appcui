import click
from commands import *

@click.group()
def cli():
    pass

cli.add_command(health)
cli.add_command(version)

if __name__ == '__main__':
    cli()