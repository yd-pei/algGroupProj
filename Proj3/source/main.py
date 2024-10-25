import idea
import priority_queue
import os
import timeit
import functools
import math

def consistencyVerification():
    """
    Check the consistency of the two algorithms
    """
    n = 10
    C, a = idea.generate_data(n)
    k = 2
    print(C,a)
    print(idea.MGTC(n, C, a, k))
    print(priority_queue.heap_least_cost(n, C, a, k))

def timeCompare():
    """
    Compare the running time of the two algorithms
    """
    times1 = []
    times2 = []
    ns = [5, 10, 25, 50, 100, 250, 500, 1000]
    for n in ns:
        C, a = idea.generate_data(n)
        partial_alg1 = functools.partial(idea.MGTC, n, C, a, 3)
        partial_alg2 = functools.partial(priority_queue.heap_least_cost, n, C, a, 3)
        duration1 = timeit.timeit(partial_alg1, number = 1)
        duration2 = timeit.timeit(partial_alg2, number = 1)
        times1.append(duration1)
        times2.append(duration2)

    os.makedirs(os.path.join("Proj3","source","data"), exist_ok=True)
    filename = os.path.join("Proj3","source","data", "comparison.csv")
    with open(filename, "w") as f:
        f.write("n,idea,priority_queue\n")
        for i in range(len(ns)):
            f.write(f"{ns[i]},{times1[i]},{times2[i]}\n")

def timer():
    """
    Measure the running time of priority queue algorithm 
    """

    # complexity n with k fixed
    times_n = []
    k = 3
    ns = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000,10000]
    for n in ns:
        C, a = idea.generate_data(n)
        partial_pq = functools.partial(priority_queue.heap_least_cost, n, C, a, 3)
        duration_n = timeit.timeit(partial_pq, number = 1)
        times_n.append(duration_n)

    average_time = sum(times_n)/len(times_n)
    complexity_n = [asym_complexity(n,k) for n in ns]
    scale_n = average_time/(sum(complexity_n)/len(complexity_n))
    scaled_complexity_n = [scale_n * c for c in complexity_n]

    os.makedirs(os.path.join("Proj3","source","data"), exist_ok=True)
    filename = os.path.join("Proj3","source","data", "pq_n.csv")
    with open(filename, "w") as f:
        f.write("n,time,theoretical_complexity,scaled_theoretical_complexity\n")
        for i in range(len(ns)):
            f.write(f"{ns[i]},{times_n[i]},{complexity_n[i]},{scaled_complexity_n[i]}\n")
        f.write(f"scale_constant,{scale_n}\n")

    # complexity k with n fixed
    times_k = []
    n = 1000
    ks = [1, 5, 10, 25, 50, 100, 250]
    for k in ks:
        C, a = idea.generate_data(n)
        partial_pq = functools.partial(priority_queue.heap_least_cost, n, C, a, k)
        duration_k = timeit.timeit(partial_pq, number = 1)
        times_k.append(duration_k)
    
    average_time = sum(times_k)/len(times_k)
    complexity_k = [asym_complexity(n,k) for k in ks]
    scale_k = average_time/(sum(complexity_k)/len(complexity_k))
    scaled_complexity_k = [scale_k * c for c in complexity_k]

    filename = os.path.join("Proj3","source","data", "pq_k.csv")
    with open(filename, "w") as f:
        f.write("k,time,theoretical_complexity,scaled_theoretical_complexity\n")
        for i in range(len(ks)):
            f.write(f"{ks[i]},{times_k[i]},{complexity_k[i]},{scaled_complexity_k[i]}\n")
        f.write(f"scale_constant,{scale_k}\n")

def asym_complexity(n,k):
    # T(n,k) = O(N^2 * k * log(N*k))
    return n**2 * k * math.log(n*k)
    

if __name__ == "__main__":
    # consistencyVerification()
    # timeCompare()
    timer()

