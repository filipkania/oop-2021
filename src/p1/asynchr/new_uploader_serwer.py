import os.path
from asyncio import sleep
from random import randint

from aiohttp import web
import aiohttp
from aiohttp.abc import BaseRequest
from aiohttp.web_middlewares import middleware
from faker import Faker
from urllib.parse import quote_plus as encode_uri
from os import path
import os

routes = web.RouteTableDef()
STORAGE_DIR = path.abspath(path.join(os.getcwd(), "storage/"))

# pip install aiohttp

"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""


@routes.get('/')
async def hello(request):
    print('request received')
    return web.json_response({'comment': f'hello, x={12}!'})

@middleware
async def middleware(request, handler):
    # "opakowuje" każdy request... można tu zrobić try... expect...
    print(f'request: {request}')
    resp = await handler(request)
    print(f'response: {resp.status}')
    return resp

@routes.get('/serve/{filename}')
async def serve_file(req):
    file_path = req.match_info.get("filename", "")
    file_path = path.realpath(path.join(STORAGE_DIR, encode_uri(file_path)))

    try:
        assert path.commonprefix([ file_path, STORAGE_DIR ]) == STORAGE_DIR
        assert path.exists(file_path)

        return web.FileResponse(file_path)
    except (FileNotFoundError, AssertionError):
        return web.json_response(status=404)

@routes.post('/upload')
async def accept_file(req: BaseRequest):
    """
    Funkcja przyjmująca upload pliku.
    """
    # https://docs.aiohttp.org/en/stable/web_quickstart.html#file-uploads
    print('file upload request hit...')
    reader = await req.multipart()

    # field = await reader.next()
    # name = await field.read(decode=True)

    token = req.rel_url.query.get("wdauth", "")
    if not token:
        return web.json_response(status=401)

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://wdauth.wsi.edu.pl/user?wdauth={encode_uri(token)}') as resp:
            if resp.status != 200:
                return web.json_response(status=resp.status)

    field = await reader.next()
    assert field.name == 'file'
    print(f'read field object: {field}')
    filename = field.filename
    # Cannot rely on Content-Length if transfer is chunked.
    print(f'filename:{filename}')

    # Warning: this code doesn't guarantee that filename will be unique.
    #          if file already exists with this name, existing file will
    #          get overwritten. we should be using random names instead
    #          of user specified filename...

    filename = path.realpath(path.join(STORAGE_DIR, encode_uri(filename)))
    assert path.commonprefix([ filename, STORAGE_DIR ]) == STORAGE_DIR

    size = 0
    with open(filename, 'wb') as f:
        file_as_bytes = b''
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            print(type(chunk))
            if not chunk:
                break
            size += len(chunk)
            file_as_bytes += chunk
            # f.write(chunk)
        f.write(file_as_bytes)

    return web.json_response({'name': field.filename, 'size': size})



async def starter():
    """
    Starter / app factory, czyli miejsce gdzie można inicjalizować asynchronicze konstrukty.
    """
    await sleep(0.2)
    print('app is starting..')
    # await database.connect()
    return app


app = web.Application(middlewares=[middleware])
app.add_routes(routes)
web.run_app(starter(), port=8888)  # ewentu
