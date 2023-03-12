"""
experimental code when reading python-binance document
"""
import yaml
from binance import Client
from yaml.loader import SafeLoader
import binance
from pprint import pprint


with open("testnet_keys.yaml") as f:
    keys = yaml.load(f, Loader=SafeLoader)

client = Client(keys['api_key'], keys['secret'], testnet=True)

# Constants are in class binance.client.Client
clt = binance.client.Client

# SPOT
print(clt.SYMBOL_TYPE_SPOT)

# order status
# ORDER STATUS NEW
print(clt.ORDER_STATUS_NEW)
print(clt.ORDER_STATUS_PARTIALLY_FILLED)
print(clt.ORDER_STATUS_FILLED)
print(clt.ORDER_STATUS_CANCELED)
print(clt.ORDER_STATUS_PENDING_CANCEL)
print(clt.ORDER_STATUS_REJECTED)
print(clt.ORDER_STATUS_EXPIRED)

# kline interval
# 1 minute
print(clt.KLINE_INTERVAL_1MINUTE)
# 3 minutes
print(clt.KLINE_INTERVAL_3MINUTE)
# 5 minutes
print(clt.KLINE_INTERVAL_5MINUTE)
# 15 minutes
print(clt.KLINE_INTERVAL_15MINUTE)
# 30 minutes
print(clt.KLINE_INTERVAL_30MINUTE)
# 1 hour
print(clt.KLINE_INTERVAL_1HOUR)
# 2 hours
print(clt.KLINE_INTERVAL_2HOUR)
# 4 hours
print(clt.KLINE_INTERVAL_4HOUR)
# 6 hours
print(clt.KLINE_INTERVAL_6HOUR)
# 8 hours
print(clt.KLINE_INTERVAL_8HOUR)
# 12 hours
print(clt.KLINE_INTERVAL_12HOUR)
# 1 day
print(clt.KLINE_INTERVAL_1DAY)
# 3 day
print(clt.KLINE_INTERVAL_3DAY)
# 1 week
print(clt.KLINE_INTERVAL_1WEEK)
# 1 month
print(clt.KLINE_INTERVAL_1MONTH)


# buy or sell side
print(clt.SIDE_BUY)
print(clt.SIDE_SELL)


# order type
print(clt.ORDER_TYPE_LIMIT)  # 限价单
print(clt.ORDER_TYPE_MARKET) # 市价单
print(clt.ORDER_TYPE_STOP_LOSS)  # 止损单
print(clt.ORDER_TYPE_STOP_LOSS_LIMIT)  # 止损限价单
print(clt.ORDER_TYPE_TAKE_PROFIT)  # 止盈单
print(clt.ORDER_TYPE_TAKE_PROFIT_LIMIT)  # 止盈限价单
print(clt.ORDER_TYPE_LIMIT_MAKER)


# time in force
print(clt.TIME_IN_FORCE_GTC)
print(clt.TIME_IN_FORCE_IOC)
print(clt.TIME_IN_FORCE_FOK)


# newOrderRespType
print(clt.ORDER_RESP_TYPE_ACK)
print(clt.ORDER_RESP_TYPE_RESULT)
print(clt.ORDER_RESP_TYPE_FULL)


# get exchange info
excg_info = client.get_exchange_info()

# get coins info
tickers_info = client.get_all_tickers()

# get exchange info for particular symbol (coin pair)
bnbbtc = client.get_symbol_info("BNBBTC")

# get daily account snapshot
snapshot = client.get_account_snapshot(type="SPOT")

# get current products
products = client.get_products()
