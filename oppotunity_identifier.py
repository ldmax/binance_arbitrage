"""
Using Bellman-Ford algorithm to identify arbitrage
oppotunity (negative cycle)

For now it's for spot market (coin-coin spot)
If arbitrage works, try spot-future market
"""

# to test dap-ui
def add(a, b, c = 1):
    print(a + b)
    return a + b + c


if __name__ == "__main__":
    print(add(1, 2))
