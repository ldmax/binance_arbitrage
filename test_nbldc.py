"""Test unicorn-binance-local-depth-cache
"""
import unicorn_binance_local_depth_cache
from pprint import pprint


ubldc = unicorn_binance_local_depth_cache.BinanceLocalDepthCacheManager(exchange="binance.com")

ubldc.create_depth_cache("BTCUSDT")

asks = ubldc.get_asks("BTCUSDT")
bids = ubldc.get_bids("BTCUSDT")

pprint(asks)
print("-"*100)
pprint(bids)
