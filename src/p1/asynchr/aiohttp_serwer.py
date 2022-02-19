from asyncio import sleep
from random import randint

from aiohttp import web
from faker import Faker

routes = web.RouteTableDef()

# pip install aiohttp

"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""


async def get_x():
    return randint(0, 100)


@routes.get('/')
async def hello(request):
    print('request received')
    x = await get_x()
    return web.json_response({'comment': f'hello, x={x}!'})


@routes.get('/welcome')
async def welcome(request):
    name = request.rel_url.query['name']
    await sleep(1.2)
    print(f'welcome request received for {name}')
    return web.json_response({'comment': f'hello {name}!'})


@routes.get('/users/{userid}/details')
async def welcome(request):
    #http://0.0.0.0:8888/users/i8811/details
    userid = request.match_info.get('userid', '')
    fake = Faker()
    user_name = fake.name()
    user_address = fake.address()
    resp = {'userid': userid, 'name': user_name, 'address': user_address }
    return web.json_response(resp)


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8888)  # ewentu
