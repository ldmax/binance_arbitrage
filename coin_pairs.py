"""
Download coin pairs via binance API
and store in memory
TODO: or store in JSON files?
"""
import yaml
from binance import Client
from yaml.loader import SafeLoader
from pprint import pprint
from math import log


with open("testnet_keys.yaml") as f:
    keys = yaml.load(f, Loader=SafeLoader)

client = Client(keys['api_key'], keys['secret'], testnet=True)

# get exchange info
exchange_info = client.get_exchange_info()

pprint(exchange_info)

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
    coin_price_dict['rate'] = client.get_avg_price(symbol=pair)['price']
    coin_price_lst.append(coin_price_dict)

pprint(coin_price_lst)

# apply Eric Han's formula
coin_ratio_lst = [{
    'from': i['from'],
    'to': i['to'],
    'ratio': log(float(i['rate']))} for i in coin_price_lst]


# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph

class Graph(object):
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist)


# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # function call
    g.BellmanFord(0)
