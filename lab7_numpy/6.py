import numpy as np


def func(y, a):
    return np.sum((y - a) ** 2)


print(func(np.array((1, 2, 3, 4, 5)), np.array((3, 2, 1, 0, -1))))
