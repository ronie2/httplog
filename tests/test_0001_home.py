import requests
import pytest

cfg = {
    "service":{
        "home": {
             "host": "http://127.0.0.1",
             "port": ":8080",
             "resource": "",
                }
        }
    }

uri = cfg["service"]["home"]["host"] + \
      cfg["service"]["home"]["port"] + \
      cfg["service"]["home"]["resource"]

@pytest.fixture
def connection(params = uri):
    resp = requests.get(params)
    return resp

def test_0001_home(connection):
    assert connection.status_code == 200
    assert connection.text == "Hello, world!"

pytest.main()
