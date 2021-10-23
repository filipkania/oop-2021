import json

from src.p1.secretbox.Secret import Secret


class FileManager:
    def load_file(filename: str) -> list[Secret]:
        try:
            with open(filename, "r") as file:
                secrets = json.loads(file.read())
        except FileNotFoundError:
            secrets = []

        return [Secret(x["website"], bytes(x["data"], encoding='utf-8'), uuid=x["uuid"]) for x in secrets]

    def save_file(filename: str, data: str):
        try:
            with open(filename, "w") as file:
                file.write(data)
                file.close()
        except:
            pass

