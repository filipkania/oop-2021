from asyncio import sleep
from dataclasses import dataclass

import aiohttp
import asyncio


# https://docs.aiohttp.org/en/stable/client_quickstart.html

@dataclass
class User:
    userid: str
    name: str
    address: str

@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int

async def get_user_details(userid: str) -> User:
    # odpowiednik "requests" (blokującego)
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:8888/users/{userid}/details') as resp:
            print(resp.status)
            d = await resp.json()  # tu mamy "słownik"
            u = User(**d)
            print(User(**d))  # tu tworzymy instancję klasy MyResponse
            return u

@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int

async def login_user(album: str, password: str) -> WdToken:
    """
    Funkcja logująca studenta do WD;
    - w przypadku poprawnego logowania -- zwrócić obiekt typu WdToken (który dostaniemy z serwisu wdauth.wsi.edu.pl
    - w przypadku niepoprawnego logwania -- rzucić wyjątkiem UnauthorizedError (napisać taki wyjątek)
    :return:
    """
    pass


async def main():

    for i in range(1000):
        asyncio.create_task(get_user_details(f'u{i}'))

    await sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
