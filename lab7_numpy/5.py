import numpy as np
import timeit

n = 100
a = np.random.rand(n, n)
b = np.random.rand(n, n)


def mult(arr1, arr2):
    length = len(arr1)
    c = [[0] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                c[i][j] += arr1[i][k] * arr2[k][j]
    return c


def el_mult(arr1, arr2):
    length = len(arr1)
    c = [[0] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            c[i][j] = arr1[i][j] * arr2[i][j]
    return c


def np_mult(arr1, arr2):
    return np.dot(arr1, arr2)


def np_el_mult(arr1, arr2):
    return arr1 * arr2


print("Время работы функции mult: ", timeit.timeit(lambda: mult(a, b), number=1))
print("Время работы функции el_mult: ", timeit.timeit(lambda: el_mult(a, b), number=1))
print("Время работы функции np_mult: ", timeit.timeit(lambda: np_mult(a, b), number=1))
print("Время работы функции np_el_mult: ", timeit.timeit(lambda: np_el_mult(a, b), number=1))
