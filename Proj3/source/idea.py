import matplotlib.pyplot as plt
import timeit
import functools
import csv
import random
import os

seed = 42
random.seed(seed)
inf = float('inf')

def generate_data(n:int, max_cost:int=100):
    """Generate random input data for the Minimum Galaxy teleportation Cost problem.

    Args:
        n (int): number of galaxies
        max_cost (int, optional): . Defaults to 100.
    Return:
        C (list): cost matrix
        a (list): haunted status
    """
    c = [[inf]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i!= j:
                c[i][j] = random.randint(1, max_cost)

    a = [0] + [random.randint(0, 1) for _ in range(1, n)] + [0] # a[n]=0
    a[1] = 0
    return c, a

def MGTC(N:int, C:list, a:list, k:int):
    """Minimum Galaxy Teleportation Cost
        to reach galaxy n from galaxy 1
    Args:
        N (int): The number of galaxies
        C (list): The teleportattion cost from i to j C[i][j]
        a (list): a[i] is astro-haunted or not - 1 or 0
        k (int): The maximum number of astro-haunted galxies allowed in the path
    Returns:
        min_cost (float): The minimum cost to reach galaxy n from galaxy 1 with at most k astro-haunted visited galaxies
    """
    # Base Case
    D = [[inf] * (k+1) for _ in range(n+1)]
    D[1][0] = 0

    # Construct the D matrix
    for h in range(k+1):
        for i in range(2, n+1):
            for j in range(1, n+1):
                if i!=j:
                    D[i][h] = min(D[i][h], D[j][h-a[i]] + C[j][i])

    min_cost = min(D[n][h] for h in range(k))
    return min_cost

if __name__ == '__main__':

    # Time complexity for varying n with fixed k
    times = []
    k = 3
    ns = [5, 10, 25, 50, 100, 250, 500, 1000]
    for n in ns:
        c, a = generate_data(n)
        start_time = timeit.default_timer()
        min_cost = MGTC(n, c, a, k)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
        print('Minimum cost:', min_cost)
        print('Time taken:', end_time - start_time, 'seconds')

    theo_time = [n**2 * k + (n + 1)*k for n in ns]

    data = [['n', 'Experimental results', 'theoretical results']] + [[n, t, theo] for n, t, theo in zip(ns, times, theo_time)]

    with open('time_complexity_n_with_k_fixed.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Time complexity for fixed n and various values of k
    times = []
    n = 1000
    ks = [1, 5, 10, 25, 50, 100, 250]
    for k in ks:
        c, a = generate_data(n)
        start_time = timeit.default_timer()
        min_cost = MGTC(n, c, a, k)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
        print('Minimum cost:', min_cost)
        print('Time taken:', end_time - start_time, 'seconds')

    theo_time = [n**2 * k + k*(n+1) for k in ks]
    data = [['k', 'Experimental results', 'theoretical results']] + [[k, t, theo] for k, t, theo in zip(ks, times, theo_time)]

    with open('time_complexity_k_with_n_fixed.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)