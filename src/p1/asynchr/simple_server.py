from asyncio import sleep

from aiohttp import web
from sympy import isprime
from p1.asynchr.toolz import is_really_prime

routes = web.RouteTableDef()

# aiohttp ... (pip install aiohttp)
"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""






@routes.get('/')
async def hello(request):
    n = 1
    print(f'{n} request received')
    return web.json_response({'comment': f'hello from {n}!'})


@routes.get('/welcome')
async def hello(request):
    name = request.rel_url.query.get('name', 'none')
    n = 'kadabra'
    return web.json_response({'comment': f'hello from n!'})


# @routes.get('/start_monitor')
# @routes.get('/monitor_results') # --> wyślij zdjęcie do klienta...




@routes.get('/welcome')
async def hello2(request):
    name = request.rel_url.query['name']
    await sleep(1.2)
    print(f'welcome request received for {name}')
    return web.json_response({'comment': f'hello {name}!'})


@routes.get('/add')
async def hello(request):
    a = float(request.rel_url.query.get('a', 0))
    b = float(request.rel_url.query.get('b', 0))
    return web.json_response({'result': a + b})

@routes.get('/is_prime')
async def primeroute(r):
    a = int(r.rel_url.query.get('a', 0))

    return web.json_response({'result': isprime(a)})

async def hello3(request):
    a = float(request.rel_url.query['a'])
    b = float(request.rel_url.query['b'])
    return web.json_response({'result': a + b})

@routes.get('/is_prime1')
async def hello4(request):
    x = int(request.rel_url.query['x'])
    res = await is_really_prime(x)
    return web.json_response({'result': res})


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=4411)
