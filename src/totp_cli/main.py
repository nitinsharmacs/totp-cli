import os
import click
from totp_cli.storage import FileStorageBackend

from totp_cli.totp_manager import TOTP_Manager

FILE_PATH = f"{os.environ['HOME']}/.totp-secrets.json"

storage_backend = FileStorageBackend(FILE_PATH)
totp_manager = TOTP_Manager(storage_backend)

@click.group()
def totp_cli():
    pass

@totp_cli.command(help="Get one time OTP.")
@click.option('--name', help='Name of 2MFA', required=True)
def get(name: str):
    try:
        otp = totp_manager.get_otp(name)
        print(otp)
    except KeyError as err:
        print(err)
        exit(1)


@totp_cli.command(help="Add new 2MFA entry.")
@click.option('--name', help='Name of 2MFA', required=True)
@click.option('--secret', help='Base32 secret. Alternative to QR code while setting up 2MFA.', required=True)
def add(name: str, secret: str):
    print("add scret")
