"""
Main for totp cli
"""
import os
import sys
import click
import pyperclip

from totp_cli.storage import FileStorageBackend

from totp_cli.totp_manager import TOTP_Manager

FILE_PATH = f"{os.environ['HOME']}/.totp-secrets.json"

storage_backend = FileStorageBackend(FILE_PATH)
totp_manager = TOTP_Manager(storage_backend)

def list_avail_mfas(ctx, param, incomplete):
    return totp_manager.get_mfas()

@click.group()
def totp_cli():
    pass

@totp_cli.command(help="Get one time OTP for given MFA.")
@click.argument('name', shell_complete=list_avail_mfas)
def get(name: str):
    try:
        otp = totp_manager.get_otp(name)
        pyperclip.copy(otp)
        print(otp)
        print("OTP is copied to clipboard.")
    except KeyError as err:
        print(err)
        sys.exit(1)


@totp_cli.command(help=
    """
    Add new 2MFA entry.
    For example,
    totp add --name gitlab:user base32secret
    """
    )
@click.option('--name', help='Name of 2MFA', required=True)
@click.option(
    '--secret', 
    help="Base32 secret. Alternative to QR code while setting up 2MFA.",
    required=True)
def add(name: str, secret: str):
    totp_manager.add_mfa(name, secret)
    print("MFA added successfully.")
