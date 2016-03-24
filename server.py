from aiohttp import web

from handles.handles import *
from config.conf import cfg

app = web.Application()

for listener in cfg["server"].values():
    for method in listener.values():
        calable = method["handle"]
        app.router.add_route(method["method"],
                             method["endpoint"],
                             eval(method["handle"]))

web.run_app(app)
