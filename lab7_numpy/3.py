import numpy as np


def super_sort(rows, cols):
    a = np.random.randint(low=1, high=101, size=(rows, cols))
    b = np.copy(a)
    even_mask = np.zeros(cols, dtype=bool)
    even_mask[1::2] = True
    odd_mask = ~even_mask
    b[:, even_mask] = np.sort(b[:, even_mask], axis=0)
    b[:, odd_mask] = np.sort(b[:, odd_mask], axis=0)[::-1]
    return a, b


A, B = super_sort(4, 5)
print("Матрица A:")
print(A)
print("Матрица B:")
print(B)
