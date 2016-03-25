# httplog
**httplog** is a simple wrapper around [aiohttp](http://aiohttp.readthedocs.org) HTTP server. It can be used as simple asynchronous WEB server for tesing purpose.
**httplog** is written in **Python 3.5** (it uses `async` and `await` syntax introduced in [PEP 492](https://docs.python.org/3/whatsnew/3.5.html?highlight=async#whatsnew-pep-492)) and won't start in Python version earlier than **Python 3.5**.

To start server:
1. Edit `config/conf.py` file:
```python
cfg = {
    "server": {
        "listener_name": {
            "resource_name": {
                "method": "GET", # GET or POST or PUT or DELETE or '*' - any (wildcard)
                "endpoint": "/v1/endpoint", # endpoint say: http://127.0.0.1:5000/v1/endpoint
                "handle": "handle_method" # handle method located in handles/handles.py (any calable - say async def) to process HTTP request
            }
        }
    }
}
```
2. Edit handles/handles.py file:
```python
import asyncio                                                                      
import aiohttp                                                                      
from aiohttp import web                                                                                                                           
                                                                                    
async def handle_method(request):                                                           
    return web.Response(body = b"Hello, world!")
```
3. Run server (you need [aiohttp](http://aiohttp.readthedocs.org) HTTP client/server):
`$ python server.py`

4. Run test (you need [Pytest](http://pytest.org) testing framework to be installed):
`$ py.test`

## Note
**httplog** is under development... new features will be there ASAP (I hope)
---
Thanks!
Roman Nieviezhyn

