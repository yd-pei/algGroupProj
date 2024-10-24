import heapq

inf = float('inf')

def heap_least_cost(N:int, C:list, a:list, k:int):
    """MGTC using priority queue
    Args:
        N (int): The number of galaxies
        C (list): The teleportattion cost from i to j C[i][j]
        a (list): a[i] is astro-haunted or not - 1 or 0
        k (int): The maximum number of astro-haunted galxies allowed in the path
    Returns:
        min_cost (float): The minimum cost to reach galaxy n from galaxy 1 with at most k astro-haunted visited galaxies
    """
    # Base Case
    D = [[inf] * (k+1) for _ in range(N+1)]
    D[1][0] = 0

    q = []
    heapq.heappush(q, (0, 1, 0))
    
    while q:
        cost, i, h = heapq.heappop(q)
        if D[i][h] < cost:
            continue
        for j in range(1, N+1):
            if i!=j:
                new_cost = cost + C[i][j]
                new_h = h + a[j]
                if new_h <= k and new_cost < D[j][new_h]:
                    D[j][new_h] = new_cost
                    heapq.heappush(q, (new_cost, j, new_h))

    min_cost = min(D[N][h] for h in range(k))
    return min_cost