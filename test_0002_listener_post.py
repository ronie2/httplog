import requests
import pytest

from config.conf import cfg

uri = []

host = cfg["service"]["home"]["host"]
port = cfg["service"]["home"]["port"]

for listener in cfg["server"].values():
    for method in listener.values():
        uri.append(host + port + method["endpoint"])

@pytest.fixture(params=uri)
def connection(request):
    resp = requests.post(trequest.param)
    return resp

def test_0001_home(connection):
    assert connection.status_code == 200

pytest.main()
