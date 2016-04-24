from aiohttp import web
import asyncio

from handles.handles import *
from config.conf import cfg

main_loop = asyncio.get_event_loop()

app = web.Application(loop=main_loop)

for listener in cfg["server"].values():
    for method in listener.values():
        calable = method["handle"]
        app.router.add_route(method["method"],
                             method["endpoint"],
                             eval(method["handle"]))

web.run_app(app, host=cfg["service"]["home"]["host"],
            port=cfg["service"]["home"]["port"][1:5])
