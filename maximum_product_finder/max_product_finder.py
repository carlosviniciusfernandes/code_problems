from functools import reduce
from itertools import combinations
from time import time


def combinations_alt(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return

    indices = list(range(r))
    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
            else:
                return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def compute_combination_product(arr):
    max = None
    for item in arr:
        product = reduce(lambda a, b: a * b, item)

        if max is None or product > max:
            max = product

    return max


def max_product_finder_k(arr: list[int], k: int) -> int:
    # comb = combinations(arr, k) #inbuilt combination is slower then alt implementation for large arrays
    comb = combinations_alt(arr, k)
    max = compute_combination_product(comb)
    print(f'input: {arr} \noutput: {max}')


start = time()
max_product_finder_k([-8, 6, -7, 3, 2, 1, -9], 3)
print(f'execution time: {time() - start} seconds')