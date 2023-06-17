"""Test what each socket returns
in BinanceSocketManager instance
"""
from binance import AsyncClient, BinanceSocketManager
import yaml
import asyncio


with open("testnet_keys.yaml") as f:
    keys = yaml.load(f, Loader=yaml.SafeLoader)

api_key = keys["api_key"]
api_secret = keys["secret"]

async def depth_socket(client):
    bsm = BinanceSocketManager(client)
    async with bsm.depth_socket(symbol="BTCUSDT") as stream:
        while True:
            res = await stream.recv()
            print(res)

async def main(api_key, api_secret):
    client = await AsyncClient.create(api_key, api_secret)
    await depth_socket(client)


if __name__ == "__main__":
    asyncio.run(main(api_key, api_secret))
