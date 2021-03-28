from timeit import timeit
from typing import Callable
import numpy as np
import pandas as pd
"""
Sum sequential big numbers from 0 to n-1 in different ways, and calculate taked time on performance.
"""
Function = Callable
num = 10_000_000

def while_loop(n: int=num):
    s, cont = 0, 0
    while cont < n:
        s += 1
        cont += 1
    return s


def for_pure(n: int=num):
    s = 0
    for cont in range(n):
        s += 1
    return s


def for_loop_with_increment(n: int=num):
    s = 0
    for cont in range(n):
        s+=1
        cont += 1
    return s


def for_loop_with_conditional(n: int=num):
    s = 0
    for cont in range(n):
        if cont < n:
            s += 1
    return s


def for_loop_with_increment_conditional(n:int=num):
    s = 0
    for cont in range(n):
        if cont < n:
            s+=1
            cont+=1
    return s


def sum_builtin(n: int=num):
    return sum(range(n))


def sum_numpy(n: int=num):
    return np.sum(np.arange(n))


def sum_pandas(n: int=num):
    return pd.Series(range(n)).sum()


def sum_mathematically(n: int=num):
    return (n * (n -1)) // 2


def metrics_performance(func: Function):
    print(f'{func.__name__:<40}\t\t', timeit(func, number=1))


def run():
    metrics_performance(while_loop)
    metrics_performance(for_pure)
    metrics_performance(for_loop_with_increment)
    metrics_performance(for_loop_with_conditional)
    metrics_performance(for_loop_with_increment_conditional)
    metrics_performance(sum_builtin)
    metrics_performance(sum_numpy)
    metrics_performance(sum_pandas)    
    metrics_performance(sum_mathematically)



if __name__ == "__main__":
    ...
    run()
    # print(sum_builtin(10), sum_mathematically(10))
