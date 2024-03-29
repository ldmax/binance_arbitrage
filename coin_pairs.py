"""syncronous version of coin_pairs.py

Download coin pairs via binance API
and store in memory
TODO: or store in JSON files?
"""
from math import log

from binance import Client


def prepare_for_bellman_ford(api_key, api_secret):
    """Prepare nodes and weights of weighted DAG
    that is to be consumed by Bellman-Ford algorithm
    """
    client = Client(api_key, api_secret)#, testnet=True)
    # get exchange info
    exchange_info = client.get_exchange_info()

    # only these coins in binance?
    pairs = [{i['symbol']: {
        'from': i['baseAsset'],
        'to': i['quoteAsset']}} for i in exchange_info['symbols']]

    # get time-weighted average price (5 minutes) for each coin pairs
    coin_price_lst = []
    for coin in pairs:
        coin_price_dict = {}
        pair = list(coin.keys())[0]
        coin_price_dict['from'] = coin[pair]['from']
        coin_price_dict['to'] = coin[pair]['to']
        # TODO: use order book to replace avg price
        coin_price_dict['rate'] = client.get_avg_price(symbol=pair)['price']
        coin_price_lst.append(coin_price_dict)

    # apply Eric Han's formula
    coin_ratio_lst = [{
        'from': i['from'],
        'to': i['to'],
        'ratio': -log(float(i['rate']))} for i in coin_price_lst]
    return coin_ratio_lst
