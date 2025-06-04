from abc import ABC, abstractmethod
import json
import os

from totp_cli.json_util import read_json, write_json


class StorageBackend(ABC):
    @abstractmethod
    def find(self, key: str) -> dict:
        pass
    @abstractmethod
    def store(self, key: str, value: dict):
        pass
    @abstractmethod
    def get_keys(self) -> list[str]:
        pass


class FileStorageBackend(StorageBackend):
    def __init__(self, storage_file_path: str) -> None:
        self.storage_file_path = storage_file_path
        self.file_content = {}

        if not os.path.exists(self.storage_file_path):
            self.write()
        else:
            self.file_content = (read_json(self.storage_file_path))

    def find(self, key: str) -> dict:
        return self.file_content[key]

    def store(self, key: str, value: dict):
        self.file_content[key] = value
        self.write()

    def get_keys(self) -> list[str]:
        return list(self.file_content.keys())

    def write(self) -> None:
        write_json(self.storage_file_path, self.file_content)