import asyncio
from aiohttp import web

from conf import cfg
from handles import *

app = web.Application()

for listener in cfg["server"].values():
    for method in listener.values():
        calable = method["handle"]
        app.router.add_route(method["method"],
                             method["endpoint"],
                             eval(method["handle"]))

web.run_app(app)
