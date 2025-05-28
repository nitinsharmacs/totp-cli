import pyotp
from totp_cli.storage import StorageBackend


class TOTP_Manager:
    def __init__(self, backend: StorageBackend):
        self.backend = backend

    def get_otp(self, key: str) -> str:
        try:
            secret = self.backend.find(key)["secret"]
            totp = pyotp.TOTP(secret)
            return totp.now()
        except KeyError:
            raise KeyError("Could not find key")

    