import asyncio
import hashlib
from dataclasses import dataclass

import aiohttp


@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int


class UnauthorizedError(BaseException):
    def __str__(self) -> str:
        return 'Wrong username or password :/'


class UnknownError(BaseException):
    pass


async def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


async def login_user(album: str, password: str) -> WdToken:
    _hash = await hash_password(password)
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://wdauth.wsi.edu.pl/authenticate?album={album}&pass={_hash}') as resp:
            if resp.status == 200:
                data = await resp.json()
                return WdToken(studentid=data['token']['studentid'],
                               wdauth=data['token']['wdauth'],
                               expiry_epoch_s=data['token']['expiry_epoch_s'])
            elif resp.status == 401:
                raise UnauthorizedError
            else:
                raise UnknownError


async def main():
    token = await login_user('kurs01', '...') #f6b22d5e-a9df-4a36-8ae4-f347657faaf6
    print(token)

if __name__ == '__main__':
    asyncio.run(main())