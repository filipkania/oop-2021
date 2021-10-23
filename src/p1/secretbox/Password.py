from dataclasses import dataclass


@dataclass
class Password:
    website: str
    username: str
    password: str
    uuid: str = None
