import base64
import hashlib
import json

from cryptography.fernet import Fernet


class CryptoEngine:
    key: bytes

    def __init__(self, key):
        x = hashlib.md5(key.encode("utf-8")).hexdigest().encode("utf-8")
        self.key = base64.urlsafe_b64encode(bytes(x))

    def encrypt(self, data: dict) -> bytes:
        encrypted = Fernet(self.key).encrypt(bytes(json.dumps(data).encode("utf-8")))
        return encrypted

    def decrypt(self, data: bytes) -> dict:
        decoded = Fernet(self.key).decrypt(data)

        return json.loads(decoded)
