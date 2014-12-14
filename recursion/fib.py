from functools import lru_cache

@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(88))

# memoize = lru_cache()
# fib = memoize(fib)
#
# def memoize(f):
#     memo = {}
#     def g(x):
#         if x not in memo:
#             memo[x] = f(x)
#         return memo[x]
#     return g
