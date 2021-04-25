
from typing import Callable
from timeit import timeit
from loops import (while_loop, for_enumerate, for_pure, 
    for_loop_with_increment, for_loop_with_conditional,
    for_loop_with_increment_conditional, sum_builtin,
    sum_numpy, sum_pandas, sum_mathematically)


__author__ = '@britodfbr'
Function = Callable


def metrics_performance(func: Function):
    print(f'{func.__name__:<40}\t\t', timeit(func, number=1))


def run():
    metrics_performance(while_loop)
    metrics_performance(for_pure)
    metrics_performance(for_enumerate)
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
