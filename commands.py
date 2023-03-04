import click

@click.command()
@click.argument('service_name')
@click.option('--env', default='devint', help=' deployment environment')
def health(service_name, env):
    click.echo('Getting health info for ' + service_name + ' in ' + env)

@click.command()
@click.argument('service-name')
@click.option('--env', default='devint', help=' deployment environment')
def version(service_name, env):
    click.echo('Getting version info for ' + service_name + ' in ' + env)