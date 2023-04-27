"""
Build weighted graph using coin
pairs data extracted from binace API
"""
import networkx as nx
import yaml
from yaml.loader import SafeLoader

from coin_pairs import prepare_for_bellman_ford


def get_negative_circuits(api_key, secret):
    """Get negative circuits from coin pairs
    """
    coin_ratio_lst = prepare_for_bellman_ford(api_key, secret)
    all_unique_coins = set([i['from'] for i in coin_ratio_lst] +
                            [i['to'] for i in coin_ratio_lst])

    map = {v: k for k, v in enumerate(all_unique_coins)}

    # create graph with number of vertices
    g = nx.DiGraph()

    # add edges
    weighted_edges = [(map[i['from']], map[i['to']],
                        i['ratio']) for i in coin_ratio_lst]
    g.add_nodes_from([map[i] for i in all_unique_coins])
    g.add_weighted_edges_from(weighted_edges)
    # this is all elementary circuits
    all_seqs = nx.recursive_simple_cycles(g)

    # TODO: find out non-single-vertex and negative circuits


if __name__ == "__main__":
    with open("testnet_keys.yaml") as f:
        keys = yaml.load(f, Loader=SafeLoader)
 
    negative_circuits = get_negative_circuits(keys['api_key'], keys['secret'])

