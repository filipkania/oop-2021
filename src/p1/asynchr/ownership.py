import asyncio
from collections import defaultdict
import csv
from dataclasses import dataclass
import dataclasses
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
    __owners: dict[int, FileMeta] = {}
    async def init(self):
        if path.exists(FILE_NAME):
            print("Reading CSV file...")
            reader = csv.DictReader(open(FILE_NAME))

            for line in reader:
                file = FileMeta(**line)
                self.__owners[line["filename"]] = file

        asyncio.create_task(self.periodic_save())

    async def periodic_save(self):
        while True:
            await asyncio.sleep(10)
            writer = csv.DictWriter(open(FILE_NAME, "w"), fieldnames=["filename", "studentid", "groupid"])

            writer.writeheader()
            for filename in self.__owners:
                writer.writerow(dataclasses.asdict(self.__owners[filename]))


async def main():
    # token = await UserService.login_user('kurs01', '...')
    # print(token)
    # print(await UserService.get_user(token.wdauth))

    store = OwnershipStore()
    await store.init()

asyncio.run(main())