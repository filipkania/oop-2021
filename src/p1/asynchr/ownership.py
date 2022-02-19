import asyncio
from collections import defaultdict
import csv
from dataclasses import dataclass
from os import path
from typing import List
from wd_integration import UserService


@dataclass
class FileMeta:
    filename: str
    studentid: int
    groupid: int

FILE_NAME = "./owners.csv"


class OwnershipStore:
    __owners: dict[int, List[FileMeta]] = defaultdict(list)
    async def init(self):
        if path.exists(FILE_NAME):
            print("Reading CSV file...")
            reader = csv.DictReader(open(FILE_NAME))

            for line in reader:
                file = FileMeta(**line)
                self.__owners[line["studentid"]].append(file)


async def main():
    # token = await UserService.login_user('kurs01', '...')
    # print(token)
    # print(await UserService.get_user(token.wdauth))

    store = OwnershipStore()
    await store.init()

asyncio.run(main())