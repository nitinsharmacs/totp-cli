import click
import pyotp


@click.command()
@click.option('--name', help='Name of 2MFA', required=True)
def totp_cli(name: str):
    print(name)

