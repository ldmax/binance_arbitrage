"""
Build weighted graph using coin
pairs data extracted from binace API
"""
import yaml
from yaml.loader import SafeLoader
from coin_pairs import prepare_for_bellman_ford


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

    def enumerate_circutes(self):
        # copied from github
        # red-black-tech/find-all-cycles
        paths = []
        memo = [False for _ in self.graph]
        P = []

        def path_extension():
            for w in self.graph[P[-1]]:
                if w == s:
                    paths.append(list(P))

                if w > s and not memo[w]:
                    memo[w] = True
                    P.append(w)
                    path_extension()
                    P.pop()
                    memo[w] = False

        for s in range(len(self.graph)):
            P = [s]
            memo[s] = True
            path_extension()

        return paths



# Driver's code
if __name__ == '__main__':
    with open("testnet_keys.yaml") as f:
        keys = yaml.load(f, Loader=SafeLoader)

    coin_ratio_lst = prepare_for_bellman_ford(keys['api_key'], keys['secret'])
    all_unique_coins = set([i['from'] for i in coin_ratio_lst] +
                            [i['to'] for i in coin_ratio_lst])

    map = {v: k for k, v in enumerate(all_unique_coins)}

    # create graph with number of vertices
    g = Graph(len(all_unique_coins))

    # add edges
    for d in coin_ratio_lst:
        g.addEdge(map[d['from']], map[d['to']], d['ratio'])


    # function call
    all_ele_cycles = g.enumerate_circutes()
    print(all_ele_cycles)
