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
        except KeyError as error:
            raise KeyError("Could not find key") from error
    
    def add_mfa(self, key: str, secret: str) -> None:
        self.backend.store(key, {"secret": secret})

    def get_mfas(self) -> list[str]:
        return self.backend.get_keys()

    