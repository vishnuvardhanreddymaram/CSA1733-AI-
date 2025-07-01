from itertools import combinations

def tsp(graph):
    n = len(graph)
    memo = {}

    for k in range(1, n):
        memo[(1 << k, k)] = (graph[0][k], 0)

    for r in range(2, n):
        for subset in combinations(range(1, n), r):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k: continue
                    res.append((memo[(prev, m)][0] + graph[m][k], m))
                memo[(bits, k)] = min(res)

    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((memo[(bits, k)][0] + graph[k][0], k))
    return min(res)

# Example: 4 cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp(graph))  