"""
currying: turn multiple arguments function to single function chain, useful when we require a function that takes in only a single argument
f(x, y) ==> g(x)(y)
"""

def curried_pow(x):
    """
    pow(2, 3) ==> g(2)(3)
    >>> curried_pow(2)(3)
    8
    """
    def h(y):
        return pow(x, y)
    return h

def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f


    
