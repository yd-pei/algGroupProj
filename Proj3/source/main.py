import idea
import priority_queue
import os
import timeit
import functools
import csv

def consistency_verification():
    """Check the consistency of the two algorithms
    """
    n = 10
    C, a = idea.generate_data(n)
    k = 2
    print(C,a)
    print(idea.MGTC(n, C, a, k))
    print(priority_queue.heap_least_cost(n, C, a, k))

consistency_verification()

