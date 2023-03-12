"""
Download coin pairs via binance API
and store in memory
TODO: or store in JSON files?
"""
import yaml
from binance import Client
from yaml.loader import SafeLoader
from pprint import pprint


with open("testnet_keys.yaml") as f:
    keys = yaml.load(f, Loader=SafeLoader)

client = Client(keys['api_key'], keys['secret'], testnet=True)

# get exchange info
exchange_info = client.get_exchange_info()

pprint(exchange_info)

# are below pairs exausted?
pairs = [i['symbol'] for i in exchange_info['symbols']]
