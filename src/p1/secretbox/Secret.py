import base64
import json
from dataclasses import dataclass
from uuid import uuid4

from src.p1.secretbox.CryptoEngine import CryptoEngine
from src.p1.secretbox.Password import Password


@dataclass
class Secret:
    website: str
    data: bytes = None
    uuid: str = str(uuid4())

    def decode(self, crypto: CryptoEngine) -> Password:
        assert self.data is not None

        data = crypto.decrypt(self.data)
        return Password(self.website, data["username"], data["password"], uuid=self.uuid)

    def encode(self, crypto: CryptoEngine, entry: Password):
        encrypted_data = crypto.encrypt({
            "username": entry.username,
            "password": entry.password,
        })

        self.data = encrypted_data
