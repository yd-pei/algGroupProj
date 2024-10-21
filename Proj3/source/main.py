'''
Notation: D(i,j,m)

1. When m = 0, D(i,j,0) = APSP(i,j)
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

def MGTC(i:int,j:int,m:int,c:list,a:list):
    '''
    Minimum Galaxies Travel Cost

    Input:
        i: starting galaxy
        j: ending galaxy
        m: the number of astro-haunted galaxies that can be passed through
        c (list[list[int/floats]]): 2 dimensional list of numbers
            representing the cost of travel between galaxies
        a (list[int]): list of integers
            a[i] can be 0 or 1 (1 means that that galaxy is “astro-haunted”)

    Output:
        minCost: the minimum cost of travel between galaxies i and j
    '''

    def APSP(d:list,a:list,i:int,j:int):
        '''
        All Pairs Shortest Path Algorithm

        Input:
            d (list[list[int/floats]]): 2 dimensional list of numbers
                representing the cost of travel between galaxies
            a (list[int]): astro-haunted galaxies list
            i: starting galaxy
            j: ending galaxy

        Output:
            d[i][j]: cost of travel between galaxies i and j
        '''
        return d[i][j]
    

    return



if __name__ == '__main__':
    print("Hello World")