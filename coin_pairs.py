"""
Download coin pairs via binance API
and store in memory
TODO: or store in JSON files?
"""
from binance import Client
from math import log
import requests


def prepare_for_bellman_ford(api_key, api_secret):
    """Prepare nodes and weights of weighted DAG
    that is to be consumed by Bellman-Ford algorithm
    """
    # TODO: potential exception should be handled
    client = Client(api_key, api_secret)#, testnet=True)

    # get exchange info
    # TODO: potential exception should be handled
    exchange_info = client.get_exchange_info()

    # only these coins in binance?
    pairs = [{i['symbol']: {
        'from': i['baseAsset'],
        'to': i['quoteAsset']}} for i in exchange_info['symbols']]

    # get time-weighted average price (5 minutes) for each coin pairs
    # TODO: too slow! can socket accelerate getting avg price?
    coin_price_lst = []
    for coin in pairs:
        coin_price_dict = {}
        pair = list(coin.keys())[0]
        coin_price_dict['from'] = coin[pair]['from']
        coin_price_dict['to'] = coin[pair]['to']
        # TODO: very slow to get average price
        #        use some async or socket to accelerate
        coin_price_dict['rate'] = client.get_avg_price(symbol=pair)['price']
        coin_price_lst.append(coin_price_dict)

    # apply Eric Han's formula
    coin_ratio_lst = [{
        'from': i['from'],
        'to': i['to'],
        'ratio': -log(float(i['rate']))} for i in coin_price_lst]
    return coin_ratio_lst


def get_response(url):
    res = requests.get(url)
    res.raise_for_status()
    if res.status_code == 200:
        return res.json()
    return None


def get_exchange_info():
    base_url = 'https://api.binance.com'
    endpoint = '/api/v3/exchangeInfo'
    return get_response(base_url + endpoint)


def create_coin_pairs():
    """Create coin pairs from binance API
    """
    info = get_exchange_info()
    if info:
        pairs = info['symbols']
        full_data_dic = {s['symbol']: s for s in pairs}
        return full_data_dic.keys()
    return None
