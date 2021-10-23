import json

from cryptography.fernet import InvalidToken

from src.p1.secretbox.CryptoEngine import CryptoEngine
from src.p1.secretbox.FileManager import FileManager
from src.p1.secretbox.Password import Password
from src.p1.secretbox.Secret import Secret


class SecretBox:
    _secrets: list[Secret]
    _crypto: CryptoEngine = None
    _opened = False

    def __init__(self):
        self._secrets = FileManager.load_file("passwords.json")

    def open(self, key: str):
        self._crypto = CryptoEngine(key)
        self._opened = True

    def lock(self):
        del self._crypto
        self._opened = False

    def get_secret(self, website: str) -> list[Password]:
        assert self._opened
        r = []

        for secret in self._secrets:
            if secret.website == website:
                try:
                    r.append(secret.decode(self._crypto))
                except InvalidToken:
                    pass

        return r

    def store_secret(self, password_entry: Password):
        assert self._opened

        secret = Secret(password_entry.website)
        secret.encode(self._crypto, password_entry)

        assert secret.data is not None

        self._secrets.append(secret)

        r = []
        for secret in self._secrets:
            r.append({
                "website": secret.website,
                "uuid": secret.uuid,
                "data": secret.data.decode("utf-8")
            })

        FileManager.save_file("passwords.json", json.dumps(r))
