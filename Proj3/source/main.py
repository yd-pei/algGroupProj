'''
Notation: D(i,j,m)

1. When m = 0, D(i,j,0) = APAS(i,j)
2. When m > 0:
    For m = 1 to k
        For i = 1 to n
            For j = 1 to n
            Calculate D(i,j,m) = min { D (i,z,m-1) + D (z,j,0) for all z}
'''


import matplotlib.pyplot as plt
import timeit
import functools
import csv
import random
import os

def dataGenerator(n:int)->tuple[list,list]:
    '''
    Generate random input data for the problem.

    Input:
        n: number of galaxies

    Output:
        Should the data be floats or integers?
        c (list[list[int/floats]]): 2 dimensional list of numbers
            representing the cost of travel between galaxies
        a (list[int]): list of integers
            a[i] can be 0 or 1 (1 means that that galaxy is “astro-haunted”)
    '''
    return

def MGTC(m:int,c:list,a:list)->list:
    '''
    Minimum Galaxies Travel Cost

    Input:
        m: the number of astro-haunted galaxies that can be passed through
        c (list[list[int/floats]]): 2 dimensional list of numbers
            representing the cost of travel between galaxies
        a (list[int]): list of integers
            a[i] can be 0 or 1 (1 means that that galaxy is “astro-haunted”)

    Output:
        D (list[list[list[int/floats]]]): 3 dimensional list of numbers
            representing the minimum cost of travel between galaxies 
            passing through a maximum of m astro-haunted galaxies.
    '''

    def APAS(d:list,i:int,j:int):
        '''
        All Pairs Shortest Path Algorithm

        Input:
            d (list[list[int/floats]]): 2 dimensional list of numbers
                representing the cost of travel between galaxies
            i: starting galaxy
            j: ending galaxy

        Output:
            d[i][j]: cost of travel between galaxies i and j
        '''
        return d[i][j]
    

    return



if __name__ == '__main__':
    print("Hello World")