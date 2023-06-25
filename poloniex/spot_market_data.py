"""Play with spot APIs in Market Data section
"""
import requests
from typing import List, Dict


def get_all_tickers() -> List[Dict]:
    """Call prices API
    """
    url = 'https://api.poloniex.com/markets/price'
    res = requests.get(url)
    if res.status_code != 200:
        print('Failed to call prices API')
        return []
    return res.json()


def get_ticker(symbol: str) -> Dict:
    """Get tickers of a given symbol
    """
    url = f'https://api.poloniex.com/markets/{symbol}/price'
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Failed to call prices API for {symbol}')
        return {}
    return res.json()
