"""
Function decorator
"""

def trace1(fn):
    """
    return a version of fn that first print before it is called

    fn -> one argument function
    """
    def traced(x):
        print('calling', fn, 'on argument', x)
        return fn(x)
    return traced


def square(x):
    return x*x
square = trace1(square)

@trace1
def sum_square_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total