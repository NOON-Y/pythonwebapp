import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9980)
    logging.info('server started at http://127.0.0.1:9980...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


