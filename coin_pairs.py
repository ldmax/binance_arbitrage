"""
Download coin pairs via binance API
and store in memory
TODO: or store in JSON files?
"""
import yaml
from binance import Client
from yaml.loader import SafeLoader


with open("testnet_keys.yaml") as f:
    keys = yaml.load(f, Loader=SafeLoader)

client = Client(keys['api_key'], keys['secret'])

