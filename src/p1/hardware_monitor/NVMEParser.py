import re

from Parser import Parser

values_regex = re.compile(r'(\w*)\s*:\s(.*)')


class NVMEParser(Parser):
    data: str

    def __init__(self, filename: str):
        self.data = open(filename).read()

    def parse(self) -> dict[str, str]:
        return {k: v for k, v in values_regex.findall(self.data)}
