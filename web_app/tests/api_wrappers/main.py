from .endpoint_1_api import Endpoint1
from .endpoint_2_api import Endpoint2
from .endpoint_3_api import Endpoint3
from .endpoint_async_api import EndpointAsync
import configparser

config = configparser.ConfigParser()
config.read('web_app/tests/config.cfg')
url = config['application.access']['url']
port = config['application.access']['port']

class TestApplicationApi():
    endpoint1 = Endpoint1(url, port)
    endpoint2 = Endpoint2(url, port)
    endpoint3 = Endpoint3(url, port)
    endpoint_async = EndpointAsync(url, port)

